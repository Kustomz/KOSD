# Hero Vehicle List Workflow

This workflow builds the KOSD Hero Vehicle source list from Nitro4CSR's current CRDB master list.

## Source

- Repository: `Nitro4CSR/CSR2-DataBase`
- Branch: `Everything`
- File: `1.Cars/#AllCarCRDBs.txt`

## Rules

1. Read the complete source list as-is.
2. Remove blank lines only.
3. Detect exact duplicate CRDB identifiers before sorting.
4. Preserve distinct identifiers such as `Reward`, `RewardRecycled`, `Crew`, `CrewRecycled`, `Elite`, `Gold`, `VIP`, platform variants, and other suffix variants; these are not treated as duplicates merely because they share a vehicle name.
5. Sort the resulting identifiers using case-sensitive lexical/alphanumeric ordering, with the manufacturer/name text determining position and the full CRDB identifier used as the tie-breaker.
6. Do not modify Nitro's repository.
7. KOSD maintains its own derived Hero Vehicle list and its own numbering (`HV-001`, `HV-002`, etc.). Nitro's source ordering does not determine KOSD numbering.
8. A Hero Vehicle is not considered approved merely because its CRDB identifier exists in the source list. Artwork and KOSD approval are separate steps.

## Current correction

The source file currently begins with misplaced entries before the alphabetized section. For example, `Ford_RingbrothersMustang_1969` belongs in the Ford section, between `Ford_RadRidesTroyRoadster_1936` and `Ford_RingbrothersMustangMach1_1969`; it must not be treated as the first KOSD Hero Vehicle.

## Output

The workflow output is the KOSD-owned normalized/sorted source list. It is a derived working list and does not alter the upstream Nitro source.
