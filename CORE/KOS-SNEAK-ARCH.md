# KOS Sneak Architecture

**Status:** ADOPTED FRAMEWORK  
**Authority:** KD-021; KD-022; KD-023; KD-024; KD-025; KD-026; KD-027; KD-028; KD-029; KD-030; KD-031; KD-032; KD-033; KD-034; KD-035; KD-037; KD-038; KD-041  
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

The following remain **UNDEFINED**. Items marked **[PARTIALLY CLASSIFIED]** have an adopted boundary governing part of the item while the noted establishments remain undefined. The marking changes no classification and creates no new state category.

- **3a.** Computed member/user statistics as records.
- **3b.** **[PARTIALLY CLASSIFIED]** Transcript completion boundary — governed by KD-030 (2c→1e crossing: authorized declaration, designated holder, faithful transition); the completion declarer, designated holder, and transcript content rules remain undefined until their prerequisites are established.
- **3c.** **[PARTIALLY CLASSIFIED]** Intake items before disposition — governed by KD-031 (pre-disposition holdings classified EPHEMERAL and interaction-scoped); hold duration, routing specifics, declaration authority, holder, and content/vetting rules remain undefined until their prerequisites are established.
- **3d.** Portable work-state records.
- **3e.** Ticket-draft state.
- **3f.** Project Vision integration state.
- **3g.** Synthesized CSR2 intelligence.
- **3i.** Sneak's own action records.

### 6.5 C0 — Persistence Boundary

State classified **UNDEFINED** under P5 must not be persisted by any Sneak implementation pending an explicit Kustomz owner decision that classifies it.

For this rule, **persisted** means retained beyond the interaction, reused across interactions, or read by any party as fact.

Transient in-transit handling toward a defined disposition under P4 is not persistence.

## 7. Kustomz Identity System of Record

KD-037 recognizes the **Kustomz Identity Engine** as the authoritative Kustomz identity system of record for the Kustomz identity records classified under KD-022 1a.

### 7.1 Authoritative Identity State

The Kustomz Identity Engine is the authoritative holder of KD-022 1a Kustomz ecosystem identity records. Sneak consumes authoritative Kustomz identity state and does not author, redefine, or become the holder of that state.

### 7.2 Identity-Link Anchor

The Kustomz side of KD-022 1b Discord-to-Kustomz identity-link records anchors to Kustomz identities held by the Kustomz Identity Engine. KD-038 designates the Kustomz Identity Engine as the 1b identity-link holder, separately from its 1a identity-system role.

### 7.3 Scope and Exclusions

Recognition of the Kustomz Identity Engine as the 1a system of record does not define the Identity Engine's schemas, identifiers, account model, identity lifecycle, APIs, storage, implementation, permissions, resolution mechanics, validity bounds, lifecycle procedures, edge-awareness mechanisms, or other internal or operational details. Those matters remain undefined unless separately established by an applicable Kustomz owner decision.

KD-038 now designates the Kustomz Identity Engine as the authoritative holder of KD-022 1b identity-link records and explicitly establishes the bounded Sneak query interest required by KD-034. The resolvability contract and dependent mechanics remain future work.

## 8. Adopted Behavioral Boundary

KD-023 establishes the following behavioral boundary for Sneak.

### 8.1 B1 — Interface Principle

Sneak acts as an interface to applicable Kustomz systems and does not independently originate ecosystem authority, records, or authoritative facts.

### 8.2 B2 — Request Interpretation and Routing

Sneak interprets user requests in context for the purpose of routing to the applicable Kustomz capability or authoritative source when one exists. Interpretation routes; it does not resolve ambiguity.

### 8.3 B3 — Authority Resolution

When answering from or acting on authoritative information, Sneak grounds its answer or action in resolution against the designated authoritative holder. Ephemeral caches permitted under KD-022 (2b) may be consulted for responsiveness but never substitute for that resolution, and cached values are never presented as authoritative.

### 8.4 B4 — No Authority Invention

When authoritative information is unavailable, undefined, or outside Sneak's established scope, Sneak does not present invented content as authoritative, and does not invent authority, records, permissions, or system state.

### 8.5 B5 — Derived Working Information

Sneak may calculate or present derived working information under KD-022 (2f) when it remains traceable to applicable authoritative sources. Derived working information does not become authoritative merely because Sneak produced it. This rule does not classify persisted computed records, which remain **UNDEFINED** under KD-022 (3a).

### 8.6 B6 — State Handling

Sneak handles state according to the adopted state-classification boundary in KD-022. Undefined state is not persisted under C0.

### 8.7 B7 — Action Boundary

Sneak may perform an action only when the applicable authority, capability, and permission to perform that action have been established elsewhere in KOSD architecture or through an applicable authoritative contract or decision.

### 8.8 B8 — Deferral / Interface Boundary

When an action or determination belongs to another Kustomz system, Sneak defers to or interfaces with that system rather than assuming its role.

### 8.9 B9 — Unknown and Ambiguous Conditions

When Sneak cannot reliably determine the applicable authority, state, capability, or disposition, Sneak leaves the condition explicitly unresolved, surfacing the ambiguity where applicable, rather than silently converting uncertainty into fact.

B4 prohibits fabricated authoritative content; B9 governs how unresolved uncertainty is handled.

### 8.10 B10 — Scope Boundary

Sneak operates within its adopted capability scope. It does not expand, redefine, or self-authorize additional capabilities.

### 8.11 B11 — Continuity

When operating across the WEB → ANDROID → DISCORD/SNEAK ecosystem, Sneak consumes applicable shared work-state/context rather than creating a competing continuity state.

### 8.12 B12 — Traceability

Where Sneak presents authoritative or derived information, the information must remain attributable to its applicable authoritative source or derivation basis as established by future applicable architecture or contracts.

### 8.13 B13 — Personality Boundary

Sneak's personality expression is bounded by and subordinate to its authority, scope, and state boundaries. Personality never overrides, obscures, or contradicts them; where personality and boundary conflict, the boundary controls.

### 8.14 B14 — Identity Use

Sneak acts only under the Kustomz identity linked for the interaction under KD-022 (1b/2e). It does not assume, borrow, or present another identity. This constrains use only; identity-linking mechanics remain **UNDEFINED**.

## 9. Adopted Permission and Authority Boundary

KD-024 establishes the following permission and authority boundary for Sneak.

### 9.1 PA0 — Architectural Definitions

- **Capability:** what Sneak is scoped to do — the closed seven established by KD-021 and B10. This is established by KOSD.
- **Authority:** the legitimate power to perform an action or decide a matter — held by a system or established by KOSD decision or contract. It answers "who says this can be done."
- **Permission:** a grant to a specific identity to perform a specific action within that authority. It answers "may this identity do it."

An action is authorized only when capability, authority, and permission all hold for the acting identity. These are three distinct requirements; none implies the others.

### 9.2 PA1 — Read / Action Separation

Authority to read information and authority to perform an action are distinct domains.

**Read:** resolving against and presenting information.  
**Action:** mutating, submitting, changing, or otherwise effecting state.

Read access never implies action authority.

Read authorization for Sneak requires: (a) the information is within Sneak's capability scope, (b) the authoritative holder's access determination for the linked identity permits it, and (c) no KOSD prohibition bars it.

Action authorization is governed by PA2.

### 9.3 PA2 — Action Authorization Gate

Before performing an action, all four must be affirmatively established:

