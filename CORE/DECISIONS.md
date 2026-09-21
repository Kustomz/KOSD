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
8. **Execution / Resulting State:** Authorized execution: none against the repository. No file modification, no status change, and no promotion is authorized by this decision. Resulting state: unchanged — CORE/STD-001.md remains exactly as before this record: Status Draft, "Kustomz Decision: _Not yet reviewed._", "Master Promotion: Not yet promoted." The authoritative record of this ruling is KD-002 in this log. 

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
7. **Conditions / Blockers:**   (a) Any change, supersession, or unlock of LOCKED status requires an explicit Kustomz owner decision recorded under the adopted KOS Decision & Promotion Protocol.
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
   - These sections are existing recovery/reconciliation records, not formal pause records created under an adopted governance rule.
7. **Conditions / Blockers:**
   (a) O-003 remains DEFERRED.
   (b) No formal pause-record schema or obligation is adopted by KD-008.
   (c) No storage location or Master substitute is designated.
   (d) No resume authority or procedure is established.
   (e) No existing Pause Boundary record is reclassified as a formal governance record.
8. **Execution / Resulting State:** No repository modification is authorized by KD-008. `GOVERNANCE/GOV-001.md` remains unchanged and remains DRAFT / RECOVERY-MAPPED. O-003 remains formally DEFERRED pending a future explicit owner decision.

---

## KD-009

1. **Decision ID:** KD-009
2. **Date:** 2026-09-19
3. **Item(s):** CORE/KOS-CORE-001.md Principle 4, specifically its sentence "Locked assets remain locked unless explicitly superseded."
4. **Action:** ADOPT
5. **Rationale:** Reconcile Principle 4 with the operative LOCKED definition adopted by KD-007. The existing sentence is narrower than the adopted rule because it omits explicit change and unlock actions.
6. **Basis / Evidence:** KD-007 and direct inspection of CORE/KOS-CORE-001.md Principle 4.
7. **Conditions / Blockers:** Only Principle 4 is to be reconciled. No other KOS-CORE-001 principle or wording is modified. The new wording must preserve the original meaning while incorporating the adopted LOCKED definition.
8. **Execution / Resulting State:** Authorized execution: Principle 4 is replaced with: "Locked assets are authoritative until explicitly changed, superseded, or unlocked by an explicit Kustomz owner decision under the adopted KOS Decision & Promotion Protocol." No other KOS-CORE-001 content is changed.

---

## KD-010

1. **Decision ID:** KD-010
2. **Date:** 2026-09-19
3. **Item(s):** MANIFEST/INDEX required-module-set discrepancy affecting CORE/KOS-RELEASE.md blocker 7(c).
4. **Action:** ADOPT
5. **Rationale:** Contain the discrepancy without selecting an authority source or inventing a required-module set.
6. **Basis / Evidence:** Owner decision based on the KOS-RELEASE blocker review and direct comparison of CORE/KOS-MANIFEST.md and CORE/KOS-INDEX-001.md.
7. **Conditions / Blockers:** Neither MANIFEST nor INDEX is designated authoritative by KD-010; no required-module set is invented; KOS-RELEASE blocker 7(c) remains until resolved under later decision; no module promotion is implied.
8. **Execution / Resulting State:** The discrepancy is contained as an unresolved KOS-RELEASE promotion blocker. No authority is assigned to MANIFEST or INDEX. No file modification is authorized beyond the decision log.

---

## KD-011

1. **Decision ID:** KD-011
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning the definition of validation.
4. **Action:** ADOPT
5. **Rationale:** Establish the minimum common definition of validation without inventing detailed criteria, schemas, or workflows.
6. **Basis / Evidence:** Owner decision informed by KOS-RELEASE and STD-001 review.
7. **Conditions / Blockers:** No detailed validation criteria, evidence schema, tooling, or workflow is created by this decision.
8. **Execution / Resulting State:** Validation checks a module against requirements already established for that module; validation does not create or invent requirements; the applicable mechanism is whatever applies to the module; sufficient evidence must show validation was performed and passed; a passing module is marked VALIDATED; validation is a prerequisite for release, not release itself.

---

## KD-012

1. **Decision ID:** KD-012
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning applicable dependencies and relationships.
4. **Action:** ADOPT
5. **Rationale:** Establish minimum common definitions without inventing dependency graphs or ordering.
6. **Basis / Evidence:** Owner decision informed by KOS-RELEASE review.
7. **Conditions / Blockers:** No schemas, graphs, ordering, or workflow are invented.
8. **Execution / Resulting State:** An applicable dependency is one actually required for function, validation, or release as intended; an applicable relationship is relevant and must be accounted for to correctly understand, validate, maintain, or release an item; only explicitly release-relevant/release-required dependencies or relationships can block release; "present" means identified and documented sufficiently for release to account for it; direction/order is optional unless explicitly necessary/release-relevant; module-to-module dependencies are explicitly declared when applicable/release-relevant, but not every possible relationship.

---

## KD-013

1. **Decision ID:** KD-013
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning the definition of an applicable project decision.
4. **Action:** ADOPT
5. **Rationale:** Establish the minimum scope test for reliance on a project decision.
6. **Basis / Evidence:** Owner decision.
7. **Conditions / Blockers:** No additional applicability mechanism is invented.
8. **Execution / Resulting State:** A project decision is applicable when its stated scope explicitly covers the item or action for which the decision is being relied upon.

---

## KD-014

1. **Decision ID:** KD-014
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning the applicable validation/release process.
4. **Action:** ADOPT
5. **Rationale:** Establish the minimum project-wide process boundary without inventing detailed release criteria.
6. **Basis / Evidence:** Owner decision.
7. **Conditions / Blockers:** No detailed validation/release criteria or workflow is invented.
8. **Execution / Resulting State:** Validation and release are one combined process. The combined process applies to all KOSD modules/releases when being validated/released unless a specific requirement says otherwise. CORE/KOS-RELEASE.md defines the combined process once promoted.

---

## KD-015

1. **Decision ID:** KD-015
2. **Date:** 2026-09-19
3. **Item(s):** Definition of authoritative KOS/project state.
4. **Action:** ADOPT
5. **Rationale:** Establish the authority rule needed by KOS-RELEASE without inventing a separate Master artifact.
6. **Basis / Evidence:** Owner decision.
7. **Conditions / Blockers:** The deferred Master question remains unresolved under KD-005/KD-016; no new artifact is designated.
8. **Execution / Resulting State:** Authoritative state consists of currently adopted decisions and project content those decisions establish as authoritative. Current authoritative state is the state established by the latest applicable adopted decisions and resulting authorized project state. For KOSD, KOS state and project state are the same. If authoritative content conflicts, the latest applicable adopted decision and resulting authorized project state controls.

---

## KD-016

1. **Decision ID:** KD-016
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning "Master".
4. **Action:** DEFER
5. **Rationale:** Continue the explicit deferral established by KD-005.
6. **Basis / Evidence:** KD-005 and owner decision.
7. **Conditions / Blockers:** No Master artifact, state, authority mechanism, substitute, or precedence rule is defined. The relationship between KD-015 and any future Master remains unresolved.
8. **Execution / Resulting State:** "Master remains deferred." No repository modification authorized beyond the decision log.

---

## KD-017

1. **Decision ID:** KD-017
2. **Date:** 2026-09-19
3. **Item(s):** KOS-RELEASE blocker concerning release-version semantics.
4. **Action:** ADOPT
5. **Rationale:** Establish immutable release-version semantics without inventing release workflow.
6. **Basis / Evidence:** Owner decision.
7. **Conditions / Blockers:** Document/module version identities remain distinct; no release is promoted by this decision.
8. **Execution / Resulting State:** KOSD release versions use major.minor.patch; owner assigns release version when authorizing release; every newly authorized release gets a new version; release/document/module version identities are distinct; release versions are immutable once assigned; superseded/archived releases retain their original version and never reuse it.
---

## KD-018

1. **Decision ID:** KD-018
2. **Date:** 2026-09-19
3. **Item(s):** KD-003 blocker 7(h) only — the relationship between the protocol's `VALIDATED` module status and KOS-RELEASE's `VALIDATION` release state.
4. **Action:** ADOPT
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
6. **Basis / Evidence:** KD-021 (adopted 2026-09-19): Sneak's identity/purpose, closed seven-capability scope, authority/prohibition boundary, continuity principle, and the structural "KOSD shall define" requirements. The revised state-classification proposal, accepted for decision review 2026-09-19. KD-021's two recorded unresolved tensions: the exact traceability standard for derived statistics; the authoritative portable work-state mechanism.
7. **Conditions / Blockers:** This adoption explicitly does NOT: authorize any Sneak implementation; define storage or retention rules; define permissions; invent service contracts; define the Ticket Engine; define Project Vision; define CSR2 intelligence internals (including its relation to NSB/SCB/TRB); define identity-linking mechanics (including lifecycle and invalidation rules); assign a Sneak definition version; establish Sneak or any named artifact category as a KOSD module for KD-019 purposes; or select implementation model A, B, or C. Unresolved and carried forward: all UNDEFINED items (3a–3i); the two KD-021 tensions (the exact traceability standard for derived statistics; the authoritative portable work-state mechanism); the state-classification criteria referenced by 2b (still to be defined); the transcript and intake disposition rules referenced by 2c, 3b, and 3c; the identity-linking mechanics referenced by 2e and 3h; and the designation of the authoritative holder for purchase facts underlying 1c.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol (approval is not promotion). Upon authorized execution, the resulting state is: the adopted principles (P1–P5), classifications (AUTHORITATIVE / EPHEMERAL / UNDEFINED), and constraint C0 are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md); all UNDEFINED items remain marked as such; the two KD-021 tensions remain recorded as unresolved; and the document remains subject to the KOS Decision & Promotion Protocol, with future classification of UNDEFINED items proceeding through later KDs. No implementation is authorized by this decision.

---

## KD-023

1. **Decision ID:** KD-023
2. **Date:** 2026-09-19
3. **Item(s):** Proposed Sneak Behavioral Boundary — rules B1–B14, as revised after architectural review against KD-001 through KD-022.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts the revised Sneak behavioral boundary to establish architectural behavior constraints before implementation. The adopted rules define Sneak's interface role, request-routing boundary, authoritative resolution behavior, prohibition on authority invention, derived-working-information boundary, state handling, action gate, deferral behavior, uncertainty handling, capability scope, cross-interface continuity, traceability, personality boundary, and identity-use boundary. The rules are adopted as architectural constraints and do not define or replace the separately deferred contents identified by KD-021 and KD-022.
6. **Basis / Evidence:** KD-021 (adopted Sneak architecture), KD-022 (adopted Sneak state-classification boundary), the revised KD-023 proposal, and final architectural review confirming no remaining conflicts, gaps, or required corrections. Owner decision communicated by Kustomz/Rick on 2026-09-19.
7. **Conditions / Blockers:** This adoption does NOT authorize Sneak implementation; define permissions or role mappings; define the Ticket Engine, Project Vision, CSR2 intelligence, NSB/SCB/TRB scope, transcript rules, intake disposition rules, identity-linking mechanics or lifecycle; define the authoritative holder for purchase facts; define portable work-state mechanics or holder; define persisted computed member/user statistics; establish a Sneak definition version; establish Sneak as a KOSD module for KD-019; define the personality itself; establish conformance procedures; define the designated contract set; or otherwise resolve any item expressly left UNDEFINED or OPEN by KD-021 or KD-022. B3 permits consultation of KD-022 2b ephemeral caches for responsiveness only; such caches never substitute for authoritative resolution and are never presented as authoritative. B5 is limited to KD-022 2f derived working information and does not classify KD-022 3a computed records.
8. **Execution / Resulting State:** Append this decision to CORE/DECISIONS.md. The revised B1–B14 behavioral boundary is now adopted as authoritative Sneak architecture. Execution of the corresponding architecture-document update is a separate authorized step under the adopted protocol. No Sneak implementation or other deferred architecture is authorized by this decision.

---

## KD-024

