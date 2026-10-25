# AWS Decisions

Read for an AWS workload. Use only the sections relevant to the decision and retrieve the selected Tips with `scripts/tips.py show <ids>` relative to the skill directory. The [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) provides review questions; follow the selected service's current documentation for configuration guarantees.

## Execution, data, and messaging

Start with `aws-architecture-compute`, `aws-architecture-database`, and `aws-architecture-storage`. Compare execution limits, runtime control, traffic shape, connection pressure, transaction/query scope, and data access semantics. Identify who patches, scales, backs up, and recovers each component. An existing container image alone does not justify operating a Kubernetes control plane.

Use `aws-architecture-messaging` when asynchronous work is in scope. Establish whether the requirement is buffering work, distributing notifications, or routing events, then verify acknowledgement, redelivery, ordering scope, retention, and consumer recovery for the selected service and mode. Separate a transport guarantee from the business effect of processing an event.

Use `aws-architecture-managed-ai` only when AI hosting is part of the decision. Define model control, data location, inference capacity, and operational ownership before selecting a managed API or model deployment approach.

## Resource and access boundaries

Read `aws-architecture-multi-account`, `aws-architecture-workload-identity`, and `aws-architecture-private-access` as applicable. Map account ownership and guardrails separately from grants to runtime or deployment roles. For external CI, inspect the trusted issuer, audience, subject/repository/environment conditions, and the role's effective permissions.

Inventory every API a private workload calls, including credential, image, log, secret, and data dependencies. For each destination, verify the applicable gateway or interface endpoint, DNS, route, traffic rules, endpoint policy, and identity/resource permissions. State the remaining internet path and cost implications rather than assuming one endpoint covers all dependencies.

## Availability, migration, and cost

Read `aws-architecture-ha-dr` and verify the exact RDS deployment type, engine, read-serving behavior, failover mechanism, and application reconnection path. Keep zone recovery, read scaling, regional recovery, and restoring damaged data separate. Name the recovery destination and testable restore/promotion procedure rather than treating a replica as a complete DR plan.

For data movement, use `aws-architecture-migration-cutover` to identify write ownership, replication lag, final cutover, reconciliation, and recovery after the target accepts writes.

Use `aws-architecture-cost-controls` to compare usage reduction, capacity choices, and discount commitments. Verify the scope, timing, permissions, and service coverage of any budget action; make application demand controls explicit when they are needed to bound usage.
