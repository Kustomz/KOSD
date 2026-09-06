# CHANGELOG

## KOSD v2.0.0 — Draft

### Recovery-Derived Build Initialization
- KOSD build initiated from the Kustomz Project Recovery state.
- KOSD Core migration established as the first build phase.
- Core modules migrated/established:
  - KOS-MANIFEST
  - KOS-CORE-001
  - KOS-INDEX-001
  - STD-001
  - MODULE-TEMPLATE
  - KOS-RELEASE
  - CHANGELOG
- Existing module IDs and Draft status are preserved.
- No recovery item marked REVIEW is silently promoted to authoritative KOSD content.

### CSR2 Legends Restoration Pricing Resolver
- **RP-001** established as a locked production specification.
- RP-001 defines dynamic discovery and calculation of Legends restoration requirements from CSR2's own `RestorationCarPricing` data.
- Production logic is explicitly prohibited from hard-coding individual car restoration totals.
- CSR2 6.6.x/6.7.0 Ferrari 250 GTO reference validation reproduces **14,800 RParts** from the seven source pricing records.
- The validated source chain is `RestorationCarPricing.metadata` → `RestorationCarPricingDatabase` → `RestorationPricingManager` / `GetCostSumForRestorationLevel` → applicable `RPartsPrice` aggregation.
- The Ferrari-specific `RestorationManifest` is explicitly classified as an asset/state mapping source, not the restoration-economic source.
- RP-001 requires regression validation and future-format detection so new Legends cars can be resolved from new game data without adding per-car pricing code.

### CSR2 Direct Acquisition Model
- Locked direct acquisition model established in `ACQUISITION/CSR2_DIRECT_ACQUISITION_MODEL.md`.
- Each CSR2 version uses `ACQUISITION/<version>/base.apk` plus `ACQUISITION/<version>/com.naturalmotion.customstreetracer2/` for OBB files.
- `base.apk` is explicitly a sibling of the Android package directory, not a file inside it.
- APK acquisition uses the complete APK through Termux/regular Git while the APK remains below the regular Git individual-file limit; manual splitting is not part of the locked model.
- OBB acquisition uses complete files through Git LFS; manual `.001/.002/.003` splitting is not part of the locked model.
- Direct OBB ingestion promotes files to canonical `RESEARCH/CSR2/GAME_VERSIONS/<version>/MAIN_OBB/` and `PATCH_OBB/` locations and retains Current + Previous versions.
- The permanent APK and OBB workflows remain version-aware and do not require workflow edits for each new CSR2 release.

### Build Boundary
This entry records the current draft build state. It is not a released KOSD version.

### Next
Core validation and reconciliation must occur before a KOSD release.
