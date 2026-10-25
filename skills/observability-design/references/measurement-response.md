# Measurement and Response Guide

Read when specifying an indicator, alert rule, or observability acceptance check. Use only the parts needed for the workflow.

## Measurement contract

Record the user operation, good event, eligible population, measurement source/location, aggregation window, exclusions, and missing/late data policy. Distinguish attempts from logical operations. For a queued workflow, define whether the deadline is measured from acceptance, the business event, or another known point, and how overdue incomplete operations enter the indicator. Excluding unfinished work can hide a complete processing stall.

For an event-based success indicator, `SLI = good events / eligible events`. For an objective `S < 1`, the allowed bad fraction is `1 - S`, and burn rate is `observed bad fraction / (1 - S)` over a stated window. Use fractions consistently and comparable populations; time-based objectives need an appropriate time-based calculation. No traffic is not automatically perfect service, and missing telemetry is not evidence of success.

Choose objectives and alert windows from user tolerance and operational response. State whether targets are approved or proposed. Avoid fixed universal percentages or burn thresholds without those inputs.

## Signal-to-action map

| Failure | Detection | Diagnosis and first action |
| --- | --- | --- |
| Request failures or slow completion | Good/eligible outcome and latency distribution | Correlated trace/log with dependency, revision, timeout, and resource evidence |
| Accepted jobs never complete | Age of unfinished work, deadline misses, oldest backlog age | Job state/attempts, worker progress, downstream failure, and replay constraints |
| Successful jobs publish stale or partial data | Freshness and completeness at the consumer boundary | Input cutoff, publication/checkpoint versions, rejected records, reconciliation |
| Access or correctness violation | Controlled audit/business checks and invariant signals | Principal/resource decision evidence with protected content redacted |
| Telemetry stops arriving | Pipeline health, expected heartbeat or independent probe | Collection/export health and an alternate service check; do not silently mark healthy |

Adapt signals to the system. CPU alone does not establish user impact, and a successful synthetic probe does not cover every tenant or workflow.

## Alert record and acceptance

Specify query/metric, population, threshold, evaluation windows, minimum-volume behavior, absent-data handling, severity, route/owner, grouping, first action, and recovery behavior. A runbook should state how to confirm impact, distinguish likely causes, and choose a safe mitigation, with escalation when the evidence is insufficient.

Verify an alert from emitted signal through rule evaluation and test routing, not only by inspecting its configuration. Check legitimate healthy behavior, failure detection delay, noise, and correlation across request/job boundaries. State which channels were exercised and which remain untested. Production faults or actual pages require their own authorized scope.

## Primary guidance

- [Google SRE: Implementing SLOs](https://sre.google/workbook/implementing-slos/) for user-centered indicators, objectives, and error-budget decisions.
- [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/) for signal concepts; consult the actual instrumentation and backend versions for implementation guarantees.
