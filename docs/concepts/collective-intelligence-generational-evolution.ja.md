# Collective Intelligence and Generational Evolution

> 自律知性の社会・有限寿命・世代交代・継承構造
>
> Status: Concept Note / Working Draft  
> Date: 2026-08-20

本稿は、ASA（Autonomous Systems Architecture）における自己改善を、単一の自律知性による自己書換えではなく、**複数の有限寿命の自律知性からなる社会が世代交代を通じて進化する問題**として捉えるための概念整理である。

生物進化、社会制度、分散システム、安全工学から得られる示唆をASAへ適用するための設計仮説であり、現時点では実装仕様ではない。

## 1. Core Concept

**ASAは、有限寿命の複数の自律知性が相互に観測・批判・抑制・協調しながら世代交代し、能力と特性を遺伝し、知識と技能を文化として共有し、制度によって全体の安全性と継続性を維持する自律知性体系として捉える。**

重要な区別は次である。

- **Learning（個体内学習）**: ある個体が生涯の経験によって適応すること。
- **Evolution（世代的改善）**: 次世代候補の生成・評価・選抜・継承によってASA全体が変化すること。

個体は生涯で学習するが、ASA全体の自己改善は、稼働中の自己を直接書き換えることではなく、**次世代を作り評価すること**として扱う。

## 2. Why a Collective, Not a Single Intelligence

単一の巨大な自律知性に観測・判断・実行・自己改善を集中させると、その個体の誤り、劣化、目的のずれ、権限逸脱がシステム全体の障害になり得る。

ASAでは複数知性を単に並列化するのではなく、観測経路・役割・権限・評価経路を意図的に分離する。

- 異なる仮説や観測を持つことで、共通の誤りを発見しやすくする。
- 危険な判断を単独で実行できないよう、権限を分散する。
- 個体の異常を他個体や決定論的なPolicy Gateが検出・隔離する。
- 新しい個体を段階的に参加させ、社会全体を一度に置換しない。

概念的には次のような構造を想定する。

```text
Shared World / Environment
          │
  ┌───────┼────────┐
  ▼       ▼        ▼
Planner  Guardian  Critic
  │       │        │
  └───────┼────────┘
          ▼
 Governance / Arbitration
          ▼
 Deterministic Action Gate
          ▼
      Environment
```

安全性の源泉を「各個体が常に正しいこと」ではなく、**不完全な個体が存在しても全体として壊れにくいこと**に置く。

## 3. Finite Individual Lifetime

個体に有限の寿命を持たせることは、単なるリソース管理ではなく安全機構である。

無期限に存在する個体は、経験・権限・影響力を蓄積し続け、古い世界モデル、偏り、権力集中を固定化する可能性がある。有限寿命により、個体の権限は最終的に失効し、世代交代が通常運用として組み込まれる。

```text
Birth → Probation → Active → Mature
      → Knowledge Contribution
      → Successor Generation
      → Reduced Authority → Retirement
```

重要な原則は、**個体の存続自体を目的にしないこと**である。個体の役割は、自らの生存を最大化することではなく、ASA全体の継続、安全、知識蓄積、次世代への貢献に置く。

また、全個体を同時に入れ替えてはならない。旧世代と新世代を重複させる **overlapping generations（重複世代）** を採用し、新世代の共通欠陥が一度に全体へ広がることを避ける。

## 4. Three Inheritance Channels

世代交代を導入すると、「何をどの経路で残すか」がASAの核心になる。

現時点では、継承を次の3系統に分離する。

| 継承経路 | 対象 | 主な実装候補 | 設計上の意味 |
| --- | --- | --- | --- |
| Genetic | 能力・特性・認知傾向・内部構造 | 蒸留、学習、モデル選択、アーキテクチャ変更 | 次世代がどのような知性として生まれるかを決める |
| Cultural | 知識・技能・手順・検証済み経験 | 外部記憶、Knowledge Base、Skill、Procedure | 個体が死んでも社会として知識を保持する |
| Institutional | 憲法・権限境界・安全制約・監査・歴史 | Constitution、Policy Engine、Governance、Audit Log | 個体や世代を超えて社会のルールを維持する |

### 4.1 Genetic Inheritance

