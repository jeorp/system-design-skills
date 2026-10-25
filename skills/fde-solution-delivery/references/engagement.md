# FDE Engagement Guide

Read the section relevant to the engagement's current stage. These are working records to scale to the request, not mandatory customer paperwork.

## Discovery and readiness

| Record | Useful contents |
| --- | --- |
| Workflow case | Actor, trigger, real or sanitized input, steps, decisions, handoffs, completion evidence, exceptions, and rework |
| Outcome | Current baseline or missing measurement, desired improvement, quality requirement, measurement window, and business judge |
| Domain meaning | Terms, authoritative sources, identifiers, units, status transitions, time semantics, and correctness owner |
| Data profile | Representativeness, missing or incorrect values, timeliness, exceptions, access restrictions, and effect on the workflow |
| Dependency | Required access/integration, responsible role, needed-by date if agreed, current status, and proof of completion |
| Decision | Choice, owner with authority, evidence needed, due date if known, and effect of delay |

Keep reported facts separate from observations and assumptions. If an interview or access check has not happened, provide questions or a verification task instead of completed findings. Do not infer authority over rollout or data from the title of the customer contact.

## Acceptance cases

Define cases with input/preconditions, expected business result, allowed human intervention, unacceptable effects, and the role deciding correctness. Include normal work and the exceptions that would undermine adoption, such as missing data, ambiguous records, revoked permissions, dependency outages, and incomplete external work.

Compare candidates on the same cases. For AI, evaluate unacceptable outputs and tool actions alongside aggregate quality. Count user review, correction, rework, and failed attempts in whole-workflow performance. A faster generated answer may leave task completion slower.

For an external integration, specify how acceptance, processing, and completion differ; which identifiers and states can be queried; and who resolves missing, duplicate, mismatched, or unknown results. Reconcile the same business scope and time window rather than comparing counts alone.

## Experiment and pilot gates

| Stage | Evidence sought | Boundary to state |
| --- | --- | --- |
| Offline experiment | Whether a critical data, quality, integration, or usability assumption holds | Input provenance, permitted data use, representative cases, and limits of the evidence |
| Shadow observation | How candidate behavior compares with real work | Isolation of writes/outbound effects, aligned comparison, and how disagreements are judged |
| Limited live pilot | Whether users can complete real work acceptably | Authorized users/workload, action limits, human review, success/stop criteria, support, and observation window |
| Wider adoption | Whether benefits and operation persist under intended use | Capacity, exception burden, decision authority, ongoing measurement, and recovery readiness |

Before live work, define what stopping does to queued/in-flight tasks, user work, and external effects, and who reconciles the final business state. A fallback must have a workable procedure and capacity; “manual fallback” alone is incomplete. Treat candidate thresholds as proposals until agreed.

## Adoption and handover

Verify that users can find and enter the workflow, understand when to trust or escalate a result, and complete exceptions. Verify that the receiving team can identify a failed case, diagnose its state, recover or escalate, and manage configuration/access without the implementing engineer. Preserve a support owner and maintenance path for customer-specific integration work.

Report demonstrated capability separately from training delivered or documentation written. Capture unresolved responsibilities before describing handover as complete. Share reusable mechanisms only after removing confidential records, credentials, customer-specific permissions, and unsupported generalizations.

For progress and scope decisions, report evidence completed, uncertainty remaining, blocked dependencies, and the next decision with its responsible role. Explain how a new request changes the outcome, verification effort, delivery sequence, and maintenance before proposing a scope/date trade-off.
