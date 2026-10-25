---
name: architecture-change-review
description: Review a PR or diff for system-level effects on consistency, compatibility, load, and authorization by tracing changed code and adjacent execution paths. Use for architectural risk review of a concrete change. Not for broad existing-system assessments, style-only code review, or designing a feature without a diff.
---

# Architecture Change Review

Identify actionable architectural regressions introduced or exposed by a concrete change. Ground findings in the diff and the surrounding system. Communicate in the user's language. A review alone does not authorize implementation edits, deployments, or posting review comments to an external service.

## Establish the comparison

Read repository instructions and determine the requested PR, base and head revisions, or local change set. Preserve local work. Inspect the actual diff, changed tests, schemas, contracts, configuration, and deployment changes. State the comparison and coverage; if the base is ambiguous and changes the conclusion, resolve it before attributing regressions.

Understand the intended new behavior and existing invariants. Distinguish newly introduced risks from pre-existing issues. An unchanged weakness can be relevant when the change makes it reachable or increases its impact; explain that causal connection rather than reporting unrelated debt.

## Trace the effects beyond changed lines

Follow changed entry points through callers, authorization, storage, caches, events, background workers, external effects, and responses. Inspect shared guards and consumers before claiming a missing protection. Include old and new versions, delayed jobs, and retained data where they can coexist.

| Dimension | Questions to resolve from evidence |
| --- | --- |
| Consistency | Do transaction or ownership boundaries change? Can retries, concurrent requests, reordered events, or partial completion lose or duplicate effects? |
| Compatibility | Can existing clients, workers, readers, and writers handle the new API, event, schema, defaults, and missing or null fields during rollout and rollback? |
| Load | Does one request now fan out, hold locks longer, allocate more memory, create more connections, or amplify retries? Are work and backlog bounded? |
| Permissions | Does each path enforce the principal's access to the resource and tenant? Do caches, jobs, alternate routes, or revocation change that guarantee? |
| Operations | Do deployment order, configuration defaults, shutdown, observability, and recovery still support the intended behavior? |

Use only dimensions material to the change. Quantify load changes using evidenced inputs or explicit assumptions; do not label a theoretical scaling concern a demonstrated regression.

## Use supporting knowledge selectively

Select relevant IDs from the bundled [Tip index](references/tip-index.md), then read explanations, applicability, and trade-offs:

```sh
python3 "<skill-dir>/scripts/tips.py" show dual-write-outbox contract-testing expand-contract object-authorization permission-consistency request-work-limits connection-pool-math
```

Replace `<skill-dir>` with this file's directory. Tips are supporting material, not a mandatory architecture checklist. Verify version-dependent guarantees and service behavior against the target version and primary sources when they drive a finding. Do not infer a defect from a Tip title or an unsuccessful text search.

## Validate and prioritize findings

For each candidate, establish: change → reachable trigger → affected path → violated invariant or operational constraint → user/system impact. Look for counterevidence such as a shared constraint, gateway guard, bounded input, rollout gate, or existing test. Drop findings whose conditions cannot plausibly occur; keep important unknowns as investigation questions rather than confirmed defects.

Run focused, safely contained checks when useful and authorized. Do not turn review into a production experiment. Report unexecuted checks honestly. A local reproduction can establish a bug without proving that production has already suffered it.

Keep priority separate from confidence and fix effort:

- P0: demonstrated conditions warrant immediate containment, such as ongoing severe corruption or widespread exposure; avoid speculative P0s.
- P1: a plausible reachable change creates serious correctness, access, availability, or rollout risk that should be addressed before release.
- P2: a material but narrower or conditional regression should be scheduled for correction.
- P3: a lower-impact actionable issue with a concrete consequence; omit style preferences and generic best practices.

## Present a review the author can act on

Lead with findings in priority order. For each, give a concise title, a precise changed-line location where possible, the triggering conditions, causal explanation, impact, evidence confidence, and a focused mitigation or verification criterion. Use the requested review format if one is specified. Place evidence from surrounding code alongside the relevant finding; do not pretend an unchanged line is part of the diff.

Separate material unanswered questions and residual coverage limits from confirmed findings. When none are found, say that explicitly and state what was reviewed and what was not verified. Do not invent findings or certify the whole system as safe. Do not publish comments or modify the PR solely because a review was requested.