ASAにおける「遺伝子」は、モデル重みそのものではなく、**個体を再生成したときに能力・性質・行動傾向を再現するための継承可能な構成情報**と捉える。

モデル蒸留は、その遺伝を実現する一手段であり、旧個体の能力や判断特性を次世代へ圧縮・移送できる。

ただし、特定のLLMやTransformer構造をASAの遺伝子と同一視しない。長期的には、異なるモデルアーキテクチャ間でも能力を継承できることが望ましい。

### 4.2 Cultural Inheritance

知識や技能は、可能な限り個体内部へ固定的に焼き込まず、外部記憶・Skill・Procedureとして社会に残す。

これにより、モデルを世代交代しても知識を維持でき、誤った情報を修正する際にもモデル全体の再学習を避けられる。

簡潔に表現すると、

> **個体は能力を遺伝し、知識を文化として継承する。**

### 4.3 Institutional Inheritance

個体のGenomeにも共有知識にも属さない「社会そのもののルール」を独立させる。

例えば以下である。

- 実行権限の上限
- 自己複製制限
- 監査ログの保全
- 個体の昇格・隔離・退役条件
- 緊急停止や安全拒否権
- Constitutionの変更手続き

これらは、個体が自由に変更できない制度層に置く。

## 5. Shared Memory as Cultural Infrastructure

外部記憶は単なるRAGストアではなく、ASA社会が世代を超えて蓄積する**文化・文明資産**に相当する。

一方、誤情報が共有記憶へ入ると、多数の個体へ同時に影響するため、個体の誤り以上に大きな共通モード故障を生み得る。

したがって、個体が書いた情報をそのまま共有知識にしてはならない。

```text
Individual Experience
        ↓
Candidate Knowledge
        ↓
Evidence Validation
        ↓
Cross-Agent Review / Reproduction
        ↓
Validated Shared Heritage
```

この検証経路は、ASAにおける**記憶の免疫系**とみなせる。

共有知識には少なくとも、出典、検証状態、鮮度、反証履歴、適用条件を持たせ、単一個体の主張が直接「社会の真実」にならないようにする。

## 6. Self-Improvement Through Generational Succession

自己改善は、稼働中のStable個体を直接変更するのではなく、コピーまたは派生個体をCandidateとして生成し、隔離環境で評価し、権限を段階的に昇格させる。

```text
Stable Generation N
        │
  Candidate Creation
        │
 Sandbox / Simulation
        │
 Shadow Observation
        │
 Advisory Role
        │
 Limited Authority
        │
 Promotion
        ▼
Generation N+1
```

失敗したCandidateはStableへ影響を与えずに破棄・分析できる。

この方法では自己改善が「自分自身を改造すること」から「次世代を作り、評価すること」に変わる。進化の対象も個体単位に分解できるため、ASA全体を一度に危険へ晒さずに探索できる。

## 7. Biological Evolution as an Engineering Analogy

生物進化は有力なヒントを与えるが、ASAは自然選択をそのまま模倣しない。

| 生物 | ASAでの対応 |
| --- | --- |
| 個体 | Autonomous Intelligence instance |
| 寿命 | Identity / authority / runtime lifetime |
| 遺伝 | Distillation / training / architecture transfer |
| 学習 | Lifetime adaptation |
| 文化 | Shared Knowledge / Skills / Procedures |
| 生殖 | Candidate generation |
| 自然選択 | Evaluation / selection / promotion |
| 世代交代 | Promotion / retirement with overlap |
| 社会制度 | Governance / Constitution |
| 免疫 | Validation / isolation / audit |
| 種・集団 | ASA Collective |

自然界は多数の失敗や絶滅を許容するが、ASAには復元可能性と安全制約が必要である。そのため、ASAの進化は **Constrained Artificial Evolution（制約された人工進化）** として扱う。

また、性能の高い個体だけを残す単一Fitness最適化は避ける。安全性、信頼性、資源効率、協調性、長期安定性だけでなく、少数派の視点や探索的個体を保持する**多様性そのものの価値**も評価対象とする。

## 8. Expected Safety Properties

このモデルから期待される安全特性は次の通りである。

