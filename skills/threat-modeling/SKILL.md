---
name: threat-modeling
description: Model threats to a feature or system by tracing protected assets, actors, data flows, trust boundaries, and abuse paths; prioritize mitigations and verification. Use for design-time security analysis or a focused threat model of an existing system. Not for penetration testing, vulnerability scanning, compliance certification, or live incident response.
---

# Threat Modeling

Explain what must be protected, how it can be harmed, and what evidence would establish effective defenses. Ground the model in the system rather than a generic checklist. Communicate in the user's language and deliver in chat unless a saved artifact is requested. Threat analysis alone does not authorize exploitation, external scanning, access changes, or testing against production; follow existing authorization for any requested implementation or contained local verification.

## Define the protected outcomes and scope

Inspect repository instructions, the feature or system architecture, entry points, identity and permission checks, data stores, caches, asynchronous jobs, integrations, deployment and CI trust, and available controls. Trace representative sensitive reads and writes, including alternative paths. Separate intended design from implemented controls and unverified assumptions.

Identify protected data, business invariants, availability needs, actors and their legitimate privileges, assets, and relevant attacker capabilities. Establish the review boundary and dependencies without expanding a feature review into an unrelated organization-wide audit. Do not invent regulatory duties, adversary capabilities, or numeric risk probabilities.

## Map flows and trust boundaries

Show processes, stores, external entities, and flows at enough detail to locate enforcement. For each boundary crossing, identify the principal, data classification where known, authentication, resource/tenant authorization, input interpretation, and credential scope. Distinguish a network boundary from an identity or privilege boundary; internal traffic is not inherently authorized.

Include browser/API paths, webhooks, background jobs, shared caches, object storage, support/admin operations, and CI deployment privileges when they carry relevant authority or data. Follow permission revocation and deletion through delayed jobs and cached copies. Identify where an untrusted value becomes a query, URL, command, template, model instruction, or tool argument.

## Develop reachable threat scenarios

Use applicable explanations from the bundled [Tip index](references/tip-index.md). Replace `<skill-dir>` with this file's directory:

```sh
python3 "<skill-dir>/scripts/tips.py" show threat-modeling-boundaries object-authorization tenant-cache-isolation async-job-authorization ssrf short-lived-credentials security-detection-coverage
```

Read the [scenario and validation guide](references/threat-records.md) to develop evidence-backed threat records. STRIDE or another familiar taxonomy can prompt questions, but it is not a reason to manufacture one threat per category. Verify consequential security and platform guarantees against primary documentation for the deployed versions. Never copy secrets or personal data into evidence.

For each scenario, connect actor capability and preconditions → entry point and reachable path → crossed boundary or missing control → violated asset/invariant → impact. Examine existing shared guards, database constraints, platform protections, and counterevidence before claiming a weakness. A malicious string alone does not prove a reachable exploit.

Prioritize plausible paths involving unauthorized cross-user/tenant access, privileged action, credential misuse, injection, tampering, exfiltration, resource exhaustion, and bypass of business controls when relevant. For AI paths, treat external text as data and inspect enforcement outside the model. Avoid reducing security analysis to prompt wording.

## Choose and verify controls

For material threats, compare controls at the actual enforcement boundary. Prefer preventing unauthorized effects and limiting privilege/blast radius; detection and response can complement prevention but do not establish it. Explain residual exposure, operating burden, and legitimate behavior that a proposed control could disrupt.

Keep severity, confidence, and effort separate. Rank by evidenced reachability and plausible impact, accounting for existing controls; distinguish a demonstrated defect, a design risk, and a question requiring more evidence. Name the responsible role where known and define an observable verification criterion.

Propose or perform authorized, contained verification with synthetic principals and data. Include negative and positive cases: a denied cross-tenant read plus an allowed same-tenant read, a revoked permission through asynchronous paths, or a restricted URL fetch alongside an allowed destination. Do not probe live third parties or conduct exploit chains merely to complete a model. Security logging checks should establish that the relevant event is recorded and actionable without leaking the protected data.

## Deliver a decision-ready model

Lead with the most consequential threats and recommended controls. Include scope, assets and invariants, a compact flow/boundary map, prioritized threat records with evidence, mitigations and verification, and important unknowns or residual risks. State coverage limits; absence of identified threats does not certify safety.

System Design Diagnosis surveys broader system risks; Architecture Change Review attributes regressions to a diff. This skill builds the threat model for a bounded system or feature regardless of whether a diff exists. Keep the result usable independently without automatically invoking other skills.
