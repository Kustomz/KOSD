# CSR2 Restoration Pricing Source — Forensic Finding

## Status
**CONFIRMED — source identified and reproduced from game data.**

## Target
Determine the actual source of the CSR2 SCB **“Required to restore”** value for a Legends restoration car, using game data rather than external/wiki values.

Primary validation target:
- Car: `Ferrari_250GTOClassic_1962`
- SCB required restoration value: **14,800 R$ / RParts**
- Game version investigation: CSR2 6.6.x / 6.7.0 data

## Proven Data Source
The actual restoration economics are stored in the dedicated:

`RestorationCarPricing.metadata`

This metadata is consumed by:

`RestorationCarPricingDatabase`

and exposed to game logic through:

`RestorationPricingManager`

The relevant manager methods include:

- `GetRPartsPrice(carDBKey, restorationType, level)`
- `GetRestorationTime(carDBKey, restorationType, level)`
- `GetGoldPrice(carDBKey, restorationType, level)`
- `GetCostSumForRestorationLevel(carDBKey, restorationType, restorationLevel)`

The pricing object is `RestorationPricedAsset`, whose relevant field is:

`RPartsPrice`

## Ferrari 250 GTO Proof

Decoded `RestorationCarPricing.metadata` contains these exact records:

| Asset | RParts price | Timer |
|---|---:|---:|
| `Ferrari_250GTOClassic_1962_bod0` | 1800 | 1800 |
| `Ferrari_250GTOClassic_1962_bod1` | 2200 | 2700 |
| `Ferrari_250GTOClassic_1962_bod2` | 2600 | 3600 |
| `Ferrari_250GTOClassic_1962_whe0` | 1000 | 1800 |
| `Ferrari_250GTOClassic_1962_eng0` | 2800 | 1800 |
| `Ferrari_250GTOClassic_1962_int0` | 2000 | 1800 |
| `Ferrari_250GTOClassic_1962_int1` | 2400 | 2700 |

Total:

`1800 + 2200 + 2600 + 1000 + 2800 + 2000 + 2400 = 14800`

Therefore the SCB value **14,800 is reproducible directly from CSR2's own restoration pricing data**.

## Important Distinction: RestorationManifest

The car-specific asset:

`Ferrari_250GTOClassic_1962_RestorationManifest`

is **not** the source of the restoration prices.

Its contents describe restoration asset/state mappings such as body, interior, engine, VFX, flares, projectors, and animation assets. It does not contain the 14,800 price or the individual RParts economics.

The economic source is the generalized `RestorationCarPricing` database.

## NMG Metadata Compression

CSR2's metadata uses the NMG LZHAM Alpha8 compression format.

For `RestorationCarPricing.metadata`:

- File size: 1336 bytes
- NMG header occupies the first 16 bytes
- Header decompressed-size field: `0x00003C87` = **15,495 bytes**
- Compressed payload begins with `0E C6`
- NMG footer: final 4 bytes
- Compressed stream used for decoding: bytes `16 .. size-4`
- Decoder: **LZHAM Alpha8**, zlib-compatible stream mode
- Window setting: 15-bit

The decoded payload is JSON containing the `RestorationCarPricing.pricingList` records.

### Critical decoder lesson
Do **not** substitute the modern LZHAM 1.x codec for these CSR2 metadata files. LZHAM 1.x bitstreams are incompatible with the older Alpha format used here. The Alpha8 source successfully decodes the CSR2 metadata.

## IL2CPP Code Evidence

CSR2 IL2CPP metadata identifies:

### `RestorationPricedAsset`
Fields:
- `RPartsPrice`
- `RTimer`
- `GoldPrice`
- `PartSide`

### `RestorationPricingManager`
Relevant methods:
- `OnConfigLoadedFromJson`
- `SetupTheValues`
- `OnConfigLoadedFromBinary`
- `GetPartSide`
- `GetRPartsPrice`
- `GetRestorationTime`
- `GetGoldPrice`
- `GetCostSumForRestorationLevel`
- `GetMaxRestorationLevel`
- `GetRestorationProgressFraction`
- `GetMaxRestorationLevelsAll`
- `GetDefaultRestorationSetupForCar`
- `GetFullyRestoredSetupForCar`
- `GetRandomRestorationSetupForCar`

### `RestorationCarPricingDatabase`
Relevant identity/config:

`segment8LegendsRpartsForGoldDatabase:RestorationCarPricingDatabase`

Source path exposed by IL2CPP metadata:

`;\\Assets\\Code\\Logic\\Pricing\\RestorationCarPricingDatabase.cs`

Code namespace/type grouping:

`0Code.Logic.Pricing|RestorationCarPricingDatabase`

## Reusable Forensic Process

Use this procedure for future restoration-price investigations:

1. **Identify the SCB displayed value.**
   Record the car DB key and exact “Required to restore” value.

2. **Search game metadata for restoration-specific names.**
   Prioritize:
   - `RestorationCarPricing`
   - `RestorationCarPricingDatabase`
   - `RestorationPricingManager`
   - `RPartsPrice`
   - `GetRPartsPrice`
   - `GetCostSumForRestorationLevel`

3. **Do not assume the car's RestorationManifest is the economic source.**
   Inspect it separately and classify its fields as asset/state mappings versus pricing data.

4. **Locate `RestorationCarPricing.metadata`.**
   Extract the NMG metadata payload.

5. **Detect NMG compression.**
   A first compressed-stream byte of `0x0E` identifies the LZHAM path in the NMG compression layer.

6. **Decode using LZHAM Alpha8.**
   Strip the 16-byte NMG header and final 4-byte footer, then decompress the payload using the Alpha8 zlib-compatible stream with a 15-bit window.

7. **Parse `pricingList`.**
   Match records by the car DB key and restoration asset IDs (`bod`, `whe`, `eng`, `int`, etc.).

8. **Extract `RPartsPrice`.**
   Record every applicable restoration component/level price.

9. **Reproduce the displayed requirement.**
   Sum the applicable `RPartsPrice` values. For Ferrari 250 GTO:

   `1800 + 2200 + 2600 + 1000 + 2800 + 2000 + 2400 = 14800`

10. **Cross-check the IL2CPP calculation path.**
    Confirm the presence of `GetCostSumForRestorationLevel`, which is the game-side aggregation method for restoration costs.

11. **Classify confidence.**
    - Metadata values matching the UI number: **direct data proof**.
    - Matching manager calculation method: **code-path proof**.
    - Exact SCB UI caller still requires tracing the UI call site if absolute end-to-end caller proof is desired.

## Current Conclusion

The mystery source of the SCB restoration requirement is solved:

**SCB “Required to restore” ← restoration pricing records in `RestorationCarPricing.metadata` ← `RestorationCarPricingDatabase` / `RestorationPricingManager` ← individual `RPartsPrice` entries.**

The Ferrari 250 GTO's exact seven game-data prices independently reproduce the displayed **14,800** total.
