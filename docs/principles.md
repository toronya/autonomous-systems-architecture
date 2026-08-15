# Design Principles

[日本語](principles.ja.md)

**Status:** Initial principles — expected to evolve with evidence

These principles are not a formal safety standard. They are working architectural rules intended to guide experiments and future reference architectures.

## 1. Preserve purpose and constraints together

A system should not preserve goals while losing the constraints that define acceptable ways to pursue them.

Goals, prohibitions, permissions, invariants, and escalation conditions should be explicit enough to survive component replacement, model changes, and long periods of operation.

## 2. Treat state as a first-class architectural concern

Autonomy depends on knowing what is true, what is believed, what is uncertain, and what changed.

State should be observable, reconstructable where practical, and separated from transient model context.

## 3. Separate reasoning from authority

A reasoning system may propose actions without automatically having the authority to perform them.

Policy, permissions, capability boundaries, and execution mechanisms should constrain what can actually change the world.

## 4. Prefer deterministic mechanisms for repeatable work

If a task can be expressed as a stable rule, parser, state transition, calculation, validator, or procedure, prefer a deterministic implementation over repeated probabilistic reasoning.

Reasoning should be reserved for ambiguity, interpretation, planning, and genuinely novel situations.

## 5. Verify transitions, not just intentions

A valid plan does not guarantee a valid outcome.

Important actions should have preconditions, postconditions, observable evidence, and failure handling. Verification should occur after execution as well as before it where feasible.

## 6. Make capabilities explicit and bounded

An autonomous system should act through named capabilities whose authority is narrower than the reasoning system's conceptual ability.

A capability should make clear what it can do, what it cannot do, what permissions it needs, and how its results can be checked.

## 7. Convert experience into capability cautiously

Repeated successful reasoning may indicate that a procedure can become a reusable capability.

Capability acquisition should not mean unrestricted self-modification. New capabilities should pass an explicit lifecycle that includes implementation, testing or simulation, validation, permission assignment, registration, observation, and retirement.

## 8. Design for degradation and recovery

Long-lived systems should assume that components, communication paths, models, dependencies, and sensors can fail.

Architectures should support isolation, reduced-function operation, recovery, replacement, and re-verification rather than assuming uninterrupted ideal operation.

## 9. Preserve evidence

Important decisions and state-changing actions should leave enough durable evidence for later reconstruction and audit.

Evidence is part of system state, not merely diagnostic logging.

## 10. Keep architecture independent of current tools

Programming languages, AI models, orchestration frameworks, vendors, and deployment platforms are implementation choices.

Architectural concepts should be defined at a level that can survive changes in those technologies.

## Working rule for experiments

When an experimental system introduces a new autonomous behavior, ask:

1. What goal does it serve?
2. What constraints must survive the reasoning step?
3. What state does it rely on?
4. Which capability is authorized to act?
5. What is deterministic and what is probabilistic?
6. How is the result verified?
7. What evidence remains afterward?
8. What happens when any part of the loop fails?
