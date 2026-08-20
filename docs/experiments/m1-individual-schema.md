# M1 Individual Metadata and Authority Lease Schema

[日本語](m1-individual-schema.ja.md)

**Status:** M1 experiment contract  
**Related issue:** #13

## Purpose

This document defines the minimum implementation-independent schema required by the M1 replaceable-individual PoC to represent identity, lifetime, lifecycle state, lineage, external-memory references, audit lineage, handover references, and explicit authority leases.

## Individual record

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

### Required fields

- **Individual ID** — unique across Individuals.
- **Generation** — lineage generation number.
- **Created At** — creation timestamp.
- **Expires At** — lifetime expiry or mandatory re-evaluation time.
- **Lifecycle State** — candidate, stable, retiring, retired, or another defined lifecycle state.
- **Cognitive Profile Reference** — identifier for the evaluated cognitive characteristics.
- **External Memory References** — references to information assets independent of the Individual.
- **Audit Lineage Reference** — reference for decisions, state transitions, and authority changes.
- **Authority Leases** — current explicit authority grants; an empty list is valid.

### Optional fields

- **Parent Individual ID** — set only when lineage relationship exists.
- **Handover From** — set only when responsibility is transferred from another Individual.
- **Handover Package Reference** — set only when a handover package exists.

## Authority Lease record

Authority is represented as a time-bounded lease rather than as a permanent property of the Individual.

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

Required fields are:

- **Lease ID**
- **Individual ID**
- **Capability**
- **Scope**
- **Issued At**
- **Expires At**
- **Issued By**
- **Status**

## Invariants

1. Individual IDs are unique and must not be reused by successors.
2. A successor must not copy the predecessor's authority leases.
3. Every authority lease explicitly names its target Individual.
4. A Retired Individual must not retain active protected-operation authority.
5. An authority lease must not remain valid beyond the Individual's lifetime unless an explicit exception policy applies.
6. Handover source and destination must have different Individual IDs.
7. Lineage information explains origin; it must not imply inherited trust or authority.

## Example: Individual A

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

## Example: Individual B

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

At this point B has no authority lease. Even if B is intended to take A's operational role, a new lease must be issued explicitly.

## Minimum M1-4 validation

- A and B can be instantiated with different identities.
- Attempted copying of A's authority lease to B can be rejected.
- New authority issuance to B is auditable as an explicit event.
- After A becomes Retired, no active protected-operation authority remains for A.
- The record is sufficient to reconstruct lineage, lifetime, lifecycle state, external references, and audit reference.