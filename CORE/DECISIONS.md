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

---

## KD-003

1. **Decision ID:** KD-003
2. **Date:** 2026-09-19
3. **Item(s):** `CORE/KOS-RELEASE.md`, Version 2.0.0 (Draft), Status Draft, as reviewed at commit `89954356d7882c442c5df61ed617662111dc8912`.
4. **Action:** APPROVE-IN-PRINCIPLE
5. **Rationale:** The owner accepts the KOS-RELEASE document's current release-process design, ten release requirements, release-integrity concepts, and overall direction as the intended KOSD release framework. This is approval in principle only. It does not promote the document, make its requirements operative, or represent that the unresolved procedures and dependencies have been satisfied.
6. **Basis / Evidence:** Owner judgment based on the read-only KD-003 decision brief and the repository evidence identified there, including KOS-RELEASE, STD-001, GOV-001, recovery/reconciliation records, the recovery build map, source inventory, CHANGELOG, and the adopted KOS Decision & Promotion Protocol.
7. **Conditions / Blockers:**
   (a) STD-001 remains APPROVED-IN-PRINCIPLE and not promoted; its related release-process dependency remains unresolved until KOS-RELEASE is eventually promoted.
   (b) GOV-001 O-001/O-002/O-003 remain unresolved and unpromoted; their relationship to KOS-RELEASE requirements concerning locked content and recovery/project-state conflicts must be resolved before KOS-RELEASE promotion.
   (c) The required-module set is not yet formally enumerated or reconciled; the MANIFEST/INDEX discrepancy must be resolved before promotion.
   (d) Validation criteria/process are not yet established. No validation criteria or schemas are to be invented merely to satisfy this condition.
   (e) Applicable dependencies and relationships are not yet formally defined.
   (f) The terms "applicable project decision," "silently altered," "silently treated as authoritative," "applicable validation/release process," "authoritative KOS/project state," and "Master" require explicit resolution before promotion.
   (g) Release-version semantics require clarification before promotion.
   (h) The distinction between the protocol's `VALIDATED` state and KOS-RELEASE's `VALIDATION` terminology requires reconciliation if both are intended to represent the same state.
   (i) The strength of the "should include" / "may be used" language in Release Integrity requires owner clarification if those provisions are intended to be mandatory release requirements.
   (j) The existing boundary remains intact: do not invent detailed field schemas, validation criteria, or other missing implementation rules in order to clear these conditions.
8. **Execution / Resulting State:** No repository modification is authorized by KD-003. `CORE/KOS-RELEASE.md` remains Draft and unpromoted. Its existing "Kustomz Decision: _Not yet reviewed._" and "Master Promotion: Not yet promoted." fields remain unchanged. The authoritative record of this APPROVE-IN-PRINCIPLE ruling is KD-003 in `CORE/DECISIONS.md`. No promotion, lock, unlock, or activation is authorized.

---

## KD-004

1. **Decision ID:** KD-004
2. **Date:** 2026-09-19
3. **Item(s):** `GOVERNANCE/GOV-001.md`, section "Master / Locked / Pause Handling — O-001/O-002/O-003", Version 2.0.0 (Draft), as reviewed at commit `89954356d7882c442c5df61ed617662111dc8912`.
4. **Action:** ADOPT
5. **Rationale:** The owner recognizes the three recovery bullets under the O-001/O-002/O-003 heading as the three governance questions requiring review, but the current document does not explicitly map individual bullet text to individual O-IDs. The inferred reading used during inspection must not be silently converted into authoritative per-ID assignments.
6. **Basis / Evidence:** Owner judgment based on the KD-004 decision brief and direct inspection of `GOVERNANCE/GOV-001.md`. The section heading identifies O-001/O-002/O-003, while the three bullets themselves are not individually labeled.
7. **Conditions / Blockers:**
   (a) KD-004 does not resolve the substantive governance questions concerning Master, LOCKED, or Pause handling.
   (b) The natural inspection mapping — O-001 = Master, O-002 = LOCKED, O-003 = Pause — is recognized as an interpretation only, not as authoritative source text.
   (c) Before any substantive promotion or activation based on individual O-IDs, the repository should explicitly map each O-ID to its corresponding item.
   (d) No missing governance definitions, authority mechanisms, pause-record schema, or other implementation rules may be invented through this decision.
8. **Execution / Resulting State:** No repository modification is authorized by KD-004. `GOVERNANCE/GOV-001.md` remains unchanged and remains DRAFT / RECOVERY-MAPPED. No substantive ruling is made on: whether Master is authoritative; the meaning or authority of LOCKED; pause-record requirements. The three questions remain unresolved pending explicit owner rulings.

---

## KD-005

1. **Decision ID:** KD-005
2. **Date:** 2026-09-19
3. **Item(s):** `GOVERNANCE/GOV-001.md`, section "Master / Locked / Pause Handling — O-001/O-002/O-003", specifically the O-001 Master-authority question, reviewed through the O-001 decision brief at commit `89954356d7882c442c5df61ed617662111dc8912`.
4. **Action:** DEFER
5. **Rationale:** The repository contains an O-001 recovery statement that says "Master is authoritative," but the repository does not currently define what "Master" is, identify a formally established Master artifact or state, establish the source or mechanism of its authority, or define its relationship to recovery-derived project state and historical information. `CORE/KOS-MANIFEST.md` and `CORE/KOS-INDEX-001.md` both contain "Master" descriptions but neither is established as the authoritative Master. Selecting either, or creating a new Master construct, would require an additional owner design decision not supported by the existing source.
6. **Basis / Evidence:** Owner judgment based on the O-001 decision brief and direct repository evidence:
   - GOV-001 contains the O-001 recovery statement but does not define Master.
   - KOS-MANIFEST describes itself as the "Master table of contents for the Kustomz Operating System (KOS)."
   - KOS-INDEX-001 describes itself as the "Master index for KOS."
   - Both are Draft/unpromoted and their contents differ.
   - The recovery build map states that recovery establishes project state to be carried forward, while existing modules are not authoritative merely because they exist.
   - Source inventory states that old modules are not authoritative merely because they exist.
   - The adopted KOS Decision & Promotion Protocol establishes how owner decisions are recorded but does not itself define the Master artifact/state.
   - No existing source establishes a precedence rule between Recovery and Master.
7. **Conditions / Blockers:**
   (a) O-001 remains unresolved as an operative governance rule.
   (b) No artifact, branch, state, or record is designated as "Master" by KD-005.
   (c) No authority mechanism for Master is created or inferred by KD-005.
   (d) No precedence rule between Master, recovery-derived project state, historical information, MANIFEST, or INDEX-001 is created by KD-005.
   (e) Any future establishment of Master requires a separate explicit owner decision defining what constitutes Master and the basis of its authority.
   (f) The O-001 statement in GOV-001 must not be treated as an operative authority rule merely because it exists in the recovery-mapped document.
