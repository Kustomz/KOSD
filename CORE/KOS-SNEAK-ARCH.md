# KOS Sneak Architecture

**Status:** ADOPTED FRAMEWORK  
**Authority:** KD-021; KD-022; KD-023; KD-024; KD-025; KD-026; KD-027; KD-028  
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

## 8. Adopted Permission and Authority Boundary

KD-024 establishes the following permission and authority boundary for Sneak.

### 8.1 PA0 — Architectural Definitions

- **Capability:** what Sneak is scoped to do — the closed seven established by KD-021 and B10. This is established by KOSD.
- **Authority:** the legitimate power to perform an action or decide a matter — held by a system or established by KOSD decision or contract. It answers "who says this can be done."
- **Permission:** a grant to a specific identity to perform a specific action within that authority. It answers "may this identity do it."

An action is authorized only when capability, authority, and permission all hold for the acting identity. These are three distinct requirements; none implies the others.

### 8.2 PA1 — Read / Action Separation

Authority to read information and authority to perform an action are distinct domains.

**Read:** resolving against and presenting information.  
**Action:** mutating, submitting, changing, or otherwise effecting state.

Read access never implies action authority.

Read authorization for Sneak requires: (a) the information is within Sneak's capability scope, (b) the authoritative holder's access determination for the linked identity permits it, and (c) no KOSD prohibition bars it.

Action authorization is governed by PA2.

### 8.3 PA2 — Action Authorization Gate

Before performing an action, all four must be affirmatively established:

1. The action is within Sneak's adopted capability scope (B10).
2. The authority to perform it has been established in KOSD architecture or an applicable authoritative contract or decision (B7).
3. The linked identity holds the required permission grant, resolved against the applicable holder (PA3).
4. The action is taken under the Kustomz identity linked for the interaction (B14).

The gate is conjunctive and fail-closed: any unmet or undeterminable element means the action is not performed.

### 8.4 PA3 — Grants Live with the Holder

Permission grants are authoritative state of the applicable system under KD-022 P1.

Sneak resolves permission questions against the holder at time of evaluation. Sneak maintains no permission ledger, cache-of-record, or standing grant table of its own.

### 8.5 PA4 — No Invention, No Escalation, No Social Authorization

Sneak does not invent, infer, or escalate permissions:

- read access never implies write access;
- a permission in one capability never implies permission in another;
- a grant to one identity never transfers to another;
- a grant for one action never stretches to an adjacent action.

Conversational context, user assertion ("you said I could"), and Sneak's own prior statements never constitute authorization.

### 8.6 PA5 — Deferral to the Applicable System

When KOSD architecture has not established the authorization, the determination belongs to the applicable authoritative system — not Sneak.

Sneak interfaces with that system directly under B8, constructs no delegation chains, infers no transitive authority, and makes no authorization determination itself.

### 8.7 PA6 — Identity Binding

Every authorization evaluation is of the form "may this linked identity do this action."

There is no ambient authority, no role-abstract authority, and no Sneak-as-principal authority. This preserves B14 and KD-022 1b/2e.

### 8.8 PA7 — Deny-by-Default Posture

Where authorization cannot be affirmatively established through PA2, the action is not performed.

The boundary's default state is closed. Each future mapping, contract, or KOSD decision opens specific actions explicitly, never by implication.

### 8.9 PA8 — No Sneak-Level Access Judgments

For reads, Sneak presents what the authoritative holder provides for the linked identity and enforces rules established by KOSD.

Sneak adds no access judgments of its own: it neither widens nor narrows access on its own authority.

### 8.10 PA9 — Derivation Neither Creates Authority Nor Expands Access

Computing or presenting derived working information under B5 and KD-022 2f does not create read authority the identity lacks at the sources and does not expand access beyond what the source holders determine.

Computation does not launder access.

## 9. Adopted Permission Grant-Holder Designation Boundary

KD-025 establishes the following architectural rule for identifying and designating the authoritative holder of permission grants for Sneak authorization evaluations. PA0–PA9 remain unchanged.