1. **Decision ID:** KD-024
2. **Date:** 2026-09-19
3. **Item(s):** Proposed Sneak Permission / Authority Boundary — principles PA0–PA9 as developed at the KD-021–KD-023 architectural level.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts the Sneak permission/authority boundary to make the behavioral authorization gate structurally operable before implementation. The adopted principles distinguish capability, authority, and permission; separate read authority from action authority; establish a conjunctive action authorization gate; keep permission grants with the applicable authoritative holder; prohibit permission invention, escalation, transfer, and social authorization; defer unresolved authorization determinations to the applicable authoritative system; bind authorization to the linked Kustomz identity; establish deny-by-default behavior; prevent Sneak from becoming an access-control authority for reads; and prohibit derivation from laundering or expanding access.
6. **Basis / Evidence:** KD-021 (adopted Sneak architecture), KD-022 (adopted Sneak state-classification boundary), KD-023 (adopted Sneak behavioral boundary), the proposed PA0–PA9 boundary developed for owner review on 2026-09-19, and explicit owner approval communicated by Kustomz/Rick on 2026-09-19.
7. **Conditions / Blockers:** This adoption explicitly does NOT: create role→permission mappings; define Discord permissions; define Ticket Engine permissions; define identity-linking mechanics; define contracts or interfaces; define storage or retention; authorize any implementation; classify any KD-019 module; or establish that any action is currently authorized. Under PA7, the action gate is deny-by-default until authorization is affirmatively established. Unresolved and carried forward: grant-holder designation per capability (T1); the applicable system for cross-system actions (T2); revocation freshness standards (T3); the positive derived-information attribution standard (T4); standing-as-permission-input (T5); and the KD-021 tensions concerning derived-statistics traceability and portable work-state.
8. **Execution / Resulting State:** Decision recorded only. The PA0–PA9 boundary is adopted as authoritative Sneak architecture. Execution of the corresponding architecture-document update is a separate authorized step under the adopted protocol. No implementation or other deferred architecture is authorized by KD-024.

---

## KD-025

1. **Decision ID:** KD-025
2. **Date:** 2026-09-20
3. **Item(s):** Proposed Sneak Permission Grant-Holder Designation framework — holder qualification (H1–H4), KOSD designation (D1–D4), grant resolution (R1–R4), and undefined/unresolvable-holder handling (U1–U3) — developed 2026-09-20 to address architectural tension T1. Designates no actual holder.
4. **Action:** ADOPT. The owner adopts H1–H4, D1–D4, R1–R4, and U1–U3 as the architectural rule for identifying and designating the authoritative holder of permission grants for Sneak authorization evaluations: a holder must be a KOSD-recognized system of record for the grant domain with KOSD-established resolvability and no circularity (H1–H4); holders are designated per action-domain by explicit KD, designation conferring no authorization (D1–D4); Sneak resolves per-evaluation, identity-bound determinations, accepting them without reinterpretation and persisting none as records (R1–R4); undefined, unresolvable, circular, or irreconcilably competing holders yield no determinable holder, in which case the action is not performed (U1–U3). PA0–PA9 are preserved exactly as adopted and are unmodified by this decision.
5. **Rationale:** KD-024 PA3 requires permission grants to live with the authoritative holder, but T1 left “which holder” without a rule — leaving PA5 deferral targetless and PA7’s closed gate a default rather than a governed state. This framework establishes *how* a holder qualifies and is designated, so future per-domain designations can proceed as individual KDs without revisiting the framework, while guaranteeing that adoption designates nothing and authorizes nothing.
6. **Basis / Evidence:** KD-024 (PA0–PA9, adopted); KD-022 (P1 authoritative-reference, P5 deferral, C0); KD-023 (B7 action gate, B8 deferral, B9 unresolved conditions); KD-021 (KOSD shall define permission/authority boundaries; role→permission mapping explicitly not adopted; designated contract set as future architecture); KD-015 (latest applicable decision controls); KD-007 (explicit change); KD-001 (protocol).
7. **Conditions / Blockers:** This adoption explicitly does NOT: designate any actual permission-grant holder for any capability, action, or domain; create role→permission mappings; define Discord permissions; define Ticket Engine permissions; define identity-link mechanics; define implementation, storage, caching behavior, APIs, contracts, or runtime behavior; authorize any currently undefined action; resolve T2 (applicable holder for cross-system actions); resolve T3 (revocation freshness); resolve T4 (derived-information positive attribution standard); resolve T5 (standing as permission input); classify any KD-019 module; or select implementation model A/B/C. Unresolved and carried forward: all per-domain holder designations (each requiring its own future KD); resolvability mechanisms (future contract architecture); T2–T5.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol. Upon authorized execution, H1–H4, D1–D4, R1–R4, and U1–U3 are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md), which remains subject to the KOS Decision & Promotion Protocol; per-domain holder designations proceed through later KDs. No implementation is authorized by this decision.


---

## KD-026

1. **Decision ID:** KD-026
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T2 architectural boundary — Applicable System for Cross-System Authorization: effect decomposition (T2-P1), three-role distinction (T2-P2), establishment rule (T2-P3), no Sneak-side decomposition (T2-P4), multiplicity/conjunction (T2-P5), failure modes (T2-P6), and legitimate execution/authorization split (T2-P7) — developed 2026-09-20. Model-independent; establishes no action footprint and designates no actual owner.
4. **Action:** ADOPT. The owner adopts T2-P1–T2-P7 as the architectural rule for identifying the applicable authoritative systems when an action crosses system boundaries: a cross-system action is evaluated as its constituent state effects (T2-P1); each effect distinguishes authorization owner, grant holder, and state owner/executor as three roles that may coincide or be split, with each applicable role-owner required to provide or establish its respective determination and no role's determination substituting for another's (T2-P2); role assignment per effect is established solely by KOSD architecture/contract/decision (T2-P3); Sneak never decomposes actions, infers involved systems, or assigns roles on its own authority, and any action whose footprint is not established is not authorized (T2-P4); multi-system authorization is conjunctive with no Sneak arbitration between authoritative systems (T2-P5); undefined, ambiguous, unavailable, or circular ownership fails closed via B9 and PA7 (T2-P6); execution and authorization may belong to different systems only when the split is KOSD-established, determinations are acyclic, and the executor originates no authorization (T2-P7).
5. **Rationale:** KD-024 PA5 defers to “the applicable authoritative system,” which is indeterminate for cross-system actions when no single system is applicable. Without a rule, Sneak would have to choose the applicable system itself (forbidden) or cross-system authorization would remain permanently unevaluable. This boundary makes cross-system authorization evaluable by decomposing actions into effects, establishing three roles per effect through KOSD architecture/contract/decision, requiring conjunction, and failing closed on any gap — without authorizing any action or establishing any footprint.
6. **Basis / Evidence:** KD-021 (Sneak is an interface, not an authority or source of truth); KD-022 (P1 authoritative holder; P5 deferral); KD-023 (B7 established-authority gate; B8 defer/interface; B9 unresolved conditions); KD-024 (PA2 authority element; PA4 no invention; PA5 deferral; PA7 deny-by-default; PA8 no Sneak-level judgments); KD-025 (H1–H4 qualification; D1–D4 per-domain designation, designation ≠ authorization; U1–U3 undetermined-holder handling; H4/U3 circularity); KD-015 (latest applicable decision controls); KD-007 (explicit change); KD-001 (protocol).
7. **Conditions / Blockers:** This adoption explicitly does NOT: choose implementation model A/B/C; invent concrete services, databases, APIs, Discord permissions, Ticket Engine permissions, or role→permission mappings; designate any actual permission-grant holder, state owner, or authorization owner; authorize any currently unauthorized action; define implementation mechanics; resolve T3 (revocation freshness), T4 (derived-information positive standard), or T5 (standing as permission input); create a new source of truth; establish any action's system footprint; grant Sneak any authority-determination capability; or provide inter-system conflict arbitration (B9 + PA7 remains the complete current answer). Unresolved and carried forward: T3/T4/T5; every cross-system action's footprint; every per-effect role-owner establishment; partial-effect atomicity mechanics (implementation, explicitly undefined); and any future conflict-arbitration question.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol. Upon authorized execution, T2-P1–T2-P7 are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md), which remains subject to the KOS Decision & Promotion Protocol; action footprints and role-owner establishments proceed through later KDs and contracts. No implementation is authorized by this decision. PA7 posture is unchanged: cross-system actions remain unauthorized until their applicable footprints and role-owners are established.


---

## KD-027

1. **Decision ID:** KD-027
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T3 architectural boundary — Revocation Freshness: event-relative validity (T3-P1), cached-consultation conditions (T3-P2), invalidating events (T3-P3), loss-of-permission handling (T3-P4), unestablishable freshness (T3-P5), differential stringency (T3-P6), authorization/read-cache distinction (T3-P7), and anti-ledger guarantees (T3-P8) — developed 2026-09-20.
4. **Action:** ADOPT. The owner adopts T3-P1–T3-P8 as the architectural rule for revocation freshness of cached permission/grant determinations: freshness is event-relative within holder- or KOSD-established validity bounds, never time-derived by Sneak (T3-P1); cached determinations may be consulted in authorization only within those bounds, with no known invalidating event, as transient single-evaluation consultation that never substitutes for resolution (T3-P2); revocation, expiration, supersession, holder change, identity-link change, or altering KOSD decisions invalidate cached determinations, which must then not be used (T3-P3); loss of permission is effective when the holder or KOSD establishes it, and unobserved loss is never evidence of validity (T3-P4); unestablishable freshness fails closed via R4/PA7 (T3-P5); stringency may differ by action/domain/consequence only as KOSD-established architectural rules, never Sneak-set tiers or durations (T3-P6); authorization caching and read-data caching are distinct regimes with a common honesty requirement (T3-P7); and the cache is structurally barred from becoming a source of truth or standing permission ledger (T3-P8).
5. **Rationale:** KD-024 PA3 and KD-025 R1 require per-evaluation, at-time-of-evaluation resolution against the holder, while KD-022 2b and KD-023 B3 permit ephemeral caches — leaving “fresh enough” undefined and revocation-while-cached ungoverned. This boundary reconciles them: per-evaluation resolution is the default, cached consultation the affirmatively-bounded exception; “fresh enough” is defined event-relatively without any time-based rule; revocation, expiration, and supersession defeat cached grants; and structural guarantees keep the cache from becoming a permission ledger. All failure modes route to PA7.
6. **Basis / Evidence:** KD-021 (prohibitions; KOSD shall define permission/authority boundaries); KD-022 (2b ephemeral caches subject to future criteria; P1 authoritative-reference; P3 tripwire; C0); KD-023 (B3 never-substitute caches; B4 no invented authority; B9 unresolved conditions); KD-024 (PA3 at-time-of-evaluation, no permission ledger; PA4 no escalation; PA7 deny-by-default; PA8 no Sneak-level judgments); KD-025 (R1 per-evaluation identity-bound determination; R3 no persisted grant records; R4 fail-closed; D4 designation change; H4/U3 circularity); KD-026 (per-role-owner determinations; T2-P6 unavailable owner); KD-015; KD-007; KD-001.
7. **Conditions / Blockers:** This adoption explicitly does NOT: invent a universal TTL or any duration-based rule; choose polling intervals; specify APIs, webhooks, cache technologies, or runtime behavior; define Discord permissions or Ticket Engine mechanics; designate any actual grant holder; authorize any currently unauthorized action; define role→permission mappings; resolve T4 (derived-information positive standard) or T5 (standing as permission input); establish any validity-bound values, revocation-awareness channels, or stringency tiers (all future KOSD/contract content); classify any KD-019 module; or select implementation model A/B/C. Until validity bounds are established for a domain, T3-P5 governs (re-resolve or fail closed). Unresolved and carried forward: T4/T5; E1 (ratification of holder-established bounds); E2 (revocation-awareness channels); E3 (invalidation blast radius); E4 (read-cache presentation rules); E5 (tier calibration).
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step per the protocol. Upon authorized execution, T3-P1–T3-P8 are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md), which remains subject to the KOS Decision & Promotion Protocol; bound values, channels, and tiers proceed through later KDs and contracts. No implementation is authorized by this decision.


---

## KD-028

