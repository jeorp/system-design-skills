# Tip索引

元教材：`system-design-skill-developer` / `catalog.json`。releaseId：`v2-practice`。134件。
取り込み時刻（UTC）：2026-10-25T08:48:42+00:00。

原本のSHA-256：`2e45ba8707b23589362812a4c0862647de0795242a155c920ec290cd825b7172`。

この索引は選択用。見出しを普遍的な要件として使わず、必要なIDの本文・条件・比較を読む。
取り込み日は再レビュー日ではなく、出典の現在性や対象製品のバージョンを保証しない。
同梱snapshotだけで利用でき、元リポジトリへの接続は不要。

```sh
python3 "<skill-dir>/scripts/tips.py" search 再試行
python3 "<skill-dir>/scripts/tips.py" show timeout-budget retry-amplification
```

## CSの基礎

| ID | 話題 |
| --- | --- |
| `floating-point-money` | 金額を浮動小数点数で持つと、0.1 + 0.2 が 0.3 にならない |
| `utf8-bytes` | UTF-8はコードポイントごとに1〜4バイト。見た目の1文字は複数になることもある |
| `integer-id-overflow` | 符号付き32ビットの連番IDは、約21億の採番で上限に達する |
| `n-plus-one` | 一覧の1件ごとに関連データを読むと、クエリが「1 + 件数」回になる（N+1問題） |
| `index-sargable` | 列を加工する条件は、通常のB木で検索範囲を絞りにくい |
| `isolation-levels` | 分離レベルの既定はDBで違う。PostgreSQLはRead Committed、MySQLはRepeatable Read |
| `sql-injection` | SQLを文字列の連結で組み立てると、入力がSQLの命令として実行される（SQLインジェクション） |
| `public-key-roles` | 公開鍵暗号では、暗号化は相手の公開鍵で、署名は自分の秘密鍵で行う |
| `cache-hit-ratio` | キャッシュのヒット率を90%から99%に上げると、DBへの読み取りは10分の1になる |
| `dns-ttl` | DNSの切り替えは、すぐには全員に届かない。前もってTTLを短くしておく |
| `sql-null-logic` | SQLのNULLは「空」ではなく不明。比較すると行が消える |
| `timestamps-business-dates` | 「発生した瞬間」と「業務上の日付」を同じ日時型にしない |

## 性能・容量計画

| ID | 話題 |
| --- | --- |
| `latency-numbers` | メモリ・SSD・ネットワークの速度差は桁で覚える |
| `littles-law` | 平均同時処理数 = 到着率 × 平均滞在時間（リトルの法則） |
| `utilization-queueing` | 利用率90%は「まだ余裕」ではない。待ち時間は急に伸びる |
| `tail-latency` | 平均に加えてp99も見る。全応答を待つファンアウトは遅い1台に影響される |
| `zone-headroom` | 3AZで1AZ喪失に備えるなら、総容量の2/3を理論上限に、さらに余裕を持つ |
| `load-test-realism` | 負荷試験はデータ量・キャッシュ・偏り・時間をそろえて解釈する |
| `connection-pool-math` | DB接続の設定上限は「台数 × プロセス数 × プール上限」で見積もる |
| `cross-az-transfer` | AZをまたぐ通信には料金がかかり、複製の数だけ増える |

## 信頼性・障害対策

| ID | 話題 |
| --- | --- |
| `timeout-budget` | タイムアウトは下流ほど短く、残り時間を引き継ぐ |
| `retry-amplification` | 再試行は各層で掛け算になり、障害を大きくする |
| `load-shedding` | 過負荷では、全部を遅く処理するより一部を早く断る |
| `cache-stampede` | 人気キーの期限切れは、DBへの一斉アクセスになる |
| `availability-math` | 必須依存の可用性の積は、障害が独立というモデルで見積もる |
| `blast-radius` | 障害の影響範囲（ブラスト半径）を、先に設計で小さくしておく |
| `metastable-failure` | 負荷が下がっても戻らない障害がある（メタステーブル障害） |
| `idempotency-keys` | 非冪等な書き込みの再試行には、冪等キーなどの重複対策が要る |
| `request-cancellation` | タイムアウトを返すだけでは裏の仕事は止まらない |