### 9.1 H — Holder Qualification

- **H1 — Recognition:** The holder must be a system or service recognized in KOSD architecture as authoritative for the grant domain in question. Sneak itself never qualifies.
- **H2 — Record-Holding:** The holder must be the system of record for the grants at issue — it originates or authoritatively maintains them — not a downstream consumer, cache, or reporter of another system's grants.
- **H3 — Resolvability:** KOSD architecture must establish how Sneak obtains the holder's determinations. The mechanism remains future contract architecture; this rule requires only that resolvability be established, not how.
- **H4 — No Circularity:** A system does not qualify where its grant determinations derive from Sneak, or where designations would create circular grant authority. Circularity yields no determinable holder.

### 9.2 D — KOSD Designation

- **D1 — Explicit KD:** A holder is designated by an explicit KOSD decision naming the holder for a given action domain.
- **D2 — Per Action-Domain:** Designation covers specific actions, capabilities, or domains and never means "all permissions." A designated holder's answers are authoritative only within its designated domain.
- **D3 — Designation Does Not Authorize:** Naming a holder opens no action. Every authorization evaluation still runs the full PA2 gate under PA7.
- **D4 — Revisable by Later KD:** Competing designations resolve under KD-015, with the latest applicable decision controlling. Genuine ambiguity yields an undetermined holder.

### 9.3 R — Grant Resolution

- **R1 — Per-Evaluation, Identity-Bound:** Sneak obtains the holder's determination for the specific linked-identity/action pair at evaluation time.
- **R2 — Acceptance Without Reinterpretation:** The holder's determination is the answer. Sneak does not second-guess, reinterpret, combine with other sources to override it, or substitute its own judgment.
- **R3 — No Persistence as Record:** Grant determinations are authoritative state under P1. Sneak does not persist them as records. Any transient handling remains subject to KD-022 2b, B3, and C0.
- **R4 — Ambiguity Fails Closed:** An ambiguous, partial, or unavailable determination is undeterminable and therefore fails PA7.

### 9.4 U — Undefined or Unresolvable Holder

- **U1 — No Designation:** No designated holder means PA5 has no target and the action is not performed under PA7. This remains the present state for actions without a designation.
- **U2 — Designated but Unresolvable:** If a designated holder's determination cannot be reliably obtained, B9 and PA7 apply. Sneak does not fall back to another holder, infer from another domain, or treat a stale determination as authoritative.
- **U3 — Circular or Irreconcilably Competing Designations:** These yield no determinable holder and therefore follow U2.

KD-025 designates no actual permission-grant holder and authorizes no action. Actual holder designations remain subject to later per-domain Kustomz decisions.

## 10. Adopted Cross-System Authorization Boundary

KD-026 establishes the following architectural rule for identifying the applicable authoritative systems when an action crosses system boundaries.

### 10.1 T2-P1 — Decomposition Rule

A cross-system action is evaluated as the set of its constituent state effects. For each effect, the applicable authoritative system is determined per-effect. There is no single applicable system for a cross-system action as a whole unless KOSD architecture, contract, or decision establishes one.

### 10.2 T2-P2 — Three Roles per Effect

For each effect, three roles are architecturally distinct:

- **Authorization owner:** determines whether the effect may occur.
- **Grant holder:** answers permission questions for the linked identity under KD-025.
- **State owner / executor:** holds the authoritative state and applies the effect.

The roles may coincide in one system or be split across systems. When split, each applicable role-owner must provide or establish its respective determination or application. No role's determination substitutes for another's.

### 10.3 T2-P3 — Establishment Rule

Which system fills each role for each effect is established by KOSD architecture, contract, or decision. Establishment is per-effect and per-role and is consistent with KD-025's per-action-domain designation boundary.

### 10.4 T2-P4 — No Sneak-Side Decomposition

Sneak does not decompose cross-system actions into effects, infer which systems are involved, or assign roles on its own authority. The action's system footprint — including its effects and applicable role-owners — must be established by KOSD architecture, contract, or decision.

An action whose footprint is not established is not authorized under PA7.

