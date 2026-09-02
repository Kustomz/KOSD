#!/usr/bin/env python3
"""Diagnose CSR2 6.7.0 OBB container structure without modifying source data."""
from __future__ import annotations
import argparse, hashlib, json, os, struct, zipfile
from pathlib import Path

CHUNK = 4 * 1024 * 1024
MAGICS = (b"UnityFS", b"UnityRaw", b"UnityWeb", b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def find_magic(path, magic, limit=20):
    hits=[]; carry=b""; base=0
    with open(path,"rb") as f:
        while len(hits)<limit:
            b=f.read(CHUNK)
            if not b: break
            d=carry+b; start=0; off=base-len(carry)
            while len(hits)<limit:
                q=d.find(magic,start)
                if q<0: break
                hits.append(off+q); start=q+1
            carry=d[-max(0,len(magic)-1):]; base += len(b)
    return hits

def sample(path):
    with open(path,"rb") as f:
        return f.read(64).hex()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("obb",action="append",required=True); ap.add_argument("--out",required=True)
    a=ap.parse_args(); report=[]
    for raw in a.obb:
        p=Path(raw); item={"path":str(p),"size":p.stat().st_size,"sha256":sha256(p),"first64_hex":sample(p)}
        try:
            with zipfile.ZipFile(p) as z:
                infos=z.infolist(); item["zip_valid"]=True; item["zip_entries"]=len(infos)
                item["zip_comment_len"]=len(z.comment)
                item["entries"]=[]
                for zi in infos[:100]:
                    entry={"name":zi.filename,"compressed":zi.compress_size,"uncompressed":zi.file_size,"method":zi.compress_type}
                    try:
                        with z.open(zi) as f: data=f.read(128)
                        entry["first128_hex"]=data.hex()
                        entry["magic_hits"]={m.decode("latin1"):find_magic_in_bytes(data,m) for m in MAGICS if find_magic_in_bytes(data,m)}
                    except Exception as e: entry["read_error"]=repr(e)
                    item["entries"].append(entry)
        except Exception as e:
            item["zip_valid"]=False; item["zip_error"]=repr(e)
        item["direct_magic_hits"]={m.decode("latin1"):find_magic(p,m) for m in MAGICS if find_magic(p,m)}
        report.append(item)
    Path(a.out).write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2)[:30000])

def find_magic_in_bytes(data, magic):
    return [i for i in range(max(0,len(data)-len(magic)+1)) if data.startswith(magic,i)]

if __name__=="__main__": main()
