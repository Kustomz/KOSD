# CSR2 Asset Database Architecture

## Full-version structure

Each full game-version cycle is stored under `ASSET_DATABASE/<version>/`.

A full version contains:

```text
<version>/
├── BASE/
├── MAIN_OBB/
├── PATCH_OBB/
├── EXTRACTED/
└── REPORTS/
```

`GAME_VERSIONS/` is not part of the KOSD architecture.

## OTA sequencing

OTA numbering is sequential within a full-update cycle and does **not** reset when a minor version changes.

Example:

```text
6.7.0 + OTA1
6.7.1 + OTA2
6.7.2 + OTA3
```

Each OTA remains permanently stored under the game version in which that OTA originally dropped. It is not copied or moved into later minor versions.

OTA folders contain only the OTA identifier; they do not contain OBB, `EXTRACTED`, or `REPORTS` folders.

When a new full-update cycle begins (for example `6.9.x` → `7.0.x`), the OTA sequence resets to `OTA1`.

The exact behavior at future version-boundary changes should be verified against the actual game release pattern before assuming a new boundary.

## Shared assets

`RESEARCH/CSR2/SHARED/` is the continuously growing, version-independent vehicle asset library. It is not versioned and is not duplicated per game release.
