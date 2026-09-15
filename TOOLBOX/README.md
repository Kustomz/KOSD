# Kustomz Toolbox

The Kustomz Toolbox is the user-facing tool system of KOSD.

It is **one synchronized Toolbox delivered through three clients**:

- **Web**
- **Discord**
- **Android APK**

These are not separate toolboxes. They use the same Toolbox functionality and shared state/data model, with each client providing its appropriate interface.

## Main Toolbox Navigation

The Toolbox follows the established editor-suite navigation structure:

- **Home**
- **NSB**
- **SCB**
- **Garage**
- **Legends**
- **Fusions**
- **Stage Six**
- **TRB**

The navigation structure is the starting point for the Toolbox UI and is not to be replaced by an independently invented category structure.

## NSB

NSB is the primary NSB save/file tool area. Its established interface includes:

- **Load NSB**
- **Export NSB**
- **Load JSON**
- **Export JSON**
- **Clean 8ED**
- **Sync to SCB**
- **Unban**
- Existing utility controls associated with the NSB interface

Additional established NSB capabilities include:

- **Fuel Pips (`fupi`)** as a public NSB capability.
- **NSB Version** as an underlying capability that remains hidden from the normal public NSB interface unless specifically requested.
- **Clean 8ED** is a separate single-purpose 8ED operation surfaced from NSB for convenience; it is not an NSB function.

## File Handling

The established import/export wrapper applies to **NSB, SCB, 8ED-LNF, and TRB**:

1. Format-specific prefix where applicable.
2. Generate a new 40-character value.
3. Add a newline.
4. Add the JSON payload.
5. GZIP-compress the complete result.
6. Save using the game-required filename, regardless of the imported filename.

## Fusions

The established Fusion manufacturer/level model is:

- **Fusion Level 0 = Green**
- **Fusion Level 1 = Blue**
- **Fusion Level 2 = Red**

Manufacturer identifiers use the established `id_<manufacturer>` form. These levels are universal across the manufacturer records verified in the KOSD NSB source data.

## Source-of-Truth Rule

Toolbox functionality must be built from verified KOSD source-of-truth data and established project specifications. Do not invent game data, fabricate identifiers, or substitute mock data for real source data.

## Repository Separation

- `CORE/` — KOSD governance, standards, and core specifications.
- `ACQUISITION/` — acquired source APK/OBB artifacts.
- `RESEARCH/` — researched and verified game data.
- `WORKFLOWS/` — KOSD research/processing workflows.
- `TOOLBOX/` — the synchronized user-facing Toolbox system and its client-facing implementation.

## Development Principle

Build the Toolbox as **one system with three synchronized clients**, keeping functionality and source-of-truth behavior consistent across Web, Discord, and Android APK while adapting presentation and interaction to each platform.
