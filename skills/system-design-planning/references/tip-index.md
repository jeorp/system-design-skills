# Tip Index

Source: `system-design-skill-developer` / `catalog.en.json`. Release: `v2-practice`. 212 Tips.
Imported at (UTC): 2026-10-25T10:09:35+00:00.

Source SHA-256: `95382ad3b8592a2f24d976f586f39374e4778786a943974815771d7869ed2c7a`.

Use this index to select Tips, then read their explanations, conditions, and trade-offs.
Titles are not universal requirements. Importing does not revalidate claims or guarantee current sources or product versions.
The bundled snapshot is self-contained; access to the source repository is not required.

```sh
python3 "<skill-dir>/scripts/tips.py" search retry
python3 "<skill-dir>/scripts/tips.py" show timeout-budget retry-amplification
```

## CS fundamentals

| ID | Topic |
| --- | --- |
| `floating-point-money` | Store money as floating point and 0.1 + 0.2 is not 0.3 |
| `utf8-bytes` | UTF-8 uses 1–4 bytes per code point; one visible character may contain several |
| `integer-id-overflow` | Signed 32-bit sequential IDs exhaust their range after about 2.1 billion allocations |
| `n-plus-one` | Loading related data per row turns one list into 1 + N queries (the N+1 problem) |
| `index-sargable` | Expressions on a column can prevent efficient range lookup in a plain B-tree |
| `isolation-levels` | Default isolation levels differ: PostgreSQL uses Read Committed, MySQL uses Repeatable Read |
| `sql-injection` | Build SQL by string concatenation and input runs as SQL (SQL injection) |
| `public-key-roles` | In public-key cryptography, encrypt with the recipient's public key and sign with your own private key |
| `cache-hit-ratio` | Raising a cache hit ratio from 90% to 99% cuts database reads to a tenth |
| `dns-ttl` | A DNS change does not reach everyone at once, so lower the TTL ahead of time |
| `sql-null-logic` | SQL NULL means unknown, and comparisons can silently exclude rows |
| `timestamps-business-dates` | Separate an event instant from a business calendar date |

## Performance & capacity

| ID | Topic |
| --- | --- |
| `latency-numbers` | Memorize latency gaps by orders of magnitude |
| `littles-law` | Mean concurrency = arrival rate × mean time in system (Little’s law) |
| `utilization-queueing` | 90% utilization is not headroom; waiting time explodes |
| `tail-latency` | Track p99 as well as the mean: fan-out that waits for every response inherits the slowest |
| `zone-headroom` | For one-AZ loss across three AZs, two-thirds of total capacity is a theoretical ceiling; add headroom |
| `load-test-realism` | Interpret load tests with representative data, caches, skew, and duration |
| `connection-pool-math` | Estimate configured DB connection ceilings as instances × processes × pool limit |
| `cross-az-transfer` | Traffic between AZs is billed, and replication multiplies it |

## Reliability

| ID | Topic |
| --- | --- |
| `timeout-budget` | Shorter timeouts downstream, and pass the remaining budget along |
| `retry-amplification` | Retries multiply across layers and amplify outages |
| `load-shedding` | Under overload, reject some requests quickly instead of serving all slowly |
| `cache-stampede` | An expiring hot key turns into a database stampede |
| `availability-math` | Estimate required dependency availability with a product only under an independence model |
| `blast-radius` | Shrink the blast radius by design, before the outage |
| `metastable-failure` | Some outages do not end when the load drops (metastable failures) |
| `idempotency-keys` | Retries of non-idempotent writes need deduplication such as idempotency keys |
| `request-cancellation` | Returning a timeout does not stop the work behind it |
| `unknown-write-outcomes` | A timed-out write may have an unknown outcome rather than a failure |

## Database design & transactions

