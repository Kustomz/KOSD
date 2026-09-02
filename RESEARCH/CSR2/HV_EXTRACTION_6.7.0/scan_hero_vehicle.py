#!/usr/bin/env python3
"""KOSD CSR2 6.7.0 Hero Vehicle discovery scanner.

Research/acquisition stage only. Uses the proven SCB OBB extraction approach:
unpack each canonical OBB as ZIP, recurse nested ZIP archives, locate embedded
UnityFS bundles at arbitrary offsets, and inventory Unity objects matching the
exact Nitro CRDB target or related identifiers. No production artwork is made.
"""
from __future__ import annotations
import argparse, hashlib, json, struct, tempfile, zipfile
from pathlib import Path

MAGIC=b"UnityFS"
CHUNK=4*1024*1024
TARGETS=("AMC_RingbrothersJavelinDefiant_1972","RingbrothersJavelin","JavelinDefiant")

def sha256(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def extract_zip(src,dst):
 dst.mkdir(parents=True,exist_ok=True); count=0
 with zipfile.ZipFile(src) as z:
  for i,zi in enumerate(z.infolist()):
   if zi.is_dir(): continue
   out=dst/f"m_{i:06d}_{Path(zi.filename).name}"
   with z.open(zi) as a,open(out,"wb") as b:
    for x in iter(lambda:a.read(CHUNK),b""): b.write(x)
   count+=1
 return count

def nested(root,maxdepth=3):
 queue=[(p,0) for p in root.rglob("*") if p.is_file()]; found=[]; seen=set()
 while queue:
  p,d=queue.pop(0)
  if d>maxdepth or str(p) in seen: continue
  seen.add(str(p))
  try:
   with open(p,"rb") as f:
    if f.read(4)!=b"PK\x03\x04": continue
   out=p.parent/f"nested_{d}_{p.stem}"; out.mkdir(exist_ok=True)
   n=extract_zip(p,out); found.append({"archive":str(p),"depth":d,"members":n})
   queue += [(x,d+1) for x in out.rglob("*") if x.is_file()]
  except Exception: pass
 return found

def magic_offsets(p):
 hits=[];carry=b"";base=0
 with open(p,"rb") as f:
  while True:
   b=f.read(CHUNK)
   if not b: break
   d=carry+b; off=base-len(carry); start=0
   while True:
    q=d.find(MAGIC,start)
    if q<0: break
    hits.append(off+q);start=q+1
   carry=d[-6:];base+=len(b)
 return hits

def bundle_header(p,off):
 with open(p,"rb") as f:
  f.seek(off)
  if f.read(7)!=MAGIC:return None
  f.read(1)
  for _ in range(3):
   while True:
    b=f.read(1)
    if not b:return None
    if b==b"\0":break
  x=f.read(20)
  if len(x)!=20:return None
  size,comp,uncomp,flags=struct.unpack(">QIII",x)
  if size<=0 or size>p.stat().st_size-off:return None
  return {"file_size":size,"compressed_blocks_info_size":comp,"uncompressed_blocks_info_size":uncomp,"flags":flags}

def carve(src,off,dst):
 h=bundle_header(src,off)
 if not h:return None
 dst.parent.mkdir(parents=True,exist_ok=True);left=h["file_size"]
 with open(src,"rb") as a,open(dst,"wb") as b:
  a.seek(off)
  while left:
   x=a.read(min(CHUNK,left))
   if not x:return None
   b.write(x);left-=len(x)
 return {"source":str(src),"offset":off,"path":str(dst),**h}

def names(obj):
 out=[]
 try:
  x=obj.peek_name()
  if x:out.append(str(x))
 except Exception:pass
 try:
  if obj.container:out.append(str(obj.container))
 except Exception:pass
 try:
  x=obj.read(check_read=False)
  for attr in ("name","m_Name"):
   n=getattr(x,attr,None)
   if n:out.append(str(n))
 except Exception:pass
 return list(dict.fromkeys(out))

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--obb",action="append",required=True);ap.add_argument("--out",required=True)
 a=ap.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 import UnityPy
 report={"tool":"KOSD CSR2 6.7.0 Hero Vehicle discovery scanner","target_crdb":TARGETS[0],"terms":TARGETS,"obbs":[],"nested_archives":[],"unityfs_hits":[],"matches":[]}
 with tempfile.TemporaryDirectory(prefix="kosd_hv_") as td:
  temp=Path(td);carved=temp/"bundles"
  for arg in a.obb:
   src=Path(arg);info={"path":str(src),"size":src.stat().st_size,"sha256":sha256(src)};root=temp/src.stem
   try: members=extract_zip(src,root)
   except Exception as e:
    info["zip_error"]=repr(e);report["obbs"].append(info);continue
   info["zip_members"]=members;report["nested_archives"]+=nested(root)
   seen=set();sig=0
   for p in root.rglob("*"):
    if not p.is_file():continue
    try: offs=magic_offsets(p)
    except OSError:continue
    sig+=len(offs)
    for i,off in enumerate(offs):
     q=carved/f"{hashlib.sha1(str(p).encode()).hexdigest()}_{i:05d}.bundle";c=carve(p,off,q)
     if not c:continue
     h=sha256(q)
     if h in seen:continue
     seen.add(h);report["unityfs_hits"].append(c)
     try:objs=list(UnityPy.load(str(q)).objects)
     except Exception:continue
     for obj in objs:
      ns=names(obj);joined=" | ".join(ns)
      if not any(t.lower() in joined.lower() for t in TARGETS):continue
      try:typ=obj.type.name
      except Exception:typ=str(getattr(obj,"type","unknown"))
      report["matches"].append({"obb":str(src),"source_file":str(p),"bundle":str(q),"bundle_sha256":h,"path_id":getattr(obj,"path_id",None),"type":typ,"names":ns})
   info["unityfs_signature_count"]=sig;info["unique_bundles_scanned"]=len(seen);report["obbs"].append(info)
 report["summary"]={"unityfs_signature_hits":len(report["unityfs_hits"]),"unityfs_bundles_scanned":len({x.get("bundle_sha256") for x in report["unityfs_hits"]}),"target_matches":len(report["matches"]),"nested_archives":len(report["nested_archives"])}
 (out/"hero_vehicle_discovery.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
 print(json.dumps(report["summary"],indent=2))
 for m in report["matches"]: print(m["type"],"|"," | ".join(m["names"]))

if __name__=="__main__":main()
