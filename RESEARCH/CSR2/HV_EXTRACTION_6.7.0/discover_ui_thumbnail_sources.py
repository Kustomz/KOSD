#!/usr/bin/env python3
"""Broad inventory of likely CSR2 2D vehicle-thumbnail sources in 6.7.0 OBBs.

This is discovery only: it does not render 3D models or label an image as a
vehicle thumbnail unless its source/name metadata supports that conclusion.
"""
import hashlib, json, os, re, zipfile
from pathlib import Path
import UnityPy

OBBS = [os.environ["MAIN_OBB"], os.environ["PATCH_OBB"]]
OUT = Path("hv-output/ui-thumbnail-discovery")
IMG = OUT / "textures"
OUT.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

TARGETS = [
"Bentley_ContinentalGTV8SF8_2014","Chevrolet_CorvetteStingRayC2F8_1966",
"Dodge_ChallengerSRTDemonF8_2018","Dodge_ChargerRTF1_1970","Dodge_ChargerRTF8_1970",
"FnF_FlipCar_2013","Honda_S2000F2_2001","Jaguar_FTypeRCoupeF8_2016",
"Lamborghini_MurcielagoLP640F8_2006","LocalMotor_RallyFighterF8_2013",
"Mazda_RX7F1_1993","Mazda_RX7F3_1993","MercedesAMG_GTSF8_2015",
"Mitsubishi_EclipseF1_1995","Mitsubishi_LancerEvolutionVIIF2_2002",
"Nissan_350ZF3_2003","Nissan_SkylineGTRF4_2002","Nissan_SkylineGTRR34F2_1999",
"Plymouth_RoadRunnerGTXF8_1971","Subaru_BRZF8_2013","Subaru_WRXSTIF8_2018",
"Toyota_SupraMKIVF1_1994","Volkswagen_JettaF1_1995"]
def norm(x): return re.sub(r"[^a-z0-9]", "", str(x).lower())
target_norm = {norm(t):t for t in TARGETS}
terms = ("icon","thumbnail","thumb","garage","showroom","selection","carselect",
         "vehicle","carimage","car_image","cardetail","roster","portrait","2d",
         "caricon","caricons","ui_car","ui-car")
report = {"source_version":"6.7.0","targets":TARGETS,"obbs":[],"candidate_members":[],
          "textures":[],"errors":[],"notes":[
          "Broad source discovery only; extracted textures are not assumed to be the final thumbnail.",
          "No 3D rendering or image recreation is performed.",
          "Target matches include exact CRDB-like names and normalized fragments; generic UI candidates are separately tagged."]}
seen_hashes=set()
for obb_path in OBBS:
    zf=zipfile.ZipFile(obb_path)
    report["obbs"].append({"path":obb_path,"bytes":Path(obb_path).stat().st_size,"members":len(zf.infolist())})
    for info in zf.infolist():
        member=info.filename
        nm=norm(member)
        target_hits=[t for key,t in target_norm.items() if key in nm]
        keyword_hits=[term for term in terms if norm(term) in nm]
        # Include exact target-path hits plus broad UI/car imagery candidates.
        if not target_hits and not keyword_hits:
            continue
        if info.is_dir() or info.file_size == 0: continue
        report["candidate_members"].append({"obb":Path(obb_path).name,"member":member,
            "size":info.file_size,"target_path_hits":target_hits,"keyword_hits":keyword_hits})
        # Parse only likely serialized bundles/assets; raw images are read directly.
        try:
            data=zf.read(info)
            if member.lower().endswith((".png",".jpg",".jpeg",".webp")):
                key=hashlib.sha256(data).hexdigest()
                if key in seen_hashes: continue
                seen_hashes.add(key)
                dest=IMG/(key[:16]+Path(member).suffix.lower())
                dest.write_bytes(data)
                report["textures"].append({"obb":Path(obb_path).name,"member":member,
                    "target_path_hits":target_hits,"keyword_hits":keyword_hits,"format":"direct-image",
                    "output":str(dest),"bytes":len(data),"sha256":key})
                continue
            # Avoid attempting UnityPy on arbitrary text/config files.
            if not any(x in member.lower() for x in (".astc",".bundle",".assets",".assetbundle",".ab")):
                continue
            env=UnityPy.load(data)
            for idx,obj in enumerate(env.objects):
                if obj.type.name != "Texture2D": continue
                try:
                    tex=obj.read()
                    image=getattr(tex,"image",None)
                    if image is None: continue
                    texname=str(getattr(tex,"m_Name","") or "")
                    name_norm=norm(texname)
                    name_hits=[t for key,t in target_norm.items() if key in name_norm or name_norm in key]
                    if not target_hits and not name_hits and not keyword_hits:
                        continue
                    image.save(IMG/f"{hashlib.sha256((member+str(idx)+texname).encode()).hexdigest()[:16]}.png")
                    dest=IMG/f"{hashlib.sha256((member+str(idx)+texname).encode()).hexdigest()[:16]}.png"
                    pixels=image.convert("RGB")
                    colors=len(pixels.getcolors(maxcolors=1000000) or [])
                    report["textures"].append({"obb":Path(obb_path).name,"member":member,
                        "target_path_hits":target_hits,"texture_name":texname,"texture_name_target_hits":name_hits,
                        "keyword_hits":keyword_hits,"width":image.width,"height":image.height,"mode":image.mode,
                        "unique_rgb_colors_sampled":colors,"output":str(dest),
                        "sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
                except Exception as e:
                    report["errors"].append({"member":member,"object_index":idx,"error":repr(e)})
        except Exception as e:
            # Not every candidate member is a Unity bundle; preserve errors as diagnostics.
            report["errors"].append({"member":member,"error":repr(e)})
    zf.close()
report["summary"]={"obb_member_counts":{x["path"]:x["members"] for x in report["obbs"]},
    "candidate_members":len(report["candidate_members"]),"texture_outputs":len(report["textures"]),
    "target_names_mentioned_in_paths":sorted({t for x in report["candidate_members"] for t in x["target_path_hits"]}),
    "texture_names_with_target_matches":sorted({t for x in report["textures"] for t in x.get("texture_name_target_hits",[])}),
    "errors":len(report["errors"])}
(OUT/"ui_thumbnail_discovery_report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report["summary"],indent=2))