| ID | Topic |
| --- | --- |
| `composite-index-order` | In a composite index, put equality columns first and range columns last |
| `foreign-key-index` | PostgreSQL does not index the referencing side of a foreign key for you |
| `lost-update` | Read, compute, write back, and a concurrent update disappears (lost update) |
| `write-skew` | Snapshot isolation still lets writes to different rows break invariants |
| `deadlock-lock-order` | Lock rows in different orders and you get deadlocks |
| `long-transactions` | Waiting for an external API after updating or locking rows prolongs row-lock holding |
| `ddl-lock-queue` | An ALTER TABLE waiting for its lock blocks every query that arrives after it |
| `database-constraints-races` | Checking before INSERT does not prevent duplicates; enforce a database constraint |
| `conditional-state-transitions` | Put the expected state in UPDATE instead of checking and then writing |

## Data consistency & storage

| ID | Topic |
| --- | --- |
| `dual-write-outbox` | Separate DB updates and message sends can succeed independently |
| `replication-lag` | Reading from async replicas can hide your own writes |
| `lsm-vs-btree` | Compare LSM and B-tree write, read, and amplification costs under real workloads |
| `backup-restore` | Replicas alone do not protect against accidental deletion; verify backups by restoring them |
| `saga` | Chain work across services with compensating steps (a saga) |
| `throttled-backfill` | Run big updates and deletes in small, throttled batches |

## Distributed systems & scale

| ID | Topic |
| --- | --- |
| `cap-pacelc` | CAP forces a choice only during a network partition |
| `quorum` | R + W > N guarantees intersecting read/write sets within the same replica set |
| `consistent-hashing` | hash mod N moves almost every key when you add one node |
| `hot-keys` | Adding shards never spreads a single hot key |
| `fencing-tokens` | A distributed lock cannot stop a client that missed its expiry |
| `clocks` | Machine clocks drift; don't rely on wall time for order or duration |
| `queue-backlog` | A queue does not remove overload; it defers it, and the debt comes due |
| `exactly-once-boundary` | Effects outside an exactly-once guarantee need their own deduplication |
| `dead-letter-recovery` | Moving a failed message aside does not complete the business operation |

## APIs & protocols

| ID | Topic |
| --- | --- |
| `http-method-semantics` | "Safe" and "idempotent" HTTP methods are what retries and automated clients rely on (RFC 9110) |
| `cursor-pagination` | Paginate lists with cursors, not OFFSET |
| `http-caching-defaults` | Without Cache-Control, caches guess how long to keep a response (RFC 9111) |
| `json-number-precision` | Large integers in JSON get silently rounded in JavaScript (RFC 8259) |
| `uuidv7` | Random UUIDv4 primary keys scatter writes across the index (RFC 9562) |
| `tls-early-data` | Requests sent in TLS 1.3 0-RTT can be replayed by an attacker (RFC 8446, RFC 8470) |
| `http2-load-balancing` | HTTP/2 and gRPC bundle requests onto one connection, so L4 load balancers skew load (RFC 9113) |
| `server-side-validation` | Validate again at the API boundary, even when the form validates |
| `api-error-contract` | Return an HTTP status and a stable error type instead of branching on prose |
| `patch-field-presence` | Distinguish omitted, null, zero, false, and empty strings in partial updates |
| `request-work-limits` | Limit work per request as well as the number of requests |

## Operations & cloud native

| ID | Topic |
| --- | --- |
| `container-resources` | CPU limits can throttle work; exceeding memory limits can lead to OOM termination |
| `autoscaling-lag` | Autoscaling takes effect minutes after the load arrives |
| `cold-start` | Serverless pays a startup cost on the first request (cold starts) |
| `graceful-shutdown` | Errors on every deploy? Check your shutdown |
| `health-check-depth` | Health checks that are too shallow or too deep both make outages worse |
| `pod-disruption-budget` | Without a PodDisruptionBudget, a node upgrade can stop a service's Pods all at once |
| `spot-interruptions` | Use spot instances assuming they will be taken away |
| `slo-burn-rate` | Page on SLO burn rate and complement it with preventive capacity alerts |
| `trace-propagation` | Carry one trace ID across services so logs connect |
| `metric-cardinality` | Put user IDs in metric labels and the time series explode |
| `autoscaling-downstream-limits` | Adding application instances can overload a shared database or API |

## Cloud-native development

