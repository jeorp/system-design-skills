# Design Questions by Path

Use the sections that affect the proposed design. Each question should lead to a concrete mechanism, boundary, or validation step; it is not a checklist of mandatory infrastructure.

## Writes, payments, and asynchronous side effects

- Which invariant must be atomic, and which database constraint or conditional write enforces it under concurrency? A read-before-write check alone does not close the race.
- Define an idempotency key's scope, request matching, concurrent claims, result persistence, and expiry. What happens after an external action succeeds but before its result is stored?
- If a database write and message publication must agree, describe how pending work is durably recorded and retried. Consumers still need to handle duplicate delivery.
- Define event identity, ordering needs, poison-message handling, and compensation for operations that cannot be rolled back.

Relevant Tips: `database-constraints-races`, `conditional-state-transitions`, `idempotency-keys`, `dual-write-outbox`, `exactly-once-boundary`, `saga`, `webhook-verification`.

## APIs, data representation, and authorization

- State who may act on which object or tenant, where the check occurs, and how revocation affects cached permissions and in-flight work.
- Define money, large IDs, timestamps, omitted fields versus null, pagination, and stable errors where they cross a boundary. Preserve existing client compatibility.
- Bound request size and total work, not only request frequency. If fetching user-provided URLs, define allowed destinations and redirects.

Relevant Tips: `object-authorization`, `permission-consistency`, `floating-point-money`, `json-number-precision`, `timestamps-business-dates`, `patch-field-presence`, `cursor-pagination`, `api-error-contract`, `request-work-limits`, `ssrf`.

## Downstream dependencies and queues

- Allocate an end-to-end deadline. Which work is cancelled, which continues, and who owns retries? Account for retries at other layers.
- Decide which failures are retryable, how retries are bounded, and how to avoid synchronized retries or replaying non-idempotent operations.
- Define concurrency limits, rejection behavior, maximum backlog age, and recovery behavior when arrivals exceed processing capacity.

Relevant Tips: `timeout-budget`, `request-cancellation`, `retry-amplification`, `load-shedding`, `queue-backlog`, `metastable-failure`.

## Storage, caching, and capacity

- Derive queries and indexes from access patterns, data size, and skew. State the consistency needed after writes and whether replica lag or stale cache entries are acceptable.
- Explain invalidation, hot-key behavior, cache misses during an outage, and what happens when a popular key expires.
- Estimate configured connection ceilings and concurrency with units and assumptions. Identify which measurements or representative workload would validate them.

Relevant Tips: `composite-index-order`, `n-plus-one`, `replication-lag`, `hot-keys`, `cache-stampede`, `cache-down`, `connection-pool-math`, `littles-law`, `load-test-realism`.

## Release, migration, and recovery

- Describe compatibility while old and new applications coexist. Separate additive schema changes, resumable backfill, reader/writer transitions, and removal of the old representation.
- Identify locks, throttling, progress checkpoints, validation of migrated data, and when old data ceases to be usable for rollback.
- Define rollout stop conditions, shutdown behavior for in-flight work, recovery objectives, and evidence that a restore can meet them.

Relevant Tips: `expand-contract`, `throttled-backfill`, `ddl-lock-queue`, `progressive-rollout`, `graceful-shutdown`, `backup-restore`, `iac-replacement`.

## Operations and AI-dependent behavior

- Name signals that detect broken business invariants, dependency failure, and growing backlog. Connect alerts to an action, keep metric labels bounded, and avoid logging secrets or complete sensitive payloads.
- For LLM or retrieval paths, apply permissions before exposing retrieved content, treat external text as untrusted, define output validation and tool authority, and specify latency, cost, fallback, and quality evaluation boundaries.

Relevant Tips: `slo-burn-rate`, `trace-propagation`, `metric-cardinality`, `safe-structured-logs`, `rag-retrieval-first`, `filtered-vector-search`, `prompt-injection`, `llm-evals`, `llm-fallback`.