- **Failure containment** — 個体の失敗を局所化し、全体障害へ波及しにくくする。
- **Authority decay** — 寿命によって権限が永久固定化されない。
- **Diversity** — 異なる役割・モデル・世代・観測経路によって共通モード故障を減らす。
- **Reversibility** — 旧世代を保持し、失敗した世代交代から復元できる。
- **Independent verification** — Generator、Evaluator、Governorを権限上分離する。
- **Institutional continuity** — 個体が入れ替わっても安全制約・監査・目的境界を保持する。

ただし、**複数個体であるだけでは安全にならない**。

全員が同じモデル、同じデータ、同じ世界モデルを共有すれば共通して誤る。また、単純多数決は、多数派の誤りや談合的挙動を防げない。

重要判断には、決定論的制約、安全拒否権、証拠検証、専門性に応じた重み付けなどを組み合わせる必要がある。

## 9. Risks and Unresolved Questions

| 論点 | 問い |
| --- | --- |
| 個体の境界 | 独立個体と呼ぶために、記憶・目的・権限・モデルのどこまでを分離する必要があるか。 |
| Genomeの定義 | 能力・特性のうち、どこまでを遺伝可能にし、どこを固定または外部化するか。 |
| 継承審査 | 誰がどの基準で、個体経験を社会知識や次世代能力へ昇格させるか。 |
| 多様性 | モデル、学習データ、役割、世代の多様性をどの程度意図的に維持するか。 |
| 寿命 | 時間、処理量、世代数、信頼度低下など、何を寿命の基準にするか。 |
| 社会的挙動 | 信頼・評判・同盟・権力集中などの創発をどこまで許容・制約するか。 |
| 制度変更 | Constitution自体を長期的に改善する必要が生じたとき、誰がどの手続きで変更できるか。 |
| 外部監督 | ASAの内部社会が共通方向へ誤った場合、どの独立系が最終的な安全境界を担うか。 |

## 10. Working Design Principles

### Collective Intelligence Principle

ASAは単一の自律知性に依存せず、異質な複数個体と独立した評価経路から構成する。

### Finite Individual Lifetime Principle

自律知性の個体は無期限に存在・権限保持せず、有限のライフサイクルを持つ。

### Self-Improvement Isolation Principle

稼働中のStable自己を直接変更せず、改善は隔離Candidateとして生成・評価・昇格する。

### Separated Inheritance Principle

能力・特性の遺伝、知識・技能の文化継承、制度の継承を分離する。

### Validated Heritage Principle

個体経験は、検証・抽象化を経ずに共有知識や次世代能力へ昇格させない。

### Overlapping Generations Principle

世代交代は重複世代で行い、新世代の共通欠陥が一度に全体へ広がることを防ぐ。

### Constrained Evolution Principle

進化は、Constitutionと決定論的安全境界が許す探索空間内でのみ行う。

## 11. Current Concept Definition

### Long form

> **ASAは、有限寿命の自律知性が世代交代しながら、能力と特性を遺伝し、知識と技能を文化として共有し、制度と安全制約を社会として継承することで、個体を超えて長期的に存続・進化する自律知性体系である。**

### Short form

> **個体は死に、能力は遺伝し、知識は文化として残り、制度が社会を存続させる。**

## 12. Next Research Questions

次の段階では、以下を具体化する。

1. **ASA Genome** — 能力・特性をモデル非依存にどう表現するか。
2. **Individual Boundary** — 独立した「個体」の最小構成と、識別・記憶・権限の境界。
3. **Generational Protocol** — Candidate生成、Shadow運用、評価、昇格、退役、Rollbackの状態遷移。
4. **Knowledge Immune System** — 外部記憶への登録・反証・更新・失効の決定論的プロトコル。
5. **Governance** — 投票、拒否権、専門性、信頼、少数派保護、緊急時権限の設計。
6. **Constitutional Change** — 制度そのものを安全に進化させる二階のガバナンス。

## Status

本稿の内容は設計仮説であり、現時点で有効性が実証されたものではない。

次の段階では、既存の分散システム、安全工学、進化計算、マルチエージェント研究との対応を検証し、ASA固有の要素と既存手法で代替できる要素を切り分ける必要がある。
