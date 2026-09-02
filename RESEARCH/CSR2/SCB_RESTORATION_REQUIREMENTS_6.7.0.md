# CSR2 SCB Restoration Requirements — 6.7.0 Investigation Checkpoint

**Status:** PAUSED — checkpoint locked for recovery
**Date:** 2026-09-02
**Scope:** CSR2 6.7.0 Main OBB + Patch OBB

## Objective

Determine the actual source of the SCB **“Required to restore”** values, with primary target **Ferrari 250 GTO Classic 1962** and the reported **14,800** requirement.

The investigation must trace the value from the original game data rather than infer it from the SCB interface or an edited NSB/SCB file.

## Required Evidence Chain

1. Canonical CSR2 6.7.0 Main OBB and Patch OBB.
2. `Ferrari_250GTOClassic_1962_RestorationManifest.ASTC.27` and its containing Unity AssetBundle data.
3. The exact serialized Unity object/structure represented by that RestorationManifest.
4. The exact field, key, property, array element, or referenced object that produces **14,800**.
5. Verification against additional Legend restoration manifests to determine whether the same structure supplies their restoration requirements.
6. Determine how the game/SCB derives and displays **“Required to restore.”**

## Known Evidence

- 6.7.0 Main OBB is stored in KOSD as the canonical Git LFS artifact under `RESEARCH/CSR2/GAME_VERSIONS/6.7.0/MAIN_OBB/`.
- 6.7.0 Patch OBB is stored in KOSD as the canonical Git LFS artifact under `RESEARCH/CSR2/GAME_VERSIONS/6.7.0/PATCH_OBB/`.
- The Main OBB contains `assets/AppDataRoot/AssetBundles/ASTC/Ferrari_250GTOClassic_1962_RestorationManifest.ASTC.27`.
- A raw OBB string/path search previously located that asset and identified the surrounding OBB offsets, but this does **not** yet prove the serialized field producing 14,800.

## Evidence Boundary

**Proven:** The target RestorationManifest exists in the 6.7.0 Main OBB.

**Not yet proven:** The exact serialized field/key producing 14,800; whether the value is stored directly or derived; whether Patch contributes to the requirement; whether all Legend restoration requirements use the same structure; and the exact SCB display derivation.

## Investigation Rule

Do not promote an inferred field or guessed mapping to KOS authority. The next research step is to decode the Unity AssetBundle/serialized data and establish the exact provenance of the requirement value.

## Recovery Checkpoint

This document is the authoritative research checkpoint for resuming the SCB restoration-value investigation. Preserve the distinction between evidence, interpretation, and eventual validated KOS implementation.
