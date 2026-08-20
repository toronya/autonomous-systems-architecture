# Individual

[日本語](individual.ja.md)

**Status:** Concept — M0 working definition  
**Related issue:** #6

## Definition

An **Individual** in ASA is an autonomous intelligence treated as a single unit of responsibility for decisions and actions during a bounded lifetime, with a unique identity, defined genesis, bounded authority, cognitive characteristics, and an auditable state history.

An Individual is not identical to a model, process, virtual machine, session, or hardware instance. These may host or implement an Individual, but continuity of the Individual depends on continuity of identity, authority, lifecycle, and auditable state lineage.

## Minimum structure

An Individual should minimally define:

- **Identity** — a unique individual identifier and lineage/generation reference.
- **Genesis** — the configuration and conditions under which the Individual came into existence.
- **Lifetime** — creation time, expiry conditions, and lifecycle state.
- **Authority** — permitted capabilities, limits, and authority expiry.
- **Cognitive profile** — model and other characteristics relevant to evaluated behavior.
- **Individual state** — temporary or private state not treated as shared system knowledge.
- **External references** — links to shared knowledge, skills, procedures, and institutional rules.
- **Audit lineage** — a reconstructable history of relevant decisions, actions, and state transitions.

## Identity continuity

A runtime restart does not by itself create a new Individual. An Individual may survive process restart, host migration, hardware replacement, or equivalent infrastructure changes if the following remain continuous and verifiable:

- individual identity;
- genesis and lineage;
- lifetime and lifecycle state;
- authority contract;
- valid state continuity;
- audit lineage.

## When a new Individual is required

A new Individual should be created when a change materially exceeds the characteristics under which the current Individual was evaluated.

Examples include substantial changes to the cognitive model, reasoning architecture, behavioral policy, or other factors expected to materially alter decision behavior.

This is summarized by the principle:

> **Material cognitive change creates a new Individual.**

Minor adaptation may remain within the same Individual only while it remains inside an explicitly accepted **Allowed Adaptation Envelope**. Defining that envelope is a later research task.

## Examples

| Scenario | Same Individual? | Rationale |
| --- | --- | --- |
| Process crashes and restarts from valid state | Yes | Runtime changed; responsibility lineage did not. |
| Execution migrates to another machine after hardware failure | Yes | Hardware does not define identity. |
| Context is compacted and restored with validated continuity | Usually yes | State representation changed, not the responsibility unit. |
| Underlying language model is replaced by a materially different model | Normally no | Decision characteristics may no longer match the evaluated Individual. |
| A prompt is edited without changing intended behavior | Conditional | Allowed only if the change remains inside the accepted adaptation envelope. |
| A complete copy is started in parallel | No | Once both can form independent decision histories, they require distinct identities. |
| A checkpoint is restored as the sole recovery continuation after failure | Potentially yes | It may continue one auditable lineage rather than form a concurrent branch. |

## Ambiguous case: online learning

Continuous adaptation creates an identity boundary problem. ASA should not define identity by parameter equality. Instead, continuity should depend on whether adaptation stays within the behavior and assurance range previously accepted for the Individual.

When an adaptation exceeds that range, it should be treated as a successor candidate rather than an in-place self-modification.

## Design implications

1. **An Individual is a responsibility unit, not an execution unit.**
2. **A concurrent copy is a different Individual.**
3. **Material cognitive change is treated as birth of a successor candidate.**
4. **Runtime recovery and generational succession are distinct operations.**

## Open question

The main unresolved question is how to define and measure the Allowed Adaptation Envelope in a model- and implementation-independent way.