### 10.5 T2-P5 — Multiplicity and Conjunction

When multiple systems are relevant, including multiple effects or split roles, authorization is conjunctive across every applicable role-owner. If role-owner determinations conflict, Sneak does not arbitrate between authoritative systems. B9 and PA7 apply.

### 10.6 T2-P6 — Failure Modes Fail Closed

Undefined ownership, meaning no established role-owner for an effect, means the action is not authorized.

Ambiguous ownership, where multiple candidates exist without KOSD-established precedence, invokes B9 and PA7.

An established but unavailable owner also invokes B9 and PA7; no substitute owner or stale determination is accepted.

Circular ownership, including mutual dependency between role determinations for the same action, yields no determinable authorization and therefore PA7.

### 10.7 T2-P7 — Legitimate Execution / Authorization Split

Execution and authorization may belong to different systems only when:

1. the split and each system's role are established by KOSD architecture, contract, or decision;
2. determinations form an acyclic dependency structure; and
3. the execution system does not originate authorization.

Grant and authorization determinations remain with their respective owners. Any circular dependency invokes T2-P6.


## 10. Explicitly Undefined / Not Established by KD-021, KD-022, KD-023, KD-024, and KD-025

KD-021 through KD-027 do not establish or select:

- Sneak implementation model A, B, or C.
- Executable Sneak implementation within KOSD.
- Project Vision definition.
- Ticket Engine definition.
- CSR2 intelligence definition, including NSB, SCB, or TRB scope.
- Platform or service contracts.
- Role-to-permission mappings.
- Discord permissions.
- Ticket Engine permissions.
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
- Grant-holder designation per capability.
- Actual authorization owners, grant holders, or state owners/executors for any specific action.
- The system footprint for any specific cross-system action.
- Validity-bound values, revocation-awareness channels, holder-bound ratification, and action/domain stringency values for revocation freshness.
- Application of derived-information attribution to specific derivations.
- Provenance retention mechanics, attribution presentation/display, description sufficiency criteria, conflict presentation choices, and reuse of derived values across interactions.
- Standing-as-permission-input rules.
- Any other item not explicitly adopted by KD-021, KD-022, KD-023, or KD-024.

All such items remain **UNDEFINED** or **OPEN** as applicable, except where a later adopted decision establishes a specific boundary.

## 11. Adopted Revocation Freshness Boundary

KD-027 establishes the following architectural rule for revocation freshness of cached permission/grant determinations.

### 11.1 T3-P1 — Event-Relative Freshness

Freshness is event-relative, not time-relative. A cached determination is fresh only within its established validity bounds and while no invalidating event has occurred. Validity bounds are established by KOSD architecture or the applicable holder's determination terms, never by Sneak's clock, heuristics, or assumptions. Elapsed time alone neither validates nor invalidates a determination.

### 11.2 T3-P2 — Cached Consultation in Authorization

During the PA2 gate, Sneak may consult a cached grant determination only when:

1. established validity bounds still cover the evaluation;
2. no invalidating event is known;
3. the consultation is transient and limited to the single evaluation; and
4. the cached value does not substitute for resolution under B3, but only reproduces the holder's still-valid determination.

If any condition fails, Sneak must re-resolve. If re-resolution is impossible, R4 and PA7 apply. Stricter requirements established for a domain may require direct holder resolution regardless of caching.

### 11.3 T3-P3 — Invalidating Events

A cached determination becomes invalid upon:

- explicit revocation established by the holder;
- expiration of its established validity bounds;
- supersession by a newer determination for the same linked-identity/action pair;
- change in the designated holder under KD-025 D4;
- an identity-link change affecting the evaluated identity under B14; or
- a KOSD decision altering the authorization landscape for the applicable domain under KD-015.

An invalid determination must not be used in any evaluation. Removal or cache-invalidation mechanics remain implementation-owned.

### 11.4 T3-P4 — Loss of Permission

Loss of permission is effective when the holder or KOSD establishes that loss, not when Sneak becomes aware of it. A cached affirmative grant does not survive an established revocation, expiration, or supersession. Failure to observe a loss is never evidence that permission remains valid.