| ID | Topic |
| --- | --- |
| `build-once-promote` | Build the image once and promote that same image to production |
| `image-digest` | Tags can be overwritten. Pin production images by digest |
| `container-pid1` | When a shell is PID 1, check that SIGTERM reaches the application |
| `kubernetes-secrets` | Kubernetes Secrets are not encrypted by default |
| `gitops-drift` | Hand-fix production and the next sync undoes it, or the drift lingers |
| `iac-replacement` | IaC replacement creates a different resource: check data restoration and retention settings |
| `sidecar-startup` | If the app starts before its sidecar proxy, its first calls fail |

## Development & release

| ID | Topic |
| --- | --- |
| `trunk-based-development` | The longer a branch lives, the more integration pain you pay all at once later |
| `small-changes` | Big changes wait longer for review and get reviewed less carefully |
| `contract-testing` | Check service compatibility early with contracts and retain key end-to-end tests |
| `flaky-tests` | If 500 tests fail independently with probability 0.1%, about 40% of CI runs fail |
| `progressive-rollout` | Roll out changes gradually, and keep rollback instant |
| `feature-flag-debt` | A feature flag you are done with stays a live branch in production until you delete it |
| `expand-contract` | Ship schema changes as expand, migrate, contract |
| `decision-records` | Record design decisions with the rejected options and the way back |
| `delivery-metrics` | Delivery speed and stability are not a trade-off; measure them together as a set |
| `database-integration-tests` | Passing mocks do not prove SQL and transaction behavior |
| `configuration-startup-validation` | Catch invalid configuration at startup before the first user does |
| `rollback-data-compatibility` | Rolling back code does not undo data written by the new version |

## DevOps & in-house development

| ID | Topic |
| --- | --- |
| `devops-service-ownership` | Service ownership needs coverage, authority, and a backup |
| `devops-ci-feedback-path` | Measure CI feedback from queue entry to actionable results |
| `devops-deploy-serialization` | Serialize deployment writes and guard against stale arrivals |
| `devops-incident-command` | During incidents, assign recovery work, coordination, and communication |
| `devops-postmortem-actions` | Close postmortems with system changes and verification |
| `devops-toil-budget` | Prioritize repetitive operations by hands-on time and automation upkeep |
| `inhouse-team-boundaries` | Assess team autonomy by independent validation and delivery |
| `inhouse-knowledge-transfer` | Verify knowledge transfer by having the receiving team deliver a change |
| `inhouse-legacy-seams` | Start legacy replacement with a switchable boundary and a source of truth |
| `inhouse-platform-golden-path` | Design the update path alongside internal project templates |
| `inhouse-platform-product` | Measure internal platform value through user friction and waiting |
| `inhouse-build-buy-exit` | Compare build and buy through maintenance and exit, beyond setup |
| `inhouse-repository-delivery-map` | Trace a code path from its entry point to the revision running in production |
| `inhouse-local-bootstrap` | Verify development setup by starting from a clean environment |
| `inhouse-reproducible-fixtures` | Build test data from the conditions under test without copying personal data |
| `inhouse-preview-isolation` | Isolate preview data and external effects alongside preview URLs |
| `inhouse-dependency-lockfiles` | Align dependencies with a lockfile and validate upgrades as explicit changes |
| `inhouse-module-boundary-tests` | Enforce module boundaries with dependency checks alongside diagrams |
| `inhouse-legacy-characterization` | Capture current behavior before changing poorly understood legacy code |
| `inhouse-migration-rehearsal` | Rehearse database migrations with volume, invalid data, and concurrent work |
| `inhouse-terraform-state-locking` | Investigate active work before clearing a Terraform state lock |
| `inhouse-ci-trust-boundaries` | Keep production mutation privileges away from jobs executing PR code |
| `inhouse-development-secret-scope` | Scope development secrets separately from production |
| `inhouse-observability-acceptance` | Include the ability to identify failing behavior and revisions in completion criteria |
| `inhouse-review-learning-loop` | Use reviews to share rationale and verification alongside fixes |
| `inhouse-library-compatibility` | Validate shared-library changes through consumer behavior, beyond version numbers |
| `inhouse-debt-change-evidence` | Prioritize technical debt through observed change and incident costs |

## Authentication & authorization