1. The action is within Sneak's adopted capability scope (B10).
2. The authority to perform it has been established in KOSD architecture or an applicable authoritative contract or decision (B7).
3. The linked identity holds the required permission grant, resolved against the applicable holder (PA3).
4. The action is taken under the Kustomz identity linked for the interaction (B14).

The gate is conjunctive and fail-closed: any unmet or undeterminable element means the action is not performed.

### 9.4 PA3 — Grants Live with the Holder

Permission grants are authoritative state of the applicable system under KD-022 P1.

Sneak resolves permission questions against the holder at time of evaluation. Sneak maintains no permission ledger, cache-of-record, or standing grant table of its own.

### 9.5 PA4 — No Invention, No Escalation, No Social Authorization

Sneak does not invent, infer, or escalate permissions:

- read access never implies write access;
- a permission in one capability never implies permission in another;
- a grant to one identity never transfers to another;
- a grant for one action never stretches to an adjacent action.

Conversational context, user assertion ("you said I could"), and Sneak's own prior statements never constitute authorization.

### 9.6 PA5 — Deferral to the Applicable System

When KOSD architecture has not established the authorization, the determination belongs to the applicable authoritative system — not Sneak.

Sneak interfaces with that system directly under B8, constructs no delegation chains, infers no transitive authority, and makes no authorization determination itself.

### 9.7 PA6 — Identity Binding

Every authorization evaluation is of the form "may this linked identity do this action."

There is no ambient authority, no role-abstract authority, and no Sneak-as-principal authority. This preserves B14 and KD-022 1b/2e.

### 9.8 PA7 — Deny-by-Default Posture

Where authorization cannot be affirmatively established through PA2, the action is not performed.

The boundary's default state is closed. Each future mapping, contract, or KOSD decision opens specific actions explicitly, never by implication.

### 9.9 PA8 — No Sneak-Level Access Judgments

For reads, Sneak presents what the authoritative holder provides for the linked identity and enforces rules established by KOSD.

Sneak adds no access judgments of its own: it neither widens nor narrows access on its own authority.

### 9.10 PA9 — Derivation Neither Creates Authority Nor Expands Access

Computing or presenting derived working information under B5 and KD-022 2f does not create read authority the identity lacks at the sources and does not expand access beyond what the source holders determine.

Computation does not launder access.

## 10. Adopted Permission Grant-Holder Designation Boundary

KD-025 establishes the following architectural rule for identifying and designating the authoritative holder of permission grants for Sneak authorization evaluations. PA0–PA9 remain unchanged.

### 10.1 H — Holder Qualification

- **H1 — Recognition:** The holder must be a system or service recognized in KOSD architecture as authoritative for the grant domain in question. Sneak itself never qualifies.
- **H2 — Record-Holding:** The holder must be the system of record for the grants at issue — it originates or authoritatively maintains them — not a downstream consumer, cache, or reporter of another system's grants.
- **H3 — Resolvability:** KOSD architecture must establish how Sneak obtains the holder's determinations. The mechanism remains future contract architecture; this rule requires only that resolvability be established, not how.
- **H4 — No Circularity:** A system does not qualify where its grant determinations derive from Sneak, or where designations would create circular grant authority. Circularity yields no determinable holder.

### 10.2 D — KOSD Designation

- **D1 — Explicit KD:** A holder is designated by an explicit KOSD decision naming the holder for a given action domain.
- **D2 — Per Action-Domain:** Designation covers specific actions, capabilities, or domains and never means "all permissions." A designated holder's answers are authoritative only within its designated domain.
- **D3 — Designation Does Not Authorize:** Naming a holder opens no action. Every authorization evaluation still runs the full PA2 gate under PA7.
- **D4 — Revisable by Later KD:** Competing designations resolve under KD-015, with the latest applicable decision controlling. Genuine ambiguity yields an undetermined holder.

### 10.3 R — Grant Resolution

- **R1 — Per-Evaluation, Identity-Bound:** Sneak obtains the holder's determination for the specific linked-identity/action pair at evaluation time.
- **R2 — Acceptance Without Reinterpretation:** The holder's determination is the answer. Sneak does not second-guess, reinterpret, combine with other sources to override it, or substitute its own judgment.
- **R3 — No Persistence as Record:** Grant determinations are authoritative state under P1. Sneak does not persist them as records. Any transient handling remains subject to KD-022 2b, B3, and C0.
- **R4 — Ambiguity Fails Closed:** An ambiguous, partial, or unavailable determination is undeterminable and therefore fails PA7.

### 10.4 U — Undefined or Unresolvable Holder

- **U1 — No Designation:** No designated holder means PA5 has no target and the action is not performed under PA7. This remains the present state for actions without a designation.
- **U2 — Designated but Unresolvable:** If a designated holder's determination cannot be reliably obtained, B9 and PA7 apply. Sneak does not fall back to another holder, infer from another domain, or treat a stale determination as authoritative.
- **U3 — Circular or Irreconcilably Competing Designations:** These yield no determinable holder and therefore follow U2.

KD-025 designates no actual permission-grant holder and authorizes no action. Actual holder designations remain subject to later per-domain Kustomz decisions.

## 11. Adopted Cross-System Authorization Boundary

KD-026 establishes the following architectural rule for identifying the applicable authoritative systems when an action crosses system boundaries.

### 11.1 T2-P1 — Decomposition Rule

A cross-system action is evaluated as the set of its constituent state effects. For each effect, the applicable authoritative system is determined per-effect. There is no single applicable system for a cross-system action as a whole unless KOSD architecture, contract, or decision establishes one.

### 11.2 T2-P2 — Three Roles per Effect

For each effect, three roles are architecturally distinct:

- **Authorization owner:** determines whether the effect may occur.
- **Grant holder:** answers permission questions for the linked identity under KD-025.
- **State owner / executor:** holds the authoritative state and applies the effect.

The roles may coincide in one system or be split across systems. When split, each applicable role-owner must provide or establish its respective determination or application. No role's determination substitutes for another's.

### 11.3 T2-P3 — Establishment Rule

Which system fills each role for each effect is established by KOSD architecture, contract, or decision. Establishment is per-effect and per-role and is consistent with KD-025's per-action-domain designation boundary.

### 11.4 T2-P4 — No Sneak-Side Decomposition

Sneak does not decompose cross-system actions into effects, infer which systems are involved, or assign roles on its own authority. The action's system footprint — including its effects and applicable role-owners — must be established by KOSD architecture, contract, or decision.

An action whose footprint is not established is not authorized under PA7.

### 11.5 T2-P5 — Multiplicity and Conjunction

When multiple systems are relevant, including multiple effects or split roles, authorization is conjunctive across every applicable role-owner. If role-owner determinations conflict, Sneak does not arbitrate between authoritative systems. B9 and PA7 apply.

### 11.6 T2-P6 — Failure Modes Fail Closed

Undefined ownership, meaning no established role-owner for an effect, means the action is not authorized.

Ambiguous ownership, where multiple candidates exist without KOSD-established precedence, invokes B9 and PA7.

An established but unavailable owner also invokes B9 and PA7; no substitute owner or stale determination is accepted.

Circular ownership, including mutual dependency between role determinations for the same action, yields no determinable authorization and therefore PA7.

### 11.7 T2-P7 — Legitimate Execution / Authorization Split

Execution and authorization may belong to different systems only when:

1. the split and each system's role are established by KOSD architecture, contract, or decision;
2. determinations form an acyclic dependency structure; and
3. the execution system does not originate authorization.

Grant and authorization determinations remain with their respective owners. Any circular dependency invokes T2-P6.


