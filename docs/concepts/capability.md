# Capability

[日本語](capability.ja.md)

**Status:** Concept — initial definition

## Definition

A **Capability** is a named, bounded, and verifiable ability through which an autonomous system can affect or inspect its environment.

A capability is more than a function or piece of code. It is an architectural contract that connects intent to authorized execution.

A useful capability definition should make explicit:

- **Purpose** — what the capability is for.
- **Inputs** — what information it accepts.
- **Outputs** — what it returns or reports.
- **Preconditions** — what must be true before execution.
- **Effects** — what state it may change.
- **Permissions** — what authority it requires.
- **Prohibitions** — what it must never do.
- **Invariants** — properties that must remain true.
- **Verification** — how success or failure is determined.
- **Evidence** — what record is produced.
- **Version** — which behavioral contract is being invoked.
- **Failure behavior** — how partial failure, timeout, or uncertainty is handled.

## Why capabilities matter

A reasoning system may understand many possible actions, but that does not mean it should be allowed to perform all of them directly.

Capabilities create a boundary between:

```text
What the system can imagine
            │
            ▼
What policy permits
            │
            ▼
What registered capabilities can actually do
```

This makes authority explicit and reduces the blast radius of reasoning errors.

## Example

A repository-management capability might be represented conceptually as:

```text
Capability: CheckMergeReadiness

Input:
- pull request identifier

May:
- inspect CI status
- inspect unresolved review state
- inspect required acceptance conditions

May not:
- merge the pull request
- delete branches
- change repository settings

Output:
- READY | NOT_READY | UNKNOWN
- evidence supporting the result
```

A separate `MergePullRequest` capability would have different permissions, preconditions, effects, and verification requirements.

The same pattern applies to physical systems. A spacecraft capability that isolates a power subsystem should be distinct from the reasoning process that decides isolation may be necessary.

## Capability lifecycle

A capability should have an explicit lifecycle rather than appearing as unrestricted executable code.

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

Different domains will require different levels of assurance. A read-only software inspection tool and a physical actuator should not share the same validation threshold.

## Capability acquisition

A long-lived autonomous system may discover that it repeatedly performs the same reasoning pattern successfully.

Instead of reasoning from first principles forever, it may propose that pattern as a candidate capability:

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

This is **not equivalent to unrestricted self-modification**.

The important architectural distinction is that capability acquisition remains subject to a trusted validation and authorization process. The system may propose or implement new abilities, but it should not be able to silently expand its own authority.

## Capability registry

A mature autonomous system may need a registry containing the capabilities currently available to it.

A registry could include metadata such as:

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

This allows a planner to reason about available abilities without requiring direct knowledge of every implementation detail.

## Open questions

This concept still leaves important research questions:

- How should capability assurance levels be represented across very different domains?
- Which parts of capability validation can themselves be autonomous?
- What must remain outside the authority of the system that proposes a capability?
- How should capabilities be revoked when assumptions change?
- How should multiple capabilities be composed without creating unintended aggregate authority?
- When should repeated reasoning remain reasoning rather than being converted into a deterministic capability?

These questions should be treated as research topics rather than assumed solved by the initial model.
