#!/usr/bin/env python3
"""KOSD CSR2 6.7.0 Hero Vehicle discovery scanner.

Research/acquisition stage only. The canonical 6.7.0 OBBs are ZIP containers
whose members include UnityFS bundles. Discovery therefore works at the ZIP
member boundary instead of carving UnityFS signatures out of the compressed
OBB byte stream. Vehicle lookup is deliberately relative: candidate assets
are surfaced from internal Unity object identity evidence, rather than by
requiring an exact CRDB folder/file name.
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
TARGET_TOKENS = ("AMC", "Ringbrothers", "Javelin", "Defiant", "1972")


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
    return [t for t in TARGET_TOKENS if norm(t) in n]


def object_names(obj) -> list[str]:
    out: list[str] = []
    try:
        x = obj.peek_name()
        if x:
            out.append(str(x))
    except Exception:
        pass
    try:
        if obj.container:
            out.append(str(obj.container))
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


def scan_unity_bundle(bundle_path: Path, source_name: str, obb: Path, report: dict, sha: str):
    import UnityPy

    try:
        env = UnityPy.load(str(bundle_path))
    except Exception as e:
        report["bundle_errors"].append({
            "obb": str(obb),
            "source_member": source_name,
            "bundle_sha256": sha,
            "error": repr(e),
        })
        return

    objects = list(env.objects)
    bundle_record = {
        "obb": str(obb),
        "source_member": source_name,
        "bundle_sha256": sha,
        "object_count": len(objects),
    }
    report["bundles"].append(bundle_record)

    for obj in objects:
        names = object_names(obj)
        if not names:
            continue
        joined = " | ".join(names)
        hits = token_hits(joined)
        if not hits:
            continue
        try:
            typ = obj.type.name
        except Exception:
            typ = str(getattr(obj, "type", "unknown"))
        evidence = {
            "obb": str(obb),
            "source_member": source_name,
            "bundle_sha256": sha,
            "path_id": getattr(obj, "path_id", None),
            "type": typ,
            "names": names,
            "matched_tokens": hits,
            "token_count": len(hits),
        }
        report["identity_candidates"].append(evidence)


def scan_archive(path: Path, obb: Path, report: dict, work: Path, depth: int = 0, max_depth: int = 3):
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
                    head = src.read(7)
                    src.seek(0)
                    if head == MAGIC:
                        bundle_path = work / f"bundle_{len(report['bundles_seen']):06d}.bundle"
                        with bundle_path.open("wb") as dst:
                            for chunk in iter(lambda: src.read(CHUNK), b""):
                                dst.write(chunk)
                        sha = sha256(bundle_path)
                        if sha in report["seen_bundle_sha256"]:
                            continue
                        report["seen_bundle_sha256"].add(sha)
                        report["bundles_seen"].append({
                            "obb": str(obb),
                            "source_member": name,
                            "depth": depth,
                            "size": zi.file_size,
                            "sha256": sha,
                        })
                        scan_unity_bundle(bundle_path, name, obb, report, sha)
                        continue

                    if depth < max_depth and head[:4] == b"PK\x03\x04":
                        nested_path = work / f"nested_{depth}_{index:06d}.zip"
                        with nested_path.open("wb") as dst:
                            for chunk in iter(lambda: src.read(CHUNK), b""):
                                dst.write(chunk)
                        report["nested_archives"].append({
                            "obb": str(obb),
                            "parent_archive": str(path),
                            "source_member": name,
                            "depth": depth + 1,
                        })
                        scan_archive(nested_path, obb, report, work, depth + 1, max_depth)
            except Exception as e:
                report["member_errors"].append({
                    "obb": str(obb),
                    "archive": str(path),
                    "source_member": name,
                    "error": repr(e),
                })
    finally:
        z.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obb", action="append", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    report = {
        "tool": "KOSD CSR2 6.7.0 Hero Vehicle discovery scanner",
        "target_crdb": TARGET_CRDB,
        "target_tokens": list(TARGET_TOKENS),
        "search_rule": "relative discovery; asset-derived identity evidence",
        "obbs": [],
        "bundles_seen": [],
        "bundles": [],
        "identity_candidates": [],
        "nested_archives": [],
        "archive_errors": [],
        "member_errors": [],
        "bundle_errors": [],
        "seen_bundle_sha256": set(),
    }

    with tempfile.TemporaryDirectory(prefix="kosd_hv_") as td:
        work = Path(td)
        for arg in a.obb:
            src = Path(arg)
            info = {"path": str(src), "size": src.stat().st_size, "sha256": sha256(src)}
            try:
                with zipfile.ZipFile(src) as z:
                    info["zip_members"] = len(z.infolist())
                report["obbs"].append(info)
                scan_archive(src, src, report, work)
            except Exception as e:
                info["zip_error"] = repr(e)
                report["obbs"].append(info)

    report["seen_bundle_sha256"] = sorted(report["seen_bundle_sha256"])
    report["summary"] = {
        "zip_members": sum(x.get("zip_members", 0) for x in report["obbs"]),
        "unityfs_bundles_seen": len(report["bundles_seen"]),
        "unityfs_bundles_loaded": len(report["bundles"]),
        "identity_candidates": len(report["identity_candidates"]),
        "nested_archives": len(report["nested_archives"]),
        "bundle_errors": len(report["bundle_errors"]),
    }

    (out / "hero_vehicle_discovery.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(report["summary"], indent=2))
    for item in report["identity_candidates"][:100]:
        print(item["type"], "|", " | ".join(item["names"]), "| tokens:", ",".join(item["matched_tokens"]))


if __name__ == "__main__":
    main()
