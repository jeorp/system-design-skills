---
name: observability-design
description: Design user-centered SLIs/SLOs, logs, metrics, traces, alerts, and response evidence for a service or workflow. Use when defining instrumentation, monitoring, or diagnosability acceptance criteria. Not for live incident command, a generic dashboard inventory, or an unrequested monitoring-provider migration.
---

# Observability Design

Make important failures detectable and explainable, with signals that support an operational decision. Communicate in the user's language and deliver in chat unless a saved artifact is requested. A design request alone does not authorize installing agents, exporting telemetry, modifying alerts, or paging people. Continue within existing authorization when implementation is requested.

## Trace the user outcome and existing visibility

Inspect repository instructions, key request/job flows, telemetry, dashboards, alert rules, deployment metadata, runbooks, and available incident evidence. Follow an important operation through dependencies, persistence, queues, external effects, and completion. Identify what operators can actually distinguish today; the existence of a dashboard or instrumentation library is not evidence of useful coverage.

Establish critical user journeys, correctness and timeliness requirements, service ownership, response coverage, dependencies, and known blind spots. Separate user requirements and measured baselines from assumptions. Preserve the existing stack unless a demonstrated limitation justifies a change. Do not assign an arbitrary SLO or invent an on-call team.

## Define indicators and objectives precisely

Select relevant explanations from the bundled [Tip index](references/tip-index.md). Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" show slo-burn-rate trace-propagation metric-cardinality safe-structured-logs inhouse-observability-acceptance etl-freshness-completeness
```

For each critical journey, define good/eligible events or a precise time-based indicator, measurement point, aggregation/window, exclusions, and missing-data behavior. Count asynchronous success at the business completion boundary, not only at enqueue or HTTP acceptance. Track correctness, freshness, or completeness alongside availability/latency when success responses can conceal a failed outcome.

Choose candidate objectives from user needs, baseline evidence, and response capability. Distinguish an SLO from an external SLA and an agreed target from a proposal. Explain what the error budget measures and how it would change decisions; do not promise 100% reliability. Use the [measurement and response guide](references/measurement-response.md) for formulas, alert behavior, and acceptance checks.

## Connect signals to investigation questions

Map each material failure mode to detection, diagnosis, and response. Use bounded metrics for aggregate health and resource pressure, structured logs for relevant state transitions, and traces for a request/job's causal path. Include business operation IDs and release/configuration identifiers where useful, respecting privacy and cardinality. Do not put raw user IDs, request IDs, or unbounded URLs in metric labels.

Propagate trace context through HTTP and messaging where supported, including retries and job execution. Establish how asynchronous work is correlated; a shared trace ID alone does not capture every causal relationship or prove completion. Distinguish retries, attempts, and logical operations in metrics so denominators and success rates remain meaningful.

Define redaction/allowlisting, access, retention, and sampling for telemetry. Avoid logging secrets, full request bodies, unrestricted prompts, or retrieved private documents by default. Sampling affects what an absent trace or log can prove; do not use sampled traces as an exhaustive correctness ledger. Keep durable business/audit records where the invariant requires them.

Verify SDK, collector, backend, and semantic-convention behavior for actual versions against primary documentation. Plan telemetry volume, bounded label sets, collection overhead, and failure behavior. Telemetry export failure should have explicit buffering/drop limits rather than silently exhausting application resources.

## Design alerts people can act on

Tie paging to actionable user impact or imminent exhaustion needing immediate intervention; route slower, nonurgent conditions to an appropriate ticket or review path. Define metric/query, threshold status, time windows, minimum traffic or low-volume behavior, missing-data handling, owner/route, and the first useful action. Include dependency and collection failures where they could hide a service failure.

Use error-budget burn alerts where an agreed event-based SLO makes them meaningful, with windows chosen for the response needs. Complement them with preventive capacity, stalled-work, correctness, or freshness signals where waiting for user-visible errors would be too late. Avoid one page per unhealthy component when a shared incident can be grouped without concealing independent failures.

## Prove detection and diagnosis

Define authorized, contained checks for a known failed operation, delayed job, dependency timeout, and telemetry gap as relevant. Verify the signal arrives, correlates to the affected operation/release, triggers the intended rule, and gives enough evidence for the first response. Exercise rule evaluation and routing through a test destination when appropriate; do not send real pages without authorization. Label proposed checks separately from executed results.

Deliver the recommended measurement points, SLI/SLO definitions, signal-to-failure mapping, alert/response rules, telemetry constraints, and staged acceptance checks. Lead with the highest-impact blind spot and what the plan will make observable. Incident Learning analyzes a past event; this skill designs evidence for future detection and diagnosis and remains usable independently.
