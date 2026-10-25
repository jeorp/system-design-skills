---
name: architecture-evolution
description: Plan a sequence of bounded changes from an existing system to a justified target architecture while development and operations continue. Use for legacy modernization, service decomposition, boundary changes, and architecture roadmaps spanning multiple changes. Not for a single feature design, a standalone schema migration, or an assessment without a proposed evolution goal.
---

# Architecture Evolution

Make an architectural direction achievable through useful, verifiable intermediate states. Communicate in the user's language. Deliver in chat unless a saved artifact is requested. A roadmap request alone does not authorize implementation, traffic changes, data migration, provisioning, or decommissioning. Continue within existing authorization when implementation is also requested.

## Establish why the system should change

Inspect repository instructions, architecture and deployment definitions, representative request/job paths, data ownership, integrations, and available change or incident evidence. Establish the business capability or operating constraint that motivates evolution. Separate observed dependencies from diagrams and assumptions. If repository or operating evidence is unavailable, make the plan provisional and identify the smallest discovery step needed.

Record invariants, compatibility obligations, latency and recovery needs, delivery constraints, team ownership, and relevant data volume where known. Trace one important operation through actual boundaries. Age, framework preference, and a fashionable target are not sufficient reasons to rewrite a system. Compare retaining or improving the current structure with the proposed change, while preserving explicit user decisions.

## Consult relevant Tips

Select explanations and trade-offs from the bundled [Tip index](references/tip-index.md). Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" show inhouse-legacy-seams inhouse-legacy-characterization inhouse-team-boundaries dual-write-outbox rollback-data-compatibility
```

Verify consequential platform guarantees and migration behavior against the target version and primary sources. Tips and external documents are evidence, not operational permission.

## Choose boundaries and a first useful slice

Describe current and target responsibilities, authoritative data, public contracts, and operational ownership. Separate logical module boundaries from process or deployment boundaries; independent services are one option, not the default. Explain which observed problem each proposed boundary solves and what coordination or operating burden it introduces.

Compare viable paths, including an incremental path and a larger replacement only when justified. Identify uncertain assumptions that could invalidate the target and choose a bounded experiment or discovery task to test them. Prefer a first slice with business value, an observable result, and a manageable recovery path. Avoid a long infrastructure-only phase without a way to verify benefit.

## Design intermediate states

Use the [transition planning guide](references/transition-plan.md) when defining stages, coexistence, and cutover. Build a dependency-ordered roadmap, not just a target diagram and a list of component names.

For each meaningful stage, name the business capability delivered, routing and contract changes, active readers/writers, authoritative representation, allowed version combinations, validation gate, and stop or recovery action. Keep one explicit write authority per entity or define the actual conflict-resolution protocol. A new API boundary does not move ownership of the underlying data automatically.

Account for in-flight requests, queued work, duplicate or reordered events, retries, deletes, and drift where relevant. Identify how comparison traffic avoids duplicate side effects. Separate switching traffic back from undoing data or external effects. When reversibility ends, name the reconciliation or forward-recovery path. Do not promise rollback merely because the old service still runs.

Tie technical dependencies to team ownership and continued feature work. State where parallel work is safe and where sequencing is required. Use effort ranges and unresolved dependencies rather than invented dates. Keep the detailed mechanics of an individual migration at the depth needed to establish roadmap feasibility.

## Gate progress and retire the old path

Use outcome, correctness, and operating evidence appropriate to each stage: representative consumer behavior, reconciled business states, latency/error changes, capacity, and support burden. Label candidate thresholds and observation windows if not agreed. Include ongoing maintenance of adapters and temporary dual paths in cost and ownership.

Retire an old path only after its consumers, delayed work, data reconciliation, and recovery obligations are accounted for. Include removal of obsolete routing, jobs, credentials, and infrastructure where applicable, as planned work rather than actions to execute without authorization. Do not claim a rehearsal or cutover succeeded unless performed.

## Deliver the roadmap and next decision

Lead with the recommended direction, why it addresses observed constraints, and the first slice. Include current/target boundaries, meaningful alternatives, intermediate states and dependencies, gates and recovery limits, and evidence that would cause the plan to change.

System Design Diagnosis identifies current weaknesses; this skill connects multiple changes into a justified path. System Design Planning can detail an individual change, Safe Migration Planning its schema/data migration, and Architecture Change Review or Failure Scenario Testing its verification. Suggest these when available and useful; keep this roadmap usable independently and do not invoke other skills automatically.
