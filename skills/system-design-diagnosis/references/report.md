# A Diagnosis the User Can Act On

Normally deliver the result in chat. Save a document or file only when requested, using the specified format. The following is a content guide, not a fixed set of headings or finding counts. Keep narrow assessments short. If no issues are found, state coverage, designs worth keeping, and remaining unknowns without inventing findings.

## 1. Lead with the recommended decision

Briefly explain:

- What to address first and which user impact that reduces.
- Whether anything needs verification before implementation.
- Where keeping the current design is reasonable, and under which conditions.

Present any P0 finding first. Do not give a blanket safety or production-readiness verdict that hides unknowns.

Then state the target, version or commit if known, review date, and scope. Identify material assumptions, checks actually run and their results, and unverified areas such as production or external settings. A repository assessment is not an inspection of production.

## 2. List priorities and reasons

Order findings by action and use stable IDs to connect details and options. If there are many, show the decision-critical findings first and explain where the rest can be found. Do not inflate the count with similar symptoms.

| Order | ID and finding | Priority / evidence | Business impact and reason for priority | Effort | Recommended decision |
| --- | --- | --- | --- | --- | --- |
| 1 | F-01: Finding summary | P1; confirmed; high confidence | Trigger, user impact, and why now | Estimate with assumptions, or not estimated | Temporary mitigation followed by a lasting fix |

This row illustrates structure; do not report the fictional F-01 as an actual finding. Briefly summarize the criteria nearby: impact, exposure, and urgency determine priority, while confidence and effort are shown separately. Put significant unknowns in a separate small table with investigation priority, potential impact, and required evidence.

## 3. Give enough detail to decide on leading findings

For each finding, include the following. Small findings may be grouped, but retain reasons and options.

- **Observations and evidence:** Links to files and lines actually inspected, settings, and results of checks actually run. Note defenses in other layers. Verify line references against the version read.
- **Trigger and business impact:** The causal path from entry point to side effect. Distinguish an observed incident from a demonstrated possibility.
- **Priority rationale and confidence:** Which criteria apply and what new information would change the assessment. Label hypothetical calculations with units and assumptions.
- **Relevant knowledge:** Tip IDs and primary sources supporting claims about the target technology. Do not claim to have verified primary documentation that you have not opened.
- **Options and recommendation:** Compare feasible responses using the structure below and explain their fit for this product.
- **Completion criteria:** Which retries, races, failures, migrations, or other scenarios need verification, and which observations would establish reduced risk. Adding a setting or having one test is not enough by itself.

### Comparing options

For major decisions, present as many feasible options as needed. Do not invent alternatives for a simple issue. List all covered finding IDs when an option addresses several findings.

| Option | Benefit | Remaining risks and limits | Effort and ongoing cost | Change impact and recovery |
| --- | --- | --- | --- | --- |
| A: Temporary mitigation | Triggers or harm reduced | Unprotected cases and expiry | Supported estimate, or not estimated | Usage restrictions, switching, and restoration |
| B: Lasting fix | Invariants and scope protected | Guarantee boundaries and operational burden | As above | Compatibility, migration needs, and rollback limits |
| C: Defer or investigate | Benefit of avoiding change now, or what investigation establishes | Accepted risks or unresolved decisions | As above | Monitoring and when or under what conditions to revisit |

Not every row is needed every time. A temporary mitigation followed by a lasting fix is also an option. If deferral fails requirements, state that explicitly. Explain why the recommendation fits better than alternatives and the conditions for adopting it. Do not describe irreversible data changes as simply "reversible."

## 4. Ask for a concrete decision

Present the diagnosis, comparison, and recommendation before asking. Do not hand the problem back with "What do you want to do?" without reaching a conclusion. Ask only questions necessary for the decision.

For example: "For F-01, I recommend restricting usage with A, then designing B. Would you choose A followed by B, start B directly, or investigate with C? You can also adjust the scope or conditions." Connect finding IDs, options, and next actions. Keep this separate from requests for missing information during the assessment.

Use a multiple-choice question tool if available and appropriate, or end with a normal question. Make compact answers possible, for example, "F-01=A then B; F-02=investigate; F-03=defer until the next review." Even when using a question tool, keep the diagnosis and recommendation in the final answer the user can read.

Treat a pending response as an unresolved decision. Silence is not consent to a mitigation, acceptance of residual risk, or a request for implementation. If the user has already chosen, do not ask again. Confirm the finding IDs, selected options, remaining risks, owners and deadlines if specified, and next actions. For deferrals, agree on review triggers. Do not invent owners, deadlines, or choices.
