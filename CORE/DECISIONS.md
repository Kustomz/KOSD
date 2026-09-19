# KOS Decision Log

**Protocol:** KOS Decision & Promotion Protocol — adopted KD-001 (2026-09-19).
**Rules:** This log is append-only. Decision records are immutable historical records and are never edited in place. Corrections, reversals, supersessions, and clarifications are recorded as new decision records citing the original record.

---

## KD-001

1. **Decision ID:** KD-001
2. **Date:** 2026-09-19
3. **Item(s):** KOS Decision & Promotion Protocol — design proposal presented to the project owner on 2026-09-19 (eight-field decision record; append-only decision log; approval/promotion distinction; status pipeline; bootstrap rule for circular dependencies; adoption handling for existing locked items). The proposal was not a repository file at the time of decision.
4. **Action:** ADOPT
5. **Rationale:** Read-only investigation (2026-09-19) established that the repository contains no coherent decision/promotion mechanism and that none can be reconstructed from recovered material without inventing procedure: no defined decision record, no approval/promotion distinction, and a circular STD-001 ↔ KOS-RELEASE ↔ GOV-001 dependency. The protocol supplies the minimal mechanism capable of supporting the project's needs: one append-only log, one decision-ID scheme, one controlled action list, and the rule that status changes cite decisions.
6. **Basis / Evidence:** Project-owner judgment, informed by read-only inspection of CORE/KOS-RELEASE.md, GOVERNANCE/GOV-001.md, CORE/MODULE-TEMPLATE.md, CORE/CHANGELOG.md, and the recovery reconciliation records. Classification, stated plainly: owner judgment on inspected repository evidence.
7. **Conditions / Blockers:** None. Adoption is unconditional and effective upon this record.
8. **Execution / Resulting State:** Authorized execution: create this log (CORE/DECISIONS.md) with KD-001 as its first entry. No promotion, lock, unlock, supersession, or other status change is authorized by this decision. Resulting state: CORE/DECISIONS.md created containing KD-001; all other repository files unchanged.

---

## KD-002

1. **Decision ID:** KD-002
2. **Date:** 2026-09-19
3. **Item(s):** CORE/STD-001.md — Version 2.0.0 (Draft), Status: Draft, as reviewed on 2026-09-19 prior to this record. The file is untouched by this decision.
4. **Action:** APPROVE-IN-PRINCIPLE
5. **Rationale:** The eight Core Requirements and the overall standard direction are accepted as the intended KOS standard. Promotion is withheld, not rejected, pending the blockers below.
6. **Basis / Evidence:** Project-owner judgment following read-only inspection of STD-001 against KOS-RELEASE (Draft), GOV-001 (REVIEW items), and the recovery reconciliation migration rules. Classification, stated plainly: owner judgment — not derived data.
7. **Conditions / Blockers:**
   - Requirements 6 and 8 reference the KOSD change/release process, which is not approved (KOS-RELEASE remains Draft).
   - Requirement 5's locking/unlocking authority is unresolved (GOV-001 O-001/O-002/O-003 at REVIEW, not promoted).
   - The terms "silently," "applicable validation/release process," and "Master" need clarification once the governing documents are reviewed.
   - The Boundary stays intact: no detailed field schemas or validation criteria are to be invented.
8. **Execution / Resulting State:** Authorized execution: none against the repository. No file modification, no status change, and no promotion is authorized by this decision. A future PROMOTE decision may cite KD-002 once its blockers clear; that future action requires its own decision. Resulting state: unchanged — CORE/STD-001.md remains exactly as before this record: Status Draft, "Kustomz Decision: _Not yet reviewed._", "Master Promotion: Not yet promoted." The authoritative record of this ruling is KD-002 in this log.
