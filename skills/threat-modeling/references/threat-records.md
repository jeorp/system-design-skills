# Threat Scenarios and Validation

Use when recording threats, comparing controls, or defining verification. Keep each record tied to a reachable path.

## Threat record

| Field | Evidence or decision |
| --- | --- |
| Asset/invariant | Protected data, action, business rule, or service behavior |
| Actor and preconditions | Available credentials, access, timing, and required capabilities |
| Path and boundary | Entry point, affected components, and where authority or data crosses trust |
| Existing controls | Actual enforcement location and counterevidence, not only configuration names |
| Failure and impact | What protection fails and who or what is affected |
| Priority and confidence | Impact/reachability rationale and whether the claim is observed or provisional |
| Response | Control location, alternatives, owner if known, and residual risk |
| Verification | Input/principal, expected allowed/denied behavior, evidence, and containment |

Group paths that share a mechanism when the mitigation is shared. Keep separate records when different authority boundaries require different fixes. Do not count a missing document as proof of a missing runtime control.

## Boundary prompts

- **Identity to resource:** can a valid principal select another user's resource, tenant, object-storage key, or cached response? Is permission rechecked where delayed work executes?
- **Data to execution:** can caller-controlled input alter SQL, command arguments, template evaluation, outbound destinations, or model-driven tool execution? Inspect parsers and downstream use, not just input filtering.
- **Low to high privilege:** can PR code, support tools, jobs, or a compromised service obtain deployment or administrator authority? Trace credential issuance and use.
- **State and time:** can replay, concurrency, stale authorization, or an unexpected transition bypass a business rule? Include caches and alternate routes.
- **Shared resource:** can one tenant exhaust work, storage, connections, or model/tool budget for others? Identify limits at the costly operation.
- **Detection:** would a meaningful denied action or privileged change produce a usable, access-controlled audit signal? Do not log credentials or full sensitive bodies as proof.

## Validate the control, not just the rejection

Use controlled local fixtures where appropriate. Show that the prohibited effect did not occur, even if the API returned an error; also verify legitimate operations still work. Include alternate entry points or asynchronous consumers when the same resource can be reached there. Record unexecuted checks as proposed checks.

For uncertain exploitability, state the exact missing evidence and a contained way to obtain it. A priority label should not conceal assumptions about access, network reachability, or privileges.

## Primary guidance

[OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) provides the system, threat, mitigation, and validation framing. Apply it to the actual scope and evidence rather than treating a taxonomy as proof of coverage.
