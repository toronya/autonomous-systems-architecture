# Individual Lifecycle and Promotion Model

[日本語](individual-lifecycle.ja.md)

**Status:** Concept — M0 working definition  
**Related issues:** #9, #10, #11

## Purpose

This document defines how an ASA Individual moves from candidate creation through evaluation, promotion, stable operation, degradation, isolation, retirement, and rollback.

The central rule is:

> **A trusted Stable Individual is not modified in place for material cognitive or behavioral changes. A materially changed successor is evaluated as a separate Candidate Individual and receives authority only through explicit promotion.**

## Lifecycle states

The minimum lifecycle states are:

1. **Candidate** — a newly created successor or materially changed Individual with no inherited trust.
2. **Sandboxed** — evaluated in an isolated environment with no production authority.
3. **Shadow** — observes production-relevant inputs and produces proposed decisions without executing them.
4. **Advisory** — may provide recommendations to authorized Individuals or governance mechanisms, but cannot independently perform protected actions.
5. **Limited Authority** — receives explicitly scoped, time-bounded authority for a restricted set of capabilities.
6. **Stable** — has passed the required evaluation and is authorized for its designated operational role.
7. **Degraded** — remains active with reduced authority or scope because of uncertainty, reduced societal capacity, expiring lifetime, or detected risk.
8. **Isolated** — prevented from affecting normal operations while evidence is preserved for diagnosis.
9. **Retiring** — no new protected work is accepted; authority is revoked or reduced while handover and audit finalization occur.
10. **Retired** — no operational authority remains. Identity, lineage, and required audit records may remain as historical records.

## State transitions

Typical forward progression is:

```text
Candidate
  -> Sandboxed
  -> Shadow
  -> Advisory
  -> Limited Authority
  -> Stable
```

Operational safety transitions may occur from active states:

```text
Stable / Limited Authority
  -> Degraded
  -> Stable                 (if confidence is restored)
  -> Isolated               (if risk becomes unacceptable)
  -> Retiring
  -> Retired
```

A Candidate may also be rejected from any pre-Stable state and retired without ever receiving production authority.

## Promotion

Promotion is the explicit grant of a higher-trust lifecycle state or broader authority. Promotion must not be inferred from age, similarity to a predecessor, lineage, or inherited reputation.

Promotion should require evidence appropriate to the role, including where applicable:

- behavioral evaluation against defined acceptance criteria;
- safety and policy checks;
- capability-specific validation;
- evidence from sandbox, shadow, or limited-authority operation;
- confirmation that societal authority capacity remains sufficient after role changes;
- independent approval where the function's risk requires it;
- a rollback or containment path for the promoted scope.

A successor starts with no inherited operational trust beyond explicitly reusable evidence. **Trust is re-established; it is not inherited.**

## Demotion and degradation

An Individual may be demoted or moved into Degraded state when confidence falls but immediate isolation is not required.

Triggers may include:

- unexplained behavioral drift;
- repeated disagreement with validated observations;
- reduced evidence quality;
- authority nearing expiry;
- partial infrastructure failure;
- reduced societal authority coverage;
- changes in operating conditions outside the evaluated range.

Degradation should reduce blast radius while preserving useful service where safe.

## Isolation

Isolation is required when continued participation could compromise safety, integrity, governance, or evidence quality.

An Isolated Individual should:

- lose normal production authority;
- be prevented from modifying shared knowledge or institutional state unless explicitly authorized for forensic purposes;
- retain enough evidence for diagnosis and audit;
- not be restored directly to Stable without re-evaluation.

## Retirement

Retirement is a normal lifecycle outcome, not necessarily a failure.

The preferred retirement sequence is:

```text
Revoke or reduce authority
  -> stop accepting new protected work
  -> produce handover package
  -> finalize evidence and audit lineage
  -> transfer validated knowledge through approved processes
  -> Retired
```

Retirement must not silently transfer identity, authority, trust, or private internal state to a successor.

## Rollback

Rollback restores a previously validated operational configuration when a promoted successor causes unacceptable degradation or risk.

Rollback requires:

- retention of a recoverable prior Stable configuration or equivalent recovery path;
- preserved external knowledge and institutional state compatible with restoration;
- separation between successor-specific state and shared validated state;
- auditability of what changed before and during rollback;
- re-evaluation if restored conditions differ materially from the state under which the prior Stable configuration was validated.

Rollback does not mean that the previous Individual automatically regains expired authority. Authority leases and societal authority requirements still apply.

## Stable immutability principle

A Stable Individual may undergo normal runtime recovery and explicitly bounded lifetime adaptation. However, a material cognitive or behavioral change that exceeds its accepted adaptation envelope must create a new Candidate Individual.

This prevents self-improvement from becoming uncontrolled in-place mutation of the currently trusted operational subject.

## Failure containment

A Candidate must not be able to damage the Stable path merely by being evaluated. Candidate evaluation should therefore separate:

- production authority;
- shared-knowledge write authority;
- institutional or governance authority;
- external side effects;
- resource consumption where exhaustion could affect Stable operation.

The evaluation environment may relax some constraints only when the possible effect is contained and reversible.

## M1 handoff

M1 should implement the smallest lifecycle subset needed to test replaceability:

- Candidate;
- Stable;
- Retiring;
- Retired;
- explicit authority lease;
- handover package;
- preserved audit lineage;
- a reproducible replacement from Individual A to Individual B.

Sandbox, Shadow, Advisory, Limited Authority, Degraded, Isolation, and automated rollback may initially be represented as states and policies before being fully automated.

## Open questions

- What minimum evidence is required for each promotion boundary?
- Which state transitions require independent approval?
- How long should a prior Stable configuration be retained for rollback?
- How should promotion interact with dynamic societal authority capacity?
- What constitutes sufficient equivalence when a rollback target's dependencies have changed?