8. **Execution / Resulting State:** No repository modification is authorized by KD-005. `GOVERNANCE/GOV-001.md` remains unchanged and remains DRAFT / RECOVERY-MAPPED. O-001 is formally DEFERRED pending a future explicit owner decision establishing what "Master" is and how its authority operates. O-002 and O-003 remain untouched and unresolved. No promotion, lock, unlock, activation, or new governance mechanism is authorized.

---

## KD-006

1. **Decision ID:** KD-006
2. **Date:** 2026-09-19
3. **Item(s):**
   - `ACQUISITION/CSR2_DIRECT_ACQUISITION_MODEL.md`
   - `PRODUCTION/RP-001.md`
   - Their existing `LOCKED` status labels, as identified in the O-002 decision brief.
4. **Action:** ADOPT
5. **Rationale:** The repository contains two pre-existing files explicitly labeled LOCKED, both predating the adopted KOS Decision & Promotion Protocol and neither citing a prior decision that granted LOCKED status. Their historical LOCKED labels therefore cannot be retroactively treated as having been granted under the new protocol. At the same time, removing, stripping, or reclassifying those labels without an explicit owner decision would alter existing project state. The owner therefore adopts preservation of their existing status as historical project state pending substantive resolution of O-002.
6. **Basis / Evidence:** Owner judgment based on the O-002 decision brief and direct repository evidence:
   - `ACQUISITION/CSR2_DIRECT_ACQUISITION_MODEL.md` is explicitly labeled `Status: LOCKED`, effective 2026-09-06.
   - `PRODUCTION/RP-001.md` is explicitly labeled `Status: LOCKED SPECIFICATION`, version 1.0.
   - Neither file cites a decision, authority grant, or unlock mechanism for its LOCKED status.
   - KD-001 adopted the KOS Decision & Promotion Protocol only after these labels already existed.
   - KD-001 did not retroactively grant or validate those LOCKED statuses.
   - The O-002 substantive definition and authority of LOCKED remain unresolved.
7. **Conditions / Blockers:**
   (a) KD-006 does not define what LOCKED means.
   (b) KD-006 does not establish who or what grants LOCKED authority.
   (c) KD-006 does not establish an unlock, change, or supersession procedure.
   (d) KD-006 does not validate the historical basis of either existing LOCKED label.
   (e) KD-006 does not strip, downgrade, re-lock, or otherwise alter either existing status label.
   (f) The two files are preserved in their existing state pending substantive O-002 resolution.
   (g) Future locking, unlocking, changing, or superseding of these files remains subject to an explicit owner decision; KD-006 does not itself authorize any such action.
   (h) O-001 remains deferred under KD-005 and is not resolved or used to establish authority by KD-006.
   (i) O-003 remains untouched and unresolved.
8. **Execution / Resulting State:** No repository modification is authorized by KD-006. `ACQUISITION/CSR2_DIRECT_ACQUISITION_MODEL.md` remains unchanged and retains its existing `LOCKED` status label. `PRODUCTION/RP-001.md` remains unchanged and retains its existing `LOCKED SPECIFICATION` status label. O-002 remains unresolved as to the operative meaning, authority, grant mechanism, and change/unlock mechanism for LOCKED. No promotion, lock, unlock, supersession, or other status change is authorized by KD-006.

---

## KD-007

1. **Decision ID:** KD-007
2. **Date:** 2026-09-19
3. **Item(s):** `GOVERNANCE/GOV-001.md`, section "Master / Locked / Pause Handling — O-001/O-002/O-003", specifically the O-002 LOCKED authority and meaning question, as reviewed through the O-002 decision brief and substantive resolution proposal.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts the GOV-001 formulation as the operative definition of LOCKED because it establishes authority while preserving an explicit path for deliberate owner-authorized change, supersession, or unlocking. This is consistent with the adopted KOS Decision & Promotion Protocol, which already recognizes LOCK, UNLOCK, and SUPERSEDE as controlled actions and separates the decision authorizing an action from its execution and resulting repository state. LOCKED therefore does not mean immutable. It means authoritative and protected from silent alteration until an explicit owner-authorized action changes, supersedes, or unlocks it.
6. **Basis / Evidence:**
   - GOV-001 states: "LOCKED means authoritative until explicitly changed, superseded, or unlocked."
   - KD-001 adopted the KOS Decision & Promotion Protocol, including LOCK, UNLOCK, and SUPERSEDE as controlled actions requiring explicit decision records.
   - The protocol distinguishes decision/ruling, authorized execution, and resulting repository state.
   - CORE/KOS-CORE-001 Principle 4 states that locked assets remain locked unless explicitly superseded; this is narrower than the adopted O-002 rule and requires later textual reconciliation.
   - KD-006 preserved the two pre-existing LOCKED artifacts without retroactively validating their historical grant of LOCKED status.
   - No evidence establishes that LOCKED means permanently immutable.
7. **Conditions / Blockers:**
   (a) Any change, supersession, or unlock of LOCKED status requires an explicit Kustomz owner decision recorded under the adopted KOS Decision & Promotion Protocol.
   (b) "LOCKED" does not authorize silent modification of the locked content.
   (c) KD-007 does not establish criteria for when an item should be locked.
   (d) KD-007 does not establish validation or evidence requirements for locking, changing, superseding, or unlocking.
   (e) KD-007 does not retroactively validate the original authority or grant mechanism of the two pre-existing LOCKED artifacts.
   (f) The existing LOCKED artifacts remain preserved under KD-006.
   (g) CORE/KOS-CORE-001 Principle 4 and any other conflicting LOCKED language require later reconciliation; KD-007 does not silently rewrite those files.
   (h) O-001 remains deferred under KD-005 and is not resolved by KD-007.
   (i) O-003 remains untouched and unresolved.
8. **Execution / Resulting State:** No repository modification is authorized by KD-007. `GOVERNANCE/GOV-001.md` remains unchanged and remains DRAFT / RECOVERY-MAPPED. The operative O-002 ruling is now established in the decision log: LOCKED means authoritative until explicitly changed, superseded, or unlocked, with each such action requiring an explicit Kustomz owner decision under the adopted protocol. No lock, unlock, change, supersession, promotion, or other repository status action is executed by KD-007 itself.

---

## KD-008

