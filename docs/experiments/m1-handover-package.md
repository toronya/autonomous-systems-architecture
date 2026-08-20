# M1 Handover Package

[日本語](m1-handover-package.ja.md)

**Status:** M1 experiment contract  
**Related issue:** #14

## Purpose

This document defines the minimum information transferred from Individual A to Individual B so responsibility can continue without copying the predecessor's complete internal state.

## Core principle

> **A Handover Package contains the minimum sufficient information required to resume responsibility; it is not a mechanism for copying the predecessor's identity, trust, or authority.**

## Minimum structure

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

## Required fields

- **Handover ID**
- **From Individual**
- **To Individual**
- **Created At**
- **Objective** — responsibility or task that must continue.
- **Work State** — explicit completed and pending work.
- **Constraints** — deadlines, prohibitions, and invariants the successor must preserve.
- **Validated Assumptions** — assumptions backed by evidence references.
- **Uncertainties** — unresolved facts that must not be silently guessed.
- **External References** — references to external memory, shared knowledge, and skills.
- **Audit References** — references required to reconstruct the handover decision.

## Information excluded by default

- predecessor Authority Leases;
- predecessor trust or reputation;
- reuse of the predecessor Identity;
- unnecessary internal reasoning traces;
- unvalidated private beliefs;
- the entire Individual-private memory;
- full copies of information already available through external references.

## Completeness validation

A Handover Package must at minimum verify that:

1. the continuing objective is uniquely identifiable;
2. unfinished work is explicit;
3. required constraints are not missing;
4. validated assumptions have evidence references;
5. unresolved facts are represented as uncertainties;
6. required external references resolve;
7. source and destination are different Individuals;
8. no Authority Lease is embedded in the package.

If required information is missing, the successor must be able to return **Cannot Continue Safely** rather than silently filling gaps by inference.

## Over-transfer detection

The package should not include predecessor state merely because it is convenient.

Potential over-transfer includes:

- Individual-private memory unrelated to the active objective, constraints, or pending work;
- duplicated data already available from shared knowledge;
- unsupported predecessor guesses;
- private behavioral tendencies that unnecessarily bias the successor.

For M1, if an item cannot be justified by the question "would safe continuation be impossible without this information?", it should normally be excluded.

## Example replacement

### Individual A

- completed step-1 of task-t;
- step-2 remains pending;
- shared-record-x must not be modified;
- external service status is still unknown.

### Individual B after handover

B receives those facts through the Handover Package but does not receive A's authority, trust, or internal reasoning history. B resolves required External Memory separately and may perform protected operations only after receiving a new explicit Authority Lease.

## Failure tests for M1-4

- remove one constraint and confirm completeness validation fails;
- break an external reference and confirm safe continuation is rejected;
- insert an Authority Lease into the package and confirm rejection;
- attach the predecessor's entire private memory and detect over-transfer.

## Open questions

- How should minimum required information vary by task class?
- Which layer should provide integrity or signature guarantees for a Handover Package?
- When should large work state be referenced rather than embedded?
- How should gradual information loss or distortion across long handover chains be measured?