## 12. Explicitly Undefined / Not Established by KD-021 through KD-038

### Boundaries adopted; establishments pending

The following architectural boundaries are adopted through KD-038. Their enabling establishments — holders, declarers, rules, values, mechanics — remain undefined and proceed through later KDs, contracts, or owner decisions. Adoption of a boundary establishes none of its pending establishments.

- Permission grant-holder designation per capability/domain (boundary: KD-025; no actual holder designated).
- Actual authorization owners, grant holders, or state owners/executors for any specific action; system footprints for specific cross-system actions (boundary: KD-026).
- Validity-bound values, revocation-awareness channels, holder-bound ratification, and action/domain stringency for revocation freshness (boundary: KD-027).
- Application of derived-information attribution to specific derivations; provenance retention mechanics, attribution presentation/display, description sufficiency criteria, conflict presentation choices, and reuse of derived values across interactions (boundary: KD-028).
- Standing-as-permission-input establishments: designated standing source, designated permission holder, established standing-to-permission basis (boundary: KD-029; no mapping, designation, or authorization created).
- Transcript completion/disposition establishments: completion-declaration authority and conditions, designated transcript holder, transcript content rules (boundary: KD-030).
- Intake establishments: intake declaration authority, designated intake holder, intake routing/content rules including any hold bound (boundary: KD-031).
- Identity-link holder designation is established by KD-038. Query operation remains subject to the unresolved resolvability contract and dependent prerequisites; lifecycle procedures, validity bounds, and edge-awareness mechanism remain pending (boundaries: KD-032; KD-033; KD-034; KD-035; KD-038).
- Portable work-state record mechanics and authoritative holder (classification: KD-022 1i AUTHORITATIVE with holder designated by KOSD architecture, never Sneak; mechanics and actual holder pending; 3d records remain UNDEFINED).
- The authoritative holder for purchase-count facts (KD-022 1c).

### Not established at any level

- Sneak implementation model A, B, or C.
- Executable Sneak implementation within KOSD.
- Project Vision definition.
- Ticket Engine definition.
- CSR2 intelligence definition, including NSB, SCB, or TRB scope.
- Platform or service contracts.
- Role-to-permission mappings.
- Discord permissions.
- Ticket Engine permissions.
- Kustomz-to-Discord identity-linking implementation mechanics, lifecycle procedures, and edge-awareness mechanism.
- Conformance procedures.
- Sneak definition version.
- Sneak as a KOSD module for the purposes of KD-019.
- Computed statistics as persistent records (KD-022 3a).
- Ticket-draft persistence (3e).
- Project Vision integration state (3f).
- Synthesized CSR2 intelligence state (3g).
- Sneak action-record persistence (3i).
- Personality definition/content.
- The designated contract set and its consumption obligations.
- The interface/presentation semantic boundary's detailed definition.
- Any other item not explicitly adopted by KD-021 through KD-038.

All such items remain **UNDEFINED** or **OPEN** as applicable.

## 13. Adopted Revocation Freshness Boundary

KD-027 establishes the following architectural rule for revocation freshness of cached permission/grant determinations.

### 13.1 T3-P1 — Event-Relative Freshness

Freshness is event-relative, not time-relative. A cached determination is fresh only within its established validity bounds and while no invalidating event has occurred. Validity bounds are established by KOSD architecture or the applicable holder's determination terms, never by Sneak's clock, heuristics, or assumptions. Elapsed time alone neither validates nor invalidates a determination.

### 13.2 T3-P2 — Cached Consultation in Authorization

During the PA2 gate, Sneak may consult a cached grant determination only when:

1. established validity bounds still cover the evaluation;
2. no invalidating event is known;
3. the consultation is transient and limited to the single evaluation; and
4. the cached value does not substitute for resolution under B3, but only reproduces the holder's still-valid determination.

If any condition fails, Sneak must re-resolve. If re-resolution is impossible, R4 and PA7 apply. Stricter requirements established for a domain may require direct holder resolution regardless of caching.

### 13.3 T3-P3 — Invalidating Events

A cached determination becomes invalid upon:

- explicit revocation established by the holder;
- expiration of its established validity bounds;
- supersession by a newer determination for the same linked-identity/action pair;
- change in the designated holder under KD-025 D4;
- an identity-link change affecting the evaluated identity under B14; or
- a KOSD decision altering the authorization landscape for the applicable domain under KD-015.

An invalid determination must not be used in any evaluation. Removal or cache-invalidation mechanics remain implementation-owned.

### 13.4 T3-P4 — Loss of Permission

Loss of permission is effective when the holder or KOSD establishes that loss, not when Sneak becomes aware of it. A cached affirmative grant does not survive an established revocation, expiration, or supersession. Failure to observe a loss is never evidence that permission remains valid.

### 13.5 T3-P5 — Freshness Unestablishable

When freshness cannot be established — including where validity bounds are unknown, invalidating events cannot be reliably accounted for, or the applicable holder is unreachable — the cached determination is undeterminable. For authorization, R4 and PA7 apply and the action is not performed.

For reads, the cached value must not be presented as the holder's current determination. B3 and B9 govern any further presentation or handling.

### 13.6 T3-P6 — Differential Stringency

Freshness requirements may differ by action, domain, or consequence only through KOSD-established architectural rules. Sneak does not create its own risk tiers, consequence ratings, or duration rules.

### 13.7 T3-P7 — Authorization Freshness vs. Read-Data Caching

Authorization caching and read-data caching are distinct regimes.

For authorization caching, T3-P1 through T3-P6 apply strictly. The default posture is re-resolution unless established validity permits transient cached consultation.

For read-data caching, KD-022 2b and B3 govern. Cached data does not substitute for authoritative resolution and must not be presented as authoritative merely because it is cached.

### 13.8 T3-P8 — Anti-Ledger Guarantees

The cache does not become a source of truth or standing permission ledger:

- cached determinations carry no independent authority and are never themselves grants;
- Sneak maintains no aggregate grant-state table;
- each evaluation consults within its established bounds rather than creating cross-evaluation precedent;
- once a determination is invalid for an evaluation, it is unusable for that evaluation; and
- cache contents are not authoritative to users, other systems, or future evaluations merely because they exist.



## 14. Adopted Derived-Information Attribution Boundary

KD-028 establishes the following positive attribution and traceability standard for derived information.

### 14.1 T4-P1 — Attribution Defined

Derived information is positively attributable when it can be established:

1. which authoritative source or sources it derives from;
2. what was done to derive it, described at the architectural level; and
3. which obtained source determination it is anchored to, with any applicable freshness lineage preserved.

Attribution is an establishable property; how much of that attribution is displayed to a user remains presentation architecture. Derivation does not alter the authority status of its source content.

### 14.2 T4-P2 — Minimum Provenance

A derived value is traceable only when all three minimum elements are established:

1. **Source identity:** the authoritative holder or source identified under the applicable architecture, not merely a copy of its data.
2. **Derivation description:** the operation performed, described in ordinary architectural terms.
3. **Determination anchor:** the specific obtained source determination on which the derivation rests, rather than a reference to the source only in general.

Where a source determination is subject to KD-027/T3, T3 invalidation governs that attribution anchor. T3 is not a universal freshness regime for all read or source data.

### 14.3 T4-P3 — Direct and Multi-Source Derivation

For direct-source presentation that passes through an authoritative holder's determination without transformation, attribution requires source identity and the applicable freshness of the obtained determination; no separate transformation description is required beyond identifying the presentation as the source's determination.

