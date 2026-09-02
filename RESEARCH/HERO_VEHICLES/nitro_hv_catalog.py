#!/usr/bin/env python3
"""Generate the KOSD Hero Vehicle catalog directly from Nitro's CRDB master list.

Source of truth:
  https://github.com/CSR2-Github-DB/CSR2-DataBase/blob/Everything/1.Cars/%23AllCarCRDBs.txt

Rules:
- Preserve source line order exactly.
- Preserve each CRDB string exactly.
- HV number is 1-based source position.
- Filename is hv-xxx_<exact CRDB>.png.
- Finished HV files are transparent PNGs.
"""
from pathlib import Path
from urllib.request import urlopen

SOURCE = "https://raw.githubusercontent.com/CSR2-Github-DB/CSR2-DataBase/Everything/1.Cars/%23AllCarCRDBs.txt"
OUT = Path(__file__).with_name("HERO_VEHICLE_CATALOG.md")


def main():
    raw = urlopen(SOURCE, timeout=60).read().decode("utf-8")
    crdbs = [line.strip() for line in raw.splitlines() if line.strip()]
    if not crdbs:
        raise SystemExit("Nitro CRDB source returned no entries")

    lines = [
        "# KOSD Hero Vehicle Catalog",
        "",
        "Source: Nitro `CSR2-DataBase/1.Cars/#AllCarCRDBs.txt` (ref `Everything`)",
        "",
        "Naming: `hv-xxx_<exact CRDB>.png`",
        "",
        "| HV | Exact CRDB | Filename |",
        "|---:|---|---|",
    ]
    for number, crdb in enumerate(crdbs, 1):
        lines.append(f"| {number:03d} | `{crdb}` | `hv-{number:03d}_{crdb}.png` |")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {len(crdbs)} Hero Vehicle entries: {OUT}")


if __name__ == "__main__":
    main()
