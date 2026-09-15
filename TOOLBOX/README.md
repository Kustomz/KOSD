# Kustomz Toolbox

The Kustomz Toolbox is the user-facing tool layer of KOSD.

It provides the practical file-editing and game-data tools built from the research, specifications, and source-of-truth data maintained elsewhere in KOSD.

## Toolbox Areas

- **NSB** — NSB save/file tools and related capabilities.
- **SCB** — SCB tools.
- **Garage** — Garage tools.
- **Legends** — Legends tools.
- **Fusions** — Fusion tools.
- **Stage Six** — Stage Six tools.
- **TRB** — TRB tools.

## Repository Separation

- `CORE/` — KOSD governance, standards, and core specifications.
- `ACQUISITION/` — acquired source APK/OBB artifacts.
- `RESEARCH/` — researched and verified game data.
- `WORKFLOWS/` — KOSD research/processing workflows.
- `TOOLBOX/` — the user-facing Toolbox implementation.

## Rule

Toolbox functionality must use verified KOSD source-of-truth data and established specifications. Do not invent game data or substitute mock data for real source data.