1. **Decision ID:** KD-008
2. **Date:** 2026-09-19
3. **Item(s):** `GOVERNANCE/GOV-001.md`, section "Master / Locked / Pause Handling — O-001/O-002/O-003", specifically the O-003 pause-handling question, as reviewed through the O-003 decision brief.
4. **Action:** DEFER
5. **Rationale:** The repository demonstrates an established practice of documenting paused work through reconciliation "Pause Boundary" sections, and those existing records contain the substantive information identified by the O-003 recovery statement: stopping point, current state/hypothesis, active boundaries, and next intended target. However, the repository does not currently define a formal pause-record obligation, trigger, schema, storage location, or resume authority. The O-003 statement also requires recording in "Master," while KD-005 expressly deferred establishment of Master. Formalizing a pause-record requirement or creating an interim destination would therefore require new governance design not established by the current repository evidence. O-003 is deferred until the relationship between pause handling and the eventual definition of Master can be explicitly resolved.
6. **Basis / Evidence:**
   - GOV-001 contains the O-003 recovery statement requiring four categories of information to be recorded when a workstream is paused, but GOV-001 remains DRAFT / RECOVERY-MAPPED and unpromoted.
   - `RECOVERY/KOSD_RECOVERY_RECONCILIATION_v1.6.md` contains a "Pause Boundary" section documenting paused research, its evidence boundary, checkpoint contents, and resume condition.
   - `RECOVERY/KOSD_RECOVERY_RECONCILIATION_v1.7.md` contains a "Pause Boundary" section documenting the exact evidence boundary, proven/unresolved state, and intended resume target.
   - These sections are existing recovery/reconciliation records, not formal standalone pause records.
   - No pause-record schema, template, storage location, trigger definition, or resume-authority rule exists in the repository.
   - KD-005 established that no artifact, branch, state, or record is currently designated as Master.
   - KD-005 also established that the O-001 Master statement must not be treated as an operative authority rule merely because it exists in GOV-001.
   - KD-004 prohibited inventing a pause-record schema or missing governance definitions through interpretation.
   - KD-007 resolved O-002 but does not establish a pause-record mechanism or Master destination.
7. **Conditions / Blockers:**
   (a) O-003 remains unresolved as an operative pause-handling rule.
   (b) No formal definition of "paused" is established by KD-008.
   (c) No pause-record schema or mandatory field set is established by KD-008.
   (d) No pause-record storage location or interim Master substitute is established by KD-008.
   (e) No resume authority or authorization mechanism is established by KD-008.
   (f) Existing v1.6 and v1.7 "Pause Boundary" sections remain preserved as historical/recovery project-state records and are not declared invalid or noncompliant.
   (g) Their preservation does not constitute formal adoption of the O-003 obligation.
   (h) O-001 remains deferred under KD-005.
   (i) O-002 remains resolved under KD-007.
   (j) Any future formalization of O-003 requires an explicit owner decision defining the obligation and its relationship to Master.
8. **Execution / Resulting State:** No repository modification is authorized by KD-008. `GOVERNANCE/GOV-001.md` remains unchanged and remains DRAFT / RECOVERY-MAPPED. The existing v1.6 and v1.7 Pause Boundary records remain unchanged. O-003 is formally DEFERRED pending explicit resolution of the pause obligation, its trigger, required record contents, recording destination, and resume authority. No pause-record artifact, schema, workflow, Master substitute, promotion, lock, unlock, or other governance mechanism is created by KD-008.

---

## KD-009

1. **Decision ID:** KD-009
2. **Date:** 2026-09-19
3. **Item(s):** `CORE/KOS-CORE-001.md`, Principle 4, specifically the reconciliation of its LOCKED wording with KD-007.
4. **Action:** ADOPT
5. **Rationale:** KD-007 established the operative definition of LOCKED as authoritative until explicitly changed, superseded, or unlocked by an explicit Kustomz owner decision under the adopted KOS Decision & Promotion Protocol. CORE-001 Principle 4 currently states only that locked assets remain locked unless explicitly superseded, creating a textual discrepancy that cannot be resolved by interpretation without inventing governance meaning. KD-009 authorizes the minimum textual reconciliation necessary to make Principle 4 express the already-adopted KD-007 rule.
6. **Basis / Evidence:**
   - KD-007 resolved O-002 and established the operative LOCKED definition and decision mechanism.
   - KD-007 field 7(g) explicitly identified CORE-001 Principle 4 as requiring later reconciliation.
   - KD-007 field 8 explicitly withheld repository modification authority.
   - The reconciliation brief established that the current Principle 4 wording is not fully compatible with KD-007 by interpretation alone.
   - The reconciliation brief identified the following minimum replacement wording: "4. Locked assets are authoritative until explicitly changed, superseded, or unlocked by an explicit Kustomz owner decision under the adopted KOS Decision & Promotion Protocol."
   - The reconciliation brief found no other CORE-001 principle requiring modification as part of this reconciliation.
7. **Conditions / Blockers:**
   (a) Only Principle 4 may be changed under KD-009.
   (b) The replacement text must be exactly the wording identified in the reconciliation brief, unless a further owner decision explicitly authorizes a different wording.
   (c) No other principle, section, metadata, version, status, or file may be changed under KD-009.
   (d) KD-009 does not alter CORE-001's Draft status.
   (e) KD-009 does not promote CORE-001.
   (f) KD-009 does not establish lock criteria, validation requirements, additional authority roles, approval chains, schemas, or unlock procedures beyond KD-007.
   (g) O-001 remains deferred under KD-005.
   (h) O-003 remains deferred under KD-008.
   (i) KD-007 remains unchanged.
8. **Execution / Resulting State:** Authorize one repository modification only: Replace the existing CORE-001 Principle 4 sentence: "Locked assets remain locked unless explicitly superseded." With: "Locked assets are authoritative until explicitly changed, superseded, or unlocked by an explicit Kustomz owner decision under the adopted KOS Decision & Promotion Protocol." No other repository modification is authorized. Do not modify GOV-001.md. Do not modify STD-001.md. Do not modify KOS-RELEASE.md. Do not modify either existing LOCKED artifact. Do not modify any other file. Do not commit or push as part of KD-009.

---

## KD-010

