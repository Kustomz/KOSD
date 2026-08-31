# CSR2 Future-Car Asset Mining — 6.7.0 Research Checkpoint

**Date:** 2026-08-31  
**State:** PAUSED / RESEARCH  
**Authority:** Research only; not an authoritative KOS rule

## Exact Kustomz Future-Car List

The following identifiers must be preserved exactly as supplied. Do not normalize, rename, substitute variants, infer from model year, or replace one identifier with a related vehicle.

1. `Buick_GrandNationalF4_1987`
2. `Honda_VeilsideNSX_1995`
3. `Lamborghini_ZacoeTemerario_2024`
4. `Dodge_ChargerSixpack_2025`
5. `Jaguar_XJR15_1991`
6. `Nissan_R390GT1_1997`
7. `TVR_CerberaSpeed12_1996`
8. `BMW_M3E46GTR_2005`
9. `Aspark_OwlSP600_2024`
10. `Ford_DutchboysTorino_1969`
11. `Renault_ClioV6Phase2_2005`
12. `RUF_CTR3EVO_2023`
13. `Ford_MustangSVTCobraR_2000`
14. `Ferrari_296Speciale_2026`
15. `Nissan_LBSkylineR32_1993`
16. `Lamborghini_RevueltoSV_2027`

## Working Definition

A future car is not established merely because its identifier appears in game data, event data, pricing, rewards, or a database. The investigation must distinguish:

- game-data identity/reference;
- actual Unity vehicle asset presence;
- asset completeness;
- release/usability state.

The historical mining target is a vehicle identity that can be established while the corresponding usable Unity vehicle asset payload is not yet present.

## 6.7.0 Findings

- Exact-name searches across the inspected 6.7.0 MAIN/PATCH asset-file inventory produced no direct filename matches for the 16 exact identifiers.
- This result is **not** proof that the vehicles are absent; identifiers may be serialized inside generic Unity bundles or represented under internal structures.
- 6.7.0 contains explicit placeholder vehicle assets, including `Placeholder_CoveredCar_1234_*` and `Placeholder_Car_1234_*`, and associated placeholder body/LOD/wheel/driver/icon assets.
- `CarPricing.bin` also contains a `Placeholder_CoveredCar_1234` parts/stat block, confirming that placeholder content is represented in game data.
- Placeholder content should not be confused with the actual identifier of a future vehicle.

## Nitro4CSR Evidence — 2026-08-31

Nitro4CSR reported that finished 6.7.0 cars had been added to his database while RX-7, MX-5, and Lotus Emira i4 were being held back because changes were suspected.

This establishes an important research distinction:

> database inclusion, asset presence, completeness, and live/released status are separate signals.

Therefore, absence from a third-party finished-car database is not proof that a vehicle is absent from the game data or OBB.

## Historical Discovery

Kustomz previously found future cars during an earlier mining effort, apparently while looking for something else. The exact game version for that accidental discovery has **not yet been recovered**.

Kustomz has historical CSR2 OBBs from approximately 3.0.x through current 6.7.0, with 6.5.0 currently missing. The historical version hunt is intentionally paused.

## Current Pause Boundary

Do not promote this research into a finalized KOS rule. Do not claim any of the 16 vehicles is verified as a future car solely from the current evidence. Resume only when explicitly requested.