1. **Decision ID:** KD-028
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T4 architectural boundary — Derived-Information Positive Attribution: attribution defined (T4-P1), minimum provenance (T4-P2), direct vs. multi-source (T4-P3), attributable transformation (T4-P4), source failure modes (T4-P5), authority preservation (T4-P6), presentation without record-creation (T4-P7), and attribution vs. authorization (T4-P8) — developed 2026-09-20 and reviewed before adoption.
4. **Action:** ADOPT. The owner adopts T4-P1–T4-P8 as the positive attribution/traceability standard for derived information, with the following review corrections: T4-P6 does not establish an undefined hierarchy of “lowest authority status”; instead, derivation acquires no authority merely through computation, each source retains its existing authority status, and the derived result remains derived unless a later explicit Kustomz decision establishes otherwise. Where a source determination is subject to KD-027/T3, T3 invalidation governs that attribution anchor; T3 is not thereby made a universal freshness regime for all read/source data. Attribution is the establishable property of which authoritative source(s), what architectural-level operation, and which obtained source determination a derived value rests on; traceability requires all three as the minimum provenance; direct-source presentation requires source identity plus applicable freshness, while multi-source derivation requires per-source attribution and no invented consensus; transformations are described in ordinary architectural terms sufficient for independent logical reproduction without implementation schemas or artifacts; unknown, unavailable, ambiguous, stale, or conflicting sources are handled without invention; derived information does not gain or alter authority merely through derivation; attributed ephemeral presentation does not classify or create persisted computed records; and attribution and authorization remain independent requirements.
5. **Rationale:** KD-021 left the exact traceability standard for derived statistics undefined, and KD-023 B12 deferred the positive attribution standard to future architecture. KD-022 2f, KD-023 B5/B12, and KD-024 PA9 established the need for traceability while prohibiting authority creation or access laundering. T4 supplies the affirmative, model-independent standard while preserving KD-022 3a and C0. The review corrections prevent T4 from inventing an authority-ranking hierarchy or accidentally applying T3's authorization-freshness regime to all source data.
6. **Basis / Evidence:** KD-021 (Sneak architecture and traceability tension); KD-022 (P1, 2f, 3a, C0); KD-023 (B5, B9, B12); KD-024 (PA4, PA9); KD-025 (R2); KD-026 (per-effect/per-role ownership); KD-027 (T3-P3 and T3-P7); KD-015; KD-007; KD-001; and owner approval communicated by Kustomz/Rick on 2026-09-20 after architectural review.
7. **Conditions / Blockers:** This adoption explicitly does NOT: define database schemas; invent provenance formats, IDs, APIs, logging systems, or storage mechanisms; designate any actual source system; define CSR2 intelligence internals; define Project Vision or Ticket Engine; authorize any action or require any derivation; create a new source of truth; resolve T5 (standing as permission input); classify persistent computed statistics under KD-022 3a; define presentation/display rules; classify any KD-019 module; or select implementation model A/B/C. It does not establish an authority-status hierarchy. It does not make KD-027/T3 a universal freshness regime for ordinary read/source data. Unresolved and carried forward: T5; E1 provenance retention without shadow records; E2 attribution display; E3 description sufficiency; E4 conflict presentation choice; E5 reuse pressure on the 3a line; and any source-data freshness rules not otherwise established by applicable architecture/contracts.
8. **Execution / Resulting State:** Decision only; execution is a separately authorized step under the protocol. Upon authorized execution, T4-P1–T4-P8, as corrected above, are recorded in the authoritative Sneak architecture document (CORE/KOS-SNEAK-ARCH.md), which remains subject to the KOS Decision & Promotion Protocol. No implementation is authorized by this decision.


---

## KD-029

1. **Decision ID:** KD-029
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T5 architectural boundary — Standing as Permission Input: four-level distinction (L1 authoritative standing fact, L2 standing as permission input, L3 standing-derived information, L4 standing as permission), prerequisites T5-R1–T5-R4, fail-closed conditions T5-F1–T5-F4, and associated exclusions and interactions with KD-022 through KD-028.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts a boundary that distinguishes authoritative standing facts from their possible future use as inputs to permission determinations, while explicitly prohibiting the inference that standing itself constitutes permission. Standing may be considered by an applicable permission holder only under an established basis; Sneak does not perform the standing-to-permission inference, does not originate permission, and does not override the holder's determination. The boundary closes the previously undefined inference gap while enabling no currently unauthorized action.
6. **Basis / Evidence:** KD-021 through KD-028, including KD-022 1c and 3a/C0; KD-023 B3, B4, B5, B7, B8, B9, B10, B12, and B14; KD-024 PA0, PA2, PA3, PA4, PA5, PA6, PA7, and PA9; KD-025 D1, R1–R4; KD-026 per-effect authorization roles; KD-027 freshness rules; KD-028 attribution and authorization separation; the T5 proposal reviewed for owner decision; and explicit owner approval communicated by Kustomz/Rick on 2026-09-20.
7. **Conditions / Blockers:**
   - **T5-P1:** L1 standing is an authoritative ecosystem fact; L2 is standing considered by the permission holder as an input under an established basis; L3 is standing-derived information subject to KD-022 2f, B5, PA9, and KD-028; L4 is treating standing itself as permission and is prohibited. L1–L3 never imply L4.
   - **T5-P2:** Standing may be an authorization input in principle, but the standing-to-permission inference is never Sneak's. The applicable permission holder performs the determination under an established basis; Sneak may resolve/provide standing facts when legitimately required, but never frames standing as permission.
   - **T5-P3:** The permission holder remains responsible for the actual grant determination. Standing is an input, not the decision; a holder denial or unavailable determination governs and cannot be overridden by favorable standing.
   - **T5-P4:** Informational eligibility is not authorization and does not satisfy any element of the PA2 action gate.
   - **T5-R1:** The authoritative source/holder for the standing facts in question must be designated before Sneak relies on those facts as an authorization input.
   - **T5-R2:** The permission holder for the action must be designated under KD-025 D1.
   - **T5-R3:** An established standing-to-permission basis must exist, whether through a future KOSD-established mapping or a holder-established determination procedure; T5 chooses neither path.
   - **T5-R4:** Standing evaluation is bound to the linked identity and may not use another identity's, aggregate, or comparative standing.
   - **T5-F1:** Standing that is unavailable, ambiguous, stale, or conflicting makes a dependent permission evaluation undeterminable and therefore subject to PA7. Stale standing follows applicable T3 validity; conflicting standing is not synthesized.
   - **T5-F2:** A change in standing supersedes prior standing-anchored inputs; affected evaluations must be re-evaluated. Identity-link changes require re-evaluation for the newly evaluated subject.
   - **T5-F3:** A permission-holder denial or unavailable determination is not bypassed or cured by favorable standing.
   - **T5-F4:** Computed standing statistics classified under KD-022 3a remain UNDEFINED as records and may not be persisted or used by Sneak as permission inputs under C0; only authoritative standing facts within the established prerequisites may participate.
   - T5 does not designate any actual standing source, permission/grant holder, or system; create role-to-permission mappings; authorize any currently unauthorized action; classify KD-022 3a; establish a standing-to-permission threshold, event taxonomy, or inference rule; choose between holder-internal consideration and a future KOSD mapping; define implementation, storage, schemas, contracts, APIs, or runtime mechanics; or modify any prior adopted boundary.
   - The authoritative standing fact remains distinct from its authorization usability: absence of a designated source or permission basis prevents Sneak from relying on standing for authorization, but does not by itself demote or invalidate the standing fact under KD-022 1c.
   - Current prerequisites for standing-aware permission remain unmet where their respective designations or bases have not been established; adoption of T5 therefore enables no action by implication.
8. **Execution / Resulting State:** Append KD-029 to CORE/DECISIONS.md. The T5 standing-as-permission-input boundary is now adopted as authoritative Sneak architecture. Execution of the corresponding architecture-document update is a separate authorized step under the adopted protocol. No implementation, holder designation, role-to-permission mapping, or currently unauthorized action is authorized by this decision.

---

## KD-030

1. **Decision ID:** KD-030
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T6 architectural boundary — Transcript Completion & Disposition Boundary: the 2c in-progress transcript capture to 1e dispositioned transcript record crossing, including no-silent-promotion (T6-P1), declaration-authority establishment (T6-P2), disposition/status-transition distinction (T6-P3), designated-holder requirement (T6-P4), faithful transition (T6-P5), and separation of 1e transcript records from 3i Sneak action records (T6-P6), with prerequisites T6-R1–T6-R3 and fail-closed conditions T6-F1–T6-F4.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts a minimum architectural boundary for the currently undefined 2c→1e transcript lifecycle crossing. The boundary prevents silent promotion, prevents Sneak from inventing completion authority, requires a designated holder before a dispositioned record can exist, preserves content fidelity during the status transition, and keeps Sneak action records distinct from transcript records. The boundary closes the transition rule without prematurely defining transcript content, destinations, retention, implementation mechanics, or the unresolved fate of undeliverable captures.
6. **Basis / Evidence:** KD-021 through KD-029, including KD-022 2c/1e/3b/3i and P4/C0; KD-023 B4, B6, B9, and B12; KD-024 PA4 and the fail-closed action boundary; KD-025 holder-designation principles; KD-026 cross-system authorization boundary; KD-027 freshness boundary; KD-028 attribution and presentation-versus-record distinction; KD-029 prerequisite/fail-closed pattern; the T6 proposal reviewed by Rico and revised to replace the ambiguous “must drain” wording in T6-F1; and explicit owner approval communicated by Kustomz/Rick on 2026-09-20.
7. **Conditions / Blockers:**
   - **T6-P1:** A 2c capture buffer becomes a 1e dispositioned record only upon an authorized completion declaration. Aging, accumulation, session end, or Sneak unilateral action do not constitute a declaration.
   - **T6-P2:** Completion-declaration authority and its conditions must be established by KOSD architecture/decision. Sneak does not declare completion on its own authority; inactivity, session idle, and conversational closure are not declarations.
   - **T6-P3:** Disposition is the authorized status transition from 2c to 1e. Destination, format, channel, and other mechanics remain future architecture/contracts/implementation concerns.
   - **T6-P4:** Effective disposition requires a KOSD-designated holder for the dispositioned transcript record. Without a designated holder, a declaration is ineffective and does not create a 1e record.
   - **T6-P5:** Disposition changes status, not content. Sneak does not summarize, redact, reorder, or reinterpret during the transition. Any transformation requires separate KOSD establishment and applicable T4 attribution; the default transition is faithful.
   - **T6-P6:** A 1e transcript record concerns the interaction itself; 3i Sneak action records remain a distinct UNDEFINED category and are not classified by T6.
   - **T6-R1:** Completion-declaration authority and conditions remain to be established.
   - **T6-R2:** The designated holder for dispositioned transcript records remains to be established under KD-022 P3 and is distinct from permission grant-holder designation under KD-025.
   - **T6-R3:** Transcript content rules remain undefined under KD-021 and must exist before disposition can occur.
   - **T6-F1:** If no authorized declaration exists, content remains 2c and remains subject to KD-022 P4. It may not be retained indefinitely as an unauthorized persistent record. No discard, archival, transfer, or other final disposition is implied until an applicable disposition authority and rule are established.
   - **T6-F2:** A declaration without a designated holder is ineffective. The undeliverable buffer must not become a de facto 1e record through retention.
   - **T6-F3:** Sneak never self-declares completion; idle, inactivity, and conversational closure are not declarations.
   - **T6-F4:** The undeliverable-transcript case has no authorized resolution under T6. No archiving, indefinite retention, or discard authority is established; the gap remains an explicit future decision item.
   - T6 does not define transcript content, formats, schemas, channels, destination mechanics, retention durations, actual holder designation, grant-holder designation, completion declarer, KD-022 3c intake specifics, 3i classification, implementation, or any currently unauthorized action.
   - T6 does not modify any prior adopted boundary and does not authorize implementation.
8. **Execution / Resulting State:** Decision only. T6-P1–T6-P6, T6-R1–T6-R3, and T6-F1–T6-F4 are now adopted as the authoritative Sneak architectural boundary for transcript completion/disposition. The corresponding update to CORE/KOS-SNEAK-ARCH.md is a separate authorized execution step under the adopted protocol. No implementation, holder designation, completion authority, or currently unauthorized action is authorized by KD-030.

---

## KD-031

1. **Decision ID:** KD-031
2. **Date:** 2026-09-20
3. **Item(s):** Proposed T7 architectural boundary — Intake Holding, Routing & Undeliverable-Content Boundary (KD-022 3c; T6-E1): T7-P1–T7-P7, prerequisites T7-R1–T7-R3, and the associated fail-closed handling.
4. **Action:** ADOPT
5. **Rationale:** KD-022 3c leaves intake pre-disposition holdings unclassified, while no adopted rule distinguishes unvetted external intake data from authoritative ecosystem state, governs routing failure, or addresses the undeliverable-content gap identified by T6-E1. The owner adopts a bounded architectural rule: intake pre-disposition holdings are EPHEMERAL and interaction-scoped; intake content is unvetted by default and is not authoritative merely because it is received; the holding is bounded within the interaction; only the structural crossing principles from T6-P1–P4 apply to intake, not T6-P5's transcript-specific fidelity rule; routing failure does not reclassify or authorize; and no cross-interaction persistence is permitted without an established authoritative holder/classification. The boundary deliberately leaves the no-authorized-next-state case unresolved rather than inventing persistence, discard, destination, holder, or authority.
6. **Basis / Evidence:** KD-021 capability #7 and authority/prohibition boundary; KD-022 P2/P3/P4/C0 and 3c; KD-023 B4/B6/B8/B9; KD-024 PA4; KD-026 cross-system effect/role boundary; KD-028 T4 attribution and attribution-versus-authorization distinction; KD-030 T6-P1–P4 and T6-E1/E2; revised T7 proposal reviewed by Rico and explicitly approved by Kustomz/Rick on 2026-09-20.
7. **Conditions / Blockers:**
   - **T7-P1:** Intake items awaiting disposition are intake buffers classified as EPHEMERAL and therefore interaction-scoped under KD-022 P2. They are not records and are not authoritative.
   - **T7-P2:** Intake content is unvetted by default. Sneak must not present it as authoritative under B4. Presentation of intake content remains subject to applicable T4 attribution; unvetted does not mean unattributed.
   - **T7-P3:** Intake holding is bounded within the interaction. Cross-interaction persistence requires a designated authoritative holder under KD-022 P3; none is designated by KD-031. Sneak may not invent a hold bound.
   - **T7-P4:** Intake disposition adopts only T6's structural crossing principles: no silent promotion; established declaration authority; disposition as status transition rather than destination; designated receiving holder; and no transition until T7-R1–R3 are established. T6-P5's transcript-specific content-fidelity requirements are not extended to intake. Intake vetting/transformation/content rules remain undefined.
   - **T7-P5:** For content authorized for disposition but lacking a designated holder/destination, Sneak has no discard, archival, transfer, or other final-disposition authority. While the relevant interaction/state exists, Sneak may surface the undecidable disposition to the Kustomz owner under B8/B9 and KD-001/KD-007. This does not authorize retaining the item across interaction end merely to await a later decision; “await” implies no persistence, callback, or retained state.
   - **T7-P6:** Routing failure does not reclassify or authorize. Sneak does not retry beyond established rules, reroute to an unestablished destination, or treat failure as disposition.
   - **T7-P7:** KD-022 does not permit an intake holding to outlive the interaction absent an authoritative holder/classification. If no authorized holder/state exists at interaction end, KD-031 establishes no authorized next state and invents none. Any mechanism permitting unresolved intake to survive the interaction requires a future Kustomz decision establishing the necessary authoritative holder/classification.
   - **T7-R1:** Intake declaration authority remains to be established.
   - **T7-R2:** Designated intake holder remains to be established.
   - **T7-R3:** Intake routing/content rules, including any hold bound, remain to be established.
   - No new state category, implementation, schema, API, storage mechanism, contract, destination, actual holder, discard authority, or currently unauthorized action is established. Adopted capability #7 remains intact; cross-interaction retention/disposition is simply not authorized where its required holder/classification has not been established.
   - T6 is otherwise unchanged, and all prior adopted decisions remain unchanged.