1. **Decision ID:** KD-010
2. **Date:** 2026-09-19
3. **Item(s):** The required-module-set discrepancy between `CORE/KOS-MANIFEST.md` and `CORE/KOS-INDEX-001.md`, as documented in the MANIFEST/INDEX discrepancy brief, and its relationship to KOS-RELEASE requirement 1.
4. **Action:** ADOPT
5. **Rationale:** Contain the discrepancy without inventing a required-module set, selecting a canonical document, or silently treating either Draft enumeration as authoritative.
6. **Basis / Evidence:**
   - KOS-RELEASE requirement 1 states: "Required modules are present." No enumeration of the required-module set exists anywhere in the repository.
   - KD-003 field 7(c): "The required-module set is not yet formally enumerated or reconciled; the MANIFEST/INDEX discrepancy must be resolved before promotion."
   - KD-005 field 7(b): "No artifact, branch, state, or record is designated as 'Master' by KD-005." KD-005 did not itself designate a required-module-set authority.
   - The MANIFEST/INDEX discrepancy brief documented six line-item differences between the two Draft enumerations: "Recovery Reconciliation v1.7" present in MANIFEST Core but absent from INDEX Core; a five-item "Research / Recovery Checkpoints" section present in MANIFEST but absent from INDEX; a declared "6. Assets" section in INDEX with no content; status/version labeling differences; and a within-MANIFEST naming overlap ("Recovery Reconciliation v1.7" vs. "KOSD ↔ Recovery Reconciliation v1.7").
   - Both documents are Draft and unpromoted: MANIFEST carries `**Status:** Draft`; INDEX-001 carries `**Version:** 2.0.0 (Draft)` with no Status field.
   - The existing anti-silent-promotion principle (CHANGELOG): "No recovery item marked REVIEW is silently promoted to authoritative KOSD content."
   - GOV-001: "They must not be fabricated or silently promoted from inference."
7. **Conditions / Blockers:**
   (a) The repository has no formally established required-module set for KOS-RELEASE.
   (b) Neither `CORE/KOS-MANIFEST.md` nor `CORE/KOS-INDEX-001.md` is authoritative for establishing that required-module set. This statement is a narrow corollary of KD-005's existing non-designation of a Master; KD-005 did not itself designate a required-module-set authority.
   (c) The MANIFEST/INDEX discrepancies remain explicitly unresolved.
   (d) KOS-RELEASE requirement 1 remains blocked and must not be satisfied by treating either Draft enumeration as authoritative.
   (e) No module is considered required or non-required solely from its presence or absence in either Draft enumeration.
   (f) This KD must not be interpreted as resolving O-001, designating a Master, or establishing any authority hierarchy.
   (g) O-001 / Master remains deferred under KD-005.
   (h) No promotion of MANIFEST, INDEX-001, or KOS-RELEASE is authorized by this KD.
   (i) KD-005 and all prior decisions remain unchanged.
8. **Execution / Resulting State:** Add KD-010 to `CORE/DECISIONS.md` only. No repository modification is authorized beyond this log entry: do not modify `CORE/KOS-MANIFEST.md`, `CORE/KOS-INDEX-001.md`, `CORE/KOS-RELEASE.md`, or `GOVERNANCE/GOV-001.md`; do not modify KD-005 or any prior decision. No promotion, lock, unlock, merge, rename, or authority designation is authorized. No commit or push is authorized as part of KD-010 until the resulting diff is audited against this decision.

---

## KD-011

1. **Decision ID:** KD-011
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(d) — validation criteria/process. Owner decision on the six 7(d) questions surfaced in the owner-decision brief: the meaning of validation, its criteria basis, the validation mechanism, required evidence, resulting status, and the validation↔release relationship.
4. **Action:** ADOPT — adoption of the owner's 7(d) decision (blocker 7(d) only)
5. **Rationale:** The owner has explicitly decided the 7(d) questions. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only owner-decision brief for KD-003 blocker 7(d). Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** The following KD-003 blockers are explicitly preserved and remain open; nothing in this decision resolves, narrows, or absorbs them:
   - 7(e) — applicable dependencies and relationships remain undefined.
   - 7(f) — unresolved terminology remains unresolved, including "applicable validation/release process." This decision's use of the word "applicable" (see owner statements below) does not define "applicable" and does not identify the applicable process.
   - 7(g) — release-version semantics remain unclarified.
   - 7(h) — the distinction between the protocol's `VALIDATED` state and KOS-RELEASE's `VALIDATION` terminology remains unreconciled. This decision's "marked VALIDATED" statement does not establish whether KOS-RELEASE's `VALIDATION` state is identical to the protocol's `VALIDATED` state.
   - 7(i) — the strength of "should include" / "may be used" remains unclarified; this decision does not fix the normative force of "should" or "may."

   This decision does not define: detailed validation criteria, acceptance thresholds, schemas, a universal validation workflow, a specific human/tool performer, evidence format or schema, release-version semantics, or dependency rules.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 blocker 7(d) recorded as resolved by owner decision; blockers 7(e)–7(i) remain open as stated above.

**Owner's decided statements (recorded verbatim as the decision content):**

1. Validation checks a KOSD module against the requirements already established for that module.
2. Validation does not create, invent, or establish those requirements.
3. The validation mechanism is whatever mechanism is applicable to that module.
4. Sufficient evidence must exist to demonstrate that the applicable validation was performed and passed.
5. A module that passes validation is marked VALIDATED.
6. Validation is a prerequisite for release, but validation itself does not constitute release.

---

## KD-012

