# Azure Decisions

Read for an Azure workload. Use only the sections relevant to the decision and retrieve the selected Tips with `scripts/tips.py show <ids>` relative to the skill directory. The [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) provides review questions; verify the current service, tier, region, and configuration before relying on a guarantee.

## Execution, data, and messaging

Start with `azure-architecture-compute`, `azure-architecture-database`, and `azure-architecture-storage`. Compare execution model, runtime control, scale and connection behavior, SQL compatibility, access patterns, transaction or partition scope, and object/file/block access. Record the remaining patching, scaling, backup, and recovery responsibilities.

Use `azure-architecture-messaging` to distinguish work queues, event notification, and event streams. Verify acknowledgement, redelivery, ordering scope, retention/replay, and consumer recovery for the selected service and tier. A service label does not establish idempotent business processing.

Use `azure-architecture-managed-ai` only when AI hosting is in scope. Establish model control, deployment and processing location, capacity, and operations requirements; verify the current product and deployment options rather than relying on a historical product name.

## Governance, identities, and private access

Read `azure-architecture-governance` and `azure-architecture-workload-identity` as applicable. Separate management-group/subscription/resource ownership, policy enforcement, control-plane roles, and data-plane permissions. Trace runtime and CI principals separately. For managed identities, check attachment, reuse, lifecycle, and grants; for external federation, inspect issuer, audience, subject, and resulting permissions.

Use `azure-architecture-private-access` to trace the client FQDN, target subresource, endpoint approval, Private DNS zone links or forwarding, routing, traffic restrictions, and data authorization. Verify legitimate private connectivity and public network access settings independently. An endpoint's existence does not prove that outside clients are denied or that its private DNS works from every client network.

## Recovery, migration, and cost

Read `azure-architecture-ha-dr` and verify the exact database product and tier. Separate zone redundancy, regional switching, application reconnection and capacity, prevention of conflicting writers, and restore from damaged data. State the evidence still needed to establish the recovery targets.

For PostgreSQL movement, use `azure-architecture-migration-cutover` to identify write ownership, catch-up, final cutover, reconciliation, and recovery once the target accepts writes. Verify tool and engine support instead of assuming every managed migration follows the same procedure.

Use `azure-architecture-cost-controls` to distinguish notifications and automated actions from application usage controls and discount commitments. Include applicable minimum capacity, database throughput/capacity, replicas, private endpoints, network traffic, logs, and recovery resources. Verify action coverage and timing before claiming a spending bound.