## DB設計・トランザクション

| ID | 話題 |
| --- | --- |
| `composite-index-order` | 複合インデックスは、等しい値で絞る列を先に、範囲で絞る列を後に置く |
| `foreign-key-index` | PostgreSQLは、外部キーの参照する側の列にインデックスを自動で作らない |
| `lost-update` | 読んで計算して書き戻すと、同時の更新が消える（lost update） |
| `write-skew` | スナップショット分離でも、別々の行への書き込みで不変条件が壊れる |
| `deadlock-lock-order` | 行をロックする順番がそろっていないと、デッドロックになる |
| `long-transactions` | 更新・ロックの後に外部APIを待つと、行ロックの保持が長くなる |
| `ddl-lock-queue` | ALTER TABLEはロックを待っている間も、後から来たクエリを止める |
| `database-constraints-races` | 「存在しなければINSERT」だけでは重複する。最後はDB制約で守る |
| `conditional-state-transitions` | 状態を読んでから更新せず、「今もその状態なら」をUPDATEに入れる |

## データ整合性・ストレージ

| ID | 話題 |
| --- | --- |
| `dual-write-outbox` | 別々のDB更新とメッセージ送信は、片方だけ成功しうる |
| `replication-lag` | 非同期レプリカから読むと、自分の書き込みが見えないことがある |
| `lsm-vs-btree` | LSMとB木は、書き込み・読み取り・増幅を実負荷で比べる |
| `backup-restore` | レプリカだけでは誤削除に備えられない。バックアップは復元して確かめる |
| `saga` | サービスをまたぐ処理は、取り消しの手順（サーガ）でつなぐ |
| `throttled-backfill` | 大量の更新・削除は、小分けにして様子を見ながら流す |

## 分散システム・スケール

| ID | 話題 |
| --- | --- |
| `cap-pacelc` | CAPの選択はネットワーク分断のときに迫られる |
| `quorum` | R＋W＞Nが保証するのは、同じレプリカ集合内での読み書き集合の交差 |
| `consistent-hashing` | hash mod N は、ノードを1台足すだけでほぼ全キーが動く |
| `hot-keys` | シャードを増やしても、1つのホットキーは分散しない |
| `fencing-tokens` | 分散ロックは、期限切れに気づかないクライアントを止められない |
| `clocks` | マシンの時計はずれる。順序や経過時間を壁時計で決めない |
| `queue-backlog` | キューは過負荷を消さない。先送りした分は、あとで返す必要がある |
| `exactly-once-boundary` | exactly-onceの保証範囲の外では、別途重複対策が要る |

## API・プロトコル

| ID | 話題 |
| --- | --- |
| `http-method-semantics` | HTTPメソッドの「安全」と「冪等」は、再試行と自動アクセスの前提になっている（RFC 9110） |
| `cursor-pagination` | 一覧はOFFSETではなく、カーソルでページングする |
| `http-caching-defaults` | Cache-Controlを書かないと、キャッシュは推測で期限を決める（RFC 9111） |
| `json-number-precision` | JSONの大きな整数は、JavaScriptで黙って丸められる（RFC 8259） |
| `uuidv7` | ランダムなUUIDv4を主キーにすると、インデックスへの書き込みが散らばる（RFC 9562） |
| `tls-early-data` | TLS 1.3の0-RTTで送ったリクエストは、攻撃者に再送されうる（RFC 8446・RFC 8470） |
| `http2-load-balancing` | HTTP/2とgRPCは接続を1本に束ねるので、L4のロードバランサーでは負荷が偏る（RFC 9113） |
| `server-side-validation` | 画面の入力チェックを通っても、APIで検証し直す |
| `api-error-contract` | エラー文言で分岐しない。HTTPステータスと安定した種類を返す |
| `patch-field-presence` | 部分更新で「未指定」「null」「0・false・空文字」を混ぜない |
| `request-work-limits` | APIの上限はリクエスト数だけでなく「1件の重さ」にも付ける |