1. **Decision ID:** KD-012
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(e) — applicable dependencies and relationships. Owner decision on the six 7(e) questions surfaced in the owner-decision brief: what makes a dependency applicable, what makes a relationship applicable, which are mandatory for release, the meaning of "present" in KOS-RELEASE requirement 5, whether dependency direction/order is required, and whether module-to-module dependencies must be explicitly declared.
4. **Action:** ADOPT — adoption of the owner's 7(e) decision (blocker 7(e) only)
5. **Rationale:** The owner has explicitly decided the 7(e) questions. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only owner-decision brief for KD-003 blocker 7(e). Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 7(f) — unresolved terminology remains open, including "applicable validation/release process" and "applicable project decision." This decision defines "applicable" only for dependencies and relationships under 7(e); it does not define "applicable" for any other governance term.
   - KD-003 7(g) — release-version semantics remain open.
   - KD-003 7(h) — the distinction between the protocol's `VALIDATED` state and KOS-RELEASE's `VALIDATION` terminology remains unreconciled.
   - KD-003 7(i) — the strength of "should include" / "may be used" remains unclarified.
   - KD-003 7(c) — the required-module-set question remains separate and unresolved; this decision does not enumerate the required-module set (KD-010's containment stands).
   - KD-011 — the validation definition remains intact and unchanged; this decision does not redefine validation or create validation-gate criteria.
   - KD-003 7(j) — the no-invention boundary remains intact.

   This decision does not create: dependency schemas, a dependency graph, mandatory ordering, universal module metadata, verification criteria, release-gate criteria, required-module lists, or implementation workflows. The statement in owner decision 3 below — that only explicitly identified release-relevant/release-required dependencies or relationships can block a release — is the owner's explicit statement, not a new release gate invented through this record.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 blocker 7(e) recorded as resolved by owner decision; blockers 7(c), 7(f), 7(g), 7(h), 7(i) remain open as stated above; KD-011 and 7(j) unchanged.

**Owner's decided statements (recorded verbatim as the decision content):**

1. An applicable dependency is one actually required for the module/release being considered to function, be validated, or be released as intended, rather than merely being related to it or mentioned somewhere.
2. An applicable relationship is one relevant to the module/release being considered and must be accounted for to correctly understand, validate, maintain, or release it.
3. Only dependencies or relationships that have been explicitly identified as release-relevant or release-required can block a release. Other applicable relationships may need to be accounted for without automatically becoming release blockers.
4. "Present" means the applicable dependency or relationship is identified and documented sufficiently for the release to account for it. It does not, by itself, require independent verification or satisfaction of every relationship.
5. Dependency direction or order is optional unless explicitly established as necessary or release-relevant.
6. Module-to-module dependencies must be explicitly declared when they are applicable and release-relevant, but not every possible relationship between modules must be declared.

---

## KD-013

1. **Decision ID:** KD-013
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(f), term 1 only — "applicable project decision." The remaining 7(f) terms are untouched by this decision.
4. **Action:** ADOPT — adoption of the owner's 7(f) term 1 decision (term 1 only)
5. **Rationale:** The owner has explicitly decided what makes a project decision "applicable." The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief for KD-003 7(f) term 1. Factual context only, not an added rule: the adopted protocol's eight-field decision record includes a stated-scope field (Item(s)). Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** This decision resolves only 7(f) term 1. The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 7(f) terms 4 ("applicable validation/release process"), 5 ("authoritative KOS/project state"), and 6 ("Master") remain open. In particular, this decision's use of "applicable" applies only to project decisions; it does not define "applicable" for any other 7(f) term.
   - KD-003 7(f) terms 2 ("silently altered") and 3 ("silently treated as authoritative") remain as previously categorized (established by KD-007; clarification only) — untouched by this decision.
   - KD-003 blockers 7(c), 7(g), 7(h), 7(i) remain open.
   - KD-011 (validation), KD-012 (dependencies/relationships), and KD-003 7(j) (no-invention boundary) remain intact and unchanged.
   - KD-003 itself and all prior KDs are unaltered.

   This decision adds no applicability criteria beyond the owner's explicit statement, invents no new protocol action, and does not redefine the KOS Decision & Promotion Protocol.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(f) term 1 recorded as resolved by owner decision; all other 7(f) terms and blockers remain as stated above.

**Owner's decided statement (recorded verbatim as the decision content):**

1. A project decision is applicable when its stated scope explicitly covers the item or action for which the decision is being relied upon.

---

## KD-014

1. **Decision ID:** KD-014
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(f), term 4 only — "applicable validation/release process." The remaining 7(f) terms are untouched by this decision.
4. **Action:** ADOPT — adoption of the owner's 7(f) term 4 decision (term 4 only)
5. **Rationale:** The owner has explicitly decided the remaining term 4 questions: whether validation and release are one process or two, what makes the combined process applicable, and whether KOS-RELEASE defines it. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief and evidence pass for KD-003 7(f) term 4, including KD-003's acceptance of KOS-RELEASE "as the intended KOSD release framework" and KD-003 7(a)'s recording of KOS-RELEASE promotion as the resolution path. Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** This decision resolves only 7(f) term 4. The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 7(f) terms 5 ("authoritative KOS/project state") and 6 ("Master") remain open.
   - KD-003 7(f) terms 2 ("silently altered") and 3 ("silently treated as authoritative") remain as previously categorized — untouched by this decision.
   - KD-003 7(h) — the distinction between the protocol's `VALIDATED` state and KOS-RELEASE's `VALIDATION` terminology remains unreconciled. This decision does not establish any state identity, mapping, or transition.
   - KD-003 blockers 7(c), 7(g), 7(i) remain open.
   - KD-011 (validation definition), KD-012 (dependencies/relationships), KD-013 ("applicable project decision"), and KD-003 7(j) (no-invention boundary) remain intact and unchanged. In particular, this decision does not redefine validation, does not broaden KD-013's "applicable" beyond project decisions, and adds no applicability criteria beyond the owner's explicit statement 2 below.
   - KOS-RELEASE is **not** promoted by this decision. The designation in owner statement 3 takes effect only upon a future promotion of KOS-RELEASE, which requires its own owner decision. KOS-RELEASE remains Draft and unpromoted.
   - KD-001 through KD-013 are unaltered.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(f) term 4 recorded as resolved by owner decision; all other 7(f) terms and blockers remain as stated above.

**Owner's decided statements (recorded verbatim as the decision content):**

1. Validation and release are one combined process.
2. The combined validation/release process is applicable to all KOSD modules and releases when they are being validated or released, unless a specific requirement establishes otherwise.
3. CORE/KOS-RELEASE.md is designated as the document defining that combined validation/release process, once KOS-RELEASE is promoted.

---

## KD-015

1. **Decision ID:** KD-015
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(f), term 5 only — "authoritative KOS/project state." The remaining 7(f) term 6 ("Master") is untouched by this decision.
4. **Action:** ADOPT — adoption of the owner's 7(f) term 5 decision (term 5 only)
5. **Rationale:** The owner has explicitly decided the term 5 questions: what composes the authoritative KOS/project state, how "current" is determined, the KOS/project state relationship, and conflict precedence. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief for KD-003 7(f) term 5. Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** This decision resolves only 7(f) term 5. The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 7(f) term 6 ("Master") remains open. KD-005's deferral is preserved exactly: Master remains undefined/deferred; no artifact, branch, state, or record is designated as Master by this decision; no authority mechanism or precedence rule for Master is established.
   - KD-003 7(f) terms 1 ("applicable project decision") and 4 ("applicable validation/release process") remain resolved as recorded in KD-013 and KD-014 — untouched by this decision.
   - KD-003 7(f) terms 2 ("silently altered") and 3 ("silently treated as authoritative") remain as previously categorized — untouched by this decision.
   - KD-003 blockers 7(c), 7(g), 7(h), 7(i) remain open.
   - KD-001 through KD-014 remain intact and unchanged, including KD-007 (LOCKED), KD-011 (validation), KD-012 (dependencies/relationships), KD-013 (project-decision applicability), and KD-003 7(j) (no-invention boundary).

   This decision invents no additional authority, precedence, state, or implementation rules beyond the owner's explicit statements below. The conflict-precedence stated in owner decision 4 is the owner's explicit determination, not a hierarchy invented through this record. "Applicable" in owner decisions 2 and 4 is used in the owner's own terms; this decision does not import KD-012's or KD-013's definitions of "applicable."
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(f) term 5 recorded as resolved by owner decision; 7(f) term 6 and all other blockers remain as stated above.

**Owner's decided statements (recorded verbatim as the decision content):**

1. The authoritative KOS/project state consists of the currently adopted decisions and the project content that those decisions establish as authoritative.
2. The current authoritative KOS/project state is the authoritative state established by the latest applicable adopted decisions and their resulting project state.
3. "KOS state" and "project state" refer to the same authoritative project state for purposes of KOSD.
4. When authoritative project content conflicts, the latest applicable adopted decision and its resulting authorized project state controls.

---

## KD-016

1. **Decision ID:** KD-016
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(f), term 6 only — "Master."
4. **Action:** DEFER — continuation of the existing KD-005 deferral (term 6 only)
5. **Rationale:** The owner has decided that "Master" remains deferred. This decision affirms KD-005's existing deferral and adds nothing to it. No definition of Master, no designation, no authority mechanism, no substitute, and no alteration of any other decision results from this record.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief for KD-003 7(f) term 6 and by KD-005's existing conditions. Classification, stated plainly: owner affirmation of an existing deferred decision.
7. **Conditions / Blockers:** This decision resolves only 7(f) term 6, and it resolves it by deferral only. The following are explicitly preserved; nothing in this decision changes, narrows, or absorbs them:
   - KD-005 remains in force in full, including its conditions 7(a)–7(f): O-001 remains unresolved; no artifact, branch, state, or record is designated as Master; no authority mechanism for Master is created or inferred; no precedence rule is created; any future establishment of Master requires a separate explicit owner decision defining what constitutes Master and the basis of its authority; the O-001 "Master is authoritative" REVIEW statement must not be treated as an operative authority rule merely because it exists in GOV-001.
   - This decision does not define Master.
   - This decision does not designate any artifact, branch, state, or record as Master.
   - This decision does not establish a Master authority mechanism.
   - This decision does not create a Master substitute or interim Master destination.
   - KD-015's authoritative KOS/project state definition is unaltered. This decision creates no relationship between Master and the KD-015 authoritative state — that relationship remains unresolved.
   - KD-003 7(f) terms 1, 2, 3, 4, and 5 remain resolved/recorded as in KD-013, KD-014, KD-015, and the prior categorizations — untouched by this decision.
   - KD-003 blockers 7(c), 7(g), 7(h), 7(i) remain open.
   - KD-001 through KD-015 remain intact and unchanged, including KD-008's no-substitute rule and KD-003 7(j) (no-invention boundary).
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(f) term 6 recorded as resolved-by-deferral, with the deferral defined entirely by KD-005 as affirmed above.

**Owner's decided statement (recorded verbatim as the decision content):**

- Master remains deferred.

---

## KD-017

1. **Decision ID:** KD-017
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(g) only — "release-version semantics."
4. **Action:** ADOPT — adoption of the owner's 7(g) decision (7(g) only)
5. **Rationale:** The owner has explicitly decided the release-version questions: format, assigner, timing, trigger, the release/KOS/module version relationship, immutability, and version identity retention. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief for KD-003 7(g). Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** This decision resolves only 7(g). The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 blockers 7(c) (required-module set), 7(h) (protocol `VALIDATED` vs KOS-RELEASE `VALIDATION`), and 7(i) ("should include" / "may be used" strength) remain open.
   - KD-003 7(f) terms 1–5 remain resolved/recorded as in KD-013, KD-014, KD-015, and the prior categorizations; term 6 ("Master") remains deferred under KD-005 as continued by KD-016 — untouched by this decision.
   - KD-001 through KD-016 remain intact and unchanged, including KD-011 (validation definition), KD-012 (dependencies/relationships), KD-013 ("applicable project decision"), KD-014 (combined validation/release process), KD-015 (authoritative KOS/project state), and KD-003 7(j) (no-invention boundary).
   - KOS-RELEASE is **not** promoted by this decision. Its version language (including req. 9) remains Draft proposal. This decision does not itself assign a release version to the current draft or to any release; assignment occurs only through the owner's authorization of a release, per owner statement 2 below.
   - No version-bump rules, prerelease rules, build-metadata rules, or other version semantics are established by this decision beyond the owner's explicit statements below. No additional rules are inferred from semver terminology.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(g) recorded as resolved by owner decision; all other blockers remain as stated above.

**Owner's decided statements (recorded verbatim as the decision content):**

1. KOSD release versions use the major.minor.patch format.
2. The Kustomz owner assigns the release version as part of authorizing the release.
3. Every newly authorized KOSD release receives a new release version.
4. The release version identifies the KOSD release itself; the KOS version identifies the version of the KOS/document framework; module versions identify individual modules. These are distinct version identities and do not automatically change one another.
5. Release versions are immutable once assigned.
6. A superseded or archived release permanently retains its originally assigned release version; that version is never reassigned.

---

## KD-018

1. **Decision ID:** KD-018
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(h) only — the relationship between the protocol's `VALIDATED` module status and KOS-RELEASE's `VALIDATION` release state.
4. **Action:** ADOPT — adoption of the owner's 7(h) decision (7(h) only)
5. **Rationale:** The owner has explicitly decided the 7(h) questions: whether the two states are the same or distinct, and the relationship between a module's `VALIDATED` mark and a release's `VALIDATION` state. The decision is recorded here in the owner's own terms, without extending, interpreting, or operationalizing them.
6. **Basis / Evidence:** Explicit owner decision communicated by Kustomz/Rick on 2026-09-19, informed by the read-only decision-preparation brief for KD-003 7(h). Classification, stated plainly: owner decision on inspected repository evidence.
7. **Conditions / Blockers:** This decision resolves only 7(h). The following remain explicitly preserved and open; nothing in this decision resolves, narrows, or absorbs them:
   - KD-003 blockers 7(c) (required-module set), 7(i) ("should include" / "may be used" strength) remain open.
   - KD-001 through KD-017 remain intact and unchanged, including:
     - KD-011 (validation definition) — unaltered. This decision does not redefine validation, add criteria, or change the `VALIDATED` marking rule.
     - KD-014 (combined validation/release process) — unaltered. This decision does not alter the one-process determination.
     - KD-012 ("applicable" for dependencies/relationships), KD-013 ("applicable project decision"), KD-015 (authoritative KOS/project state), KD-017 (release-version semantics), and KD-003 7(j) (no-invention boundary).
   - KOS-RELEASE is **not** promoted by this decision. Its Release States vocabulary (DRAFT, VALIDATION, RELEASED, SUPERSEDED, ARCHIVED) remains Draft proposal.
   - This decision invents no transitions, gates, sequencing, release criteria, workflows, or state models beyond the owner's explicit statements below. In particular, it establishes no transition rule into or out of the `VALIDATION` state and no gate beyond owner statement 2's stated requirement.
8. **Execution / Resulting State:** Append this record to `CORE/DECISIONS.md`; no file modification, promotion, lock, unlock, or status change is authorized. Resulting state: KD-003 7(h) recorded as resolved by owner decision; all other blockers remain as stated above.

**Owner's decided statements (recorded verbatim as the decision content):**

1. KOS-RELEASE's `VALIDATION` state and the protocol's `VALIDATED` module status are distinct.
2. A release in `VALIDATION` requires the applicable modules to have passed validation and been marked `VALIDATED`, but the release-level `VALIDATION` state is not itself a module `VALIDATED` status.

---

## KD-019

Date: 2026-09-19

Item(s): KD-003 7(c) — required-module set

Action: ADOPT

Rationale:
Resolve the authority question for the required-module set without selecting either CORE/KOS-MANIFEST.md or CORE/KOS-INDEX-001.md as authoritative.

Basis / Evidence:
Owner decision.

Conditions / Blockers:
- KD-010's containment remains in force until KOS-RELEASE is promoted.
- This decision does not promote KOS-RELEASE or establish its detailed required-module list beyond the authority rule below.
- No existing MANIFEST/INDEX discrepancy is resolved by selecting either document as authoritative.
- All prior decisions remain unchanged.

Owner statements:
1. KOS-RELEASE defines the required-module set for a KOSD release.
2. The required-module set is established by the requirements of CORE/KOS-RELEASE.md, rather than by CORE/KOS-MANIFEST.md, CORE/KOS-INDEX-001.md, or any other Draft enumeration.
3. Until KOS-RELEASE is promoted, its required-module set is not yet an authoritative released requirement.

Execution / Resulting State:
- KD-003 7(c) is resolved as an authority question.
- The actual required-module set remains to be established through KOS-RELEASE.
- No file other than CORE/DECISIONS.md is to be modified by this decision.

---

## KD-020

Date: 2026-09-19

Item(s): KD-003 7(i) — strength of “should include” and “may be used” in KOS-RELEASE

Action: ADOPT

Rationale:
Clarify the normative strength of the existing Release Integrity language without inventing additional release requirements.

Basis / Evidence:
Owner decision.

Owner statements:
1. “Should include” means the identified release content is expected to be included in a release, but the phrase does not by itself create an absolute release gate unless another requirement makes it mandatory.
2. “May be used” means the identified mechanism is optional and available for the stated purpose; its use is not mandatory by that phrase.
3. Neither phrase, by itself, creates a new release gate beyond the requirements otherwise established in KOS-RELEASE.

Conditions / Blockers:
- This decision does not modify the existing KOS-RELEASE text.
- This decision does not establish additional release gates, mandatory evidence requirements, or mandatory checksum use.
- All prior decisions remain unchanged.
- KOS-RELEASE remains Draft and is not promoted by this decision.

Execution / Resulting State:
- KD-003 7(i) is resolved.
- The existing “should include” and “may be used” language in KOS-RELEASE is interpreted according to the owner statements above.
- No file other than CORE/DECISIONS.md is to be modified by this decision.


---

## KD-021

1. **Decision ID:** KD-021
2. **Date:** 2026-09-19
3. **Item(s):** Proposed KOSD Sneak Architecture Definition — draft designation DRAFT-2026-09-19, proposed artifact path `CORE/KOS-SNEAK-ARCH.md`.
4. **Action:** ADOPT. The owner adopts the Sneak Architecture Definition into authoritative KOSD architecture, comprising:
   (a) **Identity/purpose:** Sneak is the Discord-facing conversational interface layer of the Kustomz ecosystem; not a standalone Discord bot; an interface into applicable Kustomz services and data.
   (b) **Closed seven-capability scope,** preserved exactly: (1) conversational interaction with Kustomz systems; (2) CSR2 intelligence; (3) dynamic member/user statistics; (4) Ticket Engine interaction; (5) transcript handling; (6) Project Vision integration; (7) external CSR2 data intake through the private #csr2-data-intake channel — changeable only by explicit owner decision.
   (c) **Authority/prohibition boundary:** Sneak reflects authoritative ecosystem state and never originates it. Sneak must not become a competing database, authority system, project-state source, separate source of truth, or redefiner of its own purpose, capabilities, or permissions. Prohibitions stand until overridden by explicit later owner decision recorded under the existing decision protocol.
   (d) **Continuity principle:** WEB → ANDROID → DISCORD/SNEAK. Web is the primary Toolbox experience; Android is planned. Users move between interfaces without losing relevant work-state or ecosystem context.
   (e) **Structural requirements:** KOSD shall define the authoritative boundaries for Sneak behavior rules; permission/authority rules; personality definition (with KOSD-defined rendering latitude); state classification criteria (authoritative vs. ephemeral); Kustomz↔Discord identity-linking architecture; conformance requirements; definition versioning; the interface/presentation semantic boundary; and the designated contract set with consumption obligations.
   Adoption is of the framework's shape. All currently undefined contents remain undefined.
5. **Rationale:** The owner has directed that Sneak's definition is part of authoritative KOSD architecture. Adopting the definition now fixes Sneak's identity, closed capability scope, and prohibition boundary before any implementation work begins; establishes that KOSD — not any implementation — defines Sneak's behavior, permissions, personality, state, conformance, and integration boundaries; and does so in implementation-model-independent form so the implementation-location decision remains open. It separates authoritative architecture from implementation-owned mechanics, preventing implementation-led redefinition of Sneak.
6. **Basis / Evidence:** Owner direction, 2026-09-19: Sneak is the Discord-facing conversational/interface layer of the Kustomz ecosystem (not a standalone bot, not a separate source of truth); Sneak's definition is authoritative KOSD architecture; the non-authority prohibitions; the WEB → ANDROID → DISCORD/SNEAK principle; Web primary, Android planned; the Kustomz identity as ecosystem identity distinct from a CSR2 account; the established Discord role structure, progression, and rejoin rules; Sneak as personality-driven and unique, not a generic utility bot. The proposed Sneak Architecture Definition draft (designation DRAFT-2026-09-19), reviewed with no internal contradiction requiring revision. Governing protocol context: KD-001, KD-014, KD-015, KD-017, KD-018, KD-019.
7. **Conditions / Blockers:** This adoption explicitly does NOT: select implementation model A, B, or C; place Sneak's executable implementation in KOSD; create or define Project Vision; create or define the Ticket Engine; define CSR2 intelligence (including its relation to NSB/SCB/TRB); define platform/service contracts; define role→permission mappings; define transcript rules; define #csr2-data-intake rules; define identity-linking mechanics; define state-classification criteria; define conformance procedures; assign a Sneak definition version (draft designation DRAFT-2026-09-19 is temporary and administrative only — not a version, creating no versioning precedent); or establish Sneak, or any artifact category named in the definition, as a KOSD module for KD-019 purposes (classification under KOS-RELEASE remains undetermined). All items marked UNDEFINED in the draft remain undefined. The implementation-location decision remains OPEN. Two known architectural tensions are recorded without resolution: (1) derived statistics (capability 3) must remain traceable to authoritative sources — the exact standard is undefined; (2) cross-interface continuity requires an eventual authoritative mechanism for portable work-state/context — the mechanism is undefined. Implementation-owned mechanics (hosting, runtime, libraries, Discord gateway mechanics, secret handling, presentation choices within the defined semantic boundary, caching mechanics within the to-be-defined state criteria, and other non-behavioral engineering detail) are explicitly outside the adopted architecture; nothing in this KD imposes requirements on them beyond the stated boundaries.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol (approval is not promotion). Upon authorized execution, the resulting state is: `CORE/KOS-SNEAK-ARCH.md` exists in KOSD containing the adopted framework — identity/purpose, closed capability scope, authority/prohibition boundary, continuity principle, and the structural "KOSD shall define" requirements — with all undefined contents marked as undefined and the draft's unresolved dependencies and open owner decisions carried forward. The adopted document remains subject to the KOS Decision & Promotion Protocol: future changes, including definition of currently-undefined contents, proceed through later KDs. The Sneak definition is authoritative KOSD architecture from adoption. No implementation is authorized by this KD.

---

## KD-022

1. **Decision ID:** KD-022
2. **Date:** 2026-09-19
3. **Item(s):** Proposed Sneak state-classification boundary — principles P1–P5, the AUTHORITATIVE / EPHEMERAL / UNDEFINED classifications, and proposed architectural constraint C0 — as set out in the revised proposal accepted for decision review on 2026-09-19.
4. **Action:** ADOPT. The owner adopts:
   (a) **P1–P5 as the Sneak state-classification principles:** P1 (reference rule — Sneak resolves authoritative-reference state against the authoritative holder, never originates it); P2 (discardability rule); P3 (read-as-fact rule — state read as fact requires an authoritative holder designated by KOSD architecture, which need not be KOSD itself); P4 (in-transit rule); P5 (deferral rule — classification only, imposing no persistence rule).
   (b) **The AUTHORITATIVE classifications (1a–1j) as proposed:** Kustomz ecosystem identity records; Discord↔Kustomz identity link records; member standing facts; Ticket Engine records; dispositioned transcript records; CSR2 intelligence source data; intake records post-disposition; Project Vision records (in principle); shared portable work-state (holder designated by KOSD architecture, never Sneak); and the Sneak definition itself as to *status* — 1j classifies the status of Sneak's behavior/permission/personality rules once defined, and does not imply their contents have been defined.
   (c) **The EPHEMERAL classifications (2a–2g) as proposed:** conversation/session scratch; caches of authoritative data (subject to the to-be-defined state criteria, with P3 as the tripwire); in-progress capture buffers (strictly in transit per P4); presentation state; the identity-link usage reference — the use-vs-ownership distinction only, prescribing no lifecycle or scope (2e); derived working values (traceable to authoritative sources); operational runtime state.
   (d) **The UNDEFINED classifications (3a–3i) as proposed,** preserved as UNDEFINED: computed member/user statistics as records; the transcript completion boundary; intake items pre-disposition; portable work-state records; ticket-draft state; Project Vision integration state; synthesized CSR2 intelligence; identity-link lifecycle edges; Sneak's own action records.
   (e) **C0 as an architectural constraint:** state classified as UNDEFINED under P5 must not be persisted by any Sneak implementation pending the explicit Kustomz decision that classifies it. "Persisted" means retained beyond the interaction in which the state arose, reused across interactions, or read by any party as fact. Transient in-transit handling toward a defined disposition (P4) is not persistence under this constraint.
5. **Rationale:** Establish the architectural state boundary before any implementation work begins: fix which state Sneak must resolve against authoritative holders versus may hold ephemerally; keep the boundary implementation-model-independent; preserve all undefined items and the KD-021 unresolved tensions; and make the persistence bar on UNDEFINED state an explicit adopted constraint rather than an implicit one.
6. **Basis / Evidence:** KD-021 (adopted 2026-09-19): Sneak's identity/purpose, closed seven-capability scope, authority/prohibition boundary, continuity principle, and the structural "KOSD shall define" requirements. The revised state-classification proposal, accepted for decision review 2026-09-19. KD-021's two recorded unresolved tensions: derived statistics must remain traceable to authoritative sources; cross-interface continuity requires an eventual authoritative mechanism for portable work-state/context.
7. **Conditions / Blockers:** This adoption explicitly does NOT: authorize any Sneak implementation; define storage or retention rules; define permissions; invent service contracts; define the Ticket Engine; define Project Vision; define CSR2 intelligence internals (including its relation to NSB/SCB/TRB); define identity-linking mechanics (including lifecycle and invalidation rules); assign a Sneak definition version; establish Sneak or any named artifact category as a KOSD module for KD-019 purposes; or select implementation model A, B, or C. Unresolved and carried forward: all UNDEFINED items (3a–3i); the two KD-021 tensions (the exact traceability standard for derived statistics; the authoritative portable work-state mechanism); the state-classification criteria referenced by 2b (still to be defined); the transcript and intake disposition rules referenced by 2c, 3b, and 3c; the identity-linking mechanics referenced by 2e and 3h; and the designation of the authoritative holder for purchase facts underlying 1c.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol (approval is not promotion). Upon authorized execution, the resulting state is: the adopted principles (P1–P5), classifications (AUTHORITATIVE / EPHEMERAL / UNDEFINED), and constraint C0 are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md); all UNDEFINED items remain marked as such; the two KD-021 tensions remain recorded as unresolved; and the document remains subject to the KOS Decision & Promotion Protocol, with future classification of UNDEFINED items proceeding through later KDs. No implementation is authorized by this decision.
