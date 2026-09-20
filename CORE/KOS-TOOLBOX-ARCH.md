# KOS Kustomz Toolbox Architecture

**Status:** ADOPTED ARCHITECTURAL RECOGNITION
**Authority:** KD-039; portable work-state boundary additionally governed by KD-040 and KD-042
**Scope:** Kustomz Toolbox architectural recognition for the shared CSR2 editing/tooling environment

## 1. Identity and Purpose

The Kustomz Toolbox is a shared CSR2 editing and tooling environment within the Kustomz ecosystem.

This architecture recognizes the Toolbox as a named KOSD architectural concept. It does not classify the Toolbox as a KOSD module, subsystem, or required-module-set member.

## 2. Interface Model

The adopted Toolbox interface model is:

**WEB → ANDROID → DISCORD/SNEAK**

The Toolbox interfaces are:

- **Web:** primary Toolbox experience.
- **Android:** planned Toolbox experience.
- **Discord/Sneak:** conversational Toolbox interface.

Users are intended to move between these interfaces without losing relevant work-state or ecosystem context, subject to the portable work-state boundary and mechanics recorded below.

## 3. Shared Engine Principle

The Toolbox is architecturally understood as one shared engine serving its three interfaces.

This is an adopted architectural principle. The engine's internals, contracts, schemas, APIs, storage, and other implementation mechanics remain undefined.

No interface is established as a separate source of Toolbox authority merely by virtue of presentation or access.

## 4. Authority and State Boundary

The Toolbox operates against authoritative Kustomz ecosystem state and shall not become a competing database, authority system, project-state source, or separate source of truth.

The Toolbox does not originate, redefine, or independently master authoritative ecosystem state.

Applicable KOSD state classifications remain controlling. In particular:

- **1f — CSR2 source data:** AUTHORITATIVE.
- **2f — Derived working values:** EPHEMERAL.
- **3f — Project Vision integration state:** UNDEFINED.
- **3g — Synthesized CSR2 intelligence state:** UNDEFINED.
- **1i — Portable work-state:** AUTHORITATIVE, with the holder established by KD-042 and operational mechanics remaining unresolved.

No new state category is established by this architecture.

## 5. Sneak Interface Boundary

Discord/Sneak is one of the Toolbox interfaces.

When Sneak provides the conversational interface to Toolbox functionality, all applicable Sneak architecture remains in force, including KD-021 through KD-038.

This recognition does not grant Sneak additional authority, permissions, identity-link authority, state ownership, or action authorization.

Sneak remains an interface into applicable Kustomz systems and data and remains prohibited from becoming a competing database, authority system, project-state source, or separate source of truth.

The Toolbox does not participate in or redefine the Kustomz-to-Discord identity-link resolution architecture.

## 6. Functional Scope Boundary

NSB, SCB, Garage, Legends, Fusions, Stage 6, Game Assets, and page-level or feature-level Toolbox functionality remain project-level functional material.

Such functional definitions are not adopted as KOSD architecture by this recognition.

Future Toolbox functional architecture may be established by separate explicit Kustomz owner decisions.

## 7. Portable Work-State Boundary

KD-040 adopts the portable work-state architectural boundary required by the Toolbox continuity target.

### 7.1 Definition

Portable work-state is the authoritative, Kustomz-identity-bound record of a user's in-progress Toolbox work and the ecosystem context required to resume that work across the Web, Android, and Discord/Sneak interfaces.

Portable work-state does not contain or replace authoritative CSR2 source data, Kustomz identity records, Kustomz↔Discord identity-link records, derived intelligence, dispositioned history, or interaction-scoped ephemeral state.

Portable work-state remains **AUTHORITATIVE under KD-022 1i**. KD-040 does not create or reclassify a state category; KD-042 establishes its holder.

### 7.2 Holder Boundary

KD-042 designates the **Kustomz Toolbox**, in its interface-independent capacity as the shared engine established by KD-039, as the authoritative holder of KD-022 1i portable work-state.

The designation is explicitly not made to the Web, Android, or Discord/Sneak interfaces. No interface-specific store becomes the holder, and Sneak never holds portable work-state.

The holder is scoped to Kustomz identity and holds the single authoritative portable work-state record per Kustomz identity and applicable work-state scope. Cross-interface continuity remains holder-mediated.

The holder has authority over the recognized work-state lifecycle edges — creation, update, consumption, and termination — while lifecycle procedures and mechanics remain undefined. The holder also has authority over holder-established invalidation within the existing §7.5 boundary.

Holding does not constitute write-path authorization. Permission to create, update, or terminate held records remains separately unresolved and subject to future permission-grant-holder and applicable cross-system decisions.

