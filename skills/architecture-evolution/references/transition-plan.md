# Transition Planning Guide

Use the sections relevant to the chosen architectural path. Show how the system works between milestones, including normal feature development during the transition.

## Record each meaningful state

| Field | Question |
| --- | --- |
| Delivered capability | What useful behavior or reduced constraint exists after this stage? |
| Routing | Which requests, tenants, jobs, or business entities use each path? |
| Authority | Which component owns each business fact and accepts writes? |
| Coexistence | Which reader/writer, contract, event, and schema versions can coexist? |
| Synchronization | How do updates, deletes, late work, and conflicts reach the other representation? |
| Verification | What proves business correctness and acceptable operation? |
| Stop and recovery | What stops, what remains in flight, and what can actually be reversed? |
| Ownership and exit | Who operates the temporary path, and what evidence allows its removal? |

## Check the chosen mechanism

- **Module boundary:** identify allowed entry points and dependency direction, existing violations, and checks that prevent new violations. Extraction into a process is a separate decision.
- **Routed replacement:** define the unit of routing and stable identity, write ownership, session/state dependencies, and what happens to in-flight work when routing changes.
- **Data movement:** define authoritative state, concurrent writes, idempotent restart, deletions, reconciliation by business key/state, and storage/capacity reserve. Two independent writes do not form an atomic change.
- **Shadow comparison:** identify which outputs can be compared, how inputs and time windows align, and how outbound actions and writes are disabled or isolated. Duplicating a request to a new system can duplicate business effects.
- **Event or API transition:** account for old producers/consumers, delayed messages, schema meaning, retries, duplicates, out-of-order delivery, and unknown completion outcomes.
- **Replacement cutover:** establish consumer readiness, updated operational ownership, comparison evidence, stop conditions, and whether new data remains readable by the old path.

## Make recovery limits visible

Distinguish traffic reversal, code rollback, data repair, replay, and restoration. For example, a new service that writes a representation the old service cannot read is not safely reversible by routing alone. A data restore can lose later writes and cannot undo an external payment or notification.

For each irreversible boundary, identify required evidence before crossing it and the repair or forward-recovery option afterward. If that option is unknown, keep the stage conditional rather than describing the roadmap as ready to execute.

## Keep the roadmap maintainable

Order work by real dependencies and state the first independently useful slice. Track temporary adapters, duplicated operation, feature work on both paths, and operating cost. Use measured or explicitly assumed ranges for duration and capacity; include a discovery step for missing inputs rather than inventing a schedule.

Compare results with the reason for changing the architecture. Fewer components or a new framework is not sufficient evidence of improvement. A useful gate might show that a representative business change can be delivered independently while correctness and recovery requirements remain satisfied.
