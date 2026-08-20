# External Memory and Individual State Boundary

[日本語](external-memory-boundary.ja.md)

**Status:** Concept — M0 working definition  
**Related issue:** #8

## Definition

In ASA, **External Memory** is an information asset retained independently from the internal state of an Individual and remains referencable across replacement, retirement, or re-instantiation of Individuals. Physical storage outside a process does not by itself make information shared knowledge.

The important boundary is semantic ownership, sharing scope, and validation responsibility rather than storage location.

An Individual state checkpoint stored in a database may still be Individual State if it belongs only to that Individual and is not automatically treated as shared social knowledge.

## Four information layers

ASA distinguishes at least four information layers:

1. **Transient Runtime State** — current reasoning context, intermediate calculations, tentative hypotheses, and other short-lived execution state.
2. **Persistent Individual State** — durable state used for continuity of one Individual but not treated as shared social knowledge.
3. **Shared Knowledge and Skills** — validated knowledge, skills, procedures, and generalized experience available across Individuals or generations.
4. **Institutional and Audit Records** — rules, authority history, state transitions, evidence, and records required for continuity and accountability beyond any one Individual.

## Placement principles

| Information type | Ownership | Typical placement | After retirement |
| --- | --- | --- | --- |
| Intermediate reasoning state | Individual | Transient state | Normally discarded |
| Current task context | Individual | Persistent Individual State | Only necessary subset handed over |
| Unvalidated hypothesis | Individual | Persistent Individual State | Not shared by default |
| Validated fact | Society | Shared Knowledge | Remains available |
| Skill / procedure | Society | Shared Knowledge / Capability | Remains available |
| Failure case / lesson | Conditional social asset | Shared after validation | Only validated content retained |
| Authority grant / revocation history | Institution | Audit records | Persisted |
| Significant decisions and actions | Institution | Audit records | Persisted |
| Constitutional or governance rules | Institution | Institutional records | Maintained independently of Individuals |

## State transfer during replacement

When Individual A is replaced by successor B, the full internal state of A should not be copied automatically. Transfer should be limited to a **Handover Package** containing the minimum information required to continue responsibility.

A Handover Package may include:

- unfinished tasks and current state;
- known preconditions;
- unresolved uncertainty;
- references to shared knowledge;
- important recent decisions and evidence;
- required audit references.

Unvalidated speculation, full conversation history, complete internal reasoning traces, and Individual-specific behavioral residue should not be transferred by default.

## Promotion into shared knowledge

Experience does not become shared knowledge merely because an Individual observed it.

```text
Individual observation / experience
        ↓
Candidate Knowledge
        ↓
Provenance check
        ↓
Reproduction / refutation check
        ↓
Independent validation
        ↓
Shared Knowledge
```

Shared Knowledge should carry at least:

- Provenance;
- Validation Status;
- Freshness;
- Applicability;
- Refutation History;
- originating Individual or generation path.

## Failure case: socialization of false information

Suppose Individual A forms an incorrect hypothesis X and writes it directly into shared memory without validation. Individuals B, C, and D may then treat X as a trusted premise, turning one local error into a common-mode failure.

```text
Individual A error
      ↓
Unvalidated write
      ↓
Shared Memory
   ↓   ↓   ↓
  B    C    D
      ↓
Common-mode failure
```

For this reason, **permission to write shared knowledge should be separated from ordinary execution authority and must require an explicit validation path.**

## Design principles

1. **External Memory is defined by independence from an Individual, not by physical storage location.**
2. **Persisted Individual State and Shared Knowledge are distinct.**
3. **Replacement transfers only the minimum Handover Package, not the entire internal state.**
4. **Individual experience does not become Shared Knowledge without validation.**
5. **Shared Knowledge carries provenance, validation, freshness, and refutation metadata.**
6. **Institutional and audit records remain independent from individual or generational turnover.**

## Open questions

- How should the minimum contents of a Handover Package be derived?
- How long should Persistent Individual State be retained?
- How much independent validation should Shared Knowledge require?
- How should stale shared knowledge expire or be revalidated automatically?
- How should deletion requirements interact with persistent audit obligations?