For multi-source derivation, each source must independently satisfy the applicable attribution requirements. Sources must not be blended in a manner that obscures which component derives from which source. Conflicting sources do not justify a synthesized consensus; the conflict is surfaced or the derived result is withheld under B9.

### 14.4 T4-P4 — Attributable Transformation

The derivation description states what was computed or transformed in ordinary architectural terms, such as a count, filter, sum, selection, ranking, or join, at a level sufficient for an independent reviewer with the same source determinations to reproduce the derivation's logic.

This requirement does not define metric internals, create new authoritative measures, reinterpret the meaning of a source determination, or depend on implementation artifacts such as query text, code, identifiers, or formats.

### 14.5 T4-P5 — Source Failure Modes

- **Unknown source:** attribution cannot be established; B5 does not authorize presentation as derived information and B9 governs.
- **Unavailable source:** a new derivation cannot be performed from that source; an existing derivation remains subject to the applicable freshness and validity rules for its anchored determination.
- **Ambiguous source:** B9 applies; Sneak does not guess.
- **Stale source determination:** where the applicable freshness regime establishes invalidity, the attribution anchor lapses; Sneak must re-derive or withhold.
- **Conflicting sources:** T4-P3 applies; Sneak does not invent a consensus.

### 14.6 T4-P6 — Authority Preservation

Derivation acquires no authority merely through computation. Each source retains its existing authority status, and the derived result remains derived unless a later explicit Kustomz decision establishes otherwise.

Derivation cannot promote, demote, or otherwise alter the authority status of its sources. This does not establish an authority-status hierarchy.

### 14.7 T4-P7 — Presentation Without Record-Creation

Derived working information classified under KD-022 2f may be presented as an answer within the interaction when:

1. T4-P1 and T4-P2 are satisfied;
2. the information is presented as derived and attributable, not as an authoritative record;
3. it is not persisted as an undefined record; and
4. PA9 is satisfied, with no access expansion.

Presenting an answer in-conversation does not by itself create an authoritative ecosystem record. This principle does not classify persisted computed statistics, which remain UNDEFINED under KD-022 3a and subject to C0.

### 14.8 T4-P8 — Attribution Is Not Authorization

Attribution establishes whether a derived value can be traced to its source and derivation basis. Authorization establishes whether the linked identity may see or use the information.

They are independent requirements. An attributable but unauthorized derivation must not be presented, and an authorized but unattributable derivation must not be presented as derived information. Neither requirement substitutes for the other.


## 15. Adopted Standing-as-Permission-Input Boundary

KD-029 establishes the following architectural boundary for the relationship between authoritative standing facts and future permission determinations.

### 15.1 T5-P1 — Four Levels

- **L1 — Standing as authoritative fact:** Standing facts classified under KD-022 1c are authoritative ecosystem facts. Sneak resolves them against the applicable authoritative source and does not track or originate them.
- **L2 — Standing as permission input:** Standing may be considered by the applicable permission holder within an established grant determination basis. The consideration is the holder's act, not Sneak's.
- **L3 — Standing-derived information:** Values Sneak computes from authoritative standing facts under KD-022 2f remain ephemeral derived working information, subject to B5, PA9, and KD-028 attribution. They are not authoritative merely because Sneak computed them.
- **L4 — Standing as permission:** Treating standing itself as authorizing an action is prohibited. L1, L2, and L3 never imply L4.

### 15.2 T5-P2 — Standing May Be an Input; Sneak Does Not Perform the Inference

There is no architectural bar on a designated permission holder considering authoritative standing when deciding a grant, but the standing-to-permission inference is never Sneak's. Sneak may resolve or provide standing facts when legitimately required by an established holder determination procedure, but never frames standing as permission or acts on standing alone as authorization.

### 15.3 T5-P3 — The Permission Holder Remains Responsible

Standing is an input, not the grant decision. The applicable permission holder remains responsible for the actual determination. A holder denial or unavailable determination governs and cannot be overridden by favorable standing.

### 15.4 T5-P4 — Informational Eligibility Is Not Authorization

Informational statements about eligibility do not constitute a permission grant and do not satisfy any element of the PA2 action authorization gate.

### 15.5 T5-R1 — Designated Standing Source

The authoritative source or holder for the standing facts in question must be designated before Sneak relies on those facts as an authorization input. The standing fact remains authoritative under KD-022 1c even when its authorization usability has not been established.

### 15.6 T5-R2 — Designated Permission Holder

The permission holder for the action must be designated under KD-025 D1.

### 15.7 T5-R3 — Established Standing-to-Permission Basis

An established basis must exist for standing to participate in the permission determination, whether through a future KOSD-established mapping or a holder-established determination procedure. T5 selects neither path.

### 15.8 T5-R4 — Identity Binding

Standing evaluation is bound to the linked identity. Another identity's standing, aggregate standing, or comparative standing cannot substitute for the linked identity's standing.

### 15.9 T5-F1 — Fail-Closed Standing Conditions

Standing that is unavailable, ambiguous, stale, or conflicting makes a dependent permission evaluation undeterminable and therefore subject to PA7. Stale standing follows the applicable T3 validity regime; conflicting standing is not synthesized.

### 15.10 T5-F2 — Standing Change

When standing changes, prior standing-anchored inputs are superseded and affected evaluations require re-evaluation. An identity-link change affecting the evaluated identity likewise requires re-evaluation.

### 15.11 T5-F3 — No Bypass

A permission-holder denial or unavailable determination is not bypassed or cured by favorable standing.

### 15.12 T5-F4 — Computed Statistics Excluded

Computed standing statistics classified under KD-022 3a remain UNDEFINED as records and may not be persisted or used by Sneak as permission inputs under C0. Only authoritative standing facts within the established prerequisites may participate.

### 15.13 Explicit Exclusions

KD-029 does not designate any standing source, permission or grant holder, or system; create role-to-permission mappings; authorize any currently unauthorized action; classify KD-022 3a; establish a standing-to-permission threshold, event taxonomy, or inference rule; choose between holder-internal consideration and a future KOSD mapping; define implementation, storage, schemas, contracts, APIs, or runtime mechanics; or modify any prior adopted boundary.

### 15.14 Current Authorization Posture

Adoption of KD-029 enables no action by implication. Where the prerequisites for standing-aware permission have not been established, Sneak remains closed under PA7.


## 16. Adopted Transcript Completion and Disposition Boundary

KD-030 establishes the following architectural boundary for the transition from 2c in-progress transcript capture to 1e dispositioned transcript records.

### 16.1 T6-P1 — No Silent Promotion

A 2c capture buffer becomes a 1e dispositioned record only upon an authorized completion declaration. Aging, accumulation, session end, or Sneak unilateral action do not constitute a declaration.

### 16.2 T6-P2 — Declaration Authority Is Established, Never Assumed

Completion-declaration authority and its conditions must be established by KOSD architecture or decision. Sneak does not declare completion on its own authority. Inactivity, session idle, and conversational closure are not declarations.

### 16.3 T6-P3 — Disposition Is a Status Transition, Not a Destination

Disposition is the authorized status transition from 2c to 1e. Destination, format, channel, and other mechanics remain future architecture, contract, or implementation concerns.

### 16.4 T6-P4 — Effective Disposition Requires a Designated Holder

Effective disposition requires a KOSD-designated holder for the dispositioned transcript record. Without a designated holder, a declaration is ineffective and does not create a 1e record.

### 16.5 T6-P5 — Faithful Transition

