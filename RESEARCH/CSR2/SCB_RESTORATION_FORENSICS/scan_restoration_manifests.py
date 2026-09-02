#!/usr/bin/env python3
"""KOSD CSR2 6.7.0 RestorationManifest forensic scanner.

This is research tooling only. It does not modify game data.
It extracts OBB ZIP contents, finds UnityFS AssetBundles, and inspects
Unity serialized objects for RestorationManifest targets and 14,800.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import struct
import sys
import tempfile
import traceback
import zipfile
from pathlib import Path

TARGETS = [
    "Ferrari_250GTOClassic_1962_RestorationManifest",
]
TARGET_TERMS = ["restorationmanifest", "250gtoclassic", "ferrari_250"]
TARGET_VALUE = 14800


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def json_safe(v):
    if isinstance(v, dict):
        return {str(k): json_safe(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [json_safe(x) for x in v]
    if isinstance(v, (str, int, float, bool)) or v is None:
        return v
    if hasattr(v, "__dict__"):
        return {k: json_safe(x) for k, x in vars(v).items() if not k.startswith("_")}
    return str(v)


def find_14800(obj, raw: bytes):
    hits = []
    le = struct.pack("<i", TARGET_VALUE)
    be = struct.pack(">i", TARGET_VALUE)
    for needle, label in ((le, "int32_le"), (be, "int32_be")):
        start = 0
        while True:
            p = raw.find(needle, start)
            if p < 0:
                break
            hits.append({"offset": p, "encoding": label})
            start = p + 1
    return hits


def object_name(obj):
    vals = []
    try:
        n = obj.peek_name()
        if n:
            vals.append(str(n))
    except Exception:
        pass
    try:
        c = obj.container
        if c:
            vals.append(str(c))
    except Exception:
        pass
    try:
        data = obj.read(check_read=False)
        n = getattr(data, "name", None)
        if n:
            vals.append(str(n))
    except Exception:
        pass
    # preserve order, remove duplicates
    return list(dict.fromkeys(vals))


def recursive_value_hits(value, path=""):
    hits = []
    if isinstance(value, dict):
        for k, v in value.items():
            p = f"{path}.{k}" if path else str(k)
            hits.extend(recursive_value_hits(v, p))
    elif isinstance(value, (list, tuple)):
        for i, v in enumerate(value):
            hits.extend(recursive_value_hits(v, f"{path}[{i}]"))
    elif isinstance(value, bool):
        return hits
    elif isinstance(value, (int, float)) and value == TARGET_VALUE:
        hits.append(path)
    return hits


def extract_obb(obb: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(obb) as z:
            z.extractall(out_dir)
            return {"zip": True, "members": len(z.infolist())}
    except zipfile.BadZipFile:
        return {"zip": False, "members": 0, "error": "OBB is not a ZIP archive"}


def scan_bundle(bundle: Path, target_terms):
    import UnityPy

    result = {
        "bundle": str(bundle),
        "size": bundle.stat().st_size,
        "matches": [],
        "restoration_candidates": [],
        "errors": [],
    }
    try:
        env = UnityPy.load(str(bundle))
    except Exception as e:
        result["errors"].append({"stage": "load", "error": repr(e)})
        return result

    try:
        objects = list(env.objects)
    except Exception as e:
        result["errors"].append({"stage": "objects", "error": repr(e)})
        return result

    for obj in objects:
        try:
            typ = obj.type.name
        except Exception:
            typ = str(getattr(obj, "type", "unknown"))
        names = object_name(obj)
        joined = " | ".join(names).lower()
        candidate = any(term in joined for term in target_terms)
        if not candidate:
            continue

        entry = {
            "path_id": getattr(obj, "path_id", None),
            "type": typ,
            "names": names,
            "serialized_type_has_nodes": bool(getattr(getattr(obj, "serialized_type", None), "nodes", None)),
        }
        try:
            raw = obj.get_raw_data()
            entry["raw_size"] = len(raw)
            entry["raw_14800_hits"] = find_14800(obj, raw)
        except Exception as e:
            entry["raw_error"] = repr(e)
            raw = b""

        if entry["serialized_type_has_nodes"]:
            try:
                tree = obj.read_typetree(check_read=False)
                entry["typetree"] = json_safe(tree)
                entry["typetree_14800_paths"] = recursive_value_hits(tree)
            except Exception as e:
                entry["typetree_error"] = repr(e)
                try:
                    entry["typetree_structure"] = obj.dump_typetree_structure()
                except Exception:
                    pass
        else:
            try:
                data = obj.read(check_read=False)
                entry["m_Name"] = getattr(data, "name", None)
                entry["script"] = str(getattr(data, "script", None))
                entry["raw_data_size"] = len(getattr(data, "raw_data", b""))
            except Exception as e:
                entry["read_error"] = repr(e)

        if "restorationmanifest" in joined:
            result["restoration_candidates"].append(entry)
        result["matches"].append(entry)

    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obb", action="append", required=True, help="OBB path; may be supplied twice")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report = {
        "tool": "KOSD CSR2 RestorationManifest forensic scanner",
        "python": sys.version,
        "targets": TARGETS,
        "target_terms": TARGET_TERMS,
        "target_value": TARGET_VALUE,
        "obbs": [],
        "bundles_scanned": 0,
        "bundle_results": [],
        "summary": {},
    }

    with tempfile.TemporaryDirectory(prefix="kosd_scb_forensics_") as td:
        temp = Path(td)
        for obb_arg in args.obb:
            obb = Path(obb_arg)
            info = {
                "path": str(obb),
                "size": obb.stat().st_size if obb.exists() else None,
                "sha256": sha256_file(obb) if obb.exists() else None,
            }
            extract_dir = temp / obb.stem
            info["extract"] = extract_obb(obb, extract_dir)
            report["obbs"].append(info)
            if not info["extract"].get("zip"):
                continue

            bundles = []
            for p in extract_dir.rglob("*"):
                if not p.is_file():
                    continue
                try:
                    with p.open("rb") as f:
                        if f.read(6) == b"UnityFS":
                            bundles.append(p)
                except OSError:
                    pass
            info["unityfs_bundles"] = len(bundles)
            for bundle in bundles:
                result = scan_bundle(bundle, TARGET_TERMS)
                report["bundles_scanned"] += 1
                if result["matches"] or result["errors"]:
                    report["bundle_results"].append(result)

    candidates = []
    value_hits = []
    for r in report["bundle_results"]:
        for m in r.get("matches", []):
            if "restorationmanifest" in " | ".join(m.get("names", [])).lower():
                candidates.append({"bundle": r["bundle"], "match": m})
            if m.get("raw_14800_hits") or m.get("typetree_14800_paths"):
                value_hits.append({"bundle": r["bundle"], "match": m})
    report["summary"] = {
        "restoration_manifest_candidates": len(candidates),
        "objects_with_14800_hits": len(value_hits),
        "target_value_found_in_decoded_typetree": any(
            m.get("match", {}).get("typetree_14800_paths") for m in value_hits
        ),
    }

    (out / "restoration_forensics.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Bundles scanned: {report['bundles_scanned']}")
    print(f"Full report: {out / 'restoration_forensics.json'}")


if __name__ == "__main__":
    main()
