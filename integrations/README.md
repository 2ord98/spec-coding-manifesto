# Integrations

This directory provides a machine-readable index of the repository's adapter surfaces.

## Purpose

Use `catalog.json` when an agent, app builder, maintainer, or external tool needs to discover which adapter files exist and which one to load first.

## Files

- `catalog.json`: canonical registry of repository instructions, AI adapters, plugin adapters, and GitHub ecosystem surfaces.

## Entry contract

Each catalog entry declares:

- stable `id`
- display `name`
- repository `file`
- adapter `type`
- `requires_cli`
- `supports_skills`
- `primary_use`
- ordered `load_first`
- `known_limits`
- `output_contract`
- optional `notes`

## CLI

```bash
python3 tools/sdc.py integration list
python3 tools/sdc.py integration list --format json
python3 -m sdc_cli integration list
```

## GitHub surfaces

GitHub-specific entries are usage targets, not requirements. They describe:

- Copilot repository instructions;
- Copilot path-specific instructions;
- GitHub Actions validation;
- pull request and issue templates;
- optional Codespaces/devcontainer setup.

`AGENTS.md` remains the generic agent entrypoint. GitHub integration is optional; the same Specification-Driven Coding artifacts can still be used with other agents, builders, and local CLI workflows.

## Notes

- The catalog is a repository integration registry, not a second methodology.
- The official workflow remains:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

- Adapter paths in this file must match the real repository layout, including `ai-adapters/`.
