#!/usr/bin/env python3
"""CSR2 6.7.0 HV discovery: identity -> PPtr references -> model/mesh assembly."""
from __future__ import annotations
import argparse, hashlib, json, re, tempfile, zipfile
from pathlib import Path

MAGIC=b"UnityFS"; CHUNK=4*1024*1024
TARGET_CRDB="AMC_RingbrothersJavelinDefiant_1972"
TARGET_TERMS=("AMC","Ringbrothers","Javelin","Defiant","1972")
MODEL_TYPES={"GameObject","Transform","MeshFilter","SkinnedMeshRenderer","MeshRenderer","Mesh","Material","Texture2D","Animator","AnimatorController","MonoBehaviour","PrefabInstance"}
MODEL_TERMS=("prefab","mesh","body","model","car","vehicle","createdassets","shared","common")

def sha256(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
 return h.hexdigest()

def norm(s): return re.sub(r"[^a-z0-9]+","",str(s).lower())
def exact(s): return norm(TARGET_CRDB) in norm(s)
def hits(s):
 n=norm(s); return [t for t in TARGET_TERMS if norm(t) in n]

def names(o):
 out=[]
 for fn in (lambda:o.peek_name(),lambda:o.container):
  try:
   x=fn()
   if x: out.append(str(x))
  except Exception: pass
 try:
  d=o.read(check_read=False)
  for a in ("name","m_Name"):
   x=getattr(d,a,None)
   if x: out.append(str(x))
 except Exception: pass
 return list(dict.fromkeys(out))

def safe(v,depth=0):
 if depth>4: return str(v)[:500]
 if v is None or isinstance(v,(bool,int,float,str)): return v if not isinstance(v,str) else v[:4000]
 if isinstance(v,dict): return {str(k):safe(x,depth+1) for k,x in list(v.items())[:120]}
 if isinstance(v,(list,tuple)): return [safe(x,depth+1) for x in list(v)[:80]]
 out={}
 for a in ("m_FileID","m_PathID","file_id","path_id"):
  try: out[a]=getattr(v,a)
  except Exception: pass
 if out: return {**out,"repr":str(v)[:1200]}
 return str(v)[:1200]

def typetree(o):
 try:return safe(o.read_typetree())
 except Exception as e:return {"_error":repr(e)}

def pptrs(v,path="root",depth=0,seen=None):
 if seen is None: seen=set()
 if depth>7:return []
 out=[]
 if v is None or isinstance(v,(bool,int,float,str,bytes)): return out
 if hasattr(v,"m_FileID") and hasattr(v,"m_PathID"):
  key=(id(v),getattr(v,"m_FileID",None),getattr(v,"m_PathID",None))
  if key in seen:return out
  seen.add(key); out.append((path,v)); return out
 if isinstance(v,dict):
  for k,x in list(v.items())[:200]: out += pptrs(x,f"{path}.{k}",depth+1,seen)
 elif isinstance(v,(list,tuple)):
  for i,x in enumerate(v[:120]): out += pptrs(x,f"{path}[{i}]",depth+1,seen)
 elif hasattr(v,"__dict__"):
  for k,x in list(v.__dict__.items())[:200]: out += pptrs(x,f"{path}.{k}",depth+1,seen)
 return out

def descriptor(o):
 try:t=o.type.name
 except Exception:t=str(getattr(o,"type","unknown"))
 return {"type":t,"path_id":getattr(o,"path_id",None),"names":names(o),"container":str(getattr(o,"container",None))}

def trace_refs(root,report,max_depth=4,max_refs=500):
 seen=set(); queue=[(root,0,"root")]
 while queue and len(report["resolved_references"])<max_refs:
  obj,depth,from_path=queue.pop(0)
  if depth>max_depth: continue
  try:data=obj.read(check_read=False)
  except Exception as e:
   report["reference_errors"].append({"from":from_path,"error":repr(e)}); continue
  for path,pp in pptrs(data):
   key=(id(getattr(pp,"assetsfile",None)),getattr(pp,"m_FileID",None),getattr(pp,"m_PathID",None))
   if key in seen: continue
   seen.add(key)
   rec={"from":from_path,"field":path,"m_FileID":getattr(pp,"m_FileID",None),"m_PathID":getattr(pp,"m_PathID",None)}
   try:
    dst=pp.deref()
    rec["resolved"]=descriptor(dst)
    rec["external_file"]=(str(getattr(getattr(pp,"assetsfile",None),"externals",[])[pp.m_FileID-1].path) if getattr(pp,"m_FileID",0)>0 and getattr(pp,"assetsfile",None) and pp.m_FileID-1<len(pp.assetsfile.externals) else None)
    text=" | ".join(rec["resolved"]["names"]+[rec["resolved"]["container"]])
    rec["model_relevance"]=any(x in norm(text) for x in MODEL_TERMS) or rec["resolved"]["type"] in MODEL_TYPES
    report["resolved_references"].append(rec)
    if depth<max_depth and rec["resolved"]["type"] in MODEL_TYPES: queue.append((dst,depth+1,from_path+"."+path))
   except Exception as e:
    rec["resolve_error"]=repr(e); report["reference_errors"].append(rec)

def scan_bundle(bundle,source,obb,report,work):
 import UnityPy
 try: env=UnityPy.load(str(bundle))
 except Exception as e:
  report["bundle_errors"].append({"source_member":source,"error":repr(e)}); return
 objs=list(env.objects); report["bundles"].append({"source_member":source,"sha256":sha256(bundle),"object_count":len(objs)})
 for o in objs:
  ns=names(o); joined=" | ".join(ns+[source])
  try: typ=o.type.name
  except Exception: typ=str(getattr(o,"type","unknown"))
  candidate=exact(joined)
  deep=None
  if typ in {"MonoBehaviour","GameObject","Transform","MeshFilter","SkinnedMeshRenderer","MeshRenderer","Mesh","Material","AssetBundle"} or any(x in norm(source) for x in MODEL_TERMS):
   try:
    d=o.read(check_read=False); text=str(d)
    if exact(text): candidate=True; deep=text[:16000]
   except Exception: pass
  if not candidate: continue
  item={"obb":str(obb),"source_member":source,"type":typ,"path_id":getattr(o,"path_id",None),"names":ns,"container":str(getattr(o,"container",None)),"matched_tokens":hits(joined)}
  if typ=="MonoBehaviour" and "CarMetadata" in source or exact(joined) or deep:
   item["typetree"]=typetree(o)
  if deep:item["data_excerpt"]=deep
  if typ=="MonoBehaviour" and "CarMetadata" in source:
   item["reference_trace_root"]=True
   trace_refs(o,report)
  report["identity_candidates"].append(item)

def scan_archive(path,obb,report,work,depth=0):
 try:z=zipfile.ZipFile(path)
 except Exception as e: report["archive_errors"].append({"archive":str(path),"error":repr(e)}); return
 try:
  for i,zi in enumerate(z.infolist()):
   if zi.is_dir():continue
   try:
    with z.open(zi) as src:
     head=src.read(7); src.seek(0)
     if head==MAGIC:
      bp=work/f"bundle_{len(report['bundles_seen']):06d}.bundle"
      with bp.open("wb") as dst:
       for c in iter(lambda:src.read(CHUNK),b""):dst.write(c)
      h=sha256(bp)
      if h in report["seen_bundle_sha256"]:continue
      report["seen_bundle_sha256"].add(h); report["bundles_seen"].append({"source_member":zi.filename,"size":zi.file_size,"sha256":h})
      scan_bundle(bp,zi.filename,obb,report,work)
     elif depth<3 and head[:4]==b"PK\x03\x04":
      np=work/f"nested_{depth}_{i:06d}.zip"
      with np.open("wb") as dst:
       for c in iter(lambda:src.read(CHUNK),b""):dst.write(c)
      report["nested_archives"].append({"source_member":zi.filename,"depth":depth+1}); scan_archive(np,obb,report,work,depth+1)
   except Exception as e: report["member_errors"].append({"source_member":zi.filename,"error":repr(e)})
 finally:z.close()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--obb",action="append",required=True); ap.add_argument("--out",required=True); a=ap.parse_args()
 out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
 r={"tool":"KOSD CSR2 6.7.0 HV model-reference tracer","target_crdb":TARGET_CRDB,"target_terms":list(TARGET_TERMS),"obbs":[],"bundles_seen":[],"bundles":[],"identity_candidates":[],"resolved_references":[],"reference_errors":[],"nested_archives":[],"archive_errors":[],"member_errors":[],"bundle_errors":[],"seen_bundle_sha256":set()}
 with tempfile.TemporaryDirectory(prefix="kosd_hv_") as td:
  work=Path(td)
  for arg in a.obb:
   src=Path(arg); info={"path":str(src),"size":src.stat().st_size,"sha256":sha256(src)}
   try:
    with zipfile.ZipFile(src) as z:info["zip_members"]=len(z.infolist())
    r["obbs"].append(info); scan_archive(src,src,r,work)
   except Exception as e:info["zip_error"]=repr(e); r["obbs"].append(info)
 r["seen_bundle_sha256"]=sorted(r["seen_bundle_sha256"])
 r["summary"]={"zip_members":sum(x.get("zip_members",0) for x in r["obbs"]),"unityfs_bundles_seen":len(r["bundles_seen"]),"unityfs_bundles_loaded":len(r["bundles"]),"identity_candidates":len(r["identity_candidates"]),"resolved_references":len(r["resolved_references"]),"model_references":sum(1 for x in r["resolved_references"] if x.get("model_relevance")),"reference_errors":len(r["reference_errors"]),"bundle_errors":len(r["bundle_errors"])}
 (out/"hero_vehicle_discovery.json").write_text(json.dumps(r,indent=2,ensure_ascii=True),encoding="utf-8"); print(json.dumps(r["summary"],indent=2))
 for x in r["resolved_references"][:200]:print("REF",x)
if __name__=="__main__":main()
