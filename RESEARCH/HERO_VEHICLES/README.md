# KOSD Hero Vehicles

## Source of truth

Hero Vehicle source assets come from:

`RESEARCH/CSR2/GAME_VERSIONS/6.7.0/SHARED`

**Do not use the 6.7.0 Main OBB or Patch OBB as the Hero Vehicle source.** Those OBBs belong to separate CSR2 forensic research workflows.

## Ordering

HV numbering follows Nitro's `CSR2-DataBase/1.Cars/#AllCarCRDBs.txt` order exactly.

## Filename

`hv-xxx_<exact CRDB>.png`

- `xxx` is the 1-based Nitro list position.
- The CRDB portion is copied exactly from Nitro's list.
- Final assets are transparent PNGs with a true alpha channel.

## Production pipeline

`Nitro CRDB order → 6.7.0 SHARED car asset → extraction → isolated vehicle → transparent PNG → approval → frozen Hero Vehicle master`

No artwork generation is part of the catalog/source setup step.
