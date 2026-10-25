---
name: data-pipeline-design
description: Design ETL, ELT, batch, streaming, and CDC pipelines with explicit data meaning, incremental capture, replay, publication, and reconciliation contracts. Use for analytics ingestion, data synchronization, pipeline redesign, and backfill design. Not for a standalone application schema migration, one-off data cleaning, or unrequested production pipeline execution.
---

# Data Pipeline Design

Design how data becomes a trustworthy, usable downstream representation, including partial failure and reprocessing. Communicate in the user's language; deliver in chat unless a saved artifact is requested. Design alone does not authorize connecting to private sources, exporting data, creating infrastructure, or running backfills. Continue within existing implementation authorization.

## Establish meaning before choosing machinery

Inspect repository instructions, source and destination schemas, jobs, orchestration, existing checkpoints, transformation logic, consumer queries, access controls, and operating evidence. Trace a representative business entity through extraction, transformation, publication, and consumption. Separate observed properties from assumptions.

Establish consumers, decisions supported, source of truth, row grain, business keys, units/currency, time zones, event and business dates, historical semantics, updates, and deletes. Define freshness, completeness, reconciliation, retention, and access requirements where known. A successful job is not evidence that its output is timely or complete. Mark unknown volumes, skew, lateness, and recovery goals instead of inventing them.

## Select capture and processing boundaries

Consult applicable explanations and trade-offs in the bundled [Tip index](references/tip-index.md). Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" show etl-elt-data-boundaries etl-incremental-cursor etl-cdc-snapshot-handoff etl-idempotent-publication etl-grain-reconciliation etl-backfill-isolation
```

Compare full snapshots, polling, CDC, and event ingestion using source capabilities, required freshness, deletes, ordering, volume, and operating burden. Choose ETL or ELT by where sensitive raw data may reside and who can access each representation, as well as transformation cost and maintainability. A queue or streaming framework is not automatically required.

For polling, define a stable cursor and tie handling, transaction visibility, updates, deletes, pagination, and durable progress. Updated-at ordering is not necessarily commit ordering; a timestamp plus ID handles ties but does not alone prevent missed late commits. Use a justified overlap/deduplication strategy, stronger capture mechanism, or reconciliation with explicit limits.

For CDC, connect the initial snapshot to a consistent log position, establish acknowledgment/checkpoint rules, and handle duplicate delivery, schema changes, source restarts, and expired log history. Monitor source log retention and disk pressure when consumers lag. Verify actual connector and source-version guarantees against primary documentation; do not infer end-to-end exactly-once effects from a transport claim.

## Make replay and publication correct

Read the [data contract and recovery guide](references/contracts-recovery.md) when detailing checkpoints, publication, or backfills. Define input identity/version, transformation version, processing interval, target grain, output keys, and the unit consumers observe as complete. Separate extracting data from publishing a valid result.

Specify what happens after output is written but before progress is recorded, and after progress is recorded but before output is durable. Use atomic commitment where actually supported, or an idempotent replay/reconciliation protocol. An upsert is not sufficient if keys are wrong, aggregation adds twice, deletes are omitted, or stale data can overwrite new values.

For event-time processing, distinguish arrival time, event time, and business period. Specify lateness, watermarks where applicable, correction/retraction policy, and when outputs are provisional or final. For historical dimensions, decide whether reports use attributes as they were at the event or as they are now.

Bound backfills by explicit source versions or intervals, checkpoints, capacity, and concurrency. Control conflicts with live publication so an older backfill cannot replace newer results. Define bad-record quarantine with visibility and repair; silently dropping invalid rows does not meet completeness. Keep raw retention and replay plans consistent with deletion and access obligations.

## Validate data and operation

Define reconciliation at the business grain: key uniqueness, required relationships, missing/extra entities, state transitions, aggregates by meaningful segments, and aligned source/destination cutoffs. Equal row counts do not prove equal data. Account for expected lag and legitimate transformations before calling differences defects.

Monitor job status, end-to-end data freshness, completeness, lag/backlog, quarantine, reconciliation mismatches, source pressure, and storage/cost where relevant. Define pause, resume, replay, and repair conditions with owners and observation windows. Treat unknown thresholds as candidates to validate. Include access, deletion propagation, and recovery checks in completion criteria.

## Deliver the pipeline design

Lead with the recommended flow and the largest correctness risk. Include source/consumer contracts, capture choice and alternatives, transformation/publication semantics, replay and backfill behavior, reconciliation, observability, and a staged verification plan. Distinguish measured behavior from proposed checks and estimates.

Safe Migration Planning focuses on changing a schema or moving data through a cutover; this skill focuses on ongoing data movement and its recovery semantics. Keep the design usable independently and suggest adjacent skills only when useful.
