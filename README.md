# System Design Skills

Agent skills for reviewing an existing product's architecture and deciding what to improve next.

## Usage

Clone this repository, then ask your agent from the product you want to review. Replace the path with your local checkout:

```text
Use /path/to/system-design-skills/skills/system-design-diagnosis/SKILL.md
to review this product's system design. Prioritize findings, explain
the evidence, and compare options so I can choose what to do next.
```

If the skill is installed in your agent, invoke it with `$system-design-diagnosis`. You can focus on a specific flow, such as payment webhooks or a database migration.

## What You Get

- Findings ranked P0–P3, with evidence and clearly stated unknowns.
- Practical options with trade-offs, effort, remaining risks, and completion criteria.
- A recommended next step: fix, investigate, defer, or keep the current design.

A diagnosis does not change your product's code or production settings. See the [prioritization criteria](skills/system-design-diagnosis/references/prioritization.md) and [report guide](skills/system-design-diagnosis/references/report.md) for details.

## Included Tips

Includes 134 English system-design Tips extracted from the `system-design-skill-developer` learning catalog, with explanations, trade-offs, and source links. The original repository is not needed.

The helper requires Python 3, with no additional dependencies. Run from this repository's root:

```sh
python3 skills/system-design-diagnosis/scripts/tips.py search retry
python3 skills/system-design-diagnosis/scripts/tips.py show timeout-budget retry-amplification
```

For snapshot updates, see [the skill instructions](skills/system-design-diagnosis/SKILL.md#3-turn-relevant-tips-into-evidence-based-reasoning). Tips are guidance; verify relevant product versions and primary sources before applying them.

## License

[MIT](LICENSE). Linked third-party references retain their own licenses.