Disposition changes status, not content. Sneak does not summarize, redact, reorder, or reinterpret during the transition. Any transformation requires separate KOSD establishment and applicable KD-028 attribution; the default transition is faithful.

### 16.6 T6-P6 — 1e and 3i Remain Distinct

A 1e transcript record concerns the interaction itself. 3i Sneak action records remain a distinct UNDEFINED category and are not classified by KD-030.

### 16.7 T6-R1 — Completion-Declaration Authority

Who or what may declare completion, and under what conditions, remains to be established by a future KOSD decision or architecture.

### 16.8 T6-R2 — Designated Transcript Holder

The designated holder for dispositioned transcript records remains to be established under KD-022 P3. This holder designation is distinct from permission grant-holder designation under KD-025.

### 16.9 T6-R3 — Transcript Content Rules

Transcript content rules remain undefined under KD-021 and must exist before disposition can occur.

### 16.10 T6-F1 — No Authorized Declaration

If no authorized declaration exists, content remains 2c and remains subject to KD-022 P4. It may not be retained indefinitely as an unauthorized persistent record. No discard, archival, transfer, or other final disposition is implied until an applicable disposition authority and rule are established.

### 16.11 T6-F2 — No Designated Holder

A declaration without a designated holder is ineffective. The undeliverable buffer must not become a de facto 1e record through retention.

### 16.12 T6-F3 — Sneak Does Not Self-Declare

Sneak never self-declares completion. Idle, inactivity, and conversational closure are not declarations.

### 16.13 T6-F4 — Undeliverable Case Remains Unresolved

The undeliverable-transcript case has no authorized resolution under KD-030. No archiving, indefinite retention, or discard authority is established; the gap remains an explicit future decision item.

### 16.14 T6 Exclusions

KD-030 does not define transcript content, formats, schemas, channels, destination mechanics, retention durations, actual holder designation, grant-holder designation, completion declarer, KD-022 3c intake specifics, 3i classification, implementation, or any currently unauthorized action.

KD-030 does not modify any prior adopted boundary and does not authorize implementation.


## 17. Adopted Intake Holding, Routing, and Undeliverable-Content Boundary

KD-031 establishes the following architectural boundary for external CSR2 intake through the private `#csr2-data-intake` channel.

### 17.1 T7-P1 — Interaction-Scoped Intake Buffers

Intake items awaiting disposition are intake buffers classified as **EPHEMERAL** and therefore interaction-scoped under KD-022 P2. They are not records and are not authoritative.

### 17.2 T7-P2 — Unvetted by Default

Intake content is unvetted by default. Sneak must not present it as authoritative under B4. Presentation of intake content remains subject to applicable KD-028 attribution; unvetted does not mean unattributed.

### 17.3 T7-P3 — Holding Bounded Within the Interaction

Intake holding is bounded within the interaction. Cross-interaction persistence requires a designated authoritative holder under KD-022 P3; none is designated by KD-031. Sneak may not invent a hold bound.

### 17.4 T7-P4 — Narrow Structural Crossing

Intake disposition adopts only T6's structural crossing principles: no silent promotion; established declaration authority; disposition as status transition rather than destination; designated receiving holder; and no transition until T7-R1–T7-R3 are established.

KD-030 T6-P5's transcript-specific content-fidelity requirements are not extended to intake. Intake vetting, transformation, and content rules remain undefined.

### 17.5 T7-P5 — Undeliverable Content

For content authorized for disposition but lacking a designated holder or destination, Sneak has no discard, archival, transfer, or other final-disposition authority.

While the relevant interaction/state exists, Sneak may surface the undecidable disposition to the Kustomz owner under B8/B9 and KD-001/KD-007. This does not authorize retaining the item across interaction end merely to await a later decision. “Await” implies no persistence, callback, or retained state.

### 17.6 T7-P6 — Routing Failure Does Not Reclassify or Authorize

A failed routing attempt leaves the item in buffer classification. Sneak does not retry beyond established rules, reroute to an unestablished destination, or treat failure as disposition.

### 17.7 T7-P7 — No Cross-Interaction Persistence Without a Holder

KD-022 does not permit an intake holding to outlive the interaction absent an authoritative holder/classification.

If no authorized holder/state exists at interaction end, KD-031 establishes no authorized next state and invents none. Any mechanism permitting unresolved intake to survive the interaction requires a future Kustomz decision establishing the necessary authoritative holder/classification.

### 17.8 T7-R1 — Intake Declaration Authority

Intake declaration authority remains to be established.

### 17.9 T7-R2 — Designated Intake Holder

The designated intake holder remains to be established.

### 17.10 T7-R3 — Intake Routing and Content Rules

Intake routing/content rules, including any hold bound, remain to be established.

### 17.11 T7 Fail-Closed Posture and Exclusions

No new state category, implementation, schema, API, storage mechanism, contract, destination, actual holder, discard authority, or currently unauthorized action is established by KD-031.

Adopted capability #7 remains intact. Cross-interaction retention/disposition is not authorized where its required holder/classification has not been established.

T6 is otherwise unchanged, and all prior adopted decisions remain unchanged.

## 18. Adopted Kustomz-to-Discord Identity-Linking Boundary

KD-032 establishes the following architectural boundary for Kustomz-to-Discord identity linking.

### 18.1 IL-D — Distinct Identities and Mapping

Kustomz identity and Discord identity remain distinct identities.

“Linked” means a holder-asserted mapping between one Discord identity and one Kustomz identity. Linking does not merge the identities.

For a Sneak interaction, one Kustomz identity must be determinable for identity-bound evaluation. If it cannot be determinately resolved, the interaction fails closed for identity-bound use under B9/PA7.

### 18.2 IL-H — Link-State Holder

The existence and status of an identity link require the authoritative Kustomz-ecosystem holder designated by KD-038 following KD-025 D1.

Sneak never qualifies as the holder.

The identity-link holder is architecturally distinct from any permission-grant holder. The same underlying system may fill both roles only if each role is separately established for its applicable domain.

### 18.3 IL-L — Link-State Lifecycle

Sneak consumes link state and never authors it.

The adopted lifecycle semantics include creation, change, suspension, removal, and restoration as lifecycle edges under KD-035. Lifecycle procedures for those edges, together with validity bounds and the edge-awareness mechanism, remain unestablished until separately established.

A link change is an invalidating event for cached authorization determinations under KD-027 T3-P3.

### 18.4 IL-S — State Classification

No new state category is created.

Identity-link records remain AUTHORITATIVE under KD-022 1b. Identity-link usage reference remains EPHEMERAL under KD-022 2e. Lifecycle edges are AUTHORITATIVE holder-held state under KD-022 1b as established by KD-035 (LC-P, §21.9).

No persistence or lifecycle mechanism for 3h is established by KD-032.

### 18.5 IL-C — Identity Is Not Permission

An established link answers “who,” not “may.”

It supplies the identity term required by PA2 and PA6; the remaining authorization requirements remain independently applicable.

An absent or undeterminable link makes the identity-bound evaluation undeterminable and therefore fails closed under PA7. The link itself is not a permission grant.

### 18.6 IL-F — Freshness Interaction

Under KD-027, a link change invalidates cached authorization determinations whose identity binding depends on the changed link.

Sneak must not treat an authorization determination anchored to a superseded identity link as current where the applicable freshness boundary establishes invalidation.

### 18.7 IL-A — Attribution Interaction

KD-028 remains independent from identity authorization.

Where information is derived from an identity link and presented as derived information, applicable KD-028 attribution requirements apply.

