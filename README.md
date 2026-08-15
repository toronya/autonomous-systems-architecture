# Autonomous Systems Architecture

[日本語](README.ja.md)

A living research repository for design principles, concepts, reference architectures, hypotheses, and experiments toward long-lived autonomous systems.

> **Autonomous Systems Architecture**  
> Architecture for systems that preserve goals, constraints, and state over long periods while continuing to observe, reason, act, verify, and acquire capabilities.

## What this repository is

This is a **public research and architecture repository**, not a product specification.

It exists to develop and test reusable ideas for autonomous systems that may need to operate safely and continuously beyond the limits of conventional human-operated systems. Possible application domains range from software and infrastructure operations to robotics, social infrastructure, and long-duration spacecraft.

The repository deliberately distinguishes between:

- **Principles** — design rules we currently consider useful and durable.
- **Concepts** — shared vocabulary and architectural building blocks.
- **Reference architectures** — reusable structural patterns, not mandatory implementations.
- **Hypotheses** — ideas that still require evidence.
- **Experiments** — concrete ways to test those hypotheses.
- **Decisions** — important choices and the reasoning behind them.

## Core questions

This work explores questions such as:

- How can an autonomous system retain its purpose and constraints over long periods?
- How should probabilistic reasoning be separated from authoritative execution?
- How can actions be verified before and after they affect the world?
- How can a system degrade, recover, and continue operating when humans are unavailable?
- How can repeated experience be converted into safe, reusable capabilities?
- How should permissions, evidence, state, and memory be represented so that autonomous behavior remains inspectable?

## Initial documents

- [Vision](docs/vision.md) ([日本語](docs/vision.ja.md))
- [Design Principles](docs/principles.md) ([日本語](docs/principles.ja.md))
- [Capability](docs/concepts/capability.md) ([日本語](docs/concepts/capability.ja.md))

## Documentation language policy

English is the **canonical language** of this repository. Japanese documents use the `.ja.md` suffix and are maintained as translations for accessibility and discussion.

When an English document and its translation differ in meaning, the English version is authoritative. New architectural concepts and normative wording should be finalized in English first, then reflected in translations.

This convention is intended to scale to additional translations without coupling the architecture to a particular locale.

## Relationship to experiments

Practical projects may be used as experimental environments for these ideas. Findings should be generalized before being promoted into this repository so that the architecture does not become coupled to one implementation, toolchain, vendor, or operational environment.

## Status

**Early research / exploratory.**

The contents are expected to change as hypotheses are tested. Statements should not be treated as production safety claims unless they are backed by explicit evidence and validation.

## License

This repository uses separate licenses for research/documentation and software:

- **Documentation, research materials, architectural concepts, diagrams, and other non-software content:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)
- **Software source code, when present:** [Apache License 2.0 (Apache-2.0)](LICENSE-CODE), unless otherwise noted

This split is intentional: the research material should be broadly reusable with attribution, while future reference implementations should use a conventional open-source software license suitable for reuse in both research and production contexts.