The Kustomz Identity Engine retains only its established KD-037 1a and KD-038 1b authority. KD-042 grants it no portable work-state authority, read/write role, or lifecycle role.

Conflict-resolution policy, validity bounds, retention/disposition, schemas, storage, APIs, implementation, and the Sneak-originated update path remain undefined.

### 7.3 Identity and Continuity

Portable work-state is addressed by Kustomz identity.

For Discord-originated access, the addressing Discord identity is first resolved through the existing KD-032 through KD-038 identity-link architecture. The Discord identity does not directly address portable work-state.

Cross-interface continuity is holder-mediated. Interfaces do not transfer authoritative work-state directly to one another, and no interface-specific store may become a competing authoritative record.

### 7.4 Lifecycle Boundary

The recognized work-state lifecycle semantics are:

- creation;
- update;
- consumption;
- termination.

Lifecycle procedures, timers, retention, clearing, archiving, and other operational mechanics remain undefined.

Sneak never holds portable work-state. Sneak may consume work-state context ephemerally within an interaction. Whether Sneak-originated work may update the eventual holder remains a future cross-system action/permission question.

### 7.5 Invalidation, Staleness, Conflict, and Failure

Work-state invalidation/staleness boundaries include supersession, holder-established invalidation, any future validity-bound expiration, holder change, and applicable future KOSD decisions.

An identity-link change by itself does not invalidate Kustomz-identity-addressed work-state; it may instead affect Discord-originated identity resolution or access.

Concurrent updates constitute a conflict condition. Conflict-resolution policy remains undefined.

If the holder is unreachable or current work-state cannot be determined, work-state is undeterminable and must not be presented as current. An absent or invalid record does not authorize repair or any other unestablished action.

### 7.6 Relationship to Authoritative CSR2 State

Portable work-state may reference authoritative CSR2 source records but never redefines or becomes the authority for those source records.

The shared Toolbox engine's internal role and responsibilities beyond the holder designation remain undefined. Interaction with portable work-state does not establish any additional authority beyond the KD-042 holder boundary.

## 8. Continuity Boundary

The existing **WEB → ANDROID → DISCORD/SNEAK** continuity principle remains the Toolbox interface model.

KD-040 provides the adopted architectural boundary for portable work-state/context supporting that continuity, and KD-042 now establishes its authoritative holder. Mechanics, permissions, and implementation remain unresolved.

The existing continuity principle is recognized as part of the Toolbox interface model.

The authoritative portable work-state holder is established by KD-042 as the Kustomz Toolbox in its interface-independent capacity. The operational mechanism remains **UNDEFINED**.

This architecture does not establish or implement the mechanism. The holder designation is architectural and does not authorize implementation.

## 9. Explicitly Undefined / Not Established

The following remain undefined or unestablished by this architecture:

- Toolbox formal classification as module, subsystem, or required-module-set member.
- Shared-engine internals and mechanics.
- Engine contracts, schemas, APIs, and storage.
- Authoritative holders for Toolbox-modified state.
- Permission grant-holder designations.
- Permission mappings and authorizations.
- Portable work-state operational mechanics and procedures; the holder is established by KD-042.
- Cross-system contracts and conformance requirements.
- Implementation location and implementation model.
- NSB/SCB/page-level functional architecture.
- Validity bounds, lifecycle procedures, and other future Toolbox-specific state procedures.

## 10. Dependencies and Blockers

This architecture is constrained by:

- KD-001 — KOS Decision & Promotion Protocol.
- KD-003 — KOS-RELEASE Draft status.
- KD-019 — required-module-set authority.
- KD-021 through KD-038 — applicable Sneak architecture and boundaries.
- KD-022 — state classification.
- KD-023 through KD-029 — behavioral, permission, authority, cross-system, freshness, attribution, and standing boundaries.

The following remain genuine blockers for subsequent establishment or implementation where applicable:

1. Portable work-state operational mechanics and procedures; the holder is established by KD-042.
2. Permission grant-holder designations.
3. Authoritative holders for Toolbox-modified CSR2 state.
4. KOS-RELEASE promotion for any future module/release treatment.

The portable work-state holder blocker is satisfied by KD-042. The remaining blockers concern mechanics, permissions, other authoritative holders, and release treatment as separately identified.

## 11. Implementation Boundary

This architecture does not authorize implementation.

Implementation may be established by a future explicit Kustomz owner decision and may be located outside KOSD, subject to applicable architecture, contracts, conformance requirements, authority rules, and other decisions then in force.

Creating or updating this architecture record does not authorize implementation.

## 12. Change Control

Changes to the adopted Kustomz Toolbox architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-001 through KD-042.
