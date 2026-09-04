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

### Build Boundary
This entry records the current draft build state. It is not a released KOSD version.

### Next
Core validation and reconciliation must occur before a KOSD release.