### 11.5 T3-P5 — Freshness Unestablishable

When freshness cannot be established — including where validity bounds are unknown, invalidating events cannot be reliably accounted for, or the applicable holder is unreachable — the cached determination is undeterminable. For authorization, R4 and PA7 apply and the action is not performed.

For reads, the cached value must not be presented as the holder's current determination. B3 and B9 govern any further presentation or handling.

### 11.6 T3-P6 — Differential Stringency

Freshness requirements may differ by action, domain, or consequence only through KOSD-established architectural rules. Sneak does not create its own risk tiers, consequence ratings, or duration rules.

### 11.7 T3-P7 — Authorization Freshness vs. Read-Data Caching

Authorization caching and read-data caching are distinct regimes.

For authorization caching, T3-P1 through T3-P6 apply strictly. The default posture is re-resolution unless established validity permits transient cached consultation.

For read-data caching, KD-022 2b and B3 govern. Cached data does not substitute for authoritative resolution and must not be presented as authoritative merely because it is cached.

### 11.8 T3-P8 — Anti-Ledger Guarantees

The cache does not become a source of truth or standing permission ledger:

- cached determinations carry no independent authority and are never themselves grants;
- Sneak maintains no aggregate grant-state table;
- each evaluation consults within its established bounds rather than creating cross-evaluation precedent;
- once a determination is invalid for an evaluation, it is unusable for that evaluation; and
- cache contents are not authoritative to users, other systems, or future evaluations merely because they exist.



## 12. Adopted Derived-Information Attribution Boundary

KD-028 establishes the following positive attribution and traceability standard for derived information.

### 12.1 T4-P1 — Attribution Defined

Derived information is positively attributable when it can be established:

1. which authoritative source or sources it derives from;
2. what was done to derive it, described at the architectural level; and
3. which obtained source determination it is anchored to, with any applicable freshness lineage preserved.

Attribution is an establishable property; how much of that attribution is displayed to a user remains presentation architecture. Derivation does not alter the authority status of its source content.

### 12.2 T4-P2 — Minimum Provenance

A derived value is traceable only when all three minimum elements are established:

1. **Source identity:** the authoritative holder or source identified under the applicable architecture, not merely a copy of its data.
2. **Derivation description:** the operation performed, described in ordinary architectural terms.
3. **Determination anchor:** the specific obtained source determination on which the derivation rests, rather than a reference to the source only in general.

Where a source determination is subject to KD-027/T3, T3 invalidation governs that attribution anchor. T3 is not a universal freshness regime for all read or source data.

### 12.3 T4-P3 — Direct and Multi-Source Derivation

For direct-source presentation that passes through an authoritative holder's determination without transformation, attribution requires source identity and the applicable freshness of the obtained determination; no separate transformation description is required beyond identifying the presentation as the source's determination.

For multi-source derivation, each source must independently satisfy the applicable attribution requirements. Sources must not be blended in a manner that obscures which component derives from which source. Conflicting sources do not justify a synthesized consensus; the conflict is surfaced or the derived result is withheld under B9.

### 12.4 T4-P4 — Attributable Transformation

The derivation description states what was computed or transformed in ordinary architectural terms, such as a count, filter, sum, selection, ranking, or join, at a level sufficient for an independent reviewer with the same source determinations to reproduce the derivation's logic.

This requirement does not define metric internals, create new authoritative measures, reinterpret the meaning of a source determination, or depend on implementation artifacts such as query text, code, identifiers, or formats.

### 12.5 T4-P5 — Source Failure Modes

- **Unknown source:** attribution cannot be established; B5 does not authorize presentation as derived information and B9 governs.
- **Unavailable source:** a new derivation cannot be performed from that source; an existing derivation remains subject to the applicable freshness and validity rules for its anchored determination.
- **Ambiguous source:** B9 applies; Sneak does not guess.
- **Stale source determination:** where the applicable freshness regime establishes invalidity, the attribution anchor lapses; Sneak must re-derive or withhold.
- **Conflicting sources:** T4-P3 applies; Sneak does not invent a consensus.

