---
name: ai-system-design
description: Design an AI feature's architecture, choosing workflows or agents, retrieval or tuning, tool execution boundaries, evaluation gates, and operating controls. Use for LLM, RAG, and agent system design or architectural changes. Not for standalone prompt polishing, model rankings, or customer discovery without a defined technical problem.
---

# AI System Design

Turn a defined user task into an AI architecture with explicit quality, access, action, latency, and cost boundaries. Communicate in the user's language and deliver in chat unless a saved artifact is requested. Design alone does not authorize provisioning, model calls with private data, paid evaluations, or tool actions. Continue within existing authorization when implementation is also requested.

## Establish the task and failure cost

Inspect repository instructions, existing model calls, prompts, retrieval and ingestion paths, tool handlers, permissions, evaluations, and deployment configuration where available. Trace one representative task from input to the final answer or business action. Separate observed behavior, requirements, assumptions, and unknowns.

Define what constitutes a correct outcome, unacceptable errors, abstention or escalation, allowed autonomy, and the evidence needed for acceptance. Establish data sensitivity, freshness, tenant boundaries, latency and cost constraints, expected workload, and operational ownership where known. Do not invent target quality scores or assume AI is needed; compare a rules-based or search-only baseline when the mechanism is still open. Preserve settled product and technology decisions.

## Choose control flow and knowledge strategy

Select applicable explanations from the bundled [Tip index](references/tip-index.md). Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" show ai-architecture-workflow-or-agent ai-architecture-rag-or-tuning ai-architecture-retrieval-authorization ai-architecture-durable-agent-execution llm-evals
```

Compare deterministic orchestration, bounded model decisions, and agent loops according to the actual uncertainty in the next step. Name stopping conditions, maximum work, escalation, and the source of durable execution state. Avoid adding an agent when a known sequence meets the task.

Distinguish knowledge freshness and provenance from behavior or output-style adaptation. For retrieval, define ingestion, document identity/version, chunking, metadata, deletion, freshness, and citations. Enforce access before content crosses into a model context, cache, tool, or user response; post-filtering an answer does not undo earlier disclosure. Check permission changes and tenant isolation across retrieval and caches. For tuning, identify the behavior being learned and a suitable training/evaluation data separation; tuning is not a general freshness mechanism.

Keep the design provider-neutral unless the context fixes a provider. Verify consequential model capabilities, retention behavior, service limits, version behavior, and prices against primary documentation. Tips do not establish a provider's current guarantees.

## Define contracts and action boundaries

Specify model inputs, context assembly and truncation policy, retrieval evidence, structured outputs, and downstream validation. Syntactic schema compliance does not establish valid business values or permission to act. Treat retrieved text, documents, and tool results as untrusted data; enforce authorization and allowed operations in application code outside the model.

For tools that change state, define principal/resource authorization, argument validation, idempotency, durable action identifiers, timeouts, and reconciliation of unknown outcomes. A saved chat history is not an execution ledger. Identify when human review is needed based on actual action scope and recovery limits; honor existing authorization rather than requiring approval for every tool call. Bound iterations, concurrency, token usage, retries, and total elapsed work. Cancellation must address work already issued and effects already committed.

Budget latency and cost across retrieval, model turns, tool calls, retries, and fallbacks. Distinguish first-token time from completion of the task. Routing or fallback can change quality and permissions as well as availability; evaluate those paths and prevent duplicated effects. Label estimates and missing measurements rather than presenting unit prices or assumed throughput as total operating cost.

## Gate release with task evidence

Use the [evaluation and release guide](references/evaluation-release.md) to define acceptance cases and controlled rollout. Include representative tasks, difficult cases, denied access, prompt injection, invalid outputs, dependency failures, and action recovery where relevant. Evaluate retrieval separately from answer generation and tool/business outcomes. Break results down by consequential task or user group so averages cannot hide severe failures.

Version the model, prompts, retrieval assets, tool schemas, orchestration, and evaluation set together. Define quality, safety, latency, and cost gates with owners and candidate thresholds where agreement is missing. Distinguish offline replay, shadow execution with side effects isolated, and a live pilot. Plan trace correlation and redaction without logging unrestricted prompts, retrieved documents, or secrets.

## Deliver the architecture

Lead with the recommended approach and its principal trade-off. Include the task flow, meaningful alternatives, data and trust boundaries, tool/action contracts, resource budgets, evaluation and rollout gates, and recovery limits. Name the next measurement or unresolved decision. Do not claim evaluated quality without running an evaluation.

FDE Solution Delivery addresses customer discovery and adoption; this skill develops the AI architecture once the task is understood. System Design Planning can cover wider product integration. Keep this design usable independently without automatically invoking other skills.
