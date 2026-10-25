# Evaluation and Release Guide

Read when defining acceptance, experiments, or a release gate. Scale the detail to the feature; a search assistant and an agent issuing refunds need different evidence.

## Construct cases from real outcomes

Record input, relevant source versions, principal and permissions, expected answer or business state, unacceptable effects, and scoring method. Include correct abstention when evidence is missing or access is denied. Use authorized, redacted or synthetic data; keep evaluation cases separate from tuning and prompt-selection examples. Track provenance and dataset revisions.

Choose scoring appropriate to the task: deterministic checks for state and constraints, evidence checks for citations, and calibrated human or model-assisted judgment for open answers. Validate automated graders against human examples and inspect disagreements. Repeated trials may be needed for variable outputs; report sample size and uncertainty instead of asserting certainty from one run.

## Separate failure mechanisms

| Layer | Evidence to collect |
| --- | --- |
| Retrieval | Was accessible, relevant evidence available and retrieved at useful rank? Did deletion or revocation remove it from every serving path? |
| Generation | Is the answer grounded in that evidence, complete for the task, and appropriately uncertain? |
| Structured output | Is it parseable and are values, references, and business rules valid? |
| Tool execution | Was the action authorized, correctly targeted, and applied without duplicate effects under retry or resume? |
| Whole workflow | Did the task reach the intended business state within quality, time, and cost constraints? Include human correction effort. |

Compare against a simple baseline and the current release with matched cases. Name unacceptable failure classes separately from aggregate success. If a model cascade is proposed, measure routing mistakes and duplicated inference/tool work.

## Release and recover

- Record model/version, prompt revision, retrieval/index configuration and corpus version, tool schemas, application revision, and evaluation revision. State which provider artifacts cannot be pinned exactly.
- Choose offline, shadow, and pilot stages according to risk. Shadow runs must isolate writes, notifications, and external calls that cause effects; a second request is not inherently read-only.
- For each gate, specify metric, population, observation window, threshold status, owner, and stop action. Keep proposed thresholds distinct from approved targets.
- Distinguish reverting a prompt/model/index from undoing actions already executed. Retain action records and a repair/reconciliation path where effects are irreversible.
- Correlate model/tool traces with outcomes and releases. Redact sensitive content, control trace access and retention, and monitor telemetry cost as well as inference cost.
