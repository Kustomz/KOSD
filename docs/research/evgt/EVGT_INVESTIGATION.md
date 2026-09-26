# evgt Investigation — Final State (2026-09-26)

## Status: STOPPING POINT (banked, not abandoned)

This investigation is banked as a clean stopping point. The findings below are what we can stand behind.

---

## Banked Finding 1: L2 Taxonomy

L2 (persistent background records) is not one population.

### L2a — Account-lifetime records
- Examples: 415800030, 604, 679
- Start at or near account creation
- Multi-year persistence
- Little or no termination
- Account-specific (different accounts have different L2a sets)

### L2b — Periodic records
- Sequential series: 416000030 → 416100030 → 416200030 → 416300030 → ...
- IDs increment by ~100030
- Start dates spaced ~2 weeks apart (biweekly cadence)
- This is a structural observation independent of temporal overlap analysis
- **Open lead**: potentially a recurring scheduled game system

---

## Banked Finding 2: evgt Limitations (negative results)

The following methods were tested and found insufficient for inferring semantic event relationships from evgt alone:

| Method | Result |
|--------|--------|
| Raw temporal overlap | ❌ Contaminated by L1/L2 |
| Duration threshold (180d) | ❌ Arbitrary; doesn't separate signal from background |
| Companion intersection | ❌ Intersection ≠ relationship |
| State-transition correlation | ❌ Mostly negative (see below) |

### State-transition details:
- **300083178**: Zero surrounding transitions (isolated point event)
- **300244603**: One co-starting L2 record (likely coincidence)
- **300752254**: No transitions in tight occurrences; nsb_5 batch looks like session init, not event causation

### Boundary statement:
> evgt is sufficient to reconstruct record lifecycles and recurrence, but currently insufficient by itself to infer semantic event relationships.

---

## Abandoned: Temporal Fingerprint Taxonomy

The Class A/B/C taxonomy based on companion intersection is **abandoned**.

Reason: After filtering L1 (system) and L2 (persistent), the "fingerprints" nearly vanished:
- 300752254: 27 raw → 0 L3
- 300083178: 9 raw → 1 L3 (909090909, uninterpreted)
- 300244603: 12 raw → 0 L3

The supposed class signatures were almost entirely L2 contamination.

---

## Open Leads (for future work)

1. **L2b periodic series**: Cross-system correlation needed
   - L2b ID → timestamp → ecdm state → garage state → actual game behavior
   - If periodic records align with concrete game state, this bridges opaque evgt structure to game semantics

2. **909090909**: Sole surviving L3 companion (300083178). Single data point, not yet interpretable.

3. **Cross-system signals**: ecdm changes, garage/car-state deltas, or game-side observation may provide the L3 signal that evgt timestamps alone cannot.

---

## Methodological Lessons

1. **Intersection answers "what overlaps?" not "what belongs?"**
2. **"Present in every occurrence" can be evidence AGAINST companionship** (extreme persistence = background, not signal)
3. **Align equivalent occurrences before intersecting** (window fragmentation error)
4. **Filter by lifecycle before clustering by companionship** (L1/L2/L3 separation)
5. **Negative results constrain the model** — knowing what doesn't work is progress

---

## Files
- `evgt_lifecycle_classification.json` — L1/L2/L3 classification (178 L2, 1159 L3)
- `evgt_300752254_longitudinal.json` — Class A member 1 (raw, contaminated)
- `evgt_300083178_longitudinal.json` — Class B member (raw, contaminated)
- `evgt_300244603_longitudinal.json` — Class A member 2 (raw, contaminated)
- `evgt_universal_13_fingerprints.json` — Universal ID analysis
- `evgt_behavioral_model.json` — Chronological ordering test (99.4% concordance, sampled)
- `evgt_nsb5_cluster_fingerprints.json` — nsb_5 outlier analysis

**Note**: The longitudinal JSON files contain raw contaminated fingerprints. They are preserved as observations but should not be used as taxonomy sources.
