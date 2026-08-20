# M1 Replaceable Individual PoC

This experiment implements the minimum deterministic lifecycle needed to test replacement from Individual A to Individual B.

## Scope

Implemented:

- Candidate / Stable / Retiring / Retired lifecycle states
- explicit time-bounded authority leases
- handover validation
- authority non-inheritance checks
- retirement-time authority revocation
- protected-operation denial after retirement
- audit events for lifecycle and authority changes
- normal replacement scenario
- failure scenarios F1-F5 from the M1 acceptance contract

Not implemented:

- multi-Individual consensus
- model distillation
- autonomous promotion
- advanced Shadow / Advisory states
- dynamic societal authority topology

## Run

From the repository root with Python 3.11+:

```bash
python -m unittest experiments.m1_replaceable_individual.test_poc -v
```

The experiment uses only the Python standard library.

## Acceptance reference

See:

- `docs/experiments/m1-replaceable-individual-acceptance.md`
- `docs/experiments/m1-individual-schema.md`
- `docs/experiments/m1-handover-package.md`