## 運用・クラウドネイティブ

| ID | 話題 |
| --- | --- |
| `container-resources` | CPUの上限はスロットリング、メモリの上限超過はOOMの原因になる |
| `autoscaling-lag` | オートスケールは、負荷が来てから数分遅れて効く |
| `cold-start` | サーバーレスの最初の1回は、起動の時間を払う（コールドスタート） |
| `graceful-shutdown` | デプロイのたびにエラーが出るなら、終了処理を疑う |
| `health-check-depth` | ヘルスチェックは浅すぎても深すぎても、障害を大きくする |
| `pod-disruption-budget` | ノードの更新は、PodDisruptionBudgetがないと同じサービスのPodをまとめて止めうる |
| `spot-interruptions` | スポットのインスタンスは、取り上げられる前提で使う |
| `slo-burn-rate` | SLOの消費速度で呼び出し、容量枯渇などの予防的警告も併用する |
| `trace-propagation` | リクエストIDを全サービスに引き継ぎ、ログをつなげる |
| `metric-cardinality` | メトリクスのラベルにユーザーIDを入れると、時系列が爆発する |

## クラウドネイティブ開発

| ID | 話題 |
| --- | --- |
| `build-once-promote` | イメージは1回だけビルドし、同じものを本番まで進める |
| `image-digest` | タグは書き換えられる。本番のイメージはダイジェストで指定する |
| `container-pid1` | シェルがPID 1の起動方式では、SIGTERMがアプリへ届くか確認する |
| `kubernetes-secrets` | KubernetesのSecretは、そのままでは暗号化されていない |
| `gitops-drift` | 本番を手で直すと、次の同期で元に戻るか、ずれたまま残る |
| `iac-replacement` | IaCの置き換えは別資源の作成。データの復元・保持指定を確認する |
| `sidecar-startup` | サイドカーのプロキシより先にアプリが動き出すと、最初の通信が失敗する |

## 開発・リリース

| ID | 話題 |
| --- | --- |
| `trunk-based-development` | 長く生きるブランチほど、統合の痛みはまとめて後払いになる |
| `small-changes` | 大きな変更は、レビューを長く待つうえに見落としも増える |
| `contract-testing` | サービス間の互換性は契約テストで早く確認し、主要なE2Eも残す |
| `flaky-tests` | 独立に0.1%で落ちるテスト500本なら、CIが赤になる確率は約4割 |
| `progressive-rollout` | 本番への変更は少しずつ出し、すぐ戻せるようにする |
| `feature-flag-debt` | 使い終わった機能フラグは、消すまで本番の分岐として残り続ける |
| `expand-contract` | スキーマ変更は「追加→移行→削除」に分けて出す |
| `decision-records` | 設計の決定は「採用しなかった案」と「戻し方」と一緒に残す |
| `delivery-metrics` | 開発の速さと安定は引き換えではない。同じ指標の組で一緒に測る |
| `database-integration-tests` | モックが通っても、SQLとトランザクションが正しいとは限らない |
| `configuration-startup-validation` | 設定の誤りは最初の利用者ではなく、起動時に見つける |

## 認証・認可

| ID | 話題 |
| --- | --- |
| `password-hashing` | パスワードのハッシュはわざと遅くする。その遅さは、ログインの容量計画に入れる |
| `credential-stuffing` | 漏れたパスワードの使い回しは、IPごとの制限でもアカウントのロックでも止まりにくい |
| `oauth-pkce` | SPAとモバイルアプリは秘密を守れない。認可コードはPKCEで、要求したアプリに結びつける |
| `token-audience` | 署名が正しいトークンでも、自分宛てとは限らない（audとissを確かめる） |
| `jwt-revocation` | JWTの自己完結した検証だけでは、発行後の失効は自動で伝わらない |
| `refresh-token-rotation` | リフレッシュトークンは使うたびに替え、使用済みのものが届いたら一式を無効にする |
| `object-authorization` | 推測しにくいIDは、認可の代わりにならない |
| `permission-consistency` | 権限を外した直後でも、キャッシュした認可は古い許可を返す（new enemy problem） |

