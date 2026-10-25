---
name: safe-migration-planning
description: Plan a database schema change or data migration with old/new version coexistence, staged rollout, backfill, monitoring, abort criteria, and explicit recovery limits. Use before migrations or when reviewing their rollout plan. Not for executing production migrations, generic schema design, or treating rollback as automatically lossless.
---

# Safe Migration Planning

Produce an executable migration plan whose transitions, verification gates, and recovery limits are explicit. Communicate in the user's language. A planning request alone does not authorize running DDL, changing data, switching traffic, or deleting old representations. If execution is separately requested, preserve that scope and authorization.

## Establish data and compatibility requirements

Inspect repository instructions, current and proposed schemas, migration files, read/write paths, background workers, contracts, deployment topology, and database engine/version. Determine data volume, skew, write rate, operational limits, backup/restore evidence, downtime tolerance, and data-loss tolerance when relevant. Mark unknown values instead of inventing them.

Identify every reader and writer, including old application instances, delayed queue messages, scheduled jobs, exports, integrations, and cached data. Name the business invariants, authoritative representation at each stage, and whether conversions are reversible or lossy. Check the actual database version's DDL locking, rewrite, transaction, and online-index behavior before promising online execution.

## Consult relevant guidance

Read applicable explanations and trade-offs from the bundled [Tip index](references/tip-index.md):

```sh
python3 "<skill-dir>/scripts/tips.py" show expand-contract throttled-backfill ddl-lock-queue replication-lag dual-write-outbox backup-restore progressive-rollout
```

Replace `<skill-dir>` with this file's directory. Verify consequential engine and service guarantees against primary documentation for the target version. Tips do not prove a particular migration is safe.

## Design compatible stages

Use expand → compatible code → migrate → switch → contract when it fits; a smaller change may need fewer stages. For each stage specify prerequisites, schema/data changes, reader/writer versions allowed, authoritative data, validation gate, and recovery action.

Build a compatibility matrix covering old and new readers/writers against each intermediate schema and data representation. Mark unsupported combinations and explain how deployment ordering or gates prevent them. Application rollback must remain compatible with data already written by the newer version; changing the binary back does not undo those writes.

For concurrent writes and backfill, specify which value wins and how writes are captured or reconciled. Dual writes require a failure/reconciliation strategy; two successful-looking calls are not an atomic guarantee. Consider conditional updates, version markers, change capture, or a brief write fence according to actual constraints. Prevent stale backfill from overwriting newer values.

For large migrations, define stable chunk boundaries, durable checkpoints, idempotent resume, batch and concurrency limits, transaction bounds, throttling signals, and handling for poison records. Account for deletes and late writes. Estimate throughput and duration as ranges under stated assumptions, including impact on locks, replicas, logs, storage, and normal traffic. Avoid OFFSET-based progress over a changing dataset without demonstrating correctness.

## Make progression, stopping, and recovery concrete

For each risky stage, specify:

- Entry evidence: compatibility checks, rehearsal, capacity reserve, restoration evidence, and responsible role where known.
- Progress signals: migrated/remaining/error counts and age, correctness mismatches, and throughput.
- Health signals: user errors and latency, lock waits, replication lag, connection/CPU/storage pressure as relevant.
- Gates: metric, baseline or threshold, observation window, and action. If values are unknown, propose labeled candidate thresholds or a measurement step; do not invent approved SLOs.
- Stop behavior: distinguish pausing the backfill, stopping new rollout, disabling new writes, and reverting reads. State whether in-flight work finishes and how progress is retained.
- Recovery boundary: what can be rolled back, which data cannot, and whether repair, forward fix, replay, or restore is required.

Explain restore consequences: restore point and expected loss window, reconciliation of writes after that point, external side effects, recovery time assumptions, and system-wide consistency. A backup's existence is not evidence of a tested restoration path; rollback is not a synonym for restore.

Delay destructive contract steps until old readers/writers are retired, delayed work is handled, reconciliation passes, and the agreed rollback window closes. Make this point of no return visible. Name any retention or deletion requirement only if supported by the user's context.

## Deliver the plan

Lead with the recommended sequence and the largest migration risk. Include the compatibility matrix, ordered stages with gates, backfill/concurrent-write strategy, monitoring and abort actions, recovery limits, and verification criteria. Link supporting files and sources. Identify blocking unknowns separately from assumptions that can be validated during rehearsal.

Scale the detail to the migration. Deliver in chat unless a saved artifact is requested. Do not claim rehearsal, data validation, or restoration succeeded unless it was actually performed.
