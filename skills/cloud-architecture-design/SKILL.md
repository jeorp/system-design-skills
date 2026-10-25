---
name: cloud-architecture-design
description: Design a workload's architecture on AWS, Google Cloud, or Azure by choosing managed services, identity and network boundaries, recovery mechanisms, and cost controls. Use for cloud service selection, cloud architecture proposals, or redesigning a workload's cloud deployment. Not for certification practice, routine deployment execution, or cloud spending analysis without an architecture decision.
---

# Cloud Architecture Design

Turn workload requirements into a cloud configuration whose service choices, access paths, failure behavior, and operating responsibilities fit together. Communicate in the user's language and deliver in chat unless a saved artifact is requested. A design request alone does not authorize provisioning, paid experiments, IAM changes, or deployment. Continue within existing authorization when implementation is also requested.

## Establish the workload and fixed decisions

Inspect repository instructions, infrastructure definitions, deployment configuration, application entry points, data stores, background work, CI identities, and available operational evidence. Trace a representative request or job through its dependencies. Focus on the workload being designed rather than expanding into an organization-wide cloud review.

Separate observed configuration, user requirements, assumptions, and unknowns. Establish the outcome, existing provider and region, runtime and protocol needs, state and access patterns, data location, expected load, availability and latency goals, recovery objectives, budget, and team operating capacity where relevant. Clarify which constraints are mandatory. Do not invent traffic, prices, SLOs, RTO/RPO, compliance duties, or deadlines.

Preserve a settled provider choice. If provider selection is open, compare eligible options against the same workload and ownership constraints; do not design three full stacks by default. A multi-cloud or multi-region topology needs a concrete requirement and an account of its added data, identity, networking, and recovery work.

## Read only the relevant cloud guidance

Use the bundled [Tip index](references/tip-index.md) to find explanations and trade-offs. Replace `<skill-dir>` with the directory containing this SKILL.md:

```sh
python3 "<skill-dir>/scripts/tips.py" show aws-architecture-requirements
python3 "<skill-dir>/scripts/tips.py" show gcp-pca-requirements
python3 "<skill-dir>/scripts/tips.py" show azure-architecture-requirements
```

Run the command for the selected provider, then read the applicable [AWS](references/aws.md), [Google Cloud](references/google-cloud.md), or [Azure](references/azure.md) decision guide. Load additional Tips only for decisions in scope. The guides identify questions to verify; the catalog is learning material, not proof of a service's current behavior.

Verify decisive capabilities, regional availability, engine/edition differences, quotas, identity and network behavior, recovery guarantees, and prices against current primary documentation and the target configuration. Record the evidence and unresolved assumptions beside the choice. A service SLA, architecture diagram, or Well-Architected checklist does not establish measured end-to-end availability or compliance.

## Choose a coherent service composition

Compare feasible services by their fit to execution duration, concurrency, scaling, runtime control, connection behavior, transaction scope, query patterns, and operating ownership. Include retaining the current service when it meets the goal. Do not default to Kubernetes, serverless, or a distributed database solely because it appears more scalable.

For each important choice, connect requirement → candidate mechanism → remaining customer responsibility → trade-off → verification. Name a mandatory constraint that rules an option out. Avoid equating services across clouds by product category alone; verify the semantics the application depends on.

Trace the recommended request and background paths across ingress, compute, storage/database, messaging, and external dependencies as applicable. Check whether compute scale can exhaust database connections, quotas, or downstream capacity. Specify the relevant queue acknowledgement, redelivery, ordering, retry, idempotency, and dead-letter behavior; adding a managed queue does not settle those contracts. Keep object, shared-file, and block access requirements distinct.

## Make access and failure boundaries explicit

For each sensitive path, name the calling identity, credential acquisition, allowed resource/actions, DNS and routing, endpoint, traffic restrictions, and public exposure. Cover CI deployment and runtime identities separately. Test connectivity and authorization as separate properties; a private endpoint or federated credential does not itself establish permission to the data. Explain organization-level guardrails and workload grants at their respective scopes.

Separate instance/zone availability, regional disaster recovery, and recovery from deletion or corruption. Trace what happens to the whole application when a dependency fails: detection, retry/reconnect, promotion or restore, routing, capacity, and prevention of competing writers. Include secrets, keys, images, DNS, and other recovery-region dependencies where relevant. Treat RTO/RPO as targets until an appropriate rehearsal establishes evidence; replication does not replace restore validation.

For a migration, identify the source of writes, replication lag, final write cutover, reconciliation, and the point after which rollback requires data repair. A continuously replicating migration tool is not evidence of zero downtime or zero loss.

## Account for cost and delivery

Model meaningful cost drivers with explicit workload inputs, units, region, pricing date, and uncertainty. Include applicable idle capacity, minimum instances, replicas, backups, network/egress, endpoints, logs, requests, and support or operating effort. Compare commitments only after checking demand and flexibility. Keep budget notifications, delayed automated actions, and application usage/concurrency controls separate; do not describe an alert threshold as an instantaneous spending cap.

Define a practical delivery sequence with acceptance evidence at the uncertain boundaries: representative load, allowed and denied access, private DNS reachability, failover/reconnection, backup restore, and migration reconciliation where applicable. Scale checks to the actual change. Specify owners, observation signals, stop conditions, and recovery actions without executing infrastructure changes merely to complete the design.

Lead the result with the recommended composition and its principal trade-off. Include meaningful alternatives, a compact flow, identity/network and data boundaries, failure and recovery behavior, cost assumptions, remaining responsibilities, and the next validation or decision. Distinguish estimated, documented, and measured behavior.

System Design Planning covers wider application and domain design; this skill develops cloud placement and service composition. Safe Migration Planning can deepen an individual cutover, and AI System Design can deepen model orchestration and evaluation. Keep the cloud design useful independently without requiring or automatically invoking other skills.