8. **Execution / Resulting State:** KD-031 is adopted as the authoritative Sneak architectural boundary for intake holding, routing, and undeliverable-content handling. Execution of the corresponding update to CORE/KOS-SNEAK-ARCH.md is a separate authorized step under the adopted protocol. No implementation or currently unauthorized action is authorized by KD-031.


---

## KD-032

1. **Decision ID:** KD-032
2. **Date:** 2026-09-20
3. **Item(s):** Proposed Kustomz-to-Discord Identity-Linking Architecture (IL-D, IL-H, IL-L, IL-S, IL-C, IL-F, IL-A, IL-X, IL-R, and IL-E), establishing the architectural identity-linking boundary for Sneak without selecting implementation or designating an actual holder.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts the proposed identity-linking architecture as the bounded establishment required by KD-021. Kustomz identity and Discord identity remain distinct; a link is a holder-asserted mapping rather than a merge; Sneak consumes but never authors link state; identity-link state remains within the existing KD-022 classifications; the link answers identity, not permission; link changes participate in KD-027 invalidation; applicable KD-028 attribution remains distinct from authorization and applies where information derived from the identity link is presented; and identity continuity is explicitly separated from portable work-state continuity. No actual holder, lifecycle mechanism, verification method, schema, implementation, or authorization mapping is established by KD-032.
6. **Basis / Evidence:** KD-021 identity-linking architectural requirement and B14; KD-022 1b, 2e, 3h, and C0; KD-023 B3, B4, B11, B12, B14; KD-024 PA2, PA6, PA7, and PA9; KD-025 D1 and holder-designation principles; KD-027 T3-P3 invalidating events and freshness boundary; KD-028 attribution/authorization separation; KD-015 authoritative-state rule; KD-001 decision/promotion protocol; and the identity-linking proposal reviewed by Rico and approved by Kustomz/Rick on 2026-09-20.
7. **Conditions / Blockers:**
   - **IL-D — Distinct Identities and Mapping:** Kustomz identity and Discord identity remain distinct identities. “Linked” means a holder-asserted mapping between one Discord identity and one Kustomz identity; linking does not merge the identities. For a Sneak interaction, one Kustomz identity must be determinable for identity-bound evaluation; if it cannot be determinately resolved, the interaction fails closed for identity-bound use under B9/PA7.
   - **IL-H — Link-State Holder:** The existence and status of an identity link require an authoritative Kustomz-ecosystem holder designated by a future explicit KOSD decision following KD-025 D1. Sneak never qualifies as the holder. The identity-link holder is architecturally distinct from any permission-grant holder; the same underlying system may only fill both roles if separately established for each domain.
   - **IL-L — Link-State Lifecycle:** Sneak consumes link state and never authors it. Lifecycle procedures for creation, change, suspension, removal, and related lifecycle edges remain UNDEFINED under KD-022 3h until separately established. A link change is an invalidating event for cached authorization determinations under KD-027 T3-P3.
   - **IL-S — State Classification:** No new state category is created. Identity-link records remain AUTHORITATIVE under KD-022 1b; identity-link usage reference remains EPHEMERAL under 2e; identity-link lifecycle edges remain UNDEFINED under 3h. No persistence or lifecycle mechanism for 3h is established by KD-032.
   - **IL-C — Identity Is Not Permission:** An established link answers “who,” not “may.” It supplies the identity term required by PA2 and PA6; the remaining authorization requirements remain independently applicable. An absent or undeterminable link makes the identity-bound evaluation undeterminable and therefore fails closed under PA7; the link itself is not a permission grant.
   - **IL-F — Freshness Interaction:** Under KD-027, a link change invalidates cached authorization determinations whose identity binding depends on the changed link. Sneak must not treat an authorization determination anchored to a superseded identity link as current where the applicable freshness boundary establishes invalidation.
   - **IL-A — Attribution Interaction:** KD-028 remains independent from identity authorization. Where information is derived from an identity link and presented as derived information, applicable KD-028 attribution requirements apply. Direct presentation of authoritative identity-link state remains subject to KD-023 B12 and the applicable authoritative source; KD-028 does not become a universal attribution regime merely because the information concerns identity linking.
   - **IL-X — Cross-Interface Identity Continuity:** Identity linking provides the architectural identity-continuity substrate for WEB → ANDROID → DISCORD/SNEAK, but establishes no portable work-state mechanism. The authoritative portable work-state/context mechanism remains UNDEFINED under KD-021/KD-022 1i/3d.
   - **IL-R — Prerequisites:** Actual holder designation; lifecycle procedures; reliable link-state resolution; and any conditional cross-system role establishment required by KD-026 must be established before dependent identity-bound actions can operate. Adoption of KD-032 does not satisfy those prerequisites by implication.
   - **IL-E — Explicit Exclusions:** KD-032 does not designate the actual link holder; define link-resolution mechanics; define Discord-side identity assertion or verification strength; define a linking ceremony; define record metadata or schemas; establish broader cardinality rules beyond the one-Kustomz-identity-per-Sneak-interaction boundary; define Discord-side lifecycle state; define portable work-state mechanics; designate any permission or authorization holder; create role-to-permission mappings; authorize currently unauthorized actions; or select implementation model A/B/C.
   - Identity-link state remains subject to KD-022 C0: undefined lifecycle-edge state must not be persisted by Sneak pending explicit classification/establishment.
   - KD-032 does not modify any prior adopted boundary. It establishes no new state category, no new authority system, no competing source of truth, and no implementation authorization.
8. **Execution / Resulting State:** KD-032 is adopted as the authoritative architectural identity-linking boundary. Authorized execution includes appending this decision to CORE/DECISIONS.md and recording the corresponding IL rules in CORE/KOS-SNEAK-ARCH.md. No actual holder designation, lifecycle implementation, identity verification mechanism, permission mapping, or currently unauthorized action is authorized.


---

## KD-033

1. **Decision ID:** KD-033
2. **Date:** 2026-09-20
3. **Item(s):** Proposed Identity-Link Resolution / Resolvability architectural boundary for Sneak (RL-P, RL-D, RL-H, RL-B, RL-F, RL-T, RL-S, RL-X), establishing what reliable Kustomz-to-Discord identity-link resolution means without designating the actual link holder or selecting implementation mechanics.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts a bounded resolution boundary required by KD-032: reliable resolution means obtaining the designated holder's authoritative link-status determination for the addressing Discord identity, per interaction, with one unambiguous Kustomz identity and established validity. Sneak does not independently verify, corroborate, adjudicate, or reinterpret the holder's determination. Undeterminable resolution fails closed for identity-bound use while preserving the distinction between identity resolution and authorization.
6. **Basis / Evidence:** KD-032 IL-H, IL-C, IL-F, and IL-R; KD-025 H/D/R/U holder-resolution principles; KD-023 B3, B9, B12, and B14; KD-024 PA6 and PA7; KD-027 T3-P3 and freshness principles; KD-022 2e and C0; KD-026 T2 cross-system role boundary; the KD-033 identity-link resolution proposal reviewed by Rico and explicitly approved by Kustomz/Rick on 2026-09-20. The proposal also identifies the access/query basis for Sneak to obtain the holder determination as a prerequisite rather than an established mechanism.
7. **Conditions / Blockers:**
   - **RL-P — Resolution:** Resolution is Sneak obtaining the designated holder's authoritative link-status determination for the addressing Discord identity, per interaction. “Reliable” means holder-sourced, unambiguous as to one Kustomz identity, and within established validity. Sneak never independently verifies the holder's determination.
   - **RL-D — Determinability:** Resolution is determinable only when exactly one Kustomz identity is established for the addressing Discord identity, the determination is unambiguous, and no invalidating condition applies. No designated holder, unreachable holder, no-link/suspended/removed/unknown status, multiple candidates, stale determination, or otherwise unascertainable addressing identity makes resolution undeterminable. Undeterminable resolution fails closed for identity-bound use under B9/PA7.
   - **RL-H — Holder Authority:** Without a designated holder, no reliable resolution exists. The designated holder's determination is the answer; Sneak does not corroborate, combine sources, or adjudicate against it. Holder designation and resolution are distinct establishments.
   - **RL-B — Boundary Interaction:** B3 grounds resolution in the designated holder; KD-022 2b caches never substitute for holder resolution. B9 surfaces ambiguity without converting it into fact. The resolved identity supplies the identity term used by PA6 and applicable identity-bound evaluation. Link changes invalidate applicable determinations under T3-P3. Where validity bounds have not been established, a resolution determination is limited to the interaction's ephemeral 2e usage scope.
   - **RL-F — Failure Handling:** Unavailable resolution has no fallback, cross-domain inference, or stale reuse. Ambiguous resolution is not disambiguated by Sneak. Stale resolution requires re-resolution or R4/PA7. A conflict within the holder's determination is ambiguous; non-holder information does not override the holder's authoritative determination.
   - **RL-T — Read/Authorization Separation:** Identity-link resolution is a read determination, never authorization. It satisfies none of PA2's authorization elements 1–3; any action still requires the complete PA2 gate, including identity binding.
   - **RL-S — Transient Resolution State:** Resolution handling is transient only: in-flight request/response state, a parsed candidate, or a 2e identity-link usage reference. Sneak does not persist resolution results as a record, ledger, or cross-interaction shared state. Failed resolution leaves no retained resolution state.
   - **RL-X — Cross-System Boundary:** Cross-system crossings defer to KD-026. This proposal assigns no authorization-owner, grant-holder, or state-owner/executor role. The access/query basis by which Sneak may obtain the designated holder's determination is itself a prerequisite and is not established by KD-033.
   - **Dependencies:** D-RL1 actual holder designation; D-RL2 link-resolution mechanics; D-RL3 query/access basis; D-RL4 link lifecycle procedures; D-RL5 validity bounds; D-RL6 any conditional KD-026 cross-system role establishment.
   - **Explicitly Undefined:** The actual identity-link holder; resolution/query mechanics; the access/query basis; validity bounds; Discord-side assertion or verification mechanics; retry/timing behavior; failure-presentation wording; and all other matters excluded by the proposal. No new state category, implementation, API, schema, database, Discord ceremony, permission mapping, identity-link creation/removal mechanism, portable work-state mechanism, or currently unauthorized action is established.
   - No circularity is introduced: the resolved identity is never used to authorize or establish the authority required to resolve that identity. Sneak does not “verify” the holder through an independent authority and does not create a retained resolution ledger.
   - KD-033 does not designate an actual holder, establish the query/access contract, satisfy any unresolved KD-032 prerequisite except the architectural meaning of reliable resolution, or authorize dependent identity-bound actions by implication.
8. **Execution / Resulting State:** Authorized execution: append KD-033 to CORE/DECISIONS.md and record the corresponding RL rules in CORE/KOS-SNEAK-ARCH.md. Resulting state: KD-033 is adopted as the authoritative Sneak identity-link resolution boundary. No actual holder designation, query/access mechanism, lifecycle implementation, verification mechanism, permission mapping, or currently unauthorized action is authorized.


---

## KD-034

