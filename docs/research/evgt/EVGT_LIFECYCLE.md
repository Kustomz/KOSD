# EVGT Lifecycle Classification

## Three-Layer Model

| Layer | Name | Behavior | Treatment |
|-------|------|----------|-----------|
| L1 | System | Universal across saves/events | Filter from companion analysis |
| L2 | Persistent background | Very long-lived / account-spanning | Filter from companion analysis |
| L3 | Event-bound | Temporal lifecycle tied to occurrence | Fingerprint candidates |

## L2 Sub-populations

### L2a — Account-lifetime records
- Start at or near account creation
- Multi-year persistence, little/no termination
- Examples: 415800030, 604, 679
- Account-specific sets

### L2b — Periodic records
- Sequential IDs incrementing by ~100030
- Start dates spaced ~2 weeks apart
- See EVGT_L2B_OPEN_LEAD.md

## Classification Rule
L2 = any occurrence with >180 day duration OR active with >180 day old start timestamp.

**Caveat**: This threshold is a convenient cutoff, not a proven semantic boundary. Do not tune it to manufacture surviving fingerprints.

## Counts (2026-09-26, 10-save corpus)
- L1: 13 (universal set)
- L2: 178
- L3: 1159
