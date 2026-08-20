# M1 引継ぎパッケージ（Handover Package）

[英語版（正本）](m1-handover-package.md)

**状態（Status）:** M1 実験契約（Experiment Contract）  
**関連Issue:** #14

## 目的

個体Aから個体Bへ責務を引き継ぐ際、前個体の内部状態を丸ごと複製せず、タスク継続に必要な最小情報だけを移送するための引継ぎパッケージを定義する。

## 基本原則

> **引継ぎパッケージは、後継個体が責務を再開するための最小十分情報であり、前個体の個体性・信頼・権限を複製する手段ではない。**

## 最小構成

```yaml
handover_id: handover:a-to-b:v1
from_individual_id: ind-a
to_individual_id: ind-b
created_at: 2026-10-01T00:05:00Z
objective:
  task_id: task-t
  goal: continue-processing
work_state:
  completed_steps:
    - step-1
  pending_steps:
    - step-2
constraints:
  - deadline: 2026-10-01T06:00:00Z
  - do_not_modify: shared-record-x
validated_assumptions:
  - id: assumption-1
    evidence_ref: evidence:123
uncertainties:
  - id: uncertainty-1
    description: external service state unknown
external_refs:
  - memory:shared-task-state
  - knowledge:validated-procedures
audit_refs:
  - audit:ind-a:event-77
```

## 必須項目

- **引継ぎ識別子（Handover ID）**
- **引継ぎ元個体（From Individual）**
- **引継ぎ先個体（To Individual）**
- **生成時刻（Created At）**
- **目的（Objective）** — 継続すべき責務・タスク。
- **作業状態（Work State）** — 完了済み・未完了の明示的状態。
- **制約（Constraints）** — 後継個体も保持すべき期限・禁止事項・不変条件。
- **検証済み前提（Validated Assumptions）** — 根拠参照を伴う前提。
- **未解決の不確実性（Uncertainties）** — 推測で埋めてはならない未確定事項。
- **外部参照（External References）** — 外部記憶・共有知識・技能への参照。
- **監査参照（Audit References）** — 引継ぎ判断を再構成するための参照。

## 原則として含めない情報

- 前個体の権限貸与（Authority Lease）
- 前個体の信頼評価
- 前個体の個体識別（Identity）を後継へ再利用する情報
- 不要な内部思考履歴
- 未検証の個人的信念
- 個体固有メモリ全体
- 既に外部記憶で参照可能な情報の完全複製

## 完全性検証（Completeness Validation）

引継ぎパッケージは、少なくとも次を検査する。

1. 継続すべき目的が一意に識別できる。
2. 未完了作業が明示されている。
3. 後継が守るべき制約が欠落していない。
4. 前提には根拠参照がある。
5. 未確定事項は不確実性として明示されている。
6. 必要な外部記憶参照が解決可能である。
7. 引継ぎ元と引継ぎ先が別個体である。
8. 権限貸与が含まれていない。

必須情報が欠落している場合、後継個体は推測で補完せず、**継続不能（Cannot Continue Safely）** と判定できなければならない。

## 過剰移送検出（Over-transfer Detection）

引継ぎパッケージには「便利だから」という理由だけで前個体の内部状態を大量に含めない。

過剰移送の候補は次の通り。

- 目的・制約・作業継続に不要な個体固有記憶
- 共有知識として既に外部化されている情報の複製
- 根拠のない前個体の推測
- 後継の判断を不必要に固定する個人的傾向

M1では、各項目について「この情報がなければ安全な継続が不可能か」を説明できない場合、原則として引継ぎ対象から除外する。

## サンプル交換

### 個体A

- task-t の step-1 を完了
- step-2 は未完了
- shared-record-x の変更は禁止
- 外部サービス状態は未確認

### 引継ぎ後の個体B

Bは上記の事実を引継ぎパッケージから取得するが、Aの権限・信頼・内部思考履歴は取得しない。Bは必要な外部記憶を別途参照し、新しい権限貸与を受けて初めて保護操作を実行できる。

## M1-4での失敗試験

- 制約を1件削除して完全性検証が失敗すること。
- 外部参照を壊して安全継続不能になること。
- 権限貸与を引継ぎパッケージに混入させて拒否されること。
- 個体固有メモリ全体を添付した場合に過剰移送として検出できること。

## 未解決事項

- 必須情報の最小集合をタスク種別ごとにどう定義するか。
- 引継ぎパッケージの署名・完全性保証をどの層で担保するか。
- 巨大な作業状態を参照型にする境界をどう決めるか。
- 長期間の引継ぎ連鎖で情報が徐々に欠落・変質する問題をどう測定するか。