| ID | Topic |
| --- | --- |
| `password-hashing` | Make password hashing slow on purpose, and put that slowness in your login capacity plan |
| `credential-stuffing` | Reused leaked passwords slip past both per-IP limits and account lockout |
| `oauth-pkce` | SPAs and mobile apps cannot keep secrets: bind the authorization code to the requesting app with PKCE |
| `token-audience` | A token with a valid signature is not necessarily meant for you: check aud and iss |
| `jwt-revocation` | Self-contained JWT verification alone does not learn about later revocation |
| `refresh-token-rotation` | Rotate refresh tokens on every use, and revoke the whole set when a used one comes back |
| `object-authorization` | Hard-to-guess IDs are not a substitute for authorization |
| `permission-consistency` | Right after you revoke access, a cached authorization check still says yes (the new enemy problem) |
| `async-job-authorization` | A queued job may outlive the permission that allowed it |

## Security

| ID | Topic |
| --- | --- |
| `ssrf` | A feature that makes your server fetch URLs is a door into your internal network |
| `short-lived-credentials` | Limit credential lifetime and permissions to reduce exposure after leakage |
| `webhook-verification` | Until you check the signature, you do not know who sent a Webhook |
| `envelope-encryption` | Encrypt data with a data key, and have the KMS only wrap that key |
| `safe-structured-logs` | Keep tokens and complete request bodies out of diagnostic logs |
| `threat-modeling-boundaries` | Map protected data and trust boundaries before building (threat modeling) |
| `vulnerability-remediation-loop` | Track vulnerabilities through production remediation, beyond detection |
| `privileged-access-lifecycle` | Design administrator access from granting through removal |
| `security-detection-coverage` | Test that audit logging detects the operations you need to see |
| `incident-response-rehearsal` | Rehearse incident contacts and decision authority before an incident |
| `leaked-secret-response` | Stop use of an exposed secret before relying on file cleanup |
| `incident-containment-evidence` | Contain a suspected compromise while preserving evidence |
| `incident-scope-communication` | Communicate verified impact separately from uncertain scope |
| `secure-incident-recovery` | Verify safe recovery by closing re-entry paths before restoring service |
| `security-postmortem-actions` | Turn incident lessons into owned improvements with verification criteria |
| `tenant-cache-isolation` | Tenant-separated databases can still leak through shared cache keys |

## AI & LLM systems

| ID | Topic |
| --- | --- |
| `llm-output-latency` | When LLM decoding dominates, shorter output reduces completion latency |
| `prompt-caching` | For prefix-based prompt caching, place stable content first |
| `kv-cache-concurrency` | KV-cache capacity and concurrency meeting latency goals are different limits |
| `rag-retrieval-first` | When RAG answers wrong, first check whether retrieval missed |
| `filtered-vector-search` | Adding a filter to vector search can leave you short of results |
| `llm-evals` | Check prompt and model changes for regressions on an evaluation set before shipping |
| `prompt-injection` | Treat outside text an LLM reads as data, not instructions (prompt injection) |
| `agent-step-reliability` | Estimate end-to-end step success with explicit independence or conditional probabilities |
| `llm-fallback` | Decide how to wait and where to fall back before an LLM API rate-limits or overloads |

## FDE & engineering in the AI era

