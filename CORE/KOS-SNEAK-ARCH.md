# KOS Sneak Architecture

**Status:** ADOPTED FRAMEWORK  
**Authority:** KD-021  
**Scope:** Kustomz ecosystem conversational interface architecture

## 1. Identity and Purpose

Sneak is the Discord-facing conversational interface layer of the Kustomz ecosystem.

Sneak is not a standalone Discord bot in the architectural sense. Sneak is an interface into applicable Kustomz services and data.

## 2. Adopted Capability Scope

Sneak's adopted capability scope is limited to:

1. Conversational interaction with Kustomz systems.
2. CSR2 intelligence.
3. Dynamic member/user statistics.
4. Ticket Engine interaction.
5. Transcript handling.
6. Project Vision integration.
7. External CSR2 data intake through the private `#csr2-data-intake` channel.

This capability scope may be changed only by an explicit Kustomz owner decision recorded under the adopted KOS Decision & Promotion Protocol.

## 3. Authority and Prohibitions

Sneak reflects authoritative Kustomz ecosystem state; it does not originate that authority.

Sneak shall not become:

- a competing database;
- an authority system;
- a project-state source;
- a separate source of truth; or
- a system that redefines its own purpose, capabilities, or permissions.

These prohibitions remain in force unless overridden by an explicit later Kustomz owner decision recorded under the adopted protocol.

## 4. Cross-Interface Continuity

The adopted ecosystem continuity model is:

**WEB → ANDROID → DISCORD/SNEAK**

The Web interface is the primary Toolbox experience. Android is planned. Sneak is the Discord/conversational interface.

Users are intended to move between these interfaces without losing relevant work-state or ecosystem context.

The authoritative portable work-state/context mechanism required to fully realize this continuity is currently **UNDEFINED**.

## 5. KOSD Architectural Requirements

KOSD shall define authoritative boundaries for:

- Sneak behavior rules.
- Permission and authority rules.
- Sneak personality definition, with KOSD-defined rendering latitude.
- State classification criteria distinguishing authoritative state from ephemeral state.
- Kustomz-to-Discord identity-linking architecture.
- Conformance requirements.
- Sneak definition versioning.
- The interface/presentation semantic boundary.
- A designated contract set and Sneak's obligations to consume those contracts.

The contents of these requirements remain **UNDEFINED** unless separately adopted by a later owner decision.

## 6. Explicitly Undefined / Not Established by KD-021

KD-021 does not establish or select:

- Sneak implementation model A, B, or C.
- Executable Sneak implementation within KOSD.
- Project Vision definition.
- Ticket Engine definition.
- CSR2 intelligence definition, including NSB, SCB, or TRB scope.
- Platform or service contracts.
- Role-to-permission mappings.
- Transcript rules.
- `#csr2-data-intake` rules.
- Kustomz-to-Discord identity-linking mechanics.
- Identity/state classification mechanics.
- Conformance procedures.
- Sneak definition version.
- Sneak as a KOSD module for the purposes of KD-019.
- Any other item not explicitly adopted by KD-021.

All such items remain **UNDEFINED** or **OPEN** as applicable.

## 7. Known Architectural Tensions

### 7.1 Derived Statistics

Derived statistics must remain traceable to authoritative sources.

The standard, mechanism, and evidence requirements for that traceability are currently **UNDEFINED**.

### 7.2 Cross-Interface Continuity

The adopted WEB → ANDROID → DISCORD/SNEAK continuity model requires an eventual authoritative portable work-state/context mechanism.

That mechanism is currently **UNDEFINED**.

## 8. Implementation-Owned Mechanics

The following remain implementation-owned mechanics unless a later owner decision establishes otherwise:

- Hosting and runtime.
- Libraries and frameworks.
- Discord gateway mechanics.
- Secret handling.
- Presentation choices within the adopted semantic boundary.
- Caching mechanics, pending authoritative state-classification criteria.
- Other non-behavioral engineering details that do not alter authoritative Sneak behavior.

## 9. Architectural Boundary

KOSD owns the authoritative definition and boundaries adopted for Sneak.

Implementation may realize that architecture outside KOSD, subject to future applicable contracts, conformance requirements, authority rules, and other decisions that have not yet been established.

Creating this architecture record does not authorize implementation.

## 10. Change Control

Changes to the adopted Sneak architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-021.
