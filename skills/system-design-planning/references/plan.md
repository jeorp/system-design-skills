# Plan Guide

Use enough detail for the actual decision and implementation scope. These are content requirements where applicable, not mandatory headings or a fixed document template. A small feature can fit in a short answer; do not invent components, alternatives, or estimates to fill sections.

## Recommendation and context

Lead with the proposed approach, its fit for the product, and the most consequential trade-off. State the user outcome, scope, non-goals, constraints, and assumptions that could change the design. Reference existing code and contracts when planning an extension.

Express essential requirements as observable behavior or invariants. Separate user commitments from proposed targets that still need agreement. Identify decision-blocking unknowns without postponing unrelated design work.

## Options and decisions

For meaningful alternatives, compare:

| Approach | Requirements and guarantees met | Remaining risks and limits | Build and operating burden | Reversibility |
| --- | --- | --- | --- | --- |
| A feasible option | What it protects and under which conditions | Failures or workloads outside the guarantee | Supported estimates or qualitative comparisons with assumptions | What can be changed later and at what cost |

Explain the recommendation and the trigger that would justify reconsidering it. If the user has already chosen an approach, explain how to meet the goal within it and surface only material conflicts. A technology name alone is not a design decision or rationale.

## Architecture and contracts

Show a compact flow or diagram when it clarifies responsibilities and boundaries. Distinguish existing components from proposed additions. Include the relevant:

- Entry points, actors, authorization checks, and tenant or trust boundaries.
- Sources of truth, data ownership, keys, constraints, state transitions, and retention.
- API or event contracts, errors, compatibility, and transaction boundaries.
- External side effects, acknowledgement points, and ownership of retries and recovery.

Trace one representative success path and the failure paths that could break a requirement. For example, a payment webhook plan should explain what happens when the same event arrives concurrently or when a worker stops after an external effect succeeds. Use Tip IDs to connect a design mechanism to its rationale; do not substitute a list of Tips for the design.

## Delivery and validation

Break work into coherent slices in dependency order. For each significant slice, specify the behavior delivered, affected areas or interfaces, prerequisites, and observable completion criteria. Avoid guessed file paths in an unfamiliar repository and unsupported effort estimates.

Where applicable, describe schema compatibility, migration checks, rollout stages, operational signals, stop conditions, and recovery. State limits on rollback after external actions or irreversible data changes. Name the evidence required before removing the old path.

Map validation to the requirements and mechanisms. Relevant checks may cover:

- Concurrent requests, duplicated or reordered messages, lost acknowledgements, and interrupted work.
- Permission denial, tenant isolation, revocation, malformed inputs, and sensitive logging.
- Dependency timeouts, bounded retries, cancellation, overload, and backlog recovery.
- Old/new version compatibility, migration reconciliation, restore behavior, and rollout reversal.
- Representative performance or AI evaluation cases where those drive a decision.

Specify the expected outcome, environment, and limits of each material check. Distinguish planned validation from checks actually executed; do not present projections as measured results. Do not run production writes, destructive tests, or paid experiments as an implied part of planning.

## Open decisions and next steps

List only unresolved choices that affect the plan, explain their consequence, and give a recommendation or a safe way to resolve them. Identify implementation checks separately. End with the next action or a concrete choice consistent with the user's existing authorization. A completed planning-only request does not require starting implementation.