Direct presentation of authoritative identity-link state remains subject to KD-023 B12 and the applicable authoritative source. KD-028 does not become a universal attribution regime merely because the information concerns identity linking.

### 18.8 IL-X — Cross-Interface Identity Continuity

Identity linking provides the architectural identity-continuity substrate for WEB → ANDROID → DISCORD/SNEAK, but establishes no portable work-state mechanism.

The authoritative portable work-state/context mechanism remains UNDEFINED under KD-021/KD-022 1i/3d.

### 18.9 IL-R — Prerequisites

The following remain prerequisites for dependent identity-bound operation:


- Lifecycle procedures.
- Reliable link-state resolution.
- Any conditional cross-system role establishment required by KD-026.

Adoption of KD-032 does not satisfy these prerequisites by implication.

### 18.10 IL-E — Explicit Exclusions

KD-032 does not:

- designate the actual identity-link holder;
- define link-resolution mechanics;
- define Discord-side identity assertion or verification strength;
- define a linking ceremony;
- define record metadata or schemas;
- establish broader cardinality rules beyond the one-Kustomz-identity-per-Sneak-interaction boundary;
- define Discord-side lifecycle state;
- define portable work-state mechanics;
- designate any permission or authorization holder;
- create role-to-permission mappings;
- authorize currently unauthorized actions; or
- select implementation model A/B/C.

Identity-link lifecycle-edge state remains subject to KD-022 C0: undefined lifecycle-edge state must not be persisted by Sneak pending explicit classification/establishment.

KD-032 does not modify any prior adopted boundary. It establishes no new state category, no new authority system, no competing source of truth, and no implementation authorization.

## 19. Adopted Identity-Link Resolution / Resolvability Boundary

KD-033 establishes the following architectural boundary for reliable Kustomz-to-Discord identity-link resolution.

### 19.1 RL-P — Resolution

Resolution means Sneak obtaining the designated holder's authoritative link-status determination for the addressing Discord identity, per interaction. “Reliable” means the determination is holder-sourced, unambiguous as to one Kustomz identity, and within established validity. Sneak never independently verifies the holder's determination.

### 19.2 RL-D — Determinability

Resolution is determinable only when exactly one Kustomz identity is established for the addressing Discord identity, the determination is unambiguous, and no invalidating condition applies.

No designated holder, unreachable holder, no-link/suspended/removed/unknown status, multiple candidates, stale determination, or otherwise unascertainable addressing identity makes resolution undeterminable. Undeterminable resolution fails closed for identity-bound use under B9/PA7.

### 19.3 RL-H — Holder Authority

Without a designated holder, no reliable resolution exists.

The designated holder's determination is the answer. Sneak does not corroborate, combine sources, or adjudicate against it. Holder designation and resolution are distinct establishments.

### 19.4 RL-B — Boundary Interaction

B3 grounds resolution in the designated holder. KD-022 2b caches never substitute for holder resolution.

B9 surfaces ambiguity without converting it into fact. The resolved identity supplies the identity term used by PA6 and applicable identity-bound evaluation.

Link changes invalidate applicable determinations under KD-027 T3-P3. Where validity bounds have not been established, a resolution determination is limited to the interaction's ephemeral 2e usage scope.

### 19.5 RL-F — Failure Handling

Unavailable resolution has no fallback, cross-domain inference, or stale reuse. Ambiguous resolution is not disambiguated by Sneak. Stale resolution requires re-resolution or R4/PA7.

A conflict within the holder's determination is ambiguous. Non-holder information does not override the holder's authoritative determination.

### 19.6 RL-T — Read / Authorization Separation

Identity-link resolution is a read determination, never authorization.

It satisfies none of PA2's authorization elements 1–3. Any action still requires the complete PA2 gate, including identity binding.

### 19.7 RL-S — Transient Resolution State

Resolution handling is transient only: in-flight request/response state, a parsed candidate, or a 2e identity-link usage reference.

Sneak does not persist resolution results as a record, ledger, or cross-interaction shared state. Failed resolution leaves no retained resolution state.

### 19.8 RL-X — Cross-System Boundary

Cross-system crossings defer to KD-026. KD-033 assigns no authorization-owner, grant-holder, or state-owner/executor role.

The access/query basis by which Sneak may obtain the designated holder's determination is itself a prerequisite and is not established by KD-033.

### 19.9 RL Dependencies and Undefined Prerequisites

The following remain prerequisites:

- D-RL1 — KD-038 identity-link holder designation.
- D-RL2 — Link-resolution mechanics.
- D-RL3 — Query/access basis — **SATISFIED BY KD-041**.
- D-RL4 — Link lifecycle procedures.
- D-RL5 — Validity bounds.
- D-RL6 — Any conditional KD-026 cross-system role establishment.

Resolution/query mechanics, access/query basis, validity bounds, Discord-side assertion or verification mechanics, retry/timing behavior, failure-presentation wording, and all other excluded implementation or architectural mechanics remain UNDEFINED.

No new state category, implementation, API, schema, database, Discord ceremony, permission mapping, identity-link creation/removal mechanism, portable work-state mechanism, or currently unauthorized action is established.

### 19.10 RL Boundary and Circularity Check

The resolved identity is never used to authorize or establish the authority required to resolve that identity. Sneak does not independently verify the holder through another authority and does not create a retained resolution ledger.

KD-033 does not designate an actual holder, establish the query/access contract, satisfy unresolved KD-032 prerequisites except by defining the architectural meaning of reliable resolution, or authorize dependent identity-bound actions by implication.

KD-033 does not modify any prior adopted boundary.

## 20. Adopted Identity-Link Resolution Access / Query Basis Boundary

KD-034 establishes the following architectural boundary for Sneak obtaining the designated identity-link holder's authoritative link-status determination.

### 20.1 QB-P — Decision-Derived Query Interest

Sneak's identity-link query interest is decision-derived, not grant-derived. KD-038 explicitly establishes Sneak's bounded query interest alongside the identity-link holder designation. The query interest is limited to per-interaction link-status determinations for the addressing Discord identity.

This does not authorize bulk reads, enumeration, access to records beyond the required link-status determination, permission-state access, or any authorized action.

### 20.2 QB-Q — Preconditions for Legitimate Query

No legitimate query exists until all applicable prerequisites are established: an explicit KD designates the identity-link holder; a resolvability contract exists; the holder-designation KD explicitly establishes Sneak's bounded query interest; and no applicable KOSD prohibition prevents the query.

Naming a holder alone does not silently establish query interest. KD-038 explicitly establishes Sneak's bounded query interest. Until the remaining prerequisites are satisfied, identity-link query operation remains unestablished and dependent resolution is undeterminable under RL-D/B9/PA7.

### 20.3 QB-R — Query Routed Through Authorization Boundary

The query is routed through PA1 rather than bypassing it. The relevant scope is identity-link resolution, and the query-interest element is satisfied by KD-038's explicit establishment of that interest. No applicable prohibition may be present.

The query result feeds RL-D and the PA6 identity term only. It is never itself a permission grant and does not satisfy PA2 authorization elements 1–3.

### 20.4 QB-I — Addressing Identity Input

The addressing Discord identity is forwarded as a lookup parameter from interaction context. Sneak does not invent, select, assert, or independently verify that identity for purposes of establishing link state.

If no addressing Discord identity is available, the query cannot be formed and resolution remains undeterminable under the applicable RL-D failure condition. Forwarding interaction context is not an assertion of link state.

### 20.5 QB-F — Query Failure Handling

