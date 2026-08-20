# 能力（Capability）

[英語版（正本）](capability.md)

**状態（Status）:** 概念 — 初期定義（Concept — initial definition）

> この文書は英語版の日本語翻訳です。内容に差異がある場合は英語版を正とします。

## 定義

**能力（Capability）** とは、自律システムが環境へ影響を与えたり、環境を観測したりするための、名前付き・境界付き・検証可能な能力です。

能力（Capability）は単なる関数やコード片ではありません。意図（Intent）を、権限付与された実行（Execution）へ接続するアーキテクチャ上の契約（Contract）です。

有用な能力（Capability）定義では、少なくとも次を明示すべきです。

- **目的（Purpose）** — 何のための能力（Capability）か。
- **入力（Inputs）** — どの情報を受け取るか。
- **出力（Outputs）** — 何を返す、または報告するか。
- **事前条件（Preconditions）** — 実行前に何が成立している必要があるか。
- **影響（Effects）** — どの状態（State）を変更し得るか。
- **許可（Permissions）** — どの権限を必要とするか。
- **禁止事項（Prohibitions）** — 絶対に行ってはならないことは何か。
- **不変条件（Invariants）** — 常に維持されるべき性質は何か。
- **検証（Verification）** — 成功・失敗をどのように判定するか。
- **根拠（Evidence）** — どの記録を残すか。
- **版（Version）** — どの行動契約（Behavioral Contract）を呼び出しているか。
- **失敗時動作（Failure behavior）** — 部分失敗、時間切れ（Timeout）、不確実性をどう扱うか。

## 能力（Capability）が重要な理由

推論システムは多くの行動可能性を理解できても、そのすべてを直接実行できるようにすべきとは限りません。

能力（Capability）は、次の間に境界を作ります。

```text
システムが想像できること
            │
            ▼
方針（Policy）が許可すること
            │
            ▼
登録済み能力（Capability）が実際にできること
```

これにより権限（Authority）が明示され、推論エラーの影響範囲（Blast Radius）を小さくできます。

## 例

リポジトリ（Repository）管理の能力（Capability）は、概念的には次のように表現できます。

```text
能力（Capability）: CheckMergeReadiness

入力（Input）:
- Pull Request identifier

許可されること（May）:
- CI statusを確認する
- 未解決Reviewの状態を確認する
- 必須Acceptance Conditionを確認する

許可されないこと（May not）:
- Pull Requestをmergeする
- Branchを削除する
- Repository Settingsを変更する

出力（Output）:
- READY | NOT_READY | UNKNOWN
- 判定を支える根拠（Evidence）
```

別の `MergePullRequest` 能力（Capability）には、これとは異なる許可（Permission）、事前条件（Precondition）、影響（Effect）、検証（Verification）要件が必要です。

同じパターンは物理システム（Physical System）にも適用できます。たとえば宇宙船の電力サブシステム（Subsystem）を隔離する能力（Capability）は、「隔離が必要かもしれない」と判断する推論プロセスとは分離されるべきです。

## 能力（Capability）のライフサイクル

能力（Capability）は、無制限に実行可能なコードとして突然現れるのではなく、明示的なライフサイクルを持つべきです。

```text
必要性を識別（Need identified）
      ↓
候補能力（Candidate capability）
      ↓
実装（Implementation）
      ↓
静的検査 / テスト / シミュレーション（Static checks / tests / simulation）
      ↓
安全性・許可の検証（Safety and permission validation）
      ↓
登録（Registration）
      ↓
権限付き利用（Authorized use）
      ↓
監視・根拠収集（Monitoring and evidence collection）
      ↓
改訂または退役（Revision or retirement）
```

必要な保証水準（Assurance Level）は分野によって異なります。読み取り専用（Read-only）のソフトウェア検査ツール（Software Inspection Tool）と物理アクチュエータ（Physical Actuator）に、同じ検証閾値（Validation Threshold）を適用すべきではありません。

## 能力獲得（Capability Acquisition）

長寿命な自律システムは、同じ推論パターンを繰り返し成功裏に実行していることを発見するかもしれません。

その場合、毎回第一原理（First Principles）から推論し続ける代わりに、そのパターンを候補能力（Candidate Capability）として提案できます。

```text
反復経験（Repeated experience）
        ↓
パターン検出（Pattern detected）
        ↓
手順の一般化（Procedure generalized）
        ↓
候補能力を生成（Candidate capability generated）
        ↓
検証・許可レビュー（Verification and permission review）
        ↓
登録済み能力（Registered capability）
```

これは、**無制限な自己改変と同義ではありません**。

重要なアーキテクチャ上の区別は、能力獲得（Capability Acquisition）が信頼できる検証（Validation）と権限付与（Authorization）のプロセスに従うことです。システムは新しい能力を提案・実装できても、自らの権限（Authority）を密かに拡張できるべきではありません。

## 能力台帳（Capability Registry）

成熟した自律システムでは、現在利用可能な能力（Capability）を保持する台帳（Registry）が必要になる可能性があります。

台帳（Registry）には、たとえば次のメタデータ（Metadata）を含められます。

```text
能力ID（Capability ID）
版（Version）
目的（Purpose）
入出力スキーマ（Input/output schema）
必要許可（Required permissions）
事前条件（Preconditions）
影響（Effects）
不変条件（Invariants）
検証器（Verifier）
実装参照（Implementation reference）
信頼 / 保証水準（Trust / assurance level）
運用状態（Operational status）
根拠履歴（Evidence history）
```

これにより計画役（Planner）は、各実装の詳細を直接知らなくても、利用可能な能力について推論（Reasoning）できます。

## 未解決の問い

この概念（Concept）には、まだ重要な研究課題があります。

- 大きく異なる分野間で、能力保証水準（Capability Assurance Level）をどのように表現すべきか。
- 能力検証（Capability Validation）のどの部分を自律化できるか。
- 能力（Capability）を提案するシステム自身の権限（Authority）の外側に、何を残すべきか。
- 前提条件が変化したとき、能力（Capability）をどのように失効（Revocation）すべきか。
- 複数能力（Capability）を組み合わせる際、意図しない集約権限（Aggregate Authority）をどう防ぐか。
- 繰り返される推論を、いつ決定論的能力（Deterministic Capability）へ変換せず推論（Reasoning）のまま残すべきか。

これらは初期モデルですでに解決済みとみなさず、研究テーマとして扱います。
