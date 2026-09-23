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

normalize_version() {
  local raw="$1"
  if [[ "$raw" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    printf '%s' "$raw"
  elif [[ "$raw" =~ ^([0-9])([0-9])([0-9])$ ]]; then
    printf '%s.%s.%s' "${BASH_REMATCH[1]}" "${BASH_REMATCH[2]}" "${BASH_REMATCH[3]}"
  else
    return 1
  fi
}

canonical_obb_name() {
  local obb="$1"
  local lower="$(basename "$obb" | tr '[:upper:]' '[:lower:]')"
  case "$lower" in
    main.obb|patch.obb)
      printf '%s' "$lower"
      ;;
    main_[0-9]*.com.naturalmotion.customstreetracer2.obb)
      printf 'main.%s.com.naturalmotion.customstreetracer2.obb' "${lower#main_}" | sed 's/\.com\..*/.com.naturalmotion.customstreetracer2.obb/'
      ;;
    patch_[0-9]*.com.naturalmotion.customstreetracer2.obb)
      printf 'patch.%s.com.naturalmotion.customstreetracer2.obb' "${lower#patch_}" | sed 's/\.com\..*/.com.naturalmotion.customstreetracer2.obb/'
      ;;
    main.[0-9]*.com.naturalmotion.customstreetracer2.obb|patch.[0-9]*.com.naturalmotion.customstreetracer2.obb)
      printf '%s' "$lower"
      ;;
    *)
      return 1
      ;;
  esac
}

# Pull only acquisition OBBs this run can process. Do not perform an
# unfiltered multi-GB LFS pull.
mapfile -t acquisition_obb_paths < <(find "$SOURCE_ROOT" -type f -path "*/$EXPECTED_PACKAGE/*.obb" -print | sort)
if (( ${#acquisition_obb_paths[@]} > 0 )); then
  git lfs install --local
  include_list="$(printf '%s,' "${acquisition_obb_paths[@]}")"
  include_list="${include_list%,}"
  log "Pulling only acquisition OBBs: ${#acquisition_obb_paths[@]} file(s)"
  git lfs pull --include="$include_list"
else
  log "No acquisition OBBs found; nothing to pull."
fi

processed=0

while IFS= read -r -d '' version_dir; do
  raw_version="$(basename "$version_dir")"
  version="$(normalize_version "$raw_version")" || fatal "Unrecognized ACQUISITION version directory: $version_dir"

  package_dir="$version_dir/$EXPECTED_PACKAGE"
  [[ -d "$package_dir" ]] || { log "Skipping $version_dir: expected package directory is absent"; continue; }

  mapfile -t obbs < <(find "$package_dir" -maxdepth 1 -type f -iname '*.obb' -printf '%f\n' | sort -V)
  (( ${#obbs[@]} > 0 )) || { log "Skipping $version_dir: no OBB files found"; continue; }

  for obb in "${obbs[@]}"; do
    source_path="$package_dir/$obb"
    size="$(stat -c '%s' "$source_path")"
    (( size > 100000000 )) || fatal "OBB is unexpectedly small: $source_path ($size bytes)"

    target_name="$(canonical_obb_name "$obb")" || fatal "Unsupported OBB filename: $obb"
    case "$target_name" in
      main*) target_dir="$ROOT/$version/MAIN_OBB" ;;
      patch*) target_dir="$ROOT/$version/PATCH_OBB" ;;
      *) fatal "Unable to classify canonical OBB filename: $target_name" ;;
    esac

    mkdir -p "$target_dir"
    target_path="$target_dir/$target_name"
    sha="$(sha256sum "$source_path" | awk '{print $1}')"

    log "Verified OBB: $source_path ($size bytes)"
    log "SHA-256: $sha"
    log "Promoting: $source_path -> $target_path"
    cp -f "$source_path" "$target_path"
    rm -f "$source_path"
    processed=$((processed + 1))
  done

done < <(find "$SOURCE_ROOT" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

# Retention policy: keep the newest two game versions per OBB type.
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
    log "Retention: removing OBB data from old version $old_obb_dir"
    find "$old_obb_dir" -maxdepth 1 -type f -iname '*.obb' -delete
  done
done < <(find "$ROOT" -mindepth 2 -maxdepth 2 -type d -name '*_OBB' -print0 | sort -z)

log "Ingestion complete: $processed OBB file(s) processed."
