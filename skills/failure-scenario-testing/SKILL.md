---
name: failure-scenario-testing
description: Design and, when needed, implement tests for retries, races, timeouts, partial failures, and interrupted work in an existing feature. Use when the happy path works but failure behavior or recovery is uncertain. Not for routine happy-path unit tests, capacity estimates, or unrequested production chaos experiments.
---

# Failure Scenario Testing

Turn concerns about how a feature breaks into reproducible scenarios with observable correctness and recovery criteria. Communicate in the user's language. Match the requested scope: case design alone stays a plan; a request to verify failure behavior can include focused local test implementation and execution.

## Understand the invariant and execution path

Read repository instructions, the relevant implementation, schemas, dependency configuration, and existing tests. Trace input → authorization → state changes → external effects → acknowledgement → retry or recovery. Identify the business invariant, such as one charge per order, no lost accepted job, or no cross-tenant result.

Locate transaction boundaries, deduplication records and retention, queue acknowledgement or lease boundaries, deadlines, cancellation, shutdown handling, and recovery workers. Check protections in shared layers before concluding they are absent. Distinguish confirmed behavior from assumptions; ask only for missing information that changes the test or expected outcome.

## Select scenarios from actual failure windows

Use the bundled [Tip index](references/tip-index.md) and read only relevant explanations and trade-offs:

```sh
python3 "<skill-dir>/scripts/tips.py" show idempotency-keys database-constraints-races timeout-budget request-cancellation dual-write-outbox graceful-shutdown database-integration-tests
```

Replace `<skill-dir>` with the directory containing this file. Tips are guidance, not requirements. Verify consequential version-specific behavior against the target version and primary documentation; retain uncertainty when verification is unavailable.

Choose applicable cases rather than running an exhaustive catalog:

| Failure window | Evidence the test should capture |
| --- | --- |
| Duplicate delivery or retry after an acknowledgement is lost | External effect count, durable result, response to the retry, deduplication scope and expiry |
| Concurrent requests for the same state or resource | Final invariant, winning and losing outcomes, transaction or constraint enforcement |
| Timeout before or after a dependency commits | Whether the outcome is unknown, whether work continues, reconciliation and retry behavior |
| Crash between durable state, external effect, and acknowledgement | What survives restart, how unfinished work is found, duplicate or lost effects |
| Lease expiry or redelivery while an earlier worker remains active | Whether both workers can commit, stale-worker protection, final state |
| Dependency outage and subsequent recovery | Bounded attempts, deadlines, resource release, backlog recovery without an uncontrolled burst |
| Out-of-order events or permission changes during work | Valid transitions and authorization at the point where the effect occurs |

For each selected case specify the initial state, exact fault/interleaving, action, expected durable state and side effects, expected response, recovery condition, and observation method. Give cases stable IDs. Prioritize irreversible effects, data loss, permission violations, and plausible high-impact windows.

## Implement reproducible checks where needed

Use the existing test framework and the smallest environment that preserves the behavior being tested. For transaction isolation, constraints, locking, or persistence across restarts, use a disposable real database or appropriate integration environment; a mocked repository does not establish database guarantees. For external services, a controlled fake can record whether an effect occurred before dropping its response; state which real-service properties remain unverified.

Control interleavings with barriers, hooks, fake clocks, or explicit signals instead of arbitrary sleeps. Give waits and retries finite bounds. Preserve durable test state across the simulated crash where recovery depends on it. Assert business outcomes and effect counts, not merely the exception type or log text. Check recovery and cleanup as well as initial rejection.

Use isolated fixtures and bounded data. Inspect destinations and side effects before execution. A local verification request does not authorize production fault injection, live charges, messages to people, or shared-environment load tests. Honor already established authorization without adding redundant approval steps. If an environment is unavailable, implement useful checks where possible and clearly mark cases that were not run.

If a test exposes a defect, preserve the reproduction and explain the failure. Change production implementation only when fixes are also within the user's requested scope. Do not weaken the expected invariant to make a test pass.

## Deliver the result

Lead with the most important failure found or the confidence gained. Provide the selected case matrix, evidence or test links, commands and results for checks actually run, and unresolved risks. Separate passed, failed, and unexecuted cases. Explain limitations such as mocked dependencies or untested crash persistence; passing selected scenarios is not proof that every failure mode is safe.
