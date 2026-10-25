# Prioritization Criteria

These are decision rules for this skill, not a standard score such as CVSS or measured failure probabilities. Prefer the user's explicit criteria, deadlines, and SLOs, and explain any changes to the criteria. Do not invent aggregate scores or false precision such as an "85% safety rating."

## 1. Separate harm from triggering conditions

Assess the following for each finding. When an assessment depends on assumptions, explain how changing them would affect the priority.

| Dimension | What to establish |
| --- | --- |
| Business impact | Data exposure or loss, unauthorized actions, financial inconsistency, or disruption or delay of key actions. Is recovery possible? Does it break a commitment to users? |
| Scope | One operation, user, tenant, the whole system, or external partners. Distinguish potential scope in code from observed harm. |
| Triggers and exposure | Can ordinary retries or concurrency trigger it? Does it require authentication? Is it externally reachable? Does it depend on special privileges or future scale? |
| Urgency | Is harm ongoing? Will a planned launch or migration establish the conditions? Has time to exhaustion been measured? Do not invent deadlines. |
| Existing defenses and recovery | How much do authorization in another layer, database constraints, rate limits, monitoring, and restoration reduce harm? Is only configuration known, or has effectiveness been verified? |

Severe consequences do not establish a high likelihood. If frequency data is unavailable, explain concrete triggers rather than inventing probabilities.

## 2. Response priority: P0–P3

| Priority | Criteria | Recommended response |
| --- | --- | --- |
| P0: Immediate decision | Evidence of ongoing severe harm, or verified exposure that makes severe harm imminent without adequate defenses. | Lead with it. Propose containment or delaying a launch and explain business impact. Seek the responsible person's decision; diagnosis alone does not authorize production operations. |
| P1: High priority | Current or imminent usage conditions allow serious exposure, corruption, inconsistency, or disruption of key features without adequate defenses. Observed harm is not required. | Normally address before the next relevant release or feature launch. Propose the order of temporary and lasting fixes. Base specific deadlines on actual plans. |
| P2: Planned improvement | Impact is limited, some defenses exist, or the issue requires particular load or changes. The target's requirements justify improvement. | Include in normal development planning. Identify measurements and dependencies needed to schedule it. |
| P3: Monitor and revisit | Current requirements are met, but there is room to prepare for future growth or operational burden. | Offer keeping the current design, with review triggers and metrics. Exclude findings based only on preference. |

Give a reason for each priority, such as "P1: a retry can duplicate a financial operation, and no business constraint prevents it." Do not automatically translate priorities into a fixed number of days.

## 3. Evidence status and confidence

Show what is known separately from priority.

| Status | Definition and wording |
| --- | --- |
| Confirmed | A traced path, configuration, constraint, or safe reproduction establishes the defect. Report a confirmed defect separately from confirmed production harm. |
| Conditional | A concrete defect path exists, but a prerequisite such as exposure or usage is unknown. State "Occurs if X; X needs verification." |
| Unverified | Missing documents, access, or measurements prevent a conclusion about whether a defect exists. Do not dismiss protections that have been established. |

Express confidence as high (the path and mitigations were traced or reproduced), medium (part of the path or operational conditions remains unknown), or low (fragmentary evidence or inference), with a reason. Code paths and specifications can establish high confidence without executing tests. The existence of a test alone is not verification.

Qualify conditional findings, for example, "Provisional P1, pending exposure verification." For purely unverified items, do not assign a P rating as if a defect were established. State the potential impact if the conditions hold and assign investigation priority.

### Investigation priority for unknowns

- **Verify first:** A concrete possibility of severe harm could change a decision or imminent launch. Specify the evidence needed, where to obtain it, a safe verification method, and next steps for either outcome.
- **Planned verification:** The unknown does not block an imminent decision. Schedule measurement or verification in normal planning.

Place "verify first" items near the top, separately from confirmed findings, and first in the action order when appropriate. Not finding backup configuration in a repository does not establish "no backups, P1." However, uncertain restorability before an imminent data migration warrants verification first.

## 4. Action order and effort

Order work using these considerations and explain material departures:

1. Put decisions about P0 findings or ongoing harm first.
2. Order verification that affects imminent decisions and P1 responses by actual deadlines and dependencies.
3. Within a priority, compare harm, exposure, urgency, and existing defenses.
4. Then favor options that reduce harm with less effort or enable other mitigations.

A cheap P2 task may proceed in parallel; that does not make it more severe than P1. Allow ties when warranted.

Provide effort ranges, such as person-days, only when there is a basis for estimation. Otherwise state "Not estimated; requires mapping the affected areas." Include validation, migration, review, operational work, and ongoing costs alongside implementation, and state assumptions. Do not launch unnecessary large investigations just to produce an estimate.

## Examples

- A live payment path creates a new external charge on every retry, with no protection: P1, confirmed. If duplicate charges are observed to be ongoing, consider P0 based on that evidence.
- Restoration is unknown because configuration documents are unavailable: unverified. Verify first if an important data migration is imminent. Missing documentation does not prove restoration is impossible.
- A query might need an index: inspect data volume, execution plans, and latency first. Do not assert a performance defect or improvement percentage before measurement.
- A small system in one region meets agreed recovery requirements: do not list the absence of multiple regions as a finding.
