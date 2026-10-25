---
name: capacity-planning
description: Estimate system capacity and bottlenecks under growth, peak traffic, backlog recovery, and component failure using explicit assumptions. Use for questions such as 10x users, DB connection budgets, worker concurrency, queue drain time, and failure headroom. Not for unrequested load-test execution or presenting estimates as measured limits.
---

# Capacity Planning

Build a transparent estimate that identifies what constrains growth and what should be measured next. Communicate in the user's language. Keep assumptions, measurements, configured limits, and estimates distinct. A capacity question alone does not authorize provisioning, paid experiments, or load tests against shared systems.

## Translate the growth question into workload

Inspect repository instructions, request paths, deployment/autoscaling configuration, connection pools, workers, queues, caches, and available traffic evidence. Establish the current and target workload, time horizon, latency/error goals, resource limits, and relevant failure scenario. Ask only for unknowns that materially change the result; otherwise use labeled ranges.

Do not multiply registered users by ten and call the result RPS. Model active fraction, actions per active user, peak window, request mix, reads/writes, fan-out, retries, cache misses, job production, data size, retention, and skew as relevant. Distinguish logical requests from attempts and downstream operations. State which quantities scale with users and which may change nonlinearly.

Use a compact input table with value/range, units, source/time window, and status (measured, configured, assumed, or derived). Do not fabricate measurements or prices.

## Use the relevant capacity model

Consult the bundled [Tip index](references/tip-index.md) and selected explanations:

```sh
python3 "<skill-dir>/scripts/tips.py" show littles-law connection-pool-math queue-backlog utilization-queueing zone-headroom autoscaling-lag load-test-realism hot-keys
```

Replace `<skill-dir>` with this file's directory. Verify current service limits, instance specifications, and prices against primary sources for the actual configuration when needed. Tips and provider maxima are not benchmarks of the user's workload.

Use only applicable models and show units:

| Quantity | Model and limits |
| --- | --- |
| Peak logical arrival rate | Active users × actions/user in the window × requests/action ÷ window seconds; add an explicit burst factor only if not already included |
| Downstream operations | Sum each request class's arrival rate × fan-out × expected attempts, with cache misses where applicable; nested retry ceilings multiply but are not expected retry rates |
| Mean work in the system | L = λ × W for a stable system with matching boundaries and mean residence time; p99 latency is not a substitute for mean W |
| DB connection ceiling | Sum instances × processes/instance × pool limit/process across services, replicas of the application, workers, and deployment surge, plus admin/migration reserve; compare each DB endpoint with its usable budget |
| Worker service capacity | Approximate μ = effective concurrent slots ÷ mean service seconds/job for the measured job mix; account for downstream limits and contention |
| Backlog growth and drain | Growth ≈ max(0, λ − μ) × duration; drain time ≈ backlog ÷ (μ − λ) only when μ > λ and new arrivals continue at λ |
| Failure utilization | Demand ÷ surviving sustainable capacity; for N identical equally loaded units losing k, utilization scales by N/(N − k), assuming traffic can redistribute |
| Stored data | Ingested records/time × bytes/record × retention, plus indexes, replication, logs, temporary migration space, and measured overhead where relevant |

Pool ceilings are not active DB demand; connection pooling or proxies can change client-to-server mapping. Mean concurrency is not a safe concurrency limit. Throughput must still meet the latency/error target; saturation, lock contention, and tail latency can make theoretical maxima unusable.

Do not assume linear scaling or evenly distributed keys, tenants, shards, or availability zones. Describe the limiting shared dependency. Distinguish a configured quota from measured sustainable capacity and a desired utilization target from an approved SLO.

## Compare operating scenarios and uncertainty

Estimate baseline, target peak, and the relevant degraded/recovery case. Include deployment surge, cold cache, autoscaling delay, retries, backlog replay, and maintenance reserve where they can matter. Reserve for failure before declaring normal-operation headroom available. Surviving nodes are useful only if dependencies, placement, quotas, and routing also survive.

Show bottlenecks and margin for each scenario. Vary the most influential uncertain inputs to show when the recommendation changes. Avoid false precision; a range with explicit assumptions is more useful than an exact unsupported instance count. If μ is no greater than λ, report that the queue cannot drain under that scenario rather than giving a finite recovery time.

## Recommend action and validation

Lead with the likely first constraint and the conditions behind that conclusion. Include the input table, formulas with substituted values, scenario results, confidence/unknowns, and the most useful next measurements. Compare tuning, bounding work, backpressure, caching, and added capacity only where they address the limiting resource.

Propose a representative validation experiment with request mix, data/skew, warm/cold state, duration, success metrics, and abort conditions. Do not run it solely because it is in the plan. State the operating threshold or measured evidence that would trigger a capacity change; do not claim an estimated plan has been load-tested.
