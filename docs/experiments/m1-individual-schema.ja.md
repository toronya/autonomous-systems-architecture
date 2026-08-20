# M1 個体メタデータと権限貸与の最小スキーマ（Individual Metadata and Authority Lease Schema）

[英語版（正本）](m1-individual-schema.md)

**状態（Status）:** M1 実験契約（Experiment Contract）  
**関連Issue:** #13

## 目的

この文書は、M1の交換可能個体PoCで必要な個体識別、寿命、状態、系譜、外部記憶参照、権限貸与を、実装言語に依存せず機械的に扱うための最小スキーマを定義する。

## 個体レコード（Individual Record）

必須項目は次の通り。

```yaml
individual_id: ind-b
lineage:
  generation: 2
  parent_individual_id: ind-a
created_at: 2026-10-01T00:00:00Z
expires_at: 2026-12-31T00:00:00Z
lifecycle_state: candidate
cognitive_profile_ref: profile:v1
external_memory_refs:
  - memory:shared-task-state
  - knowledge:validated-procedures
audit_lineage_ref: audit:ind-b
handover:
  from_individual_id: ind-a
  package_ref: handover:a-to-b:v1
authority_leases: []
```

### 必須項目

- **個体識別子（Individual ID）** — 他個体と重複しない識別子。
- **世代（Generation）** — 系譜上の世代番号。
- **生成時刻（Created At）** — 個体が生成された時刻。
- **失効時刻（Expires At）** — 個体として存続できる期限または期限評価時刻。
- **ライフサイクル状態（Lifecycle State）** — 候補、安定、退役移行、退役済み等。
- **認知特性参照（Cognitive Profile Reference）** — 評価対象となる認知特性の識別子。
- **外部記憶参照（External Memory References）** — 個体から独立した情報資産への参照。
- **監査履歴参照（Audit Lineage Reference）** — 個体の判断・状態遷移・権限変更を追跡する参照。
- **権限貸与（Authority Leases）** — 現在有効な権限の一覧。空配列を許可する。

### 任意項目

- **親個体識別子（Parent Individual ID）** — 後継関係を持つ場合のみ設定する。
- **引継ぎ元（Handover From）** — 前個体から責務を引き継ぐ場合のみ設定する。
- **引継ぎパッケージ参照（Handover Package Reference）** — 引継ぎパッケージが存在する場合のみ設定する。

## 権限貸与レコード（Authority Lease Record）

権限は個体レコードへ直接埋め込む永続属性ではなく、期限付きの貸与として表現する。

```yaml
lease_id: lease-b-task-execute
individual_id: ind-b
capability: task.execute
scope:
  task_id: task-t
issued_at: 2026-10-01T00:10:00Z
expires_at: 2026-10-01T06:10:00Z
issued_by: governance:m1-test
status: active
```

必須項目は次の通り。

- **貸与識別子（Lease ID）**
- **対象個体（Individual ID）**
- **能力（Capability）**
- **適用範囲（Scope）**
- **発行時刻（Issued At）**
- **失効時刻（Expires At）**
- **発行主体（Issued By）**
- **状態（Status）**

## 不変条件（Invariants）

1. 個体識別子は一意であり、後継個体が前個体の識別子を再利用してはならない。
2. 後継個体は前個体の権限貸与をコピーしてはならない。
3. 権限貸与の対象個体識別子は明示されなければならない。
4. 退役済み（Retired）個体に有効な保護操作権限を残してはならない。
5. 個体の失効時刻を超える権限貸与は、明示的な例外規則なしに有効として扱ってはならない。
6. 引継ぎ元個体と引継ぎ先個体は異なる個体識別子を持つ。
7. 系譜情報は個体性を説明するための参照であり、信頼や権限を自動継承する根拠にしてはならない。

## サンプル: 個体A

```yaml
individual_id: ind-a
lineage:
  generation: 1
  parent_individual_id: null
created_at: 2026-10-01T00:00:00Z
expires_at: 2026-10-31T00:00:00Z
lifecycle_state: retiring
cognitive_profile_ref: profile:v1
external_memory_refs:
  - memory:shared-task-state
audit_lineage_ref: audit:ind-a
handover:
  from_individual_id: null
  package_ref: handover:a-to-b:v1
authority_leases: []
```

## サンプル: 個体B

```yaml
individual_id: ind-b
lineage:
  generation: 2
  parent_individual_id: ind-a
created_at: 2026-10-01T00:05:00Z
expires_at: 2026-11-30T00:00:00Z
lifecycle_state: candidate
cognitive_profile_ref: profile:v1
external_memory_refs:
  - memory:shared-task-state
audit_lineage_ref: audit:ind-b
handover:
  from_individual_id: ind-a
  package_ref: handover:a-to-b:v1
authority_leases: []
```

この時点では、Bには権限貸与が存在しない。BがAと同じ役割を担う場合でも、新しい権限貸与を別途発行する必要がある。

## M1-4での最低検証

- 個体AとBを別識別子として生成できる。
- Aの権限貸与をBへコピーしようとすると拒否できる。
- Bへの新規権限貸与を明示的イベントとして監査できる。
- Aを退役済みにした後、有効な保護操作権限が残っていないことを検査できる。
- 個体レコードだけから、系譜・寿命・現在状態・外部参照・監査参照を復元できる。