## セキュリティ

| ID | 話題 |
| --- | --- |
| `ssrf` | サーバーにURLを取りに行かせる機能は、内側のネットワークへの入口になる |
| `short-lived-credentials` | 認証情報の漏洩に備え、有効期間と権限の広さを小さくする |
| `webhook-verification` | Webhookは、署名を確かめるまで誰が送ったかわからない |
| `envelope-encryption` | データはデータキーで暗号化し、KMSにはデータキーを包ませるだけにする |
| `safe-structured-logs` | 障害調査のログに、トークンやリクエスト全文を残さない |
| `threat-modeling-boundaries` | 作る前に、守るデータと信頼の境界を図にする（脅威モデリング） |
| `vulnerability-remediation-loop` | 脆弱性は、検出件数ではなく本番での修正完了まで追う |
| `privileged-access-lifecycle` | 管理者の権限は、付けるときから外すときまで設計する |
| `security-detection-coverage` | 監査ログは「取っている」だけでなく、必要な操作を検知できるか試す |
| `incident-response-rehearsal` | インシデントの連絡先と判断権限は、起こる前に試しておく |
| `leaked-secret-response` | 秘密情報が漏れたら、ファイルの削除より先に利用を止める |
| `incident-containment-evidence` | 侵害の疑いでは、封じ込めと証拠保全を並行して進める |
| `incident-scope-communication` | 影響調査では、確認できた事実と不明な範囲を分けて伝える |
| `secure-incident-recovery` | 復旧は「動いた」で終えず、再侵入の経路を閉じて確かめる |
| `security-postmortem-actions` | 再発防止は「注意する」ではなく、担当と確認条件を持つ改善にする |

## AI・LLMシステム

| ID | 話題 |
| --- | --- |
| `llm-output-latency` | LLMのデコードが支配的なら、出力を短くすると応答完了が速くなる |
| `prompt-caching` | プレフィックス型のプロンプトキャッシュは、固定部分を先頭へ置く |
| `kv-cache-concurrency` | KVキャッシュの収容上限と、遅延目標を満たすLLM同時処理数は別 |
| `rag-retrieval-first` | RAGの間違いは、まず検索で起きていないかを測る |
| `filtered-vector-search` | ベクトル検索に絞り込みを足すと、結果が足りなくなることがある |
| `llm-evals` | プロンプトやモデルの変更は、評価セットで回帰を確かめてから出す |
| `prompt-injection` | LLMに読ませる外部の文章は、命令ではなくデータとして扱う（プロンプトインジェクション） |
| `agent-step-reliability` | 全手順の成功率は、独立性や条件付き成功率を明示して見積もる |
| `llm-fallback` | LLMのAPIのレート制限と過負荷には、待ち方と切り替え先を先に決めておく |

## 面接で聞かれるケース

| ID | 話題 |
| --- | --- |
| `unique-id` | 「IDはどう採番しますか？」 |
| `cache-down` | 「キャッシュが全部落ちたらどうなりますか？」 |
| `region-failure` | 「リージョンが丸ごと落ちたら？」 |
| `single-point-of-failure` | 「この設計の単一障害点はどこですか？」 |
| `realtime-delivery` | 「新着メッセージをどうリアルタイムに届けますか？」 |
| `leaderboard` | 「リアルタイムのランキングをどう作りますか？」 |
| `nearby-search` | 「近くのお店をどう検索しますか？」 |
| `data-store-choice` | 「なぜそのデータベースを選んだのですか？」 |
| `ten-x-scale` | 「トラフィックが10倍になったら、どこから壊れますか？」 |
| `monitoring-plan` | 「このシステムをどう監視しますか？」 |
| `feed-fanout` | 「タイムラインは、投稿時と読み込み時のどちらで作りますか？」 |