### 12.6 T4-P6 — Authority Preservation

Derivation acquires no authority merely through computation. Each source retains its existing authority status, and the derived result remains derived unless a later explicit Kustomz decision establishes otherwise.

Derivation cannot promote, demote, or otherwise alter the authority status of its sources. This does not establish an authority-status hierarchy.

### 12.7 T4-P7 — Presentation Without Record-Creation

Derived working information classified under KD-022 2f may be presented as an answer within the interaction when:

1. T4-P1 and T4-P2 are satisfied;
2. the information is presented as derived and attributable, not as an authoritative record;
3. it is not persisted as an undefined record; and
4. PA9 is satisfied, with no access expansion.

Presenting an answer in-conversation does not by itself create an authoritative ecosystem record. This principle does not classify persisted computed statistics, which remain UNDEFINED under KD-022 3a and subject to C0.

### 12.8 T4-P8 — Attribution Is Not Authorization

Attribution establishes whether a derived value can be traced to its source and derivation basis. Authorization establishes whether the linked identity may see or use the information.

They are independent requirements. An attributable but unauthorized derivation must not be presented, and an authorized but unattributable derivation must not be presented as derived information. Neither requirement substitutes for the other.


## 13. Known Architectural Tensions

### 13.1 Derived Statistics

Derived statistics must remain traceable to authoritative sources.

The standard, mechanism, and evidence requirements for that traceability remain **UNDEFINED**.

KD-022 classifies derived working values as ephemeral only when they remain traceable to authoritative sources; computed member/user statistics as records remain **UNDEFINED**.

### 13.2 Cross-Interface Continuity

The adopted WEB → ANDROID → DISCORD/SNEAK continuity model requires an eventual authoritative portable work-state/context mechanism.

The portable work-state record mechanics and authoritative holder remain **UNDEFINED**.

### 13.3 Permission Grant-Holder Designation

PA3 requires permission grants to reside with the applicable authoritative holder, but the authoritative grant holder for each capability remains **UNDEFINED**.

### 13.4 Cross-System Authorization

KD-026 establishes the applicable-system framework for cross-system actions, but the footprint and role-owner for each specific action remain **UNDEFINED** until future architecture, contracts, or decisions establish them.

### 13.5 Revocation Freshness

KD-027 establishes the architectural freshness boundary, but validity-bound values, revocation-awareness channels, holder-bound ratification, and action/domain stringency remain **UNDEFINED**.

### 13.6 Derived-Information Attribution

KD-028 establishes the positive attribution and traceability standard. Remaining tensions are the application and mechanics left explicitly undefined by KD-028: provenance retention without shadow records; attribution display; description sufficiency; conflict presentation choice; reuse pressure on the KD-022 3a boundary; and any source-data freshness rules not otherwise established by applicable architecture or contracts.

### 13.7 Standing as Permission Input

Member standing facts are authoritative under KD-022 1c, but whether or how standing may factor into future permission grants remains **UNDEFINED** and is part of the future role-to-permission mapping question.

## 12. Implementation-Owned Mechanics

The following remain implementation-owned mechanics unless a later owner decision establishes otherwise:

- Hosting and runtime.
- Libraries and frameworks.
- Discord gateway mechanics.
- Secret handling.
- Presentation choices within the adopted semantic boundary.
- Caching mechanics, subject to the adopted state-classification boundary and future criteria.
- Other non-behavioral engineering details that do not alter authoritative Sneak behavior.

## 15. Architectural Boundary

KOSD owns the authoritative definition and boundaries adopted for Sneak.

Implementation may realize that architecture outside KOSD, subject to future applicable contracts, conformance requirements, authority rules, and other decisions that have not yet been established.

Creating or updating this architecture record does not authorize implementation.

## 16. Change Control

Changes to the adopted Sneak architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-021, KD-022, KD-023, KD-024, KD-025, KD-026, KD-027, or KD-028.