| ID | Topic |
| --- | --- |
| `fde-outcome-framing` | Translate “we want AI” into whose outcome should improve |
| `fde-workflow-observation` | After hearing about a workflow, follow one real case end to end |
| `fde-domain-data-meaning` | Align business language with data: “complete” can mean different things |
| `fde-risk-first-experiments` | Use prototypes to test the assumptions that could sink the project |
| `ai-simplest-baseline` | Compare AI with a rules-based or search-only baseline |
| `ai-workflow-total-value` | A faster AI response may still leave the whole task slower |
| `ai-task-context-contract` | Give AI the goal, constraints, and verification method together |
| `ai-generated-change-verification` | Verify AI-generated changes with counterexamples derived from requirements |
| `ai-debug-evidence-loop` | Treat AI’s proposed causes as hypotheses and narrow them with evidence |
| `ai-autonomy-action-boundaries` | Scope AI autonomy by action impact and recovery options |
| `fde-adoption-operational-handoff` | Plan adoption so local staff can keep using and recovering the service |
| `fde-field-learning-reuse` | Return field learning to the product with the conditions for reuse |
| `fde-stakeholder-decision-map` | Map who can decide on workflow, data, and operations beyond the customer contact |
| `fde-access-dependency-plan` | Track access dependencies with owners, dates, and proof of usable connectivity |
| `fde-data-readiness-profile` | Measure whether available data is timely and fit for the target workflow |
| `fde-scope-change-negotiation` | Reprioritize requests with their impact on goals, dates, and quality |
| `fde-business-acceptance-cases` | Agree business acceptance using concrete inputs and expected outcomes |
| `fde-external-integration-contract` | Agree integration semantics for acceptance, completion, and redelivery |
| `fde-shadow-to-pilot` | Shadow evaluation and a live pilot answer different questions |
| `fde-business-result-reconciliation` | Reconcile business IDs and states as well as counts after migration or sync |
| `fde-evidence-decision-updates` | Report evidence and required decisions alongside delivery progress |

## AI architecture

| ID | Topic |
| --- | --- |
| `ai-architecture-workflow-or-agent` | Keep control in code when the next step is already known |
| `ai-architecture-rag-or-tuning` | Separate updating knowledge from changing model behavior |
| `ai-architecture-retrieval-authorization` | Enforce RAG authorization before evidence crosses a trust boundary |
| `ai-architecture-output-contracts` | Schema-valid JSON can still contain unacceptable business values |
| `ai-architecture-model-routing` | Measure routing errors and duplicate work in model cascades |
| `ai-architecture-context-budget` | Budget context for tool results and output as well as history |
| `ai-architecture-end-to-end-latency` | A fast first token does not imply fast answer or action completion |
| `ai-architecture-release-manifest` | Record AI releases as a combination of model, prompt, and retrieval assets |
| `ai-architecture-quality-gates` | Use task-specific release gates for failures hidden by averages |
| `ai-architecture-observability` | Connect AI execution traces to business outcomes |
| `ai-architecture-durable-agent-execution` | Saving conversation history does not prevent duplicate side effects |
| `ai-architecture-inference-hosting` | Choose inference hosting by operating requirements, not unit price alone |

## ETL & data platforms

| ID | Topic |
| --- | --- |
| `etl-elt-data-boundaries` | Choose ETL or ELT by transformation location and raw-data boundaries |
| `etl-incremental-cursor` | Incremental cursors must distinguish update time from commit order |
| `etl-cdc-snapshot-handoff` | Start CDC with a connected snapshot and change-log position |
| `etl-idempotent-publication` | Repeatable ETL fixes the input version and publication unit |
| `etl-event-time-late-data` | Aggregate late data using event time and arrival time separately |
| `etl-schema-contracts` | Schema changes need contracts for meaning as well as types |
| `etl-grain-reconciliation` | Validate ETL grain and totals as well as row counts |
| `etl-backfill-isolation` | Backfills need publication conflict control as well as capacity limits |
| `etl-freshness-completeness` | Monitor ETL success, freshness, and completeness separately |
| `etl-partition-pruning` | Partitions help when queries actually prune the scanned range |
| `etl-business-data-interval` | Choose reprocessing intervals by business time, not execution day |
| `etl-historical-dimensions` | Decide whether historical revenue uses past or current attributes |

## Interview follow-ups

| ID | Topic |
| --- | --- |
| `unique-id` | "How would you generate IDs?" |
| `cache-down` | "What happens if the whole cache goes down?" |
| `region-failure` | "What if an entire region goes down?" |
| `single-point-of-failure` | "Where is the single point of failure?" |
| `realtime-delivery` | "How do you deliver new messages in real time?" |
| `leaderboard` | "How would you build a real-time leaderboard?" |
| `nearby-search` | "How would you find nearby places?" |
| `data-store-choice` | "Why did you choose that database?" |
| `ten-x-scale` | "If traffic grew 10x, what breaks first?" |
| `monitoring-plan` | "How would you monitor this system?" |
| `feed-fanout` | "Do you build timelines when a post is written, or when it is read?" |
