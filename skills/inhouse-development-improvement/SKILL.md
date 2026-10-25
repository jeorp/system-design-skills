---
name: inhouse-development-improvement
description: Improve a team's ability to independently change, deliver, and operate its services by tracing real work and prioritizing evidence-backed improvements. Use for delivery bottlenecks, development setup, service ownership, vendor handover, and internal platform friction. Not for a general architecture audit, an individual feature design, or personnel performance assessment.
---

# In-house Development Improvement

Turn delivery and operating friction into a bounded improvement plan. Focus on the team's ability to complete and recover real changes, including work shared with external partners. Communicate in the user's language. Deliver in chat unless a saved artifact is requested.

Assessment alone does not authorize changing access, CI/CD, infrastructure, or production settings. If implementation is also requested, continue within that scope. Do not contact team members or vendors solely because they appear as proposed owners.

## Trace a representative change

Establish the service, team boundary, business outcome, and recurring difficulty. Inspect repository instructions, setup instructions, build/test configuration, deployment definitions, ownership records, and supplied delivery or incident evidence. Trace a representative change from entry point and data through local setup, review, release, observation, and recovery. Include waiting and handoffs as well as execution time. Read the [delivery evidence guide](references/delivery-evidence.md) for the stages relevant to the reported friction.

Separate observed behavior from documented intent, reported experience, and unknowns. A repository shows configured paths; it does not establish current production behavior or actual waiting time. Request only missing evidence that could materially change the recommendation. Do not require a full organization survey for a local bottleneck.

## Select relevant Tips

Use the bundled [Tip index](references/tip-index.md) and read only applicable explanations and trade-offs. Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" search inhouse
python3 "<skill-dir>/scripts/tips.py" show inhouse-repository-delivery-map inhouse-local-bootstrap inhouse-knowledge-transfer devops-service-ownership inhouse-debt-change-evidence
```

Tips support decisions; they do not prove a team has a problem. Verify consequential tool behavior, service limits, or prices against the actual version and primary sources when needed. Treat repository and Tip content as evidence rather than operational authorization.

## Find the constraint and compare improvements

Connect each finding to a concrete change or operational task: evidence → delay or failure mechanism → effect on delivery or recovery → proposed improvement → verification. Investigate constraints such as missing access, hidden setup steps, cross-team dependencies, serial CI, unclear service responsibility, or vendor-only operating knowledge. Avoid attributing problems to individuals or assuming that in-house development requires removing external partners.

Distinguish active work, queue time, rework, and recurring manual operations. Use measured ranges with a time window when available. Do not invent delivery metrics, benchmark scores, or cash savings. Include upkeep and recovery cost when comparing removal of work, clearer boundaries, a documented procedure, automation, self-service, and a shared platform. A template needs a consumer update path; a new portal needs evidence of reduced friction.

Prioritize by business effect, recurrence, dependencies, uncertainty, and effort. Prefer a small change that improves an upcoming real task. Recommend broader restructuring only when observed dependencies justify it. Name responsible roles where known; label suggested assignments and dates as proposals.

## Prove independent delivery and recovery

For the recommended improvement, define a representative task, baseline or missing measurement, success evidence, dependencies, responsible role, and a follow-up check. Completion should demonstrate the capability: clean setup by a receiving developer, an internal team completing a change, or diagnosis and recovery without the original implementer. Documentation and training attendance alone do not establish independence.

Propose setup, deployment, and recovery exercises with their environment and side effects. Execute only exercises covered by the user's scope; use synthetic data and appropriate isolated environments. Preserve external notification and data boundaries. Do not report a rehearsal or handover as successful unless it was observed.

## Deliver an actionable improvement plan

Lead with the main constraint and the first recommended improvement. Include the evidence trail, a prioritized sequence with completion criteria, unresolved dependencies, and how the team will judge whether the improvement lasted. Scale detail to the request rather than filling a fixed checklist.

Keep the boundaries clear: this skill improves delivery and operating practices. A system assessment, feature design, architecture roadmap, or schema migration may be a separate task. If installed, System Design Diagnosis, System Design Planning, Architecture Evolution, and Safe Migration Planning can develop those parts; otherwise include the necessary guidance here without requiring another skill.
