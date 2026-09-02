#!/usr/bin/env python3
"""KOSD CSR2 6.7.0 Hero Vehicle discovery scanner.

Discovery is deliberately broad: exact asset names, relative identity terms,
folder/path names, Unity object metadata, typetrees, and object references.
A vehicle may be either a direct asset or an assembly of shared assets.

This pass can also extract a small set of game-native Texture2D PNGs from
identity-bearing bundles for visual inspection. It does not generate artwork.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path

MAGIC = b"UnityFS"
CHUNK = 4 * 1024 * 1024
TARGET_CRDB = "AMC_RingbrothersJavelinDefiant_1972"
TARGET_TERMS = ("AMC", "Ringbrothers", "Javelin", "Defiant", "1972")
DEEP_TYPES = {"MonoBehaviour", "AssetBundle", "GameObject", "Transform", "MeshRenderer", "MeshFilter", "Mesh", "Material", "Animator", "AnimatorController"}
DEEP_PATH_TERMS = ("mesh", "body", "shared", "common", "driver", "model", "car", "metadata")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def token_hits(text: str) -> list[str]:
    n = norm(text)
    return [t for t in TARGET_TERMS if norm(t) in n]


def exact_target(text: str) -> bool:
    return norm(TARGET_CRDB) in norm(text)


def object_names(obj) -> list[str]:
    out = []
    for getter in (lambda: obj.peek_name(), lambda: obj.container):
        try:
            x = getter()
            if x:
                out.append(str(x))
        except Exception:
            pass
    try:
        x = obj.read(check_read=False)
        for attr in ("name", "m_Name"):
            n = getattr(x, attr, None)
            if n:
                out.append(str(n))
    except Exception:
        pass
    return list(dict.fromkeys(out))


def inspect_references(obj) -> list[str]:
    refs = []
    try:
        data = obj.read(check_read=False)
        if hasattr(data, "__dict__"):
            for key, value in data.__dict__.items():
                text = str(value)
                if any(t in norm(text) for t in map(norm, TARGET_TERMS)):
                    refs.append(f"{key}={text}")
    except Exception:
        pass
    return refs[:100]


def safe_value(value, depth=0):
    if depth > 3:
        return str(value)[:300]
    if value is None or isinstance(value, (bool, int, float, str)):
        return value if not isinstance(value, str) else value[:2000]
    if isinstance(value, dict):
        return {str(k): safe_value(v, depth + 1) for k, v in list(value.items())[:80]}
    if isinstance(value, (list, tuple)):
        return [safe_value(v, depth + 1) for v in list(value)[:40]]
    out = {}
    for attr in ("file_id", "path_id", "m_FileID", "m_PathID"):
        try:
            v = getattr(value, attr)
            if v is not None:
                out[attr] = v
        except Exception:
            pass
    if out:
        out["repr"] = str(value)[:1000]
        return out
    return str(value)[:1000]


def typetree_snapshot(obj):
    try:
        tree = obj.read_typetree()
        if isinstance(tree, dict):
            return safe_value(tree)
        return safe_value(tree)
    except Exception as e:
        return {"_typetree_error": repr(e)}


def deep_identity(obj, source_name: str):
    try:
        typ = obj.type.name
    except Exception:
        typ = str(getattr(obj, "type", "unknown"))
    path_l = source_name.lower()
    if typ not in DEEP_TYPES and not any(t in path_l for t in DEEP_PATH_TERMS):
        return None, None
    try:
        data = obj.read(check_read=False)
        text = str(data)
    except Exception:
        return None, None
    if not exact_target(text):
        return None, None
    hits = token_hits(text)
    return hits, text[:12000]


def extract_texture_pngs(env, source_name: str, extract_dir: Path, report: dict):
    """Extract target-bearing Texture2D objects as native PNGs for inspection."""
    if extract_dir is None or report["png_extractions"]["count"] >= report["png_extractions"]["limit"]:
        return
    source_hits = token_hits(source_name)
    if not source_hits:
        return
    for obj in env.objects:
        if report["png_extractions"]["count"] >= report["png_extractions"]["limit"]:
            return
        try:
            if obj.type.name != "Texture2D":
                continue
        except Exception:
            continue
        names = object_names(obj)
        joined = " | ".join(names + [source_name])
        hits = token_hits(joined)
        if not hits:
            continue
        try:
            data = obj.read(check_read=False)
            image = getattr(data, "image", None)
            if image is None:
                continue
            raw_name = next((n for n in names if n), f"texture_{getattr(obj, 'path_id', 'unknown')}")
            safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", raw_name).strip("._") or "texture"
            out_path = extract_dir / f"{report['png_extractions']['count'] + 1:03d}_{safe_name}.png"
            extract_dir.mkdir(parents=True, exist_ok=True)
            image.save(out_path)
            report["png_extractions"]["count"] += 1
            report["png_extractions"]["files"].append({
                "path": str(out_path),
                "source_member": source_name,
                "path_id": getattr(obj, "path_id", None),
                "name": raw_name,
                "matched_tokens": hits,
                "size": image.size,
            })
            print("EXTRACTED PNG:", out_path)
        except Exception as e:
            report["png_extractions"]["errors"].append({
                "source_member": source_name,
                "path_id": getattr(obj, "path_id", None),
                "error": repr(e),
            })


def scan_unity_bundle(bundle_path: Path, source_name: str, obb: Path, report: dict, sha: str, extract_dir: Path | None):
    import UnityPy
    try:
        env = UnityPy.load(str(bundle_path))
    except Exception as e:
        report["bundle_errors"].append({"obb": str(obb), "source_member": source_name, "bundle_sha256": sha, "error": repr(e)})
        return
    objects = list(env.objects)
    report["bundles"].append({"obb": str(obb), "source_member": source_name, "bundle_sha256": sha, "object_count": len(objects)})
    extract_texture_pngs(env, source_name, extract_dir, report)
    for obj in objects:
        names = object_names(obj)
        path_evidence = [source_name]
        joined = " | ".join(names + path_evidence)
        hits = token_hits(joined)
        deep_hits, deep_text = deep_identity(obj, source_name)
        if deep_hits:
            hits = list(dict.fromkeys(hits + deep_hits))
        if not hits:
            continue
        try:
            typ = obj.type.name
        except Exception:
            typ = str(getattr(obj, "type", "unknown"))
        item = {
            "obb": str(obb), "source_member": source_name,
            "bundle_sha256": sha, "path_id": getattr(obj, "path_id", None),
            "type": typ, "names": names,
            "path_evidence": path_evidence,
            "matched_tokens": hits, "token_count": len(hits),
            "references": inspect_references(obj),
        }
        if exact_target(" | ".join(names)) or exact_target(deep_text or "") or (typ == "MonoBehaviour" and "CarMetadata" in source_name):
            item["typetree"] = typetree_snapshot(obj)
        if deep_hits:
            item["data_identity_match"] = True
            item["data_excerpt"] = deep_text
        report["identity_candidates"].append(item)


def scan_archive(path: Path, obb: Path, report: dict, work: Path, extract_dir: Path | None, depth: int = 0, max_depth: int = 3):
    try:
        z = zipfile.ZipFile(path)
    except Exception as e:
        report["archive_errors"].append({"archive": str(path), "error": repr(e), "depth": depth})
        return
    try:
        for index, zi in enumerate(z.infolist()):
            if zi.is_dir():
                continue
            name = zi.filename
            try:
                with z.open(zi) as src:
                    head = src.read(7); src.seek(0)
                    if head == MAGIC:
                        bundle_path = work / f"bundle_{len(report['bundles_seen']):06d}.bundle"
                        with bundle_path.open("wb") as dst:
                            for chunk in iter(lambda: src.read(CHUNK), b""): dst.write(chunk)
                        sha = sha256(bundle_path)
                        if sha in report["seen_bundle_sha256"]: continue
                        report["seen_bundle_sha256"].add(sha)
                        report["bundles_seen"].append({"obb": str(obb), "source_member": name, "depth": depth, "size": zi.file_size, "sha256": sha})
                        scan_unity_bundle(bundle_path, name, obb, report, sha, extract_dir)
                        continue
                    if depth < max_depth and head[:4] == b"PK\x03\x04":
                        nested_path = work / f"nested_{depth}_{index:06d}.zip"
                        with nested_path.open("wb") as dst:
                            for chunk in iter(lambda: src.read(CHUNK), b""): dst.write(chunk)
                        report["nested_archives"].append({"obb": str(obb), "parent_archive": str(path), "source_member": name, "depth": depth + 1})
                        scan_archive(nested_path, obb, report, work, extract_dir, depth + 1, max_depth)
            except Exception as e:
                report["member_errors"].append({"obb": str(obb), "archive": str(path), "source_member": name, "error": repr(e)})
    finally:
        z.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obb", action="append", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--extract-png-dir")
    ap.add_argument("--extract-png-limit", type=int, default=25)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    extract_dir = Path(a.extract_png_dir) if a.extract_png_dir else None
    report = {
        "tool":"KOSD CSR2 6.7.0 Hero Vehicle discovery scanner",
        "target_crdb":TARGET_CRDB,
        "target_terms":list(TARGET_TERMS),
        "search_rule":"exact + relative + folder/path + typetree/data search; asset-derived identity",
        "obbs":[], "bundles_seen":[], "bundles":[], "identity_candidates":[],
        "nested_archives":[], "archive_errors":[], "member_errors":[], "bundle_errors":[],
        "seen_bundle_sha256":set(),
        "png_extractions":{"count":0,"limit":max(0,a.extract_png_limit),"files":[],"errors":[]},
    }
    if extract_dir:
        extract_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="kosd_hv_") as td:
        work = Path(td)
        for arg in a.obb:
            src = Path(arg); info = {"path":str(src), "size":src.stat().st_size, "sha256":sha256(src)}
            try:
                with zipfile.ZipFile(src) as z: info["zip_members"] = len(z.infolist())
                report["obbs"].append(info); scan_archive(src, src, report, work, extract_dir)
            except Exception as e:
                info["zip_error"] = repr(e); report["obbs"].append(info)
    report["seen_bundle_sha256"] = sorted(report["seen_bundle_sha256"])
    report["summary"] = {
        "zip_members":sum(x.get("zip_members",0) for x in report["obbs"]),
        "unityfs_bundles_seen":len(report["bundles_seen"]),
        "unityfs_bundles_loaded":len(report["bundles"]),
        "identity_candidates":len(report["identity_candidates"]),
        "nested_archives":len(report["nested_archives"]),
        "bundle_errors":len(report["bundle_errors"]),
        "pngs_extracted":report["png_extractions"]["count"],
    }
    (out / "hero_vehicle_discovery.json").write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    for item in report["identity_candidates"][:100]:
        print(item["type"], "|", " | ".join(item["names"]), "| path:", item["source_member"], "| tokens:", ",".join(item["matched_tokens"]))


if __name__ == "__main__": main()
