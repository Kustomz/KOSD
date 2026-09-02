# KOSD ↔ Recovery Reconciliation — v1.7

**Date:** 2026-09-02

This recovery update locks the current CSR2 SCB restoration-requirement investigation checkpoint into KOSD. Recovery remains the source for recovered project-state context; research findings are not silently promoted to authoritative KOS policy.

## Recovery Source Reconciliation

The current recovery package is `KUSTOMZ_PROJECT_RECOVERY_v1.7_UPDATED_KOSD.zip`. Its contents are the basis for this reconciliation; the ZIP itself is a recovery distribution package and is not required to be stored as a KOSD binary artifact.

## Added Research Checkpoint

The current investigation is preserved under:

`RESEARCH/CSR2/SCB_RESTORATION_REQUIREMENTS_6.7.0.md`

The checkpoint covers the 6.7.0 Main OBB and Patch OBB, the Ferrari 250 GTO Classic 1962 RestorationManifest target, the reported SCB value of 14,800, and the required evidence chain from original game data through serialized Unity data to the SCB display value.

## Canonical OBB State

- 6.7.0 Main OBB is canonical in KOSD under `RESEARCH/CSR2/GAME_VERSIONS/6.7.0/MAIN_OBB/` using Git LFS.
- 6.7.0 Patch OBB is canonical in KOSD under `RESEARCH/CSR2/GAME_VERSIONS/6.7.0/PATCH_OBB/` using Git LFS.
- Split transport chunks and reconstructed ZIPs are not the source of truth after successful ingestion.
- The reusable ingestion workflow applies to both MAIN and PATCH OBB sets.

## Locked Investigation Boundary

**Proven:** The target Ferrari RestorationManifest exists in the 6.7.0 Main OBB.

**Unresolved:** The exact serialized field/key producing 14,800; whether the value is stored or derived; whether Patch contributes; whether the same structure supplies all Legend restoration requirements; and the exact SCB display derivation.

## Migration Rules Preserved

- Migrate; do not recreate.
- Preserve locked content and stable IDs.
- Keep research, review, validation, release, and historical states distinguishable.
- Do not silently promote research findings to authoritative KOS rules.
- Record evidence and provenance separately from conclusions.
- Release only validated modules.

## Pause Boundary

The SCB restoration-requirement investigation is paused at the exact evidence boundary above. Resume by decoding the Unity AssetBundle and serialized RestorationManifest data; do not restart from assumptions or replace the checkpoint with an inferred answer.