Unavailable, inaccessible, or refused query access is treated as unavailable. Sneak does not escalate, bypass, probe, or substitute another source merely to obtain the determination.

Ambiguous or malformed query results remain undeterminable and are not repaired or disambiguated by Sneak. These outcomes follow the KD-033 RL-F fail-closed boundary.

### 20.6 QB-S — Transient Query State

Query working state is ephemeral under KD-022 2a/2e. In-flight query state and the interaction-scoped addressing identity are not persisted, ledgered, or retained as cross-interaction identity state by Sneak.

### 20.7 QB-X — Cross-System Boundary

Cross-system crossings defer to KD-026. KD-034 assigns no authorization-owner, permission-grant-holder, or state-owner/executor role and does not establish a cross-system action footprint.

### 20.8 QB Dependencies and Undefined Prerequisites

The following remain prerequisites or undefined dependencies:

- D-QB1 — Satisfied by KD-038: holder designation and explicit establishment of Sneak's bounded query interest.
- D-QB2 — Resolvability contract — **SATISFIED BY KD-041**.
- D-QB3 — Identity-link lifecycle procedures.
- D-QB4 — Validity bounds.
- D-QB5 — Any conditional KD-026 cross-system role establishment.
- D-QB6 — Platform-supplied addressing identity.

Query/resolution mechanics, query-basis implementation details, validity bounds, cross-system roles, platform presentation, Discord assertion strength, retry/timing behavior, failure wording, and all other QB-E items remain undefined.

### 20.9 QB Boundary and Authority-Leak Check

KD-034 does not allow the identity being resolved to establish the authority required to resolve itself. Query interest comes from an explicit KOSD decision, not from the resolved identity and not from the permission result being sought.

KD-038 established both the holder designation and the bounded query interest explicitly; neither is inferred from the other. Query access remains a read determination, resolution remains distinct from authorization, and no permission state is obtained through this boundary.

KD-034 does not designate the actual holder, establish implementation or API mechanics, create identity links, authorize identity-bound actions, or modify any prior adopted boundary.

## 21. Adopted Identity-Link Resolvability Contract Boundary

KD-041 establishes the following architectural contract connecting Sneak's KD-038 bounded identity-link query interest to the Kustomz Identity Engine's authoritative 1b identity-link determination.

### 21.1 RC-P — Contract Parties

- **Querier:** Sneak, acting solely on KD-038's bounded, per-interaction query interest for authoritative 1b link-status determination for the addressing Discord identity.
- **Authority:** the Kustomz Identity Engine, designated holder of KD-022 1b identity-link records under KD-038.

No other party exercises authority under this contract. No corroborating source is introduced.

### 21.2 RC-Q — Request Semantics

A contract request is:

- **Per interaction.** There is no standing, session-persistent, or pre-authorized query relationship.
- **Parameterized by the addressing Discord identity as a lookup parameter** forwarded from interaction context. Sneak does not invent, select, assert, or independently verify that identity for purposes of establishing link state. Forwarding is not assertion.
- **Scoped to a single question:** what is the holder's authoritative 1b link-status determination for this addressing Discord identity? No bulk reads, enumeration, access beyond the required determination, or permission-state access is established.
- **Routed through PA1.** KD-038's explicit bounded query interest satisfies the query-interest element.

If no addressing Discord identity is available in interaction context, no request is formed and resolution is undeterminable under the applicable RL-D/QB-I boundary.

### 21.3 RC-R — Response Semantics

The holder's authoritative determination consists of:

- **Link status** in the LC-S vocabulary: active, suspended, no-link, or unknown.
- **When status is active:** the single Kustomz identity to which the link resolves.

The determination is the answer. Sneak does not corroborate it, combine it with other sources to override it, or adjudicate against it. Non-holder information does not override the holder's determination.

This is a read determination, not authorization, and does not satisfy any PA2 authorization element.

### 21.4 RC-A — Authoritativeness Conditions

A determination counts as authoritative under this contract only when all three conditions hold:

1. **Holder-sourced** — originating from the Identity Engine's 1b records, not derived, inferred, cached, or reconstructed by Sneak.
2. **Unambiguous** — establishing exactly one Kustomz identity for the addressing Discord identity. Multiple candidates, holder-internal conflict, or otherwise ambiguous content fails this condition.
3. **Within established validity** — no validity bounds are established by KD-041; until a future decision establishes them, authoritative standing is limited to the originating interaction's established ephemeral 2e usage scope.

Sneak never independently verifies the holder's determination.

### 21.5 RC-T — Temporal Semantics

- **Per-interaction.** Each interaction obtains its own determination. Determinations are not reused across interactions as authoritative.
- **Lifecycle invalidation.** Each established lifecycle edge invalidates pre-edge determinations under the existing LC-F/T3-P3 boundary. A determination anchored before a known edge is invalid for new evaluations. Mid-interaction handling follows LC-M: no mandatory re-resolution is established solely by passage of time; a known edge renders the prior 2e usage state unusable for a new identity-bound evaluation.
- **No validity extension.** KD-041 establishes no validity duration or scope beyond the existing interaction-scoped boundary.

### 21.6 RC-F — Failure Semantics

| Contract outcome | Classification | Handling |
|---|---|---|
| Holder unreachable; query unavailable, inaccessible, or refused | Undeterminable (RL-D); unavailable (QB-F) | No escalation, bypass, probing, or substitute source |
| Ambiguous determination, including multiple candidates or holder-internal conflict | Undeterminable (RL-D, RL-F) | Not disambiguated or repaired by Sneak |
| Malformed or unusable result | QB-F; folds into RL-D/RL-F | Not repaired |
| Status unknown | Undeterminable (RL-D) | Fails closed for identity-bound use |
| No addressing identity available | RL-D failure condition (QB-I) | No request formed |

All undeterminable outcomes fail closed for identity-bound use under B9/PA7. Failed requests leave no retained resolution state. There is no fallback, cross-domain inference, or stale reuse.

### 21.7 RC-E — Explicit Exclusions

KD-041 does not establish:

- transport, endpoints, APIs, schemas, wire formats, or serialization;
- retry, timing, timeout, or failure-presentation wording;
- validity bounds;
- lifecycle procedures;
- KD-026 cross-system role establishments or action footprints;
- platform-supplied addressing identity mechanics or assertion strength;
- Discord-side verification or linking ceremony;
- any permission grant, permission mapping, or authorization;
- any new authority holder or state category; or
- implementation.

The contract is a semantic boundary connecting already-established holder authority and query interest. It does not itself authorize any identity-bound action.

### 21.8 RC-D — Dependency Consequence

KD-041 satisfies:

- **D-RL3** — the query/access basis prerequisite identified by RL-X.
- **D-QB2** — the resolvability-contract prerequisite identified by QB-Q.

The QB-Q named prerequisite set is complete at the architectural level. Legitimate query operation remains subject to the separately identified unresolved dependencies and mechanics, including D-RL2, D-RL4/D-QB3, D-RL5/D-QB4, D-RL6/D-QB5, and D-QB6.

### 21.9 RC-X — Historical and Boundary Preservation

KD-041 does not supersede, modify, or reinterpret KD-032 through KD-040.

RL-X's statement that the access/query basis was not established by KD-033 remains historically true; KD-041 is a separate establishment of that prerequisite.

QB-Q's prerequisite list is completed, not rewritten.

The resolved identity does not establish the authority required to resolve itself. Query interest remains decision-derived under KD-038, not grant-derived and not derived from the resolution result.

## 23. Adopted Identity-Link Lifecycle Boundary

