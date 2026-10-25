# Delivery Evidence Guide

Read only the stages connected to the reported friction. Trace a representative task across boundaries before recommending changes within a single stage.

| Stage | Evidence to seek | What could demonstrate improvement |
| --- | --- | --- |
| Repository to running service | Entry point, data path, build artifact/revision, deployment target, and observed running revision when available | A receiving engineer can trace a real operation to the relevant code and deployed revision |
| Local setup | Tool/runtime versions, dependency resolution, synthetic fixtures, external connections, reset/shutdown, hidden manual steps | A fresh workspace reaches a representative successful operation using the documented path |
| Validation and review | Required checks, runner queues, serial dependencies, representative failures, decision rationale, time waiting for reviewers | Actionable feedback arrives earlier without removing checks needed at the release boundary |
| Delivery | Artifact identity, privileged jobs, environment writers, deployment serialization, verification, and recovery | A representative authorized change reaches the intended environment and revision with observable verification |
| Ownership and handover | Decision authority, usable permissions, backup coverage, routine operations, exception handling, vendor-only knowledge | The receiving team completes and recovers a change without the original implementer |
| Operation | Recurring manual tasks, hands-on time, failure/recovery effort, environment/revision signals, and support demand | The task is removed or becomes easier to perform and recover, with acceptable ongoing maintenance |
| Shared platform | Real consumer tasks, failure/support patterns, supported exceptions, generated-project updates, and platform ownership | Consumers complete their work with less friction and can update existing projects |

## Keep findings tied to evidence

For each material finding, capture the task and time window, evidence link, observed waiting/rework/failure, plausible mechanism, proposed improvement, and verification. Label an unobserved mechanism as a hypothesis and choose a check that distinguishes it from alternatives. Avoid judging individuals from commit counts or equating deployment frequency with business value.

For a handover, distinguish receiving files, understanding the system, having authority and access, and demonstrating independent operation. Mark each unverified capability explicitly. A proposal to retire a vendor dependency needs a tested replacement capability and ownership for unresolved support work.

## Define a bounded improvement

Use an entry like this when it helps:

| Item | Content |
| --- | --- |
| Task and constraint | The concrete change/operation and what prevents completion |
| Baseline | Measured range and time window, or the measurement still needed |
| Improvement | Smallest useful change and why it addresses the constraint |
| Dependencies | Permissions, other teams, environment, and unresolved decisions |
| Ownership | Known responsible role, or proposed role pending agreement |
| Verification | Representative task, expected result, and observable evidence |
| Persistence | When to check for regressions and who maintains the improvement |

An authorized clean-setup check should isolate data and outbound effects. A delivery or recovery rehearsal needs an explicit environment, intended mutations, stopping condition, and cleanup/recovery plan; proposing it does not authorize running it.