1. **Decision ID:** KD-034
2. **Date:** 2026-09-20
3. **Item(s):** Proposed Sneak Identity-Link Resolution Access / Query Basis boundary (QB-P, QB-Q, QB-R, QB-I, QB-F, QB-S, QB-X), as reviewed from the KD-034 proposal and owner-approved after Rico review.
4. **Action:** ADOPT
5. **Rationale:** Sneak requires an explicit architectural basis for obtaining the future designated identity-link holder's authoritative link-status determination. The adopted boundary establishes that query interest is decision-derived, limited to per-interaction identity-link determinations for the addressing Discord identity, and distinct from authorization. The future holder-designation decision must explicitly establish that bounded query interest; naming a holder alone does not silently create query access.
6. **Basis / Evidence:** Owner judgment based on KD-032 IL-H/IL-R, KD-033 RL-P/RL-D/RL-H/RL-F/RL-T/RL-S/RL-X, KD-025 H3/R1, KD-023 PA1/B3/B9, KD-024 PA2/PA7, KD-026, KD-027, KD-022, and the reviewed KD-034 proposal. Rico review found no circularity or authority leak in the proposed separation of query basis, resolution, and authorization.
7. **Conditions / Blockers:**
   (a) A legitimate identity-link query requires a future explicit KD designating the actual link-record holder and explicitly establishing Sneak's bounded query interest for per-interaction link-status determinations for the addressing Discord identity.
   (b) A resolvability contract must exist before legitimate query operation.
   (c) No bulk reads, enumeration, access beyond the link-status determination, permission-state access, or authorized action is established.
   (d) The query is routed through PA1 and its result feeds identity resolution/PA6 only; it does not satisfy PA2 authorization elements 1–3.
   (e) The addressing Discord identity is forwarded from interaction context and is not invented, selected, asserted, or independently verified by Sneak; absent an addressing identity, no query is formed.
   (f) Unavailable, inaccessible, refused, ambiguous, or malformed results are treated as undeterminable under KD-033; no escalation, bypass, probing, repair, fallback, cross-domain inference, or stale reuse is authorized.
   (g) Query working state remains ephemeral under KD-022 2a/2e and is not persisted or ledgered.
   (h) Cross-system crossings defer to KD-026; no authorization-owner, grant-holder, or state-owner/executor role is designated by KD-034.
   (i) Actual holder, query/resolution mechanics, validity bounds, lifecycle procedures, platform presentation, Discord assertion strength, retry/timing, failure wording, and other QB-E items remain undefined.
   (j) No implementation, identity-link lifecycle action, permission mapping, portable work-state mechanism, or currently unauthorized identity-bound action is established.
8. **Execution / Resulting State:** Authorized execution: append KD-034 to `CORE/DECISIONS.md` and incorporate the adopted QB boundary into `CORE/KOS-SNEAK-ARCH.md`. Resulting state: KD-034 is the authoritative query-basis boundary for Sneak identity-link resolution. No actual identity-link holder is designated, no query/resolution implementation is authorized, and no permission or identity-bound action is enabled by this decision.


---

## KD-035

1. **Decision ID:** KD-035
2. **Date:** 2026-09-20
3. **Item(s):** Sneak Identity-Link Lifecycle / 3h architectural boundary (LC-D, LC-E, LC-S, LC-R, LC-F, LC-M, LC-U, LC-A, LC-P), as proposed and owner-approved after Rico review.
4. **Action:** ADOPT
5. **Rationale:** The identity-link lifecycle-edge category was the remaining undefined semantic center referenced by KD-032, KD-033, KD-034, and KD-027. The adopted boundary defines lifecycle state and its necessary edges without defining implementation procedures, preserving the distinction between authoritative link status, lifecycle edges, Sneak resolution, and ephemeral usage state.
6. **Basis / Evidence:** Owner judgment based on KD-022 P1/P3/P5/C0, KD-023 B3/B4/B6/B9/B12, KD-024 PA1/PA2/PA5/PA7, KD-025, KD-026, KD-027 T3-P3/T3-P4, KD-028 where applicable, KD-032 IL-L/IL-S/IL-F/IL-R, KD-033 RL-D/RL-H/RL-B/RL-F/RL-S, KD-034 QB-F/QB-S, and the reviewed KD-035 proposal.
7. **Conditions / Blockers:**
   (a) Lifecycle state means the authoritative holder's record of a link's standing through time; lifecycle semantics are established, while lifecycle procedures remain future work.
   (b) The necessary lifecycle edges are creation, change, suspension, removal, and restoration. No expiry edge is established because validity bounds remain undefined.
   (c) Link status is expressed as active, suspended, no-link, or unknown. Removed and never-existed both resolve to no-link at status level and are not distinguished by Sneak absent a future authoritative procedure establishing such history.
   (d) Link status, lifecycle edges, Sneak resolution, and Sneak usage state remain distinct concepts; resolution is not a lifecycle edge and usage state is not the authoritative link.
   (e) Each established lifecycle edge affecting authoritative link status invalidates determinations anchored to the pre-edge status. Effectiveness is established by the holder, not by Sneak's awareness.
   (f) During an interaction, no mandatory re-resolution is created. A known established edge makes the prior ephemeral usage reference unusable for new evaluations; Sneak does not infer edges, speculate about re-resolution, or retroactively alter completed work.
   (g) Unknown, stale, conflicting, or unavailable lifecycle conditions remain within the existing RL-D/RL-F/QB-F fail-closed taxonomy and do not create new failure modes.
   (h) The designated identity-link holder remains unnamed; Sneak never determines, authors, repairs, infers, or adjudicates authoritative lifecycle state.
   (i) Lifecycle state remains authoritative holder-held state under KD-022 P1/1b; Sneak persistence remains constrained by KD-022 C0/P3.
   (j) Dependencies include actual holder designation, lifecycle procedures, validity bounds, an established edge-awareness channel where required, and other previously established prerequisites. No implementation, permission mapping, portable work-state, or identity-bound action is authorized.
8. **Execution / Resulting State:** Authorized execution: append KD-035 to CORE/DECISIONS.md and incorporate the adopted lifecycle boundary into CORE/KOS-SNEAK-ARCH.md. Resulting state: KD-035 is the authoritative lifecycle-semantic boundary for identity links. The actual holder, lifecycle procedures, implementation, edge-awareness mechanism, validity bounds, and dependent identity-bound operation remain unestablished unless separately decided.


---

## KD-036

