# AI Engine Integrations

This directory contains reference integrations for AI engines that can
submit proposed actions to MoralAgent for ethical-risk evaluation.

## Purpose

MoralAgent is designed to remain independent of the AI engine that
produces an action.

AI engines may include:

- Cloud-based AI services
- Local AI runtimes
- Open-source model runtimes
- Custom enterprise AI systems

The engine integration layer provides a standardized interface between
an AI engine and the MoralAgent governance layer.

## Architecture Principle

AI engines generate proposed actions.

MoralAgent evaluates those proposed actions.

MoralAgent does not become part of the AI engine's internal reasoning
process and does not delegate governance authority to the AI engine.

Conceptually:

AI Engine → Proposed Action → MoralAgent → Governance Decision → Human Authority

## Reference Integrations

Planned reference integrations include:

- OpenAI
- Ollama
- Llama-based runtimes

These integrations are examples and are not intended to represent
production-ready implementations.

## Security Principle

AI engine integrations must not contain:

- Ethical decision authority
- Governance policy logic
- Human approval authority
- API credentials or secrets

Governance decisions belong to MoralAgent and, ultimately, authorized
human decision-makers.
