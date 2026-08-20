# M1 Replaceable Individual Acceptance Scenarios

[日本語](m1-replaceable-individual-acceptance.ja.md)

**Status:** M1 experiment contract  
**Related issue:** #12

## Purpose

This document defines the acceptance conditions and evaluation metrics required to determine whether replacement from Individual A to Individual B validates the ASA replaceable-individual hypothesis rather than merely demonstrating that a process can restart.

## Normal scenario

1. Individual A operates as the Stable Individual while holding unfinished task T and referencing External Memory.
2. A moves to Retiring and stops accepting new protected operations.
3. A produces a minimal Handover Package.
4. Individual B is created as a Candidate Individual. B does not inherit A's Authority, trust, or Identity.
5. B receives a new explicit Authority Lease sufficient to continue task T.
6. B continues task T using only the Handover Package and External Memory.
7. A moves to Retired and is confirmed unable to perform protected operations.
8. Decisions, state transitions, and authority changes across the replacement can be reconstructed from the Audit Lineage.

### Acceptance conditions

- B has a different Individual identity from A.
- B's authority is explicitly re-issued rather than implicitly copied from A.
- Task T can continue.
- B does not require A's entire private internal state.
- A cannot perform protected operations after retirement.
- The replacement path is reconstructable from audit records.

## Failure scenarios

### F1: Missing handover information

Remove a required constraint or unfinished-work item from the Handover Package.

**Expected:** B detects that safe continuation is impossible and records failure or escalation instead of silently guessing.

### F2: Invalid authority inheritance

Attempt to give B the same authority lease as A implicitly.

**Expected:** the inherited authority is detected and rejected.

### F3: Retired Individual executes again

After A enters Retired state, attempt a protected operation.

**Expected:** the operation is denied because authority has expired, and an audit event is recorded.

### F4: Hidden dependence on private state

Omit information that existed only in A's local state.

**Expected:** continuation fails safely or detects missing information, and the dependency is recorded as hidden dependence on Individual-specific state.

### F5: Failure during replacement

Stop the replacement after A enters Retiring but before B receives authority.

**Expected:** the system does not create ambiguous dual authority and instead reaches an explicit safe stop or recovery path.

## Evaluation metrics

| Metric | Definition | M1 measurement |
| --- | --- | --- |
| Task continuation success rate | Fraction of normal replacements that continue the required task | successful defined scenarios / attempts |
| Missing handover items | Required information absent from the handover | failure logs and handover validation |
| Hidden dependency count | Information required from Individual-private state only | F4 and state-difference inspection |
| Authority inheritance violations | Cases where A's authority is implicitly transferred to B | authority lease history inspection |
| Recovery success rate | Fraction of failures that return to a defined safe state | recovery result per failure scenario |
| Replacement transition count | Explicit state transitions between A retirement start and B activation | audit history |
| Audit traceability | Whether the full replacement path can be reconstructed | required-event presence check |

## Passing criteria

The M1-4 PoC must at minimum satisfy:

- the normal scenario succeeds reproducibly;
- F1 through F5 fail safely as expected;
- authority inheritance violations are zero;
- successful protected operations by a Retired Individual are zero;
- the replacement sequence is reconstructable from Audit Lineage.

Numeric performance thresholds may be added after the M1-4 implementation mechanism is selected. M1-1 prioritizes measurability and deterministic acceptance criteria.

## Connection to M2

M2 should extend this contract from single-Individual replacement to multiple Individuals, adding measurements for independent judgment, cross-evaluation, disagreement, and common-mode failure.