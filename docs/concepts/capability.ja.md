# Capability

[English (canonical)](capability.md)

**Status:** Concept — initial definition / 初期定義

> この文書は英語版の日本語翻訳です。内容に差異がある場合は英語版を正とします。

## 定義

**Capability** とは、自律システムが環境へ影響を与えたり、環境を観測したりするための、名前付き・境界付き・検証可能な能力です。

Capabilityは単なる関数やコード片ではありません。Intentを、権限付与されたExecutionへ接続するアーキテクチャ上のContractです。

有用なCapability定義では、少なくとも次を明示すべきです。

- **Purpose** — 何のためのCapabilityか。
- **Inputs** — どの情報を受け取るか。
- **Outputs** — 何を返す、または報告するか。
- **Preconditions** — 実行前に何が成立している必要があるか。
- **Effects** — どのStateを変更し得るか。
- **Permissions** — どの権限を必要とするか。
- **Prohibitions** — 絶対に行ってはならないことは何か。
- **Invariants** — 常に維持されるべき性質は何か。
- **Verification** — 成功・失敗をどのように判定するか。
- **Evidence** — どの記録を残すか。
- **Version** — どのBehavioral Contractを呼び出しているか。
- **Failure behavior** — 部分失敗、Timeout、不確実性をどう扱うか。

## Capabilityが重要な理由

推論システムは多くの行動可能性を理解できても、そのすべてを直接実行できるようにすべきとは限りません。

Capabilityは、次の間に境界を作ります。

```text
システムが想像できること
            │
            ▼
Policyが許可すること
            │
            ▼
登録済みCapabilityが実際にできること
```

これによりAuthorityが明示され、推論エラーのBlast Radiusを小さくできます。

## 例

Repository管理のCapabilityは、概念的には次のように表現できます。

```text
Capability: CheckMergeReadiness

Input:
- Pull Request identifier

May:
- CI statusを確認する
- 未解決Reviewの状態を確認する
- 必須Acceptance Conditionを確認する

May not:
- Pull Requestをmergeする
- Branchを削除する
- Repository Settingsを変更する

Output:
- READY | NOT_READY | UNKNOWN
- 判定を支えるEvidence
```

別の `MergePullRequest` Capabilityには、これとは異なるPermission、Precondition、Effect、Verification要件が必要です。

同じパターンはPhysical Systemにも適用できます。たとえば宇宙船の電力Subsystemを隔離するCapabilityは、「隔離が必要かもしれない」と判断する推論プロセスとは分離されるべきです。

## Capabilityのライフサイクル

Capabilityは、無制限に実行可能なコードとして突然現れるのではなく、明示的なライフサイクルを持つべきです。

```text
Need identified
      ↓
Candidate capability
      ↓
Implementation
      ↓
Static checks / tests / simulation
      ↓
Safety and permission validation
      ↓
Registration
      ↓
Authorized use
      ↓
Monitoring and evidence collection
      ↓
Revision or retirement
```

必要なAssurance Levelは分野によって異なります。Read-onlyなSoftware Inspection ToolとPhysical Actuatorに、同じValidation Thresholdを適用すべきではありません。

## Capability acquisition

長寿命な自律システムは、同じ推論パターンを繰り返し成功裏に実行していることを発見するかもしれません。

その場合、毎回First Principlesから推論し続ける代わりに、そのパターンをCandidate Capabilityとして提案できます。

```text
Repeated experience
        ↓
Pattern detected
        ↓
Procedure generalized
        ↓
Candidate capability generated
        ↓
Verification and permission review
        ↓
Registered capability
```

これは、**無制限な自己改変と同義ではありません**。

重要なアーキテクチャ上の区別は、Capability Acquisitionが信頼できるValidationとAuthorizationのプロセスに従うことです。システムは新しい能力を提案・実装できても、自らのAuthorityを密かに拡張できるべきではありません。

## Capability registry

成熟した自律システムでは、現在利用可能なCapabilityを保持するRegistryが必要になる可能性があります。

Registryには、たとえば次のMetadataを含められます。

```text
Capability ID
Version
Purpose
Input/output schema
Required permissions
Preconditions
Effects
Invariants
Verifier
Implementation reference
Trust / assurance level
Operational status
Evidence history
```

これによりPlannerは、各実装の詳細を直接知らなくても、利用可能な能力についてReasoningできます。

## 未解決の問い

このConceptには、まだ重要な研究課題があります。

- 大きく異なる分野間で、Capability Assurance Levelをどのように表現すべきか。
- Capability Validationのどの部分を自律化できるか。
- Capabilityを提案するシステム自身のAuthorityの外側に、何を残すべきか。
- 前提条件が変化したとき、CapabilityをどのようにRevocationすべきか。
- 複数Capabilityを組み合わせる際、意図しないAggregate Authorityをどう防ぐか。
- 繰り返される推論を、いつDeterministic Capabilityへ変換せずReasoningのまま残すべきか。

これらは初期モデルですでに解決済みとみなさず、研究テーマとして扱います。
