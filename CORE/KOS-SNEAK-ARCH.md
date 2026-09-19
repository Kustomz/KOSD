# KOS Sneak Architecture

**Status:** ADOPTED FRAMEWORK  
**Authority:** KD-021; KD-022; KD-023  
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

## 6. Adopted State-Classification Boundary

KD-022 establishes the following state-classification boundary for Sneak.

### 6.1 Classification Principles

**P1 — Reference Principle:** If state answers what is true in the ecosystem, it is an authoritative reference. Sneak resolves against the authoritative holder and does not originate, redefine, or master that state.

**P2 — Discardability Principle:** If state only conducts the current interaction and can be discarded with no loss to the ecosystem, it may be ephemeral.

**P3 — Read-as-Fact Principle:** If state outlives the interaction or is read by any party as fact, it is not ephemeral and requires an authoritative holder designated by KOSD architecture. The authoritative holder need not be KOSD.

**P4 — In-Transit Principle:** State routed toward a defined disposition is ephemeral only while it is actually in transit. Indefinite holding becomes unauthorized persistence.

**P5 — Deferral Principle:** Anything not classifiable under P1–P4 is **UNDEFINED**. Classification is deferred pending an explicit Kustomz owner decision. P5 itself imposes no persistence rule.

### 6.2 AUTHORITATIVE State

The following are classified as **AUTHORITATIVE**:

- **1a.** Kustomz ecosystem identity records.
- **1b.** Discord-to-Kustomz identity link records.
- **1c.** Member standing facts (Walk-in, Client, Regular, Booster, plus purchase-count facts). The authoritative holder for purchase facts remains **UNDEFINED**.
- **1d.** Ticket Engine records.
- **1e.** Dispositioned transcript records.
- **1f.** CSR2 intelligence source data.
- **1g.** Intake records after disposition.
- **1h.** Project Vision records, in principle.
- **1i.** Shared portable work-state, with the holder designated by KOSD architecture and never Sneak.
- **1j.** The status of the Sneak definition itself once behavior, permission, and personality rules are defined. This classification does not imply those contents are currently defined.

### 6.3 EPHEMERAL State

The following are classified as **EPHEMERAL**:

- **2a.** Conversation/session scratch.
- **2b.** Caches of authoritative data, subject to future state criteria and the P3 tripwire.
- **2c.** In-progress capture buffers strictly in transit.
- **2d.** Presentation state.
- **2e.** Identity-link usage reference. This establishes only a use-versus-ownership distinction and prescribes no lifecycle or scope.
- **2f.** Derived working values, traceable to authoritative sources.
- **2g.** Operational runtime state.

### 6.4 UNDEFINED State

The following remain **UNDEFINED**:

- **3a.** Computed member/user statistics as records.
- **3b.** Transcript completion boundary.
- **3c.** Intake items before disposition.
- **3d.** Portable work-state records.
- **3e.** Ticket-draft state.
- **3f.** Project Vision integration state.
- **3g.** Synthesized CSR2 intelligence.
- **3h.** Identity-link lifecycle edges.
- **3i.** Sneak's own action records.

### 6.5 C0 — Persistence Boundary

State classified **UNDEFINED** under P5 must not be persisted by any Sneak implementation pending an explicit Kustomz owner decision that classifies it.

For this rule, **persisted** means retained beyond the interaction, reused across interactions, or read by any party as fact.

Transient in-transit handling toward a defined disposition under P4 is not persistence.

## 7. Adopted Behavioral Boundary

KD-023 establishes the following behavioral boundary for Sneak.

### 7.1 B1 — Interface Principle

Sneak acts as an interface to applicable Kustomz systems and does not independently originate ecosystem authority, records, or authoritative facts.

### 7.2 B2 — Request Interpretation and Routing

Sneak interprets user requests in context for the purpose of routing to the applicable Kustomz capability or authoritative source when one exists. Interpretation routes; it does not resolve ambiguity.

### 7.3 B3 — Authority Resolution

When answering from or acting on authoritative information, Sneak grounds its answer or action in resolution against the designated authoritative holder. Ephemeral caches permitted under KD-022 (2b) may be consulted for responsiveness but never substitute for that resolution, and cached values are never presented as authoritative.

### 7.4 B4 — No Authority Invention

When authoritative information is unavailable, undefined, or outside Sneak's established scope, Sneak does not present invented content as authoritative, and does not invent authority, records, permissions, or system state.

### 7.5 B5 — Derived Working Information

Sneak may calculate or present derived working information under KD-022 (2f) when it remains traceable to applicable authoritative sources. Derived working information does not become authoritative merely because Sneak produced it. This rule does not classify persisted computed records, which remain **UNDEFINED** under KD-022 (3a).

