# Tip Index

Source: `system-design-skill-developer` / `catalog.en.json`. Release: `v2-practice`. 134 Tips.
Imported at (UTC): 2026-10-25T08:57:57+00:00.

Source SHA-256: `51e26c9f4336d14bc9041b733a998d065349c0b2b1595159efddfc4bd6ff4ea2`.

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
