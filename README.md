# System Design Skills

既存プロダクトの設計を診断し、根拠と優先順位・選択肢を示して、次の対応を判断するためのスキル集。

## システムデザイン診断

[system-design-diagnosis](skills/system-design-diagnosis/SKILL.md) は、コード・設定・テスト・設計資料を調べ、重要な利用者操作を入口からデータ保存・外部連携まで追って診断する。

診断結果には次を含める。

- 対応順とP0〜P3の優先度、業務影響・発生条件・緊急性による判断根拠。
- 確認済み・条件付き・未確認の区別、証拠の確かさと確認範囲。
- 対応案の効果、工数・運用費、残るリスク、変更の影響と完了条件。
- 推奨案と、ユーザーが対応・追加調査・見送りを選べる具体的な質問。

未確認の重大リスクは、修正の優先度とは別に「先行確認」として扱う。情報がないことを欠陥の証明にせず、現状維持が妥当な設計も示す。診断の依頼だけでプロダクトの実装や本番設定を変更しない。

## 使い方

診断したいプロダクトの作業環境で、スキルの `SKILL.md` を指定して依頼する。パスはこのリポジトリを配置した場所に置き換える。

```text
/path/to/system-design-skills/skills/system-design-diagnosis/SKILL.md を使って、
このプロダクトのシステムデザインを診断してください。
改善の優先順位と判断根拠を示し、対応案・追加調査・見送りを比較して、
私が次の対応を選べるようにしてください。
```

対象を「課金Webhook」「CSV取込」「次のDB移行」などに絞って依頼することもできる。スキルとして読み込まれた環境での呼び出し名は `$system-design-diagnosis`。

## Tipsの参照と更新

`system-design-skill-developer` のカタログから、134件のTipの本文・設計での使いどころ・トレードオフ・出典を抽出して同梱。クイズ等の学習UI用データは含めない。通常の診断では元リポジトリへの接続は不要。

補助スクリプトはPython 3の標準ライブラリだけで動作する。このリポジトリのルートから実行する例：

```sh
python3 skills/system-design-diagnosis/scripts/tips.py search 再試行
python3 skills/system-design-diagnosis/scripts/tips.py show timeout-budget retry-amplification
python3 skills/system-design-diagnosis/scripts/tips.py refresh --source ../system-design-skill-developer/static/releases/v1/catalog.json
```

更新処理は同梱データと索引を再生成する。出典・原本のハッシュ・取り込み時刻を記録するが、技術内容の再レビューは行わない。更新後は差分を確認する。教材の推奨は一律の設計要件にせず、対象の要件・製品仕様・バージョンに照らして使う。

優先順位の詳細は[判断基準](skills/system-design-diagnosis/references/prioritization.md)、診断結果の構成は[出力ガイド](skills/system-design-diagnosis/references/report.md)を参照。
