#!/usr/bin/env bash
set -euo pipefail

ROOT="RESEARCH/CSR2/GAME_VERSIONS"
KEEP_VERSIONS=2

log() { printf '[KOSD OBB] %s\n' "$*"; }
fatal() { printf '[KOSD OBB] ERROR: %s\n' "$*" >&2; exit 1; }

command -v unzip >/dev/null || fatal "unzip is required"
command -v sha256sum >/dev/null || fatal "sha256sum is required"

processed=0

while IFS= read -r -d '' obb_dir; do
  mapfile -t chunks < <(find "$obb_dir" -maxdepth 1 -type f -name '*.zip.[0-9][0-9][0-9]' -printf '%f\n' | sort -V)
  (( ${#chunks[@]} > 0 )) || continue

  base="${chunks[0]%.[0-9][0-9][0-9]}"
  expected=1
  for chunk in "${chunks[@]}"; do
    suffix="${chunk##*.}"
    number=$((10#$suffix))
    (( number == expected )) || fatal "Missing chunk ${expected} in ${obb_dir}"
    expected=$((expected + 1))
  done

  zip_path="${obb_dir}/${base}"
  tmp_dir="$(mktemp -d)"
  trap 'rm -rf "$tmp_dir"' EXIT

  log "Reconstructing ${zip_path} from ${#chunks[@]} chunks"
  : > "$zip_path"
  for chunk in "${chunks[@]}"; do
    cat "${obb_dir}/${chunk}" >> "$zip_path"
  done

  log "Verifying ZIP"
  unzip -tq "$zip_path"

  log "Extracting OBB"
  unzip -q "$zip_path" -d "$tmp_dir"
  mapfile -t obbs < <(find "$tmp_dir" -type f -iname '*.obb' -print)
  (( ${#obbs[@]} == 1 )) || fatal "Expected exactly one OBB in ${zip_path}; found ${#obbs[@]}"

  source_obb="${obbs[0]}"
  target_obb="${obb_dir}/$(basename "$source_obb")"
  size="$(stat -c '%s' "$source_obb")"
  sha="$(sha256sum "$source_obb" | awk '{print $1}')"
  (( size > 100000000 )) || fatal "Extracted OBB is unexpectedly small: ${size} bytes"

  log "Verified OBB: ${target_obb} (${size} bytes)"
  log "SHA-256: ${sha}"
  mv -f "$source_obb" "$target_obb"

  rm -f "$zip_path"
  for chunk in "${chunks[@]}"; do
    rm -f "${obb_dir}/${chunk}"
  done

  rm -rf "$tmp_dir"
  trap - EXIT
  processed=$((processed + 1))
done < <(find "$ROOT" -type d -name '*_OBB' -print0 | sort -z)

(( processed > 0 )) || { log "No split OBB sets found; nothing to ingest."; exit 0; }

# Retention policy: keep the newest two game versions per OBB type.
# The version before the previous version is removed after successful ingestion.
while IFS= read -r -d '' obb_parent; do
  mapfile -t versions < <(
    find "$(dirname "$obb_parent")" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' \
      | sort -V
  )
  (( ${#versions[@]} > KEEP_VERSIONS )) || continue

  delete_count=$(( ${#versions[@]} - KEEP_VERSIONS ))
  for ((i=0; i<delete_count; i++)); do
    old="$(dirname "$obb_parent")/${versions[i]}"
    old_obb_dir="$old/$(basename "$obb_parent")"
    [[ -d "$old_obb_dir" ]] || continue
    log "Retention: removing OBB data from old version ${old_obb_dir}"
    find "$old_obb_dir" -maxdepth 1 -type f \( -iname '*.obb' -o -name '*.zip.[0-9][0-9][0-9]' \) -delete
  done
done < <(find "$ROOT" -mindepth 2 -maxdepth 2 -type d -name '*_OBB' -print0 | sort -z)

log "Ingestion complete: ${processed} OBB set(s) processed."
