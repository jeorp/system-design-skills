# System Design Skills

Agent skills for designing product architecture, reviewing changes, testing failure behavior, and planning reliable operations.

## Skills

| Skill | When to use it | What you get |
| --- | --- | --- |
| [System Design Planning](skills/system-design-planning/SKILL.md) | Before building a feature or changing architecture | Recommended design, alternatives, failure handling, delivery steps, and validation criteria |
| [System Design Diagnosis](skills/system-design-diagnosis/SKILL.md) | To assess an existing product | Findings ranked P0–P3, evidence, response options, and recommended next steps |
| [Failure Scenario Testing](skills/failure-scenario-testing/SKILL.md) | When the happy path works but failure behavior is uncertain | Retry, race, timeout, and interruption cases; focused test implementation and results when in scope |
| [Architecture Change Review](skills/architecture-change-review/SKILL.md) | To review a PR or diff for system-level risks | Evidence-backed findings on consistency, compatibility, load, and authorization |
| [Safe Migration Planning](skills/safe-migration-planning/SKILL.md) | Before a schema change or data migration | Version compatibility, migration stages, monitoring gates, abort actions, and recovery limits |
| [Capacity Planning](skills/capacity-planning/SKILL.md) | To estimate growth, peak load, or failure headroom | Explicit assumptions and estimates for connections, concurrency, backlog, and bottlenecks |
| [Incident Learning](skills/incident-learning/SKILL.md) | After an incident | Evidence-linked timeline, causal factors, and prioritized actions with verification criteria |

All seven use 134 system-design Tips to support decisions and communicate in your language. Planning, review, diagnosis, or retrospective analysis alone does not change your product or production settings. Failure testing can include focused local tests; production experiments require their own authorized scope.

## Usage

Clone this repository, then ask your agent from the product you want to work on. Replace the path with your local checkout:

```text
Use /path/to/system-design-skills/skills/system-design-planning/SKILL.md
to design this feature. Compare practical options and recommend an
architecture, failure handling, implementation sequence, and validation.
```

For other tasks, use the corresponding `SKILL.md` from the table. If installed in your agent, invoke a skill by its directory name, for example:

```text
$failure-scenario-testing Check whether retrying this webhook after a timeout can duplicate its effects, and add focused local tests where needed.
$architecture-change-review Review this diff for consistency, compatibility, load, and authorization risks.
$safe-migration-planning Plan this column migration while old and new application versions coexist, including abort and recovery conditions.
$capacity-planning Estimate what breaks first at 10x usage, including DB connections, worker concurrency, queue recovery, and one-zone failure.
$incident-learning Use these logs and the incident timeline to explain the contributing factors and propose verifiable improvements.
```

## Included Tips

Each skill bundles the same 134 English Tips with explanations, trade-offs, and source links, extracted from the `system-design-skill-developer` learning catalog. Every skill works independently of this repository's other skills and the original catalog.

The helper requires Python 3, with no additional dependencies. For example, from this repository's root:

```sh
python3 skills/system-design-planning/scripts/tips.py search webhook
python3 skills/system-design-planning/scripts/tips.py show webhook-verification idempotency-keys
```

Maintain the canonical bundle in `system-design-diagnosis`, then synchronize the standalone copies:

```sh
python3 skills/system-design-diagnosis/scripts/tips.py refresh --source /path/to/catalog.en.json
python3 scripts/sync_tips.py
python3 scripts/sync_tips.py --check
```

Review the generated diff after updates. Tips are guidance; verify relevant product versions and primary sources before applying them.

## License

[MIT](LICENSE). Linked third-party references retain their own licenses.