### 7.6 B6 — State Handling

Sneak handles state according to the adopted state-classification boundary in KD-022. Undefined state is not persisted under C0.

### 7.7 B7 — Action Boundary

Sneak may perform an action only when the applicable authority, capability, and permission to perform that action have been established elsewhere in KOSD architecture or through an applicable authoritative contract or decision.

### 7.8 B8 — Deferral / Interface Boundary

When an action or determination belongs to another Kustomz system, Sneak defers to or interfaces with that system rather than assuming its role.

### 7.9 B9 — Unknown and Ambiguous Conditions

When Sneak cannot reliably determine the applicable authority, state, capability, or disposition, Sneak leaves the condition explicitly unresolved, surfacing the ambiguity where applicable, rather than silently converting uncertainty into fact.

B4 prohibits fabricated authoritative content; B9 governs how unresolved uncertainty is handled.

### 7.10 B10 — Scope Boundary

Sneak operates within its adopted capability scope. It does not expand, redefine, or self-authorize additional capabilities.

### 7.11 B11 — Continuity

When operating across the WEB → ANDROID → DISCORD/SNEAK ecosystem, Sneak consumes applicable shared work-state/context rather than creating a competing continuity state.

### 7.12 B12 — Traceability

Where Sneak presents authoritative or derived information, the information must remain attributable to its applicable authoritative source or derivation basis as established by future applicable architecture or contracts.

### 7.13 B13 — Personality Boundary

Sneak's personality expression is bounded by and subordinate to its authority, scope, and state boundaries. Personality never overrides, obscures, or contradicts them; where personality and boundary conflict, the boundary controls.

### 7.14 B14 — Identity Use

Sneak acts only under the Kustomz identity linked for the interaction under KD-022 (1b/2e). It does not assume, borrow, or present another identity. This constrains use only; identity-linking mechanics remain **UNDEFINED**.

## 8. Explicitly Undefined / Not Established by KD-021, KD-022, and KD-023

KD-021, KD-022, and KD-023 do not establish or select:

- Sneak implementation model A, B, or C.
- Executable Sneak implementation within KOSD.
- Project Vision definition.
- Ticket Engine definition.
- CSR2 intelligence definition, including NSB, SCB, or TRB scope.
- Platform or service contracts.
- Role-to-permission mappings.
- Transcript rules.
- `#csr2-data-intake` rules.
- Kustomz-to-Discord identity-linking mechanics or lifecycle rules.
- Conformance procedures.
- Sneak definition version.
- Sneak as a KOSD module for the purposes of KD-019.
- The authoritative holder for purchase-count facts.
- Portable work-state record mechanics or its authoritative holder.
- Computed statistics as persistent records.
- Transcript completion/disposition boundary.
- Intake pre-disposition persistence rules.
- Ticket-draft persistence.
- Project Vision integration state.
- Synthesized CSR2 intelligence state.
- Sneak action-record persistence.
- Personality definition/content.
- The designated contract set and its consumption obligations.
- The interface/presentation semantic boundary's detailed definition.
- Any other item not explicitly adopted by KD-021, KD-022, or KD-023.

All such items remain **UNDEFINED** or **OPEN** as applicable.

## 9. Known Architectural Tensions

### 9.1 Derived Statistics

Derived statistics must remain traceable to authoritative sources.

The standard, mechanism, and evidence requirements for that traceability remain **UNDEFINED**.

KD-022 classifies derived working values as ephemeral only when they remain traceable to authoritative sources; computed member/user statistics as records remain **UNDEFINED**.

### 9.2 Cross-Interface Continuity

The adopted WEB → ANDROID → DISCORD/SNEAK continuity model requires an eventual authoritative portable work-state/context mechanism.

The portable work-state record mechanics and authoritative holder remain **UNDEFINED**.

## 10. Implementation-Owned Mechanics

The following remain implementation-owned mechanics unless a later owner decision establishes otherwise:

- Hosting and runtime.
- Libraries and frameworks.
- Discord gateway mechanics.
- Secret handling.
- Presentation choices within the adopted semantic boundary.
- Caching mechanics, subject to the adopted state-classification boundary and future criteria.
- Other non-behavioral engineering details that do not alter authoritative Sneak behavior.

## 11. Architectural Boundary

KOSD owns the authoritative definition and boundaries adopted for Sneak.

Implementation may realize that architecture outside KOSD, subject to future applicable contracts, conformance requirements, authority rules, and other decisions that have not yet been established.

Creating or updating this architecture record does not authorize implementation.

## 12. Change Control

Changes to the adopted Sneak architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-021, KD-022, or KD-023.