KD-035 establishes the following architectural boundary for identity-link lifecycle semantics.

### 21.1 LC-D — Lifecycle State

Lifecycle state is the authoritative holder's record of a link's standing through time. KD-035 establishes lifecycle semantics; lifecycle procedures remain future architecture or contract work.

### 21.2 LC-E — Lifecycle Edges

The necessary lifecycle edges are creation, change, suspension, removal, and restoration.

Restoration is distinct from removal because suspension and removal are distinct status conditions under RL-D. No expiry edge is established; validity bounds remain undefined and expiry cannot be assumed.

### 21.3 LC-S — Lifecycle Status Vocabulary

Identity-link status is expressed as active, suspended, no-link, or unknown.

Removed and never-existed states both present as no-link at the status level. Sneak does not distinguish those histories unless a future authoritative procedure establishes a basis for doing so.

### 21.4 LC-R — Status, Edge, Resolution, and Usage Distinction

The following remain distinct:

- Link status — authoritative holder state under KD-022 1b.
- Lifecycle edge — an authoritative holder-established event affecting link status.
- Resolution — Sneak obtaining the holder's authoritative determination under KD-033.
- Usage state — Sneak's ephemeral 2e identity-link usage reference.

Resolution is not a lifecycle edge, and usage state is not the authoritative link.

### 21.5 LC-F — Lifecycle Invalidation

Each established lifecycle edge affecting authoritative link status invalidates determinations anchored to the pre-edge status under the applicable KD-027 freshness boundary.

The edge becomes effective when the authoritative holder establishes it, not when Sneak observes it. Unobserved loss of validity does not preserve a superseded determination merely because Sneak has not yet received awareness of the edge.

### 21.6 LC-M — Mid-Interaction Lifecycle Change

A Sneak interaction does not require mandatory re-resolution solely because time has passed or because a lifecycle edge might have occurred.

Where an established edge is known through an applicable established mechanism, the prior 2e usage reference is not usable for a new identity-bound evaluation. Sneak does not infer an edge, speculate about an unestablished change, or retroactively alter completed work.

### 21.7 LC-U — Unknown and Failure Conditions

Unknown, stale, conflicting, or unavailable lifecycle conditions remain within the existing KD-033 RL-D/RL-F and KD-034 QB-F fail-closed taxonomy.

Sneak does not repair, synthesize, adjudicate, or create a new failure mode for such conditions.

### 21.8 LC-A — Authoritative Lifecycle Source

Authoritative lifecycle state is held by the designated identity-link holder. The actual holder is designated by KD-038.

Sneak never determines, authors, repairs, infers, or adjudicates authoritative lifecycle state.

### 21.9 LC-P — State Classification and Persistence Boundary

Identity-link lifecycle state is authoritative holder-held state under KD-022 P1/1b. No new state category is created.

Sneak's handling remains subject to KD-022 C0/P3. KD-035 does not authorize Sneak to persist lifecycle-edge state merely because lifecycle semantics are now established.

### 21.10 LC Dependencies and Undefined Procedures

Dependent lifecycle operation still requires, as applicable:

- Lifecycle procedures.
- Validity bounds.
- An established mechanism by which relevant lifecycle-edge awareness can be obtained, where required.
- Any other applicable KD-026 cross-system role or contract prerequisite.

Lifecycle procedures, edge-awareness mechanism, validity bounds, implementation mechanics, platform presentation, retry/timing behavior, permission mappings, portable work-state, and dependent identity-bound actions remain undefined or unauthorized.

### 21.11 LC Boundary and Authority-Leak Check

KD-035 does not permit Sneak to infer authoritative lifecycle state from interaction behavior, time passage, absence of a signal, or its own observations. Invalidation does not depend on Sneak being the authority that establishes the edge.

Restoration does not authorize Sneak to infer that a prior link was restored. Removed and never-existed remain indistinguishable at the status level unless an authoritative future procedure establishes a historical distinction.

KD-035 does not designate the actual holder, establish lifecycle implementation, authorize identity-link creation/removal, establish permission mappings, create portable work-state, or authorize identity-bound actions.

KD-035 does not modify any prior adopted boundary.

## 22. Known Architectural Tensions

### 22.1 Derived Statistics

Derived statistics must remain traceable to authoritative sources.

The standard, mechanism, and evidence requirements for that traceability remain **UNDEFINED**.

KD-022 classifies derived working values as ephemeral only when they remain traceable to authoritative sources; computed member/user statistics as records remain **UNDEFINED**.

### 22.2 Cross-Interface Continuity

The adopted WEB → ANDROID → DISCORD/SNEAK continuity model requires an eventual authoritative portable work-state/context mechanism.

The portable work-state record mechanics and authoritative holder remain **UNDEFINED**.

### 22.3 Permission Grant-Holder Designation

PA3 requires permission grants to reside with the applicable authoritative holder, but the authoritative grant holder for each capability remains **UNDEFINED**.

### 22.4 Cross-System Authorization

KD-026 establishes the applicable-system framework for cross-system actions, but the footprint and role-owner for each specific action remain **UNDEFINED** until future architecture, contracts, or decisions establish them.

### 22.5 Revocation Freshness

KD-027 establishes the architectural freshness boundary, but validity-bound values, revocation-awareness channels, holder-bound ratification, and action/domain stringency remain **UNDEFINED**.

### 22.6 Derived-Information Attribution

KD-028 establishes the positive attribution and traceability standard. Remaining tensions are the application and mechanics left explicitly undefined by KD-028: provenance retention without shadow records; attribution display; description sufficiency; conflict presentation choice; reuse pressure on the KD-022 3a boundary; and any source-data freshness rules not otherwise established by applicable architecture or contracts.

### 22.7 Standing as Permission Input

KD-029 establishes the boundary for standing as a possible permission input without creating a role-to-permission mapping or authorizing any action. Standing facts remain authoritative under KD-022 1c; their authorization usability requires the KD-029 prerequisites.


### 22.8 Intake Disposition Without an Established Path

KD-031 bounds intake holdings within the interaction and prohibits cross-interaction persistence without a designated authoritative holder, but establishes no authorized next state where no holder/state exists at interaction end. The impasse is explicitly unresolved by design; any mechanism permitting unresolved intake to survive the interaction requires a future Kustomz decision establishing the necessary authoritative holder/classification. This entry records the residual; it does not authorize persistence, discard, retention, or any other disposition.


## 24. Implementation-Owned Mechanics

The following remain implementation-owned mechanics unless a later owner decision establishes otherwise:

- Hosting and runtime.
- Libraries and frameworks.
- Discord gateway mechanics.
- Secret handling.
- Presentation choices within the adopted semantic boundary.
- Caching mechanics, subject to the adopted state-classification boundary and future criteria.
- Other non-behavioral engineering details that do not alter authoritative Sneak behavior.

## 25. Architectural Boundary

KOSD owns the authoritative definition and boundaries adopted for Sneak.

Implementation may realize that architecture outside KOSD, subject to future applicable contracts, conformance requirements, authority rules, and other decisions that have not yet been established.

Creating or updating this architecture record does not authorize implementation.

## 26. Change Control

Changes to the adopted Sneak architecture shall be made through later explicit Kustomz owner decisions recorded under the adopted KOS Decision & Promotion Protocol.

This document does not supersede or independently redefine KD-021, KD-022, KD-023, KD-024, KD-025, KD-026, KD-027, KD-028, KD-029, KD-030, KD-031, KD-032, KD-033, KD-034, KD-035, KD-037, KD-038, or KD-041.
