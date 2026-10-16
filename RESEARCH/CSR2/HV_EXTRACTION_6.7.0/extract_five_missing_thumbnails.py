#!/usr/bin/env python3
"""Exhaustive 6.7.0 OBB texture pass for the five missing original 2D car thumbnails.

Scans every archive member that looks like a Unity serialized file/bundle, not just
members whose paths contain UI keywords. It never renders 3D models.
"""
import hashlib, json, os, re, zipfile
from pathlib import Path
from PIL import Image, ImageDraw
import UnityPy

OBBS = [os.environ["MAIN_OBB"], os.environ["PATCH_OBB"]]
OUT = Path("hv-output/five-missing-thumbnails")
IMG = OUT / "textures"
OUT.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

TARGETS = [
    "Mazda_RX7F3_1993",
    "Nissan_350ZF3_2003",
    "Nissan_SkylineGTRF4_2002",
    "Volkswagen_JettaF1_1995",
    "FnF_FlipCar_2013",
]
def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())
def target_hits(text):
    n = norm(text)
    return [t for t in TARGETS if norm(t) in n or n in norm(t)]

report = {
    "source_version": "6.7.0",
    "targets": TARGETS,
    "method": "Scan all OBB members with known Unity bundle/serialized extensions or UnityFS/UnityRaw signatures; inspect all object names and Texture2D assets. Export unique Texture2D images at least 96x96 regardless of aspect ratio, including square and portrait textures. No 3D rendering.",
    "obb_member_counts": {},
    "serialized_members_scanned": [],
    "target_object_name_hits": [],
    "textures": [],
    "errors": [],
}
seen_hashes = set()
candidate_paths = []

for obb_path in OBBS:
    with zipfile.ZipFile(obb_path) as zf:
        report["obb_member_counts"][Path(obb_path).name] = len(zf.infolist())
        for info in zf.infolist():
            if info.is_dir() or info.file_size < 16:
                continue
            member = info.filename
            low = member.lower()
            if not low.endswith((".astc", ".bundle", ".assets", ".assetbundle", ".ab", ".resource", ".resS", ".bytes")):
                # Include extensionless/oddly named Unity bundles by their header.
                try:
                    with zf.open(info) as f:
                        magic = f.read(16)
                except Exception:
                    continue
                if not (magic.startswith(b"UnityFS") or magic.startswith(b"UnityRaw") or magic.startswith(b"UnityWeb")):
                    continue
            try:
                data = zf.read(info)
                if not (data.startswith((b"UnityFS", b"UnityRaw", b"UnityWeb")) or low.endswith((".assets", ".assetbundle", ".bundle", ".ab", ".astc", ".resource", ".ress", ".bytes"))):
                    continue
                env = UnityPy.load(data)
                report["serialized_members_scanned"].append({"obb": Path(obb_path).name, "member": member, "bytes": info.file_size, "objects": len(env.objects)})
                for idx, obj in enumerate(env.objects):
                    try:
                        typ = obj.type.name
                        read = obj.read()
                        obj_name = str(getattr(read, "m_Name", "") or getattr(read, "name", "") or "")
                        hits = target_hits(obj_name + " " + member)
                        if hits:
                            report["target_object_name_hits"].append({
                                "obb": Path(obb_path).name, "member": member, "object_index": idx,
                                "type": typ, "object_name": obj_name, "target_hits": hits
                            })
                        if typ != "Texture2D":
                            continue
                        image = getattr(read, "image", None)
                        if image is None:
                            continue
                        w, h = image.size
                        # Keep target-related textures regardless of size; otherwise retain plausible
                        # 2D card/sprite/thumbnail shapes for a review contact sheet.
                        plausible = w >= 96 and h >= 96 and w <= 4096 and h <= 4096
                        if not hits and not plausible:
                            continue
                        rgba = image.convert("RGBA")
                        rgb_hash = hashlib.sha256(rgba.tobytes()).hexdigest()
                        if rgb_hash in seen_hashes:
                            continue
                        seen_hashes.add(rgb_hash)
                        fname = hashlib.sha256((member + "|" + str(idx) + "|" + obj_name).encode()).hexdigest()[:16] + ".png"
                        dest = IMG / fname
                        rgba.save(dest)
                        entry = {
                            "obb": Path(obb_path).name, "member": member, "object_index": idx,
                            "texture_name": obj_name, "target_hits": hits, "width": w, "height": h,
                            "mode": image.mode, "output": str(dest), "pixel_sha256": rgb_hash,
                            "plausible_thumbnail_shape": plausible,
                        }
                        report["textures"].append(entry)
                        if plausible or hits:
                            candidate_paths.append((dest, entry))
                    except Exception as e:
                        report["errors"].append({"member": member, "object_index": idx, "error": repr(e)})
            except Exception as e:
                # Some entries use non-Unity binary payloads despite their extensions.
                if low.endswith((".assets", ".assetbundle", ".bundle", ".ab", ".astc")):
                    report["errors"].append({"member": member, "error": repr(e)})

# Contact sheets make the broad candidate pool practical to inspect.
thumb_w, thumb_h, label_h = 180, 110, 34
per_sheet = 100
for page, start in enumerate(range(0, len(candidate_paths), per_sheet), 1):
    subset = candidate_paths[start:start + per_sheet]
    cols = 5
    rows = (len(subset) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (path, meta) in enumerate(subset):
        im = Image.open(path).convert("RGBA")
        im.thumbnail((thumb_w - 8, thumb_h - 8))
        x = (i % cols) * thumb_w
        y = (i // cols) * (thumb_h + label_h)
        bg = Image.new("RGBA", (thumb_w - 8, thumb_h - 8), (220, 220, 220, 255))
        bg.alpha_composite(im, ((bg.width - im.width)//2, (bg.height - im.height)//2))
        sheet.paste(bg.convert("RGB"), (x + 4, y + 4))
        label = (meta["texture_name"] or Path(meta["member"]).name)[:26]
        draw.text((x + 4, y + thumb_h), label, fill="black")
        draw.text((x + 4, y + thumb_h + 14), f'{meta["width"]}x{meta["height"]} | {meta["obb"][:4]}', fill="black")
    sheet.save(OUT / f"contact-sheet-{page:02d}.jpg", quality=88)

report["summary"] = {
    "obb_member_counts": report["obb_member_counts"],
    "serialized_members_scanned": len(report["serialized_members_scanned"]),
    "target_object_name_hits": len(report["target_object_name_hits"]),
    "unique_texture_outputs": len(report["textures"]),
    "contact_sheets": (len(candidate_paths) + per_sheet - 1) // per_sheet,
    "errors": len(report["errors"]),
}
(OUT / "five_missing_thumbnail_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report["summary"], indent=2))
