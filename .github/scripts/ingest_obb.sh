#!/usr/bin/env bash
set -euo pipefail

SOURCE_ROOT="ACQUISITION"
ROOT="RESEARCH/CSR2/GAME_VERSIONS"
KEEP_VERSIONS=2
EXPECTED_PACKAGE="com.naturalmotion.customstreetracer2"

log() { printf '[KOSD OBB] %s\n' "$*"; }
fatal() { printf '[KOSD OBB] ERROR: %s\n' "$*" >&2; exit 1; }

command -v unzip >/dev/null || fatal "unzip is required"
command -v sha256sum >/dev/null || fatal "sha256sum is required"
command -v git >/dev/null || fatal "git is required"

git lfs version >/dev/null 2>&1 || fatal "git-lfs is required"

git lfs pull

processed=0

while IFS= read -r -d '' version_dir; do
  version="$(basename "$version_dir")"
  [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || continue

  package_dir="$version_dir/$EXPECTED_PACKAGE"
  [[ -d "$package_dir" ]] || continue

  mapfile -t obbs < <(find "$package_dir" -maxdepth 1 -type f -iname '*.obb' -printf '%f\n' | sort -V)
  (( ${#obbs[@]} > 0 )) || continue

  for obb in "${obbs[@]}"; do
    source_path="$package_dir/$obb"
    size="$(stat -c '%s' "$source_path")"
    (( size > 100000000 )) || fatal "OBB is unexpectedly small: ${source_path} (${size} bytes)"

    case "$(basename "$obb" | tr '[:upper:]' '[:lower:]')" in
      main.obb) target_dir="$ROOT/$version/MAIN_OBB" ;;
      patch.obb) target_dir="$ROOT/$version/PATCH_OBB" ;;
      *) fatal "Unsupported OBB filename: $obb (expected main.obb or patch.obb)" ;;
    esac

    mkdir -p "$target_dir"
    target_path="$target_dir/$(basename "$obb")"
    sha="$(sha256sum "$source_path" | awk '{print $1}')"

    log "Verified OBB: ${source_path} (${size} bytes)"
    log "SHA-256: ${sha}"
    cp -f "$source_path" "$target_path"
    rm -f "$source_path"
    processed=$((processed + 1))
  done

done < <(find "$SOURCE_ROOT" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

# Retention policy: keep the newest two game versions per OBB type.
# Older canonical OBB data is removed after successful ingestion.
while IFS= read -r -d '' obb_parent; do
  mapfile -t versions < <(
    find "$(dirname "$obb_parent")" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' \
      | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' \
      | sort -V
  )
  (( ${#versions[@]} > KEEP_VERSIONS )) || continue

  delete_count=$(( ${#versions[@]} - KEEP_VERSIONS ))
  for ((i=0; i<delete_count; i++)); do
    old="$(dirname "$obb_parent")/${versions[i]}"
    old_obb_dir="$old/$(basename "$obb_parent")"
    [[ -d "$old_obb_dir" ]] || continue
    log "Retention: removing OBB data from old version ${old_obb_dir}"
    find "$old_obb_dir" -maxdepth 1 -type f -iname '*.obb' -delete
  done
done < <(find "$ROOT" -mindepth 2 -maxdepth 2 -type d -name '*_OBB' -print0 | sort -z)

log "Ingestion complete: ${processed} OBB file(s) processed."
