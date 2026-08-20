# Lifetime and Authority

[日本語](lifetime-authority.ja.md)

**Status:** Concept — M0 working definition  
**Related issue:** #7

## Definition

In ASA, **Lifetime** is the finite period during which an Individual may continue to exist as a single unit of responsibility. **Authority** is a time-bounded grant that permits an Individual to perform specific functions during that lifetime and does not automatically carry across lifetime expiry, re-instantiation, or generational succession.

ASA as a whole must maintain sufficient **Societal Authority Capacity** to preserve required social functions despite birth, retirement, and failure of Individuals, while adjusting the degree of authority concentration or distribution according to function scale, criticality, blast radius, and reversibility.

## Separation of lifetime and authority

Lifetime and authority validity are not the same thing. An Individual may continue to exist after some or all authority has expired. Continuing authority beyond lifetime requires a new explicit decision; it must not happen by default.

```text
Birth
  ↓
Active
  ↓
Authority Expiring
  ↓
Authority Revoked / Reduced
  ↓
Handover
  ↓
Retirement
  ↓
Archived
```

## What expires and what remains

| Element | After lifetime expiry | Principle |
| --- | --- | --- |
| Execution authority | Expires | No new execution |
| Approval / voting authority | Expires | No participation in governance decisions |
| Identity | Preserved historically | Responsibility remains traceable |
| Audit lineage | Persisted | Decisions and actions remain reconstructable |
| Individual state | Normally isolated or discarded | Not automatically transferred to a successor |
| Validated knowledge | May remain externally | Must have passed shared-knowledge validation |
| Skills / procedures | May remain independently | Managed as capabilities or procedures |
| Trust / evaluation results | Not inherited automatically | Successor must be evaluated independently |

## Authority as a lease

Authority is not a permanent intrinsic property. It should be represented as an **Authority Lease**.

A lease should minimally define:

- authority type;
- scope;
- expiry;
- preconditions;
- revocation conditions;
- renewal conditions;
- audit requirements.

A successor may inherit capabilities or knowledge, but **authority and trust are not inherited automatically**.

## Societal authority capacity

Per-Individual authority constraints are insufficient to guarantee availability of social functions. If too few authorized Individuals remain, the system may be safe in the narrow sense while still becoming unable to function.

ASA should therefore manage, per authority type:

- minimum required count;
- target count;
- currently valid count;
- soon-to-expire count;
- independence requirements;
- degraded-operation procedure.

These form **Minimum Authority Coverage**.

Where needed, independence should consider generation, implementation, failure domain, observation path, or other relevant dimensions rather than raw count alone.

## Adaptive authority topology

Authority distribution is a risk-control mechanism, not an end in itself. ASA should not require maximum distribution everywhere.

The degree of concentration or distribution should consider at least:

- **Scale**;
- **Criticality**;
- **Blast Radius**;
- **Reversibility**.

Small, low-risk, highly reversible functions may use relatively concentrated authority. Large, high-impact, low-reversibility functions should require stronger separation, independent evaluation, and multi-Individual approval.

This is referred to as **Adaptive Authority Topology**.

## Degraded operation under authority shortage

When authorized Individuals become insufficient, ASA should not preserve a distribution topology so rigidly that all social function is lost. It may enter a safe degraded mode and temporarily concentrate authority within defined limits.

Preferred order:

1. evaluate and promote successor candidates to restore coverage;
2. grant limited, time-bounded authority to existing Individuals;
3. degrade the function so it can operate under lower authority requirements;
4. only if still necessary, temporarily extend authority of an expiring Individual.

Emergency extension must remain exceptional, minimal in duration and scope, independently approved, and fully audited.

## Exception: emergency extension

A critical safety-monitoring function may otherwise lose all required authority before a successor is ready. In that case, a short and narrow authority extension can be safer than strictly enforcing expiry and losing the function entirely.

Such extension should be treated as an operational abnormality indicating insufficient succession readiness. It should end as soon as replacement coverage is restored.

## Design principles

1. **Lifetime defines the period of Individual responsibility; authority is a bounded lease inside that period.**
2. **Authority and trust do not automatically transfer to successors.**
3. **Both excessive concentration and insufficient authority coverage are risks.**
4. **Authority distribution should adapt to function risk and societal scale.**
5. **Safe degraded operation and temporary reconcentration are allowed under authority shortage.**
6. **Exceptions that preserve social function over strict retirement must remain narrow, temporary, explicit, and auditable.**

## Open questions

- Should Minimum Authority Coverage be static or dynamically derived from system state?
- How should independence among authority holders be measured?
- What is the maximum safe degree of temporary authority concentration?
- When should authority topology be reorganized as societal scale expands or contracts?
