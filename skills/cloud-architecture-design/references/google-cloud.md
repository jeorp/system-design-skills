# Google Cloud Decisions

Read for a Google Cloud workload. Use only the sections relevant to the decision and retrieve the selected Tips with `scripts/tips.py show <ids>` relative to the skill directory. The [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides review questions; verify decisive behavior in the current product documentation for the selected region and edition.

## Execution, data, and ingress

Start with `gcp-pca-compute`, `gcp-pca-relational-database`, and `gcp-pca-storage`. Compare runtime/control needs, scaling and concurrency, database connection pressure, compatibility, write and transaction scope, placement, and object/file/block access. Explain which operational work remains with the team.

Use `gcp-pca-load-balancing` when designing ingress. Verify protocol, internal or external exposure, regional/global scope, backend eligibility, health checks, and client path together; the load balancer's scope does not establish that its backends or data survive a region failure.

Use `gcp-pca-streaming-analytics` for Pub/Sub-to-BigQuery paths. Determine whether delivery alone suffices or transformations need cross-message state, windows, or joins. Specify replay, duplicate handling, late data, and reconciliation for the actual ingestion path.

Use `gcp-pca-managed-ai` only when choosing AI hosting. Separate managed API requirements from custom deployment and model-control needs, and verify data location and capacity for the chosen option.

## Organization, identity, and private access

Read `gcp-pca-resource-hierarchy` and `gcp-pca-workload-identity` as applicable. Separate project/resource ownership, network administration, service identities, and external CI federation. Check issuer/subject conditions and effective grants to the deployment and runtime principals separately.

Use `gcp-pca-private-google-access`, `gcp-pca-service-perimeter`, and `gcp-pca-hybrid-network` for the relevant paths. Trace client → DNS → route → endpoint → policy/permission for each API or database. Distinguish Google API reachability, private service endpoints, private database connectivity, hybrid transport, and general internet egress. Verify supported services and legitimate ingress/egress before proposing a service perimeter; do not treat it as a general firewall.

For key or audit requirements, read `gcp-pca-cmek-lifecycle` and `gcp-pca-audit-logs`. Establish old-key dependencies, retention and restore requirements, and which data-access events must be enabled and retained. Administrative changes alone cannot supply evidence of every sensitive data read.

## Recovery, rollout, and cost

Read `gcp-pca-ha-dr` for the chosen database topology and verify zone versus region failure coverage, lag, promotion, reconnection, and restore requirements. Use `gcp-pca-migration-cutover` for write suspension, catch-up, reconciliation, and recovery after target writes begin.

Use `gcp-pca-release-slo` for a Cloud Run rollout. Specify how revision-level errors, latency, resource use, and business outcomes determine traffic progression or a stop. Reverting traffic does not undo committed writes.

Read `gcp-pca-cost-controls` to separate rightsizing and usage reduction from discount commitments. Include applicable idle capacity, database replicas, network transfer, logging, and ingestion costs; verify quota and budget behavior before claiming a usage or spending bound.
