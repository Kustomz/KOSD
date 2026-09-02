#!/usr/bin/env python3
"""KOSD CSR2 6.7.0 RestorationManifest forensic scanner.
Research only. OBBs may contain nested/embedded UnityFS data, so this scanner
inventories ZIP members, extracts nested ZIPs, searches every extracted file
for UnityFS signatures at arbitrary offsets, carves valid UnityFS bundles, and
then uses UnityPy to inspect matching serialized objects and 14,800.
"""
from __future__ import annotations
import argparse,hashlib,json,struct,sys,tempfile,zipfile
from pathlib import Path

TERMS=("restorationmanifest","250gtoclassic","ferrari_250")
VALUE=14800
MAGIC=b"UnityFS"
CHUNK=4*1024*1024


def sha256(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def safe(v):
 if isinstance(v,dict): return {str(k):safe(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)): return [safe(x) for x in v]
 if isinstance(v,(str,int,float,bool)) or v is None:return v
 return str(v)

def value_paths(v,path=""):
 out=[]
 if isinstance(v,dict):
  for k,x in v.items(): out+=value_paths(x,f"{path}.{k}" if path else str(k))
 elif isinstance(v,(list,tuple)):
  for i,x in enumerate(v): out+=value_paths(x,f"{path}[{i}]")
 elif isinstance(v,(int,float)) and not isinstance(v,bool) and v==VALUE: out.append(path)
 return out

def raw_hits(raw):
 out=[]
 for needle,label in ((struct.pack("<i",VALUE),"int32_le"),(struct.pack(">i",VALUE),"int32_be")):
  start=0
  while True:
   p=raw.find(needle,start)
   if p<0:break
   out.append({"offset":p,"encoding":label});start=p+1
 return out

def magic_offsets(p):
 hits=[]; carry=b""; base=0
 with open(p,"rb") as f:
  while True:
   b=f.read(CHUNK)
   if not b:break
   d=carry+b; off=base-len(carry); start=0
   while True:
    q=d.find(MAGIC,start)
    if q<0:break
    hits.append(off+q);start=q+1
   carry=d[-6:];base+=len(b)
 return hits

def header(p,off):
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
  return {"file_size":size,"compressed_blocks_info_size":comp,"uncompressed_blocks_info_size":uncomp,"flags":flags,"header_end":f.tell()}

def carve(src,off,dst):
 h=header(src,off)
 if not h or h["file_size"]<=0 or h["file_size"]>src.stat().st_size-off:return None
 dst.parent.mkdir(parents=True,exist_ok=True);left=h["file_size"]
 with open(src,"rb") as a,open(dst,"wb") as b:
  a.seek(off)
  while left:
   x=a.read(min(CHUNK,left))
   if not x:return None
   b.write(x);left-=len(x)
 return {"source":str(src),"offset":off,"path":str(dst),**h}

def extract_zip(src,dst):
 dst.mkdir(parents=True,exist_ok=True); meta=[]
 try:
  with zipfile.ZipFile(src) as z:
   for i,zi in enumerate(z.infolist()):
    meta.append({"name":zi.filename,"size":zi.file_size,"compressed_size":zi.compress_size,"crc":f"{zi.CRC:08x}"})
    if zi.is_dir():continue
    out=dst/f"m_{i:06d}_{Path(zi.filename).name}"
    with z.open(zi) as a,open(out,"wb") as b:
     for x in iter(lambda:a.read(CHUNK),b""):b.write(x)
  return meta,None
 except Exception as e:return meta,repr(e)

def nested(root,maxdepth=3):
 found=[]; queue=[(p,0) for p in root.rglob("*") if p.is_file()]; seen=set()
 while queue:
  p,d=queue.pop(0); key=(str(p),d)
  if key in seen or d>maxdepth:continue
  seen.add(key)
  try:
   with open(p,"rb") as f:magic=f.read(4)
   if magic!=b"PK\x03\x04":continue
   out=p.parent/f"nested_{d}_{p.stem}";out.mkdir(exist_ok=True)
   members,_=extract_zip(p,out);found.append({"archive":str(p),"depth":d,"members":len(members)})
   queue += [(x,d+1) for x in out.rglob("*") if x.is_file()]
  except Exception:pass
 return found

def names(obj):
 out=[]
 try:
  x=obj.peek_name()
  if x:out.append(str(x))
 except Exception:pass
 try:
  x=obj.container
  if x:out.append(str(x))
 except Exception:pass
 try:
  x=obj.read(check_read=False)
  n=getattr(x,"name",None)
  if n:out.append(str(n))
 except Exception:pass
 return list(dict.fromkeys(out))

def scan_bundle(p):
 import UnityPy
 r={"bundle":str(p),"size":p.stat().st_size,"matches":[],"errors":[]}
 try: objs=list(UnityPy.load(str(p)).objects);r["object_count"]=len(objs)
 except Exception as e:r["errors"].append({"stage":"load","error":repr(e)});return r
 for o in objs:
  ns=names(o);joined=" | ".join(ns).lower()
  if not any(t in joined for t in TERMS):continue
  try:typ=o.type.name
  except Exception:typ=str(getattr(o,"type","unknown"))
  e={"path_id":getattr(o,"path_id",None),"type":typ,"names":ns}
  try:
   raw=o.get_raw_data();e["raw_size"]=len(raw);e["raw_14800_hits"]=raw_hits(raw)
  except Exception as x:e["raw_error"]=repr(x)
  try:
   tree=o.read_typetree(check_read=False);e["typetree"]=safe(tree);e["typetree_14800_paths"]=value_paths(tree)
  except Exception as x:e["typetree_error"]=repr(x)
  r["matches"].append(e)
 return r

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--obb",action="append",required=True);ap.add_argument("--out",required=True);a=ap.parse_args()
 out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
 report={"tool":"KOSD CSR2 RestorationManifest forensic scanner","revision":4,"target_value":VALUE,"target_terms":TERMS,"obbs":[],"nested_archives":[],"unityfs_hits":[],"bundle_results":[]}
 with tempfile.TemporaryDirectory(prefix="kosd_scb_") as td:
  temp=Path(td);carved=temp/"bundles"
  for arg in a.obb:
   obb=Path(arg); info={"path":str(obb),"size":obb.stat().st_size,"sha256":sha256(obb)}; root=temp/obb.stem
   members,err=extract_zip(obb,root);info["zip_members"]=len(members);info["member_inventory"]=members
   if err:info["zip_error"]=err;report["obbs"].append(info);continue
   report["nested_archives"]+=nested(root)
   bundles=[]
   for p in root.rglob("*"):
    if not p.is_file():continue
    try:offs=magic_offsets(p)
    except OSError:continue
    for i,off in enumerate(offs):
     q=carved/f"{hashlib.sha1(str(p).encode()).hexdigest()}_{i:03d}.bundle";c=carve(p,off,q)
     if c:report["unityfs_hits"].append(c);bundles.append(q)
   seen=set()
   for b in bundles:
    h=sha256(b)
    if h in seen:continue
    seen.add(h);report["bundle_results"].append(scan_bundle(b))
   info["unityfs_bundles_found"]=len(seen);report["obbs"].append(info)
 candidates=[];hits=[]
 for r in report["bundle_results"]:
  for m in r.get("matches",[]):
   if "restorationmanifest" in " | ".join(m.get("names",[])).lower():candidates.append(m)
   if m.get("raw_14800_hits") or m.get("typetree_14800_paths"):hits.append(m)
 report["summary"]={"restoration_manifest_candidates":len(candidates),"objects_with_14800_hits":len(hits),"target_value_found_in_decoded_typetree":any(m.get("typetree_14800_paths") for m in hits),"unityfs_signature_hits":len(report["unityfs_hits"]),"bundles_scanned":len(report["bundle_results"]),"nested_archives":len(report["nested_archives"])}
 (out/"restoration_forensics.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
 print(json.dumps(report["summary"],indent=2))

if __name__=="__main__":main()
