#!/usr/bin/env python3
"""Diagnose CSR2 6.7.0 OBB container structure without modifying source data."""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

CHUNK = 4 * 1024 * 1024
MAGICS = (
    b"UnityFS",
    b"UnityRaw",
    b"UnityWeb",
    b"PK\x03\x04",
    b"PK\x05\x06",
    b"PK\x07\x08",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def first64(path: Path) -> str:
    with path.open("rb") as f:
        return f.read(64).hex()


def find_all_magics(path: Path, limit: int = 100) -> dict[str, list[int]]:
    """Scan the file once for all signatures instead of rereading the OBB per magic."""
    hits = {m.decode("latin1"): [] for m in MAGICS}
    max_magic = max(len(m) for m in MAGICS)
    carry = b""
    base = 0
    with path.open("rb") as f:
        while True:
            block = f.read(CHUNK)
            if not block:
                break
            data = carry + block
            data_base = base - len(carry)
            for magic in MAGICS:
                key = magic.decode("latin1")
                if len(hits[key]) >= limit:
                    continue
                start = 0
                while len(hits[key]) < limit:
                    pos = data.find(magic, start)
                    if pos < 0:
                        break
                    hits[key].append(data_base + pos)
                    start = pos + 1
            carry = data[-(max_magic - 1):]
            base += len(block)
    return {k: v for k, v in hits.items() if v}


def inspect_zip(path: Path) -> dict:
    result: dict = {}
    try:
        with zipfile.ZipFile(path) as z:
            infos = z.infolist()
            result["zip_valid"] = True
            result["zip_entries"] = len(infos)
            result["zip_comment_len"] = len(z.comment)
            result["entries"] = []
            for zi in infos[:100]:
                entry = {
                    "name": zi.filename,
                    "compressed": zi.compress_size,
                    "uncompressed": zi.file_size,
                    "method": zi.compress_type,
                }
                try:
                    with z.open(zi) as f:
                        data = f.read(128)
                    entry["first128_hex"] = data.hex()
                    entry["magic_hits"] = {
                        m.decode("latin1"): [i for i in range(len(data) - len(m) + 1) if data.startswith(m, i)]
                        for m in MAGICS
                        if m in data
                    }
                except Exception as exc:
                    entry["read_error"] = repr(exc)
                result["entries"].append(entry)
    except Exception as exc:
        result["zip_valid"] = False
        result["zip_error"] = repr(exc)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--obb", action="append", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    report = []

    for raw in args.obb:
        path = Path(raw)
        item = {"path": str(path)}
        try:
            item["size"] = path.stat().st_size
            item["sha256"] = sha256(path)
            item["first64_hex"] = first64(path)
            item.update(inspect_zip(path))
            item["direct_magic_hits"] = find_all_magics(path)
        except Exception as exc:
            item["diagnostic_error"] = repr(exc)
        report.append(item)
        out.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")

    out.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")
    print(json.dumps(report, indent=2)[:50000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
