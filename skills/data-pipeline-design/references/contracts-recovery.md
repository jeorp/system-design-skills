# Data Contracts and Recovery

Use the relevant sections to make publication, replay, and validation executable. Do not require every field for a small batch import.

## Contract at each boundary

| Field | Decision |
| --- | --- |
| Meaning | Row grain, business identity, units, null/missing meanings, and valid states |
| Time | Event, update, arrival, and business time; time zone; interval endpoints |
| Ownership | Authoritative source, producer/consumer owners, permitted readers |
| Change | Updates, deletions, corrections, historical attributes, schema and semantic evolution |
| Capture | Snapshot identity, cursor/log position, ordering scope, retained replay window |
| Publication | Output key/version, atomic visibility unit, provisional/final marker |
| Acceptance | Freshness and completeness definitions, reconciliation cutoffs and tolerances |

Version meaning as well as field types. A currency or grain change can break a consumer while the schema remains valid. Record compatible consumers, rollout order, and handling of retained old events.

## Reason through crash windows

For each stage, name durable input, output, and progress state. Ask what replay does after a crash before/after each durable write. Avoid advancing progress ahead of recoverable output. If publication and progress cannot commit together, explain how repeat processing is harmless and how incomplete publication is detected.

For a partition replacement, prepare a complete version and publish through an atomic mechanism only when supported by the destination. For incremental writes, define stable keys, version/conflict checks, tombstones, and how additive aggregates are recomputed or deduplicated. Include external notifications or downstream triggers in the effect boundary.

## Backfill and repair

Fix the source snapshot or document how changing inputs are handled. Pin the transformation version and the business interval being repaired. Define a publication fence, generation comparison, or an explicit pause/reconciliation protocol for overlap with live processing. Rate limiting alone does not prevent stale publication.

Retain progress and rejected-record reasons without storing unnecessary sensitive payloads. State how schema-invalid records, expired CDC history, or deleted source data affect replay. If the original input is unavailable, identify reconstruction limits rather than promising full recovery.

Reconcile business keys, states, and totals at aligned cutoffs. Check segmented results so one tenant's deficit cannot be hidden by another's surplus. Record expected differences, tolerance rationale, and the action on unexplained discrepancies.

## Primary documentation

[PostgreSQL logical decoding concepts](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html) illustrates snapshot/log coordination, duplicate delivery after recovery, and replication-slot retention. Consult documentation for the actual source, connector, sink, and versions before assigning those guarantees to a pipeline.
