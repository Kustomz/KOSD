# KOS Kustomz Toolbox Architecture

**Status:** ADOPTED ARCHITECTURAL RECOGNITION
**Authority:** KD-039; portable work-state boundary additionally governed by KD-040
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

Users are intended to move between these interfaces without losing relevant work-state or ecosystem context, subject to the unresolved portable work-state boundary recorded below.

## 3. Shared Engine Principle

The Toolbox is architecturally understood as one shared engine serving its three interfaces.

This is an adopted architectural principle. The engine's internals, contracts, schemas, APIs, storage, and other implementation mechanics remain undefined.

No interface is established as a separate source of Toolbox authority merely by virtue of presentation or access.

## 4. Authority and State Boundary

The Toolbox operates against authoritative Kustomz ecosystem state and shall not become a competing database, authority system, project-state source, or separate source of truth.

The Toolbox does not originate, redefine, or independently master authoritative ecosystem state.

No authoritative holder is designated by this architecture for Toolbox-modified state.

Applicable KOSD state classifications remain controlling. In particular:

- **1f — CSR2 source data:** AUTHORITATIVE.
- **2f — Derived working values:** EPHEMERAL.
- **3f — Project Vision integration state:** UNDEFINED.
- **3g — Synthesized CSR2 intelligence state:** UNDEFINED.
- **1i — Portable work-state:** AUTHORITATIVE, with holder and mechanics remaining unresolved.

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

Portable work-state remains **AUTHORITATIVE under KD-022 1i**. KD-040 does not create or reclassify a state category.

### 7.2 Holder Boundary

A future portable work-state holder must be explicitly designated by KOSD, must not be Sneak, must be interface-independent, and must be scoped to Kustomz identity.

No holder is designated by KD-040. The Toolbox shared engine, Kustomz Identity Engine, Sneak, and any other system remain undesignated as portable work-state holder.

The Kustomz Identity Engine retains only its established KD-037 1a and KD-038 1b authority. KD-040 grants it no portable work-state authority, read/write role, or lifecycle role.

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

The shared Toolbox engine's internal role and responsibilities remain undefined. Interaction with portable work-state does not constitute holding it absent explicit KOSD designation.

## 8. Continuity Boundary

The existing **WEB → ANDROID → DISCORD/SNEAK** continuity principle remains the Toolbox interface model.

KD-040 now provides the adopted architectural boundary for portable work-state/context supporting that continuity. The holder, mechanics, permissions, and implementation remain unresolved.



The existing WEB → ANDROID → DISCORD/SNEAK continuity principle is recognized as part of the Toolbox interface model.

The authoritative portable work-state/context mechanism and its holder remain **UNDEFINED**.

This architecture does not establish, designate, or implement that mechanism or holder.

The continuity principle therefore remains an architectural target whose full implementation is blocked pending the required future KOSD decision establishing the portable work-state mechanism and holder.

## 9. Explicitly Undefined / Not Established

The following remain undefined or unestablished by KD-039:

- Toolbox formal classification as module, subsystem, or required-module-set member.
- Shared-engine internals and mechanics.
- Engine contracts, schemas, APIs, and storage.
- Authoritative holders for Toolbox-modified state.
- Permission grant-holder designations.
- Permission mappings and authorizations.
- Portable work-state holder and operational mechanics.
- Cross-system contracts and conformance requirements.
- Implementation location and implementation model.
- NSB/SCB/page-level functional architecture.
- Resolvability contract required for operational identity-bound access through Sneak.
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

1. Portable work-state holder, operational mechanics, and procedures.
2. Permission grant-holder designations.
3. Authoritative holders for Toolbox-modified CSR2 state.
4. KOS-RELEASE promotion for any future module/release treatment.
5. Resolvability contract for operational identity-bound access through Sneak.

None of these blockers is resolved by this architecture.

## 11. Implementation Boundary

This architecture does not authorize implementation.

Implementation may be established by a future explicit Kustomz owner decision and may be located outside KOSD, subject to applicable architecture, contracts, conformance requirements, authority rules, and other decisions then in force.

Creating or updating this architecture record does not authorize implementation.

## 12. Change Control

Changes to the adopted Kustomz Toolbox architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-001 through KD-039.