1. **Decision ID:** KD-036
2. **Date:** 2026-09-20
3. **Item(s):** Documentation alignment of `CORE/KOS-SNEAK-ARCH.md) following adopted KD-032 through KD-035, limited to clerical correction of stale classification references, section numbering, historical decision-range references, and terminology that no longer matches adopted architecture.
4. **Action:** ADOPT
5. **Rationale:** The owner adopts the proposed documentation-alignment scope so the architecture document accurately reflects already-adopted decisions KD-032 through KD-035. The alignment corrects stale 3h UNDEFINED statements, preserves the distinction between lifecycle semantics and lifecycle procedures, resolves duplicate and stale section numbering, and updates historical references without changing substantive architectural meaning.
6. **Basis / Evidence:** Owner judgment following Rico review of the KD-032–KD-035 checkpoint audit and the KD-036 documentation-alignment proposal. The proposed corrections are directly grounded in adopted KD-032, KD-033, KD-034, and KD-035, including KD-035 §20.9 and the adopted lifecycle semantics/procedure distinction. The audit found no substantive contradictions and identified the stale documentation as the remaining actionable issue.
7. **Conditions / Blockers:**
   (a) Alignment is strictly clerical and must be traceable to already-adopted KD-032 through KD-035.
   (b) §6.4 must no longer describe 3h as UNDEFINED; KD-035 established lifecycle state as authoritative 1b while leaving lifecycle procedures future work.
   (c) §17.3 must remove the stale "UNDEFINED under KD-022 3h" qualifier, distinguish established lifecycle semantics from undefined procedures, and include restoration in the adopted lifecycle-edge enumeration.
   (d) §17.4 must identify lifecycle edges as authoritative holder-held state under KD-022 1b as established by KD-035, while retaining the separate statement that no lifecycle mechanism was established by KD-032.
   (e) KD-034 retains section 19; the former duplicate section 19 must be renumbered as part of the documentation cascade.
   (f) KD-035 retains section 20; the former duplicate section 20 and stale 18.x subsection numbering must be corrected by cascading the affected later sections while preserving adopted boundary-section identities.
   (g) Stale "through KD-031" references in §11 and the later change-control material must be updated through KD-035 where applicable, and the corresponding "boundaries adopted; establishments pending" language must remain limited to the scopes and pending items actually established by KD-032 through KD-035.
   (h) "Lifecycle rules" must be corrected to "lifecycle procedures" where the text refers to the still-unestablished procedural layer.
   (i) The non-supersession/historical list in the change-control material must extend through KD-035.
   (j) No substantive architecture may be added, removed, broadened, narrowed, reinterpreted, or silently changed through this clerical alignment.
   (k) This decision does not designate the identity-link holder, establish lifecycle procedures, establish an edge-awareness channel, establish permissions or authorization, establish implementation, create schemas/APIs/storage, change state classification, or make any previously undefined matter actionable except to correct stale wording directly contradicted by an already-adopted decision.
   (l) Decision history remains append-only; no decision record is edited in place. Repository architecture text may be corrected only through separately authorized execution of this decision.
8. **Execution / Resulting State:** This decision authorizes the specified documentation-alignment scope, but repository execution is a separate step. Until separately executed, `CORE/KOS-SNEAK-ARCH.md` remains unchanged. No holder designation, lifecycle procedure, awareness mechanism, permission mapping, implementation, or other substantive establishment is authorized by KD-036.


---

## KD-037

1. **Decision ID:** KD-037
2. **Date:** 2026-09-20
3. **Item(s):** Recognition of the **Kustomz Identity Engine** as the authoritative Kustomz identity system of record for the Kustomz identity state classified as KD-022 1a, and the resulting architectural anchor for the Kustomz side of KD-022 1b identity-link records.
4. **Action:** ADOPT
5. **Rationale:** The adopted Sneak architecture requires Kustomz identity to be authoritative state, but the repository did not previously identify any system of record holding that identity. The owner therefore recognizes the Kustomz Identity Engine as the authoritative Kustomz identity system of record so that the existing 1a classification has a concrete authoritative holder and the Kustomz side of future 1b identity links has an architectural referent. This recognition is intentionally separate from designation of the Kustomz Identity Engine as the 1b Discord-link holder.
6. **Basis / Evidence:** Owner judgment based on the Identity Engine inventory and the adopted architecture in KD-021, KD-022, KD-032, KD-033, KD-034, and KD-035. The inventory established that the repository previously named no identity system of record and that the term "Identity Engine" was not established in the repository. The owner supplied the concrete system name **Kustomz Identity Engine** for this decision. KD-001 requires the decision to be explicit and distinguishes the decision/ruling from its later execution.
7. **Conditions / Blockers:**
   (a) KOSD recognizes the **Kustomz Identity Engine** as the authoritative Kustomz identity system of record and authoritative holder of the KD-022 1a Kustomz identity records.
   (b) The Kustomz side of KD-022 1b identity-link records anchors to Kustomz identities held by the Kustomz Identity Engine.
   (c) Sneak remains a consumer of authoritative Kustomz identity state and does not become its holder or author.
   (d) Recognition of the Kustomz Identity Engine as the 1a identity system of record does **not** designate it as the 1b Kustomz↔Discord identity-link holder. That holder requires a separate explicit owner decision under KD-032 IL-H, with the explicit query-interest establishment required by KD-034.
   (e) This decision does not define the Kustomz Identity Engine itself. Schemas, identifiers, account model, identity lifecycle, APIs, storage, implementation, permissions, resolution mechanics, validity bounds, lifecycle procedures, edge-awareness mechanisms, and other internal or operational details remain undefined unless separately decided.
   (f) No state classification is changed or newly created by this decision. KD-022 1a remains AUTHORITATIVE and KD-022 1b remains AUTHORITATIVE; this decision identifies the authoritative holder of 1a and the architectural anchor for the Kustomz side of 1b.
   (g) The future 1b holder designation, resolvability contract, lifecycle procedures, validity bounds, edge-awareness mechanism, platform addressing identity, and conditional KD-026 roles remain unresolved.
8. **Execution / Resulting State:** Authorized execution is limited to recording KD-037 in CORE/DECISIONS.md and, separately, incorporating the adopted recognition into the applicable KOSD architecture documentation. No 1b holder designation, Identity Engine implementation, identity-link mechanics, permission mapping, or currently unauthorized identity-bound action is authorized by KD-037.


---

## KD-038

1. **Decision ID:** KD-038
2. **Date:** 2026-09-20
3. **Item(s):** Kustomz Identity Engine designation as the authoritative holder of KD-022 1b Kustomz↔Discord identity-link records, separately from its KD-037 1a identity-system-of-record role, together with the bounded query interest required by KD-034.
4. **Action:** ADOPT
5. **Rationale:** KD-032 through KD-035 established that the 1b identity-link holder must be explicitly designated before reliable resolution and legitimate query operation can exist. KD-037 established the Kustomz Identity Engine as the authoritative Kustomz identity system of record and the anchor for the Kustomz side of 1b. The owner has selected the Kustomz Identity Engine to hold the 1b link records as a separate explicit designation, avoiding creation of an additional unrecognized registry while preserving the distinction between the 1a and 1b roles.
6. **Basis / Evidence:** Owner judgment based on KD-032 IL-D/IL-H/IL-A, KD-033 RL-P/RL-D/RL-H, KD-034 QB-P/QB-Q/QB-R/QB-I/QB-S, KD-035 LC-D/LC-E/LC-S/LC-F/LC-P, KD-037, and the owner's explicit selection of the Kustomz Identity Engine as the 1b holder. The designation is made separately from the 1a recognition and does not imply that either role automatically establishes the other.
7. **Conditions / Blockers:**
   (a) KOSD designates the **Kustomz Identity Engine** as the authoritative holder of KD-022 1b Kustomz↔Discord identity-link records, separately and explicitly from its KD-037 1a role.
   (b) The Kustomz Identity Engine is authoritative for the existence and status of 1b identity links and for lifecycle edges affecting that authoritative link status, consistent with KD-035. Established lifecycle edges affecting authoritative link status invalidate determinations anchored to the pre-edge status under KD-027.
   (c) Sneak is granted bounded, per-interaction query interest solely to obtain the authoritative 1b link-status determination for the **addressing Discord identity**, for identity-bound evaluation under the adopted Sneak architecture. This query interest is decision-derived under KD-034 and does not constitute permission, authorization, bulk access, enumeration, or access to unrelated Identity Engine state.
   (d) The query uses the addressing Discord identity supplied by the interaction context as its lookup parameter. Sneak does not invent, select, assert, or independently verify that addressing identity.
   (e) Query results and handling remain transient/ephemeral under KD-022 2a/2e and are not persisted as a Sneak-side link record, ledger, or cross-interaction identity state.
   (f) Designation of the 1b holder does not establish the resolvability contract, lifecycle procedures, validity bounds, edge-awareness mechanism, or addressing-identity resolution mechanics; those remain future work.
   (g) Designation does not authorize any permission or action. Authorization remains subject to PA0–PA9 and the applicable holder/system determinations under KD-024/KD-025, including the full PA2 gate where applicable.
   (h) The 1a and 1b roles are distinct. The 1a recognition does not imply 1b authority, and the 1b designation does not redefine the Kustomz Identity Engine or its 1a role.
   (i) No Identity Engine schemas, identifiers, account model, lifecycle implementation, APIs, storage, implementation model, permission model, verification mechanics, resolution mechanics, validity bounds, awareness mechanism, or other internal details are established by this decision.
   (j) No portable work-state mechanism, cross-system authorization role, identity-link creation/removal procedure, or currently unauthorized identity-bound action is established by implication.
8. **Execution / Resulting State:** Authorized execution is to append KD-038 to `CORE/DECISIONS.md` and record the corresponding adopted 1b holder/query boundary in `CORE/KOS-SNEAK-ARCH.md` as a separate execution step. Resulting state: the Kustomz Identity Engine is the explicitly designated authoritative 1b holder, and Sneak has only the bounded query interest established above. Resolvability mechanics, procedures, validity bounds, awareness, implementation, permissions, and dependent actions remain unestablished until separately decided.

## KD-039 — Kustomz Toolbox Architectural Recognition

**Decision ID:** KD-039

**Date:** 2026-09-20

**Item(s):** Kustomz Toolbox architectural recognition — identity, purpose, interface relationships, shared-engine principle, and authority/state boundary principles for the shared CSR2 editing/tooling environment, as a named KOSD architectural concept.

**Action:** ADOPT

**Rationale:** The Kustomz Toolbox is an established project-level concept but does not yet have a KOSD architectural definition. This decision establishes the smallest coherent architectural recognition needed to govern future Toolbox work without treating the Toolbox as a KOSD module or authorizing implementation.

The recognition establishes:
- the Toolbox's identity and purpose;
- Web, Android, and Discord/Sneak as its three interfaces;
- the one shared engine / three interfaces principle;
- authority and state-boundary principles;
- applicable Sneak architecture by reference;
- explicit blockers and exclusions.

It does not define implementation internals, authority holders, permissions, contracts, or storage, and does not authorize implementation.

**Basis / Evidence:**
- Owner-established project-level Toolbox concept and functional description.
- Existing KOSD three-interface and continuity architecture.
- Existing Sneak architecture, KD-021 through KD-038.
- KD-022 state-classification framework.
- KD-023 through KD-029 authority, permission, cross-system, freshness, attribution, and standing boundaries.
- KD-019 required-module-set authority.
- KD-003 KOS-RELEASE Draft status.
- KD-037 precedent for recognizing a named system without defining its internals.
- CORE/KOS-SNEAK-ARCH.md §24 implementation boundary.

**Conditions / Blockers:**
- (a) The Toolbox is recognized as a named architectural concept only. It is not classified as a KOSD module, subsystem, or required-module-set member.
- (b) The one shared engine / three interfaces principle is adopted as an architectural principle, while engine internals, contracts, schemas, APIs, storage, and mechanics remain undefined.
- (c) The three interfaces are: Web — primary; Android — planned; Discord/Sneak — conversational.
- (d) Sneak remains subject to all applicable KD-021 through KD-038 boundaries. Its identification as a Toolbox interface does not grant Sneak additional authority.
- (e) NSB/SCB/page-level functional definitions remain project-level material and are not adopted as KOSD architecture.
- (f) No authoritative holders are designated for Toolbox-modified state.
- (g) No permissions, grants, authorizations, or mappings are established.
- (h) The portable work-state mechanism and holder remain undefined. The existing WEB → ANDROID → DISCORD/SNEAK continuity principle is therefore not being newly implemented or resolved by this decision.
- (i) Implementation is not authorized. Implementation location and model remain open.
- (j) This decision does not supersede or independently redefine KD-001 through KD-038.
- (k) The future architecture artifact is CORE/KOS-TOOLBOX-ARCH.md.
- (l) The recognition decision shall be included in that architecture's authority header.
- (m) No subsequent architectural subject is established by this decision; sequencing remains open.

**Execution / Resulting State:** Upon separately authorized execution:
- Append KD-039 to CORE/DECISIONS.md.
- Separately create CORE/KOS-TOOLBOX-ARCH.md containing the adopted recognition and boundaries.
- Do not modify CORE/KOS-SNEAK-ARCH.md.
- Do not authorize or place Toolbox implementation.
- Do not establish holders, permissions, contracts, schemas, APIs, storage, or module classification.

Resulting state: Kustomz Toolbox is recognized within KOSD as a governed architectural concept with explicit boundaries and explicit unresolved dependencies.



## KD-040 — Portable Work-State Architecture Recognition

**Decision ID:** KD-040

**Date:** 2026-09-20

**Item(s):** Portable Work-State Architecture for the Kustomz Toolbox, as proposed by Izzy and reviewed by Rico in Revision 2.

**Action:** ADOPT

**Rationale:** The owner adopts the bounded architectural definition of portable work-state required to give the KD-039 Web → Android → Discord/Sneak continuity target a governed architectural basis without selecting an implementation, holder, permission model, or module classification. The adopted boundary preserves portable work-state as the existing KD-022 1i AUTHORITATIVE classification, defines what work-state is and is not, establishes holder qualification criteria without designating a holder, defines Kustomz-identity addressing and holder-mediated continuity, and establishes bounded lifecycle, invalidation, staleness, conflict, failure, and cross-system relationships. The adoption deliberately leaves the unresolved holder, write authorization, conflict policy, mechanics, contracts, implementation model, and other explicitly undefined matters for future decisions.

**Basis / Evidence:**
- KD-039 Kustomz Toolbox Architectural Recognition.
- KD-022 1i portable work-state classification and applicable state/authority boundaries.
- KD-021 through KD-038 Sneak, identity, authority, permission, cross-system, freshness, and lifecycle boundaries where referenced by the proposal.
- KD-037 Kustomz Identity Engine recognition as the authoritative 1a identity system of record.
- KD-038 Kustomz Identity Engine designation as authoritative 1b identity-link holder and bounded Sneak query interest.
- Izzy's Portable Work-State Architecture Revision 2, reviewed and accepted by Rico for owner decision.

**Conditions / Blockers:**
- (a) Portable work-state remains AUTHORITATIVE under KD-022 1i; this decision does not create or reclassify a state category.
- (b) Portable work-state is the authoritative, Kustomz-identity-bound record of a user's in-progress Toolbox work and the ecosystem context required to resume that work across Web, Android, and Discord/Sneak interfaces.
- (c) Work-state does not contain or replace authoritative CSR2 source data, identity records, identity-link records, derived intelligence, dispositioned history, or interaction-scoped ephemeral state.
- (d) A future holder must satisfy the adopted holder criteria: explicit KOSD designation, not Sneak, interface-independence, and Kustomz-identity scoping.
- (e) No holder is designated by KD-040. The Toolbox shared engine, Kustomz Identity Engine, Sneak, and any other system remain undesignated as work-state holder.
- (f) Work-state is addressed by Kustomz identity. Discord-originated access first resolves the addressing Discord identity through the existing KD-032 through KD-038 identity-link architecture; the Discord identity does not directly address work-state.
- (g) Kustomz Identity Engine remains limited to its established 1a and 1b authority. KD-040 grants it no work-state authority, read/write role, or lifecycle role.
- (h) Work-state lifecycle semantics are recognized as creation, update, consumption, and termination. Lifecycle procedures, timers, retention, clearing, archiving, and other mechanics remain undefined.
- (i) Cross-interface continuity is holder-mediated. Interfaces do not transfer authoritative work-state directly to one another, and no interface-specific store may become a competing authoritative record.
- (j) Work-state invalidation/staleness boundaries include supersession, holder-established invalidation, any future validity-bound expiration, holder change, and applicable future KOSD decisions. An identity-link change by itself does not invalidate Kustomz-identity-addressed work-state; it may instead affect Discord-originated resolution or access.
- (k) Concurrent updates are a conflict condition. Conflict-resolution policy remains undefined.
- (l) If the holder is unreachable or current state cannot be determined, work-state is undeterminable and must not be presented as current. An absent or invalid record does not authorize repair or other unestablished action.
- (m) The shared Toolbox engine's internal role and responsibilities remain undefined. Interaction with work-state does not constitute holding it absent explicit KOSD designation.
- (n) Sneak never holds portable work-state. Sneak may consume work-state context ephemerally within an interaction. Whether Sneak-originated work may update the holder remains a future cross-system action/permission question.
- (o) Portable work-state may reference authoritative CSR2 source records but never redefines or becomes the authority for those source records.
- (p) Holder designation, holder mechanics, schemas, APIs, wire formats, authentication implementation, conflict resolution, validity bounds, retention/disposition, write-path authorization, cross-system contracts/conformance, implementation location/model, NSB/SCB/page-level functional content, and any formal Toolbox classification beyond KD-039 remain undefined unless separately decided.
- (q) KD-021 §22.2 portable work-state tension is narrowed but not closed because holder designation and mechanics remain unresolved.
- (r) Permission grant-holder designations, KOS-RELEASE promotion for any future module/release treatment, Sneak resolvability contract, and authoritative holders for Toolbox-modified CSR2 state remain blockers.
- (s) No implementation is authorized by KD-040. Execution of the architecture artifact is a separate step and requires the owner's explicit authorization.
- (t) KD-001 through KD-039 remain in force and are not superseded or reinterpreted by KD-040.

**Execution / Resulting State:** Authorized execution is limited to recording KD-040 in CORE/DECISIONS.md. Creation or modification of any Toolbox architecture artifact is a separate execution step requiring explicit owner authorization. Resulting state after this decision record is appended: the portable work-state architectural boundary is adopted as KOSD architecture, while holder designation, mechanics, permissions, implementation, and the other explicitly unresolved matters remain unestablished.


## KD-041 — Identity-Link Resolvability Contract

**Decision ID:** KD-041

**Date:** 2026-09-20

**Item(s):** Identity-Link Resolvability Contract, as proposed by Izzy and reviewed by Rico, with Rico's targeted Revision 1 applied to §12.

**Action:** ADOPT

**Rationale:** The owner adopts the architectural contract connecting Sneak's already-established bounded identity-link query interest under KD-038 to the Kustomz Identity Engine's established authoritative 1b identity-link determination. The contract establishes the semantic meaning of the request, the authoritative response, authoritativeness conditions, temporal use and lifecycle invalidation semantics, and failure handling without selecting transport, APIs, schemas, retry/timing behavior, validity bounds, lifecycle procedures, KD-026 roles, permission mappings, or implementation. The adoption satisfies the explicitly named resolvability prerequisite in KD-033/RL-X and KD-034/QB-Q while preserving all separately unresolved operational dependencies.

**Basis / Evidence:**
- KD-032 — Kustomz-to-Discord identity-link architecture.
- KD-033 — identity-link resolution/resolvability boundary, including RL-P, RL-D, RL-H, RL-F, RL-S, RL-T, RL-X and D-RL prerequisites.
- KD-034 — identity-link access/query basis, including QB-P, QB-Q, QB-R, QB-I, QB-F, QB-S, QB-X and D-QB prerequisites.
- KD-035 — identity-link lifecycle boundary, including LC-S, LC-R, LC-F, LC-M, and LC-U.
- KD-037 — Kustomz Identity Engine as authoritative 1a identity system of record.
- KD-038 — Kustomz Identity Engine as authoritative 1b identity-link holder and explicit bounded Sneak query interest.
- KD-040 — Toolbox blocker identifying the resolvability contract for operational identity-bound access through Sneak.
- Izzy's Identity-Link Resolvability Contract proposal, reviewed by Rico and revised in response to Rico's §12 wording finding.

**Conditions / Blockers:**
- (a) Contract parties are Sneak as querier under KD-038's bounded, per-interaction query interest and the Kustomz Identity Engine as authoritative 1b identity-link holder.
- (b) A request is per interaction, uses the addressing Discord identity as its lookup parameter, is limited to the single holder-status determination question, and is routed through PA1.
- (c) If no addressing Discord identity is available, no query is formed and resolution remains undeterminable under the applicable RL-D/QB-I boundary.
- (d) The authoritative response uses the LC-S vocabulary: active, suspended, no-link, or unknown. When active, the determination resolves to one Kustomz identity. Sneak accepts the holder's determination and does not corroborate, override, or adjudicate it.
- (e) Authoritativeness requires the determination to be holder-sourced, unambiguous as to one Kustomz identity, and within established validity. Because validity bounds remain undefined, authoritative standing is limited to the originating interaction's established ephemeral 2e usage scope.
- (f) Determinations are per-interaction and are not reused across interactions as authoritative. Established lifecycle edges invalidate pre-edge determinations under the existing LC-F/T3-P3 boundary; no validity extension is established.
- (g) Holder unavailability, ambiguous determination, malformed/unusable result, unknown status, or absent addressing identity follows the established RL-D/RL-F/QB-F/QB-I failure taxonomy and fails closed for identity-bound use. No fallback, probing, cross-domain inference, stale reuse, repair, or substitute source is authorized.
- (h) The contract is a read determination only. It is not authorization, a permission grant, a transport/API, lifecycle procedures, validity bounds, KD-026 cross-system role establishment, or a new authority designation.
- (i) The contract does not establish transport, endpoints, APIs, schemas, wire formats, serialization, retry/timing/timeout behavior, failure-presentation wording, platform identity mechanics, Discord verification/ceremony, lifecycle procedures, validity durations/scopes, or implementation.
- (j) The contract satisfies D-RL3 and D-QB2. The named QB-Q prerequisite set is complete at the architectural level; legitimate query operation remains subject to the separately identified unresolved dependencies and mechanics, including D-RL2, D-RL4/D-QB3, D-RL5/D-QB4, D-RL6/D-QB5, and D-QB6.
- (k) This decision does not establish permission grants, KD-026 roles, validity bounds, lifecycle procedures, platform-supplied identity mechanics, or any identity-bound action.
- (l) RL-X's statement that the access/query basis was not established by KD-033 remains historically true. This decision is a separate establishment and does not retroactively modify KD-033.
- (m) QB-Q's prerequisite list is completed; the list itself is not rewritten.
- (n) KD-032 through KD-040 remain in force and are not superseded, modified, or reinterpreted by KD-041.
- (o) No implementation is authorized by KD-041. Execution of the Sneak architecture artifact is a separate step requiring explicit owner authorization.

**Execution / Resulting State:** Authorized execution is limited initially to recording KD-041 in CORE/DECISIONS.md. Updating CORE/KOS-SNEAK-ARCH.md to incorporate the adopted contract is a separate execution step requiring explicit owner authorization. Resulting state after the decision record is appended: the Identity-Link Resolvability Contract is adopted as KOSD architecture, satisfying D-RL3 and D-QB2 while the separately identified operational dependencies and mechanics remain unresolved.


## KD-042 — Portable Work-State Holder Designation

**Decision ID:** KD-042

**Date:** 2026-09-20

**Item(s):** Portable Work-State Holder Designation, as proposed by Izzy and reviewed by Rico, naming the **Kustomz Toolbox** in its interface-independent capacity as the authoritative holder of KD-022 1i portable work-state.

**Action:** ADOPT

**Rationale:** The owner designates the Kustomz Toolbox as the authoritative portable work-state holder required by KD-040 §7.2. The designation attaches to the Toolbox's interface-independent shared-engine capacity established by KD-039, not to Web, Android, or Discord/Sneak as interfaces. This satisfies the explicit holder requirement without granting any interface holder status or expanding Sneak authority.

**Basis / Evidence:**
- KD-039 — Kustomz Toolbox architectural recognition, including the one shared engine / three interfaces principle.
- KD-040 — portable work-state definition, holder criteria H-WS1–H-WS4, identity scoping, lifecycle boundary, invalidation boundary, and holder requirements.
- KD-022 1i — portable work-state classification as AUTHORITATIVE.
- KD-038 — precedent for explicit system designation while preserving separate roles and interface boundaries.
- Izzy's Portable Work-State Holder Designation proposal, reviewed by Rico and approved by Kustomz/Rick on 2026-09-20.

**Conditions / Blockers:**
- (a) **H-WS1 — KOSD designation:** The portable work-state holder is established by this explicit KOSD owner decision. No holder status existed under KD-040 before this decision.
- (b) **H-WS2 — Never Sneak:** The designated holder is the Kustomz Toolbox in its interface-independent capacity. Web, Android, and Discord/Sneak are explicitly excluded as holder interfaces; Sneak does not hold portable work-state.
- (c) **H-WS3 — Interface-independence:** The designation attaches to the shared-engine aspect of the Kustomz Toolbox established by KD-039's one-engine / three-interface model, not to any individual interface or interface-specific store.
- (d) **H-WS4 — Identity-scoping:** Held portable work-state is partitioned and addressed by Kustomz identity, consistent with KD-040 §7.3 and the established identity architecture.
- (e) The Kustomz Toolbox holds the single authoritative portable work-state record per Kustomz identity and applicable work-state scope. No competing authoritative interface-specific record is established.
- (f) The holder has authority over the recognized work-state lifecycle edges — creation, update, consumption, and termination — while lifecycle procedures and mechanics remain undefined.
- (g) The holder has authority over holder-established invalidation within the existing KD-040 §7.5 boundary. No new invalidation category or validity-bound value is established.
- (h) Designation does not authorize any write path. Holding is not a grant to create, update, or terminate held records. Write-path authorization remains subject to future permission-grant-holder and applicable cross-system decisions.
- (i) Designation does not establish conflict-resolution policy, validity bounds, retention/disposition, lifecycle procedures, schemas, storage, APIs, implementation, or internal shared-engine responsibilities.
- (j) Whether Sneak-originated work may reach the holder remains unresolved and is now a concrete future KD-026 cross-system question plus applicable permission-grant question.
- (k) The Kustomz Identity Engine retains its established KD-037 1a and KD-038 1b authority and gains no portable work-state authority, read/write role, or lifecycle role by this decision.
- (l) KD-022 1i remains AUTHORITATIVE. No state category is created or reclassified.
- (m) KD-039 and KD-040 remain in force and are not superseded, modified, or reinterpreted except that KD-040's previously unresolved holder designation is now separately established by this decision.
- (n) No implementation is authorized by KD-042. Architecture-document execution is a separate authorized step under the adopted protocol.

**Execution / Resulting State:** Authorized execution includes recording KD-042 in CORE/DECISIONS.md and, separately, updating CORE/KOS-TOOLBOX-ARCH.md to record the holder designation and resulting boundary. The portable work-state holder blocker identified by KD-040 is satisfied. Operational mechanics, write authorization, conflict resolution, validity bounds, retention/disposition, Sneak-originated update path, implementation, and the other explicitly unresolved dependencies remain unestablished.


## KD-043 — Kustomz Workspace Architectural Recognition

**Decision ID:** KD-043

**Date:** 2026-09-20

**Item(s):** Kustomz Workspace architectural recognition as the authoritative Kustomz system of record for Ticket Engine records (KD-022 1d) and their associated permission-grant state, as proposed by Izzy and reviewed by Rico.

**Action:** ADOPT

**Rationale:** The owner recognizes Kustomz Workspace as the authoritative Kustomz system of record for the already-classified Ticket Engine record domain and its associated permission-grant state. This establishes the required system boundary before any later permission-grant-holder designation. Recognition does not itself designate Kustomz Workspace as the KD-025 permission-grant holder, define the Ticket Engine, establish grant mechanics, authorize any action, or expand Sneak authority.

**Basis / Evidence:**
- KD-022 1d — Ticket Engine records are classified as AUTHORITATIVE, while their authoritative holder was previously undefined.
- KD-024 — Sneak permission and authority boundary, including PA3 and the requirement to resolve applicable permission grants against an authoritative holder.
- KD-025 — permission-grant-holder framework, including H1/H2 and the requirement for an explicit holder designation before a grant domain becomes operationally resolvable.
- KD-021 — Ticket Engine interaction is within Sneak's adopted capability scope.
- Izzy's Kustomz Workspace recognition proposal, reviewed by Rico as CLEAN.
- The recognition-first precedent established by KD-037: system recognition is established separately from later holder/contract/mechanics decisions.

**Conditions / Blockers:**
- (a) Kustomz Workspace is recognized as the authoritative Kustomz system of record for KD-022 1d Ticket Engine records.
- (b) Kustomz Workspace is also recognized as the authoritative Kustomz system of record for the associated Ticket Engine permission-grant state.
- (c) This recognition does not by itself constitute the KD-025 D1 designation of Kustomz Workspace as the permission-grant holder for Ticket Engine actions. That designation remains a separate future decision.
- (d) The Ticket Engine itself remains undefined as to contents, records, schemas, mechanics, lifecycle procedures, APIs, storage, implementation, and other internal details unless separately established.
- (e) Permission-grant semantics, mappings, authorization rules, action domains, resolution mechanics, validity/freshness behavior, and cross-system roles remain undefined unless separately established.
- (f) Sneak's existing PA5/PA7 fail-closed posture remains unchanged until a later holder designation and applicable authorization decisions establish an operational permission path.
- (g) No action is authorized by this recognition. Recognition of a system of record does not itself grant Sneak, Kustomz Workspace, or any interface permission to perform actions.
- (h) KD-037/KD-038 Identity Engine authority and KD-042 Kustomz Toolbox portable work-state holder authority are unaffected.
- (i) No implementation is authorized by KD-043. Architecture-document execution is a separate execution step under the adopted protocol.

**Execution / Resulting State:** Authorized execution includes recording KD-043 in CORE/DECISIONS.md and, separately, updating CORE/KOS-SNEAK-ARCH.md to reflect Kustomz Workspace's recognized Ticket Engine system-of-record boundary. The recognition blocker for identifying the authoritative Ticket Engine system boundary is satisfied. The separate permission-grant-holder designation, Ticket Engine definition, permission mechanics, cross-system authorization, and implementation remain unresolved.


## KD-044 — Ticket Engine Permission-Grant Holder Designation

**Decision ID:** KD-044

**Date:** 2026-09-20

**Item(s):** Explicit KD-025 D1 permission-grant-holder designation for the Ticket Engine action domain, naming **Kustomz Workspace** as the designated permission-grant holder.

**Action:** ADOPT

**Rationale:** KD-043 established Kustomz Workspace as the authoritative Kustomz system of record for KD-022 1d Ticket Engine records and their associated permission-grant state. The owner now separately establishes the KD-025 D1 holder designation for the Ticket Engine action domain. H1 and H2 are satisfied by KD-043's recognition and record-holding boundary. H3 is satisfied under the text-faithful architectural reading of KD-025: PA3 establishes that Sneak resolves permission questions against the applicable holder at evaluation time, while PA5/B8 establish the architectural obtaining/deference pattern; the concrete resolution mechanism remains future contract architecture. H4 is satisfied because no circular grant authority is established.

**Basis / Evidence:**
- KD-025 — holder qualification, explicit per-action-domain designation, grant-resolution, and fail-closed boundaries.
- KD-043 — Kustomz Workspace recognition as authoritative system of record for Ticket Engine records and associated permission-grant state.
- PA3 — permission questions are resolved against the applicable holder at evaluation time.
- PA5 and B8 — Sneak defers to and interfaces with the applicable authoritative system rather than assuming its role.
- Izzy's Ticket Engine permission-grant-holder designation proposal, reviewed by Rico and approved by Kustomz/Rick on 2026-09-20.
- Rico's review: CLEAN, with the text-faithful H3 interpretation explicitly adopted for this designation.

**Conditions / Blockers:**
- (a) **H1 — Recognition:** Kustomz Workspace is recognized by KD-043 as authoritative for the Ticket Engine grant domain.
- (b) **H2 — Record-Holding:** Kustomz Workspace is the authoritative system of record for the associated Ticket Engine permission-grant state; it is not merely a downstream consumer, cache, or reporter.
- (c) **H3 — Resolvability:** At the architectural level, Sneak's permission-resolution pattern is established through PA3 and its deferral/interface boundary through PA5/B8. The concrete resolvability mechanism remains a future contract concern and is not defined by KD-044.
- (d) **H4 — No Circularity:** No circular grant-authority dependency is established.
- (e) **D1 — Explicit KD:** Kustomz Workspace is hereby designated as the authoritative permission-grant holder for the Ticket Engine action domain.
- (f) **D2 — Per Action-Domain:** This designation applies only to the Ticket Engine action domain and does not designate Kustomz Workspace as the holder for all permissions or any other domain.
- (g) **D3 — Designation Does Not Authorize:** The designation does not authorize any action and does not complete the PA2 gate. Capability, action authority, linked-identity binding, and the applicable permission determination must still be affirmatively established.
- (h) **PA5 / U1-U2 consequence:** For the Ticket Engine domain, PA5 now has a designated holder target. If the designated holder's determination is unavailable, inaccessible, ambiguous, partial, or otherwise unresolvable, U2/B9/PA7 applies and the action fails closed.
- (i) **PA7 unchanged:** Deny-by-default remains fully in force.
- (j) Sneak does not hold permission grants, maintain a permission ledger, or make authorization determinations.
- (k) The Ticket Engine definition, permission contents, permission schemas/mappings, APIs/transport, implementation, cross-system role assignments, validity/freshness mechanics, and Sneak execution authority remain undefined or unauthorized unless separately established.
- (l) Remaining architectural work includes the concrete permission-resolution mechanism, permission contents/mappings, per-action authorization-owner/state-owner or executor designations where applicable, and KD-026 cross-system roles.
- (m) KD-043 remains in force. This decision adds the separate KD-025 D1 designation and does not reinterpret or replace the system-of-record recognition.
- (n) No implementation is authorized by KD-044. Updating the Sneak architecture artifact is a separate execution step authorized by this decision.

**Execution / Resulting State:** Authorized execution includes recording KD-044 in CORE/DECISIONS.md and, separately, updating CORE/KOS-SNEAK-ARCH.md to record Kustomz Workspace as the designated KD-025 permission-grant holder for the Ticket Engine action domain and the resulting PA5/PA7 boundary. The designation blocker is satisfied for that domain. Concrete resolution mechanics, permission contents/mappings, action authority, cross-system roles, validity/freshness mechanics, implementation, and other explicitly unresolved dependencies remain unestablished.


## KD-045 — Ticket Engine Permission-Resolution Contract

**Decision ID:** KD-045

**Date:** 2026-09-21

**Item(s):** Ticket Engine Permission-Resolution Contract (PR-1–PR-6), establishing the concrete architectural query/response relationship by which Sneak obtains Kustomz Workspace's authoritative permission-grant determination for the Ticket Engine action domain.

**Action:** ADOPT

**Rationale:** KD-044 designated Kustomz Workspace as the KD-025 D1 permission-grant holder for the Ticket Engine action domain while leaving the concrete H3 resolvability mechanism to future contract architecture. The owner adopts the stricter reading of H3 and establishes a domain-specific resolution contract comparable in function to KD-041: resolution is defined, usability criteria are established, Sneak's bounded query interest is explicitly established, the holder determination is treated as input to PA2 rather than authorization itself, handling remains transient, and the concrete mechanism remains future. This closes H3 for the Ticket Engine action domain without defining the Ticket Engine or selecting implementation.

**Basis / Evidence:**
- KD-043 — Kustomz Workspace recognition as authoritative system of record for Ticket Engine records and associated permission-grant state.
- KD-044 — explicit KD-025 D1 designation of Kustomz Workspace as permission-grant holder for the Ticket Engine action domain.
- KD-025 H3 — requirement that KOSD architecture establish how Sneak obtains the holder's determinations.
- KD-034 — precedent that naming a holder does not silently establish query interest and that query interest must be explicitly bounded.
- KD-041 — domain-specific identity-link resolvability contract precedent.
- Izzy's Ticket Engine Permission-Resolution Contract proposal, reviewed by Rico and approved by Kustomz/Rick on 2026-09-21.

**Conditions / Blockers:**
- **PR-1 — Resolution defined:** For the Ticket Engine action domain, resolution means Sneak obtaining Kustomz Workspace's authoritative permission-grant determination at evaluation time, per interaction.
- **PR-2 — Usability criteria:** A determination is usable only when it is holder-sourced from Kustomz Workspace as the KD-044-designated holder, unambiguous as to the permission question asked, and obtained at evaluation time for the action under evaluation. A determination that is unavailable, inaccessible, ambiguous, or partial is unresolvable; U2/B9/PA7 applies and the action fails closed.
- **PR-3 — Bounded query interest:** Sneak's query interest for Ticket Engine permission questions is explicitly established following the KD-034 precedent. It derives from PA5's deferral requirement directed at the KD-044-designated holder, is bounded to the Ticket Engine action domain, is evaluation-driven, and is per interaction. The query carries the action under evaluation and the linked identity as lookup parameters. Sneak queries; it does not assert, author, cache, or persist grants.
- **PR-4 — Determination as input, not authorization:** Workspace's determination is authoritative input to PA2's permission-holder element. It does not by itself satisfy PA2, grant action authority, or constitute Sneak making an authorization determination. PA2 remains conjunctive.
- **PR-5 — Transient handling:** Query and determination handling within the interaction is transient and ephemeral under KD-022 2b, subject to B3 and C0. Sneak establishes no permission ledger, grant records, or cache of record.
- **PR-6 — Mechanism future:** The concrete API, transport, schema, storage, platform mechanics, and implementation realizing this query/response relationship remain undefined and require future contract/implementation architecture. This contract establishes that Sneak resolves against Workspace and under what relationship, not how.
- **H-series evaluation:** H1 and H2 remain satisfied by KD-044; H3 is satisfied by PR-1–PR-6; H4 remains satisfied because no circular grant authority is established.
- **PA5/PA7:** PA5 now has a defined resolution relationship for the Ticket Engine domain. PA7 remains deny-by-default. PA2 remains conjunctive; a usable determination satisfies only its permission-holder element. Fail-closed behavior on unresolvable determinations is unchanged.
- **Preserved boundaries:** Ticket Engine contents, schemas, mechanics, lifecycle, and implementation remain undefined; “Discord ticket workflow/system” remains working shorthand, not architecture. The Ticket Engine is not expanded into a cross-platform system. Toolbox portable work-state architecture (KD-040/KD-042) is untouched. Permission contents and mappings, per-action authority/state ownership/execution, KD-026 cross-system roles, validity/freshness mechanics, revocation-awareness channels, APIs/transport/schemas/storage/platform mechanics, and implementation remain undefined unless separately established.
- No implementation or currently unauthorized action is authorized by KD-045.

**Execution / Resulting State:** KD-045 is adopted as the authoritative Ticket Engine permission-resolution contract for the Sneak/Workspace relationship. Authorized execution includes appending KD-045 to CORE/DECISIONS.md and incorporating PR-1–PR-6 into CORE/KOS-SNEAK-ARCH.md. The KD-025 H3 blocker is satisfied for the Ticket Engine action domain. The concrete implementation mechanism and the separately identified permission contents/mappings, per-action authority/state-owner or executor designations, and KD-026 cross-system roles remain unestablished.

## KD-046 — Identity-Link Lifecycle Edge-Awareness Contract

**Decision ID:** KD-046

**Date:** 2026-09-21

**Item(s):** Identity-Link Lifecycle Edge-Awareness Contract (EA-1–EA-7), establishing the architectural relationship by which Sneak may know that a holder-established identity-link lifecycle edge has occurred and apply the already-adopted invalidation semantics.

**Action:** ADOPT

**Rationale:** KD-035 establishes that holder-established lifecycle edges invalidate pre-edge determinations, effective when the holder establishes the edge, while LC-M requires an applicable established mechanism for Sneak to know an edge occurred. KD-038 establishes the Kustomz Identity Engine as the identity-link holder, and KD-041 establishes the per-interaction holder-resolution relationship. This decision composes those existing establishments into a bounded edge-awareness relationship, making the existing invalidation semantic operative for Sneak without defining holder-side lifecycle procedures, validity values, implementation, or new authority.

**Basis / Evidence:**
- KD-035 — identity-link lifecycle semantics, including LC-F/T3-P3 invalidation and LC-M known-edge handling.
- KD-038 — Kustomz Identity Engine designation as authoritative identity-link holder and bounded Sneak query interest.
- KD-041 — identity-link resolvability contract and per-interaction holder determination relationship.
- KD-027 — freshness/invalidation boundary for identity-bound determinations.
- Izzy's Identity-Link Lifecycle Edge-Awareness Contract proposal, reviewed by Rico and approved by Kustomz/Rick on 2026-09-21.

**Conditions / Blockers:**
- **EA-1 — Parties and purpose:** Authority is the Kustomz Identity Engine, holder of KD-022 1b identity-link records and authoritative lifecycle source under KD-038/LC-A. Consumer is Sneak, acting on its established interest in link-status currency for identity-bound evaluation. The purpose is to make LC-F/T3-P3 invalidation operative for Sneak by establishing the exclusive architectural basis of edge knowledge. No new authority, holder, or state category is created.
- **EA-2 — Awareness defined:** Awareness means Sneak obtaining the holder's authoritative assertion that a lifecycle edge has been established affecting the link under evaluation. Awareness concerns edge occurrence and resulting LC-S status, never edge mechanics, lifecycle procedures, or holder internals.
- **EA-3 — Exclusive source; no inference:** Edge knowledge comes exclusively from holder assertion obtained through Sneak's established per-interaction resolution relationship under KD-041. This exclusivity is a Sneak-side epistemic constraint: it governs what Sneak may treat as edge knowledge. It does not obligate the Identity Engine to any new proactive assertion, procedure, or conveyance beyond its established authoritative-source role. Sneak never infers edges from interaction behavior, time passage, absence of signal, or its own observations. Absence of edge awareness is not knowledge that no edge occurred.
- **EA-4 — Known edge established:** An edge is known to Sneak when obtained under EA-3. This contract is the applicable established mechanism referenced by LC-M at the architectural level. A known edge renders the pre-edge-anchored 2e usage reference unusable for new identity-bound evaluations; completed work is not retroactively altered.
- **EA-5 — Currency scope:** Within the originating interaction's established 2e usage scope, the holder's acquisition-time determination governs under RC-T. Beyond that scope, currency is re-established through the holder, never assumed or inferred. No mandatory re-resolution is imposed beyond LC-M/RC-T.
- **EA-6 — Awareness failure handling:** If edge awareness is unavailable, ambiguous, or cannot be obtained where currency is required, Sneak does not rely on the determination's currency. Such outcomes fold into the existing RL-D/QB-F/B9/PA7 fail-closed taxonomy. Failed or partial awareness leaves no retained state.
- **EA-7 — Transient awareness state; mechanism future:** Awareness state is transient and ephemeral under KD-022 2b/2e, subject to B3 and C0. Sneak holds no cross-interaction edge ledger. Transport, endpoints, push/pull, polling, timing, retry, and presentation remain undefined and future contract/implementation architecture. This contract establishes the exclusive basis and conditions of edge knowledge, not how it is conveyed.
- **Composition:** KD-041 is used, not modified; LC-F/LC-M/RC-T are composed, not redefined; KD-038's holder designation is relied upon, not extended. The contract imposes no new procedural obligation on the Identity Engine.
- **Preserved boundaries:** PA2, PA5, and PA7 are unchanged; lifecycle procedures, validity bounds/values, KD-026 cross-system roles, D-QB6 platform-supplied addressing identity, link-resolution mechanics beyond KD-041, and API/transport/schema/storage/platform mechanics remain undefined. No new authority, holder, state category, authorization, or implementation is established.
- No implementation or currently unauthorized action is authorized by KD-046.

**Execution / Resulting State:** KD-046 is adopted as the authoritative identity-link lifecycle edge-awareness contract for the Sneak/Identity Engine relationship. Authorized execution includes appending KD-046 to CORE/DECISIONS.md and incorporating EA-1–EA-7 into CORE/KOS-SNEAK-ARCH.md. The edge-awareness semantic gap identified by LC-M is closed at the architectural relationship level. Holder-side lifecycle procedures, validity values, KD-026 roles, D-QB6, and concrete awareness conveyance/implementation remain unestablished.
