# KOS Kustomz Toolbox Architecture

**Status:** ADOPTED ARCHITECTURAL RECOGNITION
**Authority:** KD-039
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

## 7. Continuity Boundary

The existing WEB → ANDROID → DISCORD/SNEAK continuity principle is recognized as part of the Toolbox interface model.

The authoritative portable work-state/context mechanism and its holder remain **UNDEFINED**.

This architecture does not establish, designate, or implement that mechanism or holder.

The continuity principle therefore remains an architectural target whose full implementation is blocked pending the required future KOSD decision establishing the portable work-state mechanism and holder.

## 8. Explicitly Undefined / Not Established

The following remain undefined or unestablished by KD-039:

- Toolbox formal classification as module, subsystem, or required-module-set member.
- Shared-engine internals and mechanics.
- Engine contracts, schemas, APIs, and storage.
- Authoritative holders for Toolbox-modified state.
- Permission grant-holder designations.
- Permission mappings and authorizations.
- Portable work-state mechanism and holder.
- Cross-system contracts and conformance requirements.
- Implementation location and implementation model.
- NSB/SCB/page-level functional architecture.
- Resolvability contract required for operational identity-bound access through Sneak.
- Validity bounds, lifecycle procedures, and other future Toolbox-specific state procedures.

## 9. Dependencies and Blockers

This architecture is constrained by:

- KD-001 — KOS Decision & Promotion Protocol.
- KD-003 — KOS-RELEASE Draft status.
- KD-019 — required-module-set authority.
- KD-021 through KD-038 — applicable Sneak architecture and boundaries.
- KD-022 — state classification.
- KD-023 through KD-029 — behavioral, permission, authority, cross-system, freshness, attribution, and standing boundaries.

The following remain genuine blockers for subsequent establishment or implementation where applicable:

1. Portable work-state mechanism and holder.
2. Permission grant-holder designations.
3. Authoritative holders for Toolbox-modified CSR2 state.
4. KOS-RELEASE promotion for any future module/release treatment.
5. Resolvability contract for operational identity-bound access through Sneak.

None of these blockers is resolved by this architecture.

## 10. Implementation Boundary

This architecture does not authorize implementation.

Implementation may be established by a future explicit Kustomz owner decision and may be located outside KOSD, subject to applicable architecture, contracts, conformance requirements, authority rules, and other decisions then in force.

Creating or updating this architecture record does not authorize implementation.

## 11. Change Control

Changes to the adopted Kustomz Toolbox architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-001 through KD-039.
