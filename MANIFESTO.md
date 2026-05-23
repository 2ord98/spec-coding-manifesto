# Specification-Driven Coding Manifesto

[Versione italiana →](MANIFESTO.it.md)

## 1. The real problem is not only the prompt

Vague prompts are a visible failure mode, but they are not the whole problem.

The deeper problem is the AI product-generation loop that turns incomplete intent into average software. When a request leaves gaps, models, app builders, and agentic workflows complete those gaps with training priors, product templates, median UI patterns, familiar stacks, shallow planning habits, and hidden assumptions.

The result can look functional while still being generic. It can pass a demo while failing the domain.

Specification-Driven Coding exists because the failure is systemic: weak intent, model defaults, builder templates, missing project memory, missing constraints, skipped skills or plugins, lazy stack selection, and weak evaluation all compound into products that are plausible but not specific.

It is a method and guide layer, not a project factory, app generator, or replacement for engineering judgment. Its tools scaffold specification workspaces and validation surfaces; they do not produce finished products by themselves.

## 2. Vibe coding changed the speed of creation

Vibe coding changed software creation in a real way. It made prototyping faster, exploration cheaper, and software building more accessible to people who could express an idea before they could specify an architecture.

That matters. Fast exploration is useful. Natural-language iteration is useful. Throwaway prototypes are useful.

The problem starts when exploratory generation becomes product construction without a stronger contract. Speed without specificity produces motion, but not necessarily product judgment.

## 3. But vibe-coded products converge

When AI systems fill missing intent with average patterns, products converge.

They converge into the same landing pages, the same dashboards, the same rounded cards, the same auth flows, the same generated copy, the same generic SaaS stacks, the same fake polish, the same placeholder data, and the same weak domain fit.

They converge architecturally too: default frameworks, default databases, default auth, default deployment assumptions, default admin panels, default RAG, default multi-agent flows.

This is not only an aesthetic problem. It is a product and engineering problem. Convergent software hides missing decisions behind familiar shape. It looks finished before it is understood.

## 4. Structured specification is the minimum

Specification-Driven Coding starts from a practical minimum established by structured specification-driven development workflows: constitution, specification, clarification, checklist, technical plan, tasks, analysis, implementation, templates, agent prompt files, and validation scripts.

That minimum is important because it moves AI-assisted development away from one-shot prompting and toward explicit artifacts.

Specification-Driven Coding goes further. It adds raw-request intake, project profile selection, Vertical Blueprint Contracts, builder ingestion, targeted-change workflows, scorecards, anti-genericity gates, cross-agent adapters, and stronger handling of incomplete intent.

Basic specification-first workflows make the path from specification to implementation more disciplined. Specification-Driven Coding adds the missing front and middle layers: how raw intent becomes a domain-specific specification, and how that specification becomes an execution contract strong enough for app builders, coding agents, and multi-agent systems.

## 5. Definition

**Specification-Driven Coding** is an AI-native development method that compiles incomplete human intent into explicit, domain-specific, tool-ingestible construction contracts before product generation or code implementation.

In this repository, `spec` means **specification**. Specificity is the outcome: software anchored to a real user, domain, workflow, stack rationale, data model, constraints, security posture, tests, and evaluation criteria.

The official pipeline is:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

## 6. The repo is not a prompt collection

This repository is not a collection of longer prompts.

It is an ingestion layer and toolkit for AI builders, coding agents, app generators, and multi-agent workflows. Its job is to force the system to ask, assume, constrain, specialize, build, validate, and score.

A longer prompt can still be generic. A strong Specification-Driven Coding packet is different: it binds intent, domain, constraints, stack, file output, safety, fallback, acceptance, and evaluation before generation begins.

The method must be proportional. When a prompt is already structured, specific, constrained, and paired with a capable tool, Specification-Driven Coding should act as lightweight steering: preserve the existing decisions, check assumptions, expose missing gates, and validate the output. When the prompt is fragile, the builder is likely to default to templates, or the product risk is high, the method should become stricter and require the full intake, profile, blueprint, plan, tasks, and scorecard path.

## 7. The Specification-Driven Prompt

A valid Specification-Driven Prompt contains or derives:

- intent;
- primary user;
- domain;
- non-goals;
- constraints;
- assumptions;
- project profile;
- stack rationale;
- data model;
- UX direction;
- file/output contract;
- integrations;
- security;
- performance;
- tests;
- acceptance criteria;
- scorecard.

When those elements are missing, the agent or builder must not silently fill them with defaults. It must ask a compact set of blocking questions or produce a visible assumption ledger with rationale, impact, reversibility, and verification.

## 8. The Vertical Blueprint Contract

The Vertical Blueprint Contract is the key extension beyond basic specification-driven development.

It comes before the final plan and tasks because it defines the execution contract. It binds role, stack, file tree, architecture, output format, implementation boundaries, fallback behavior, quality gates, and domain-specific behavior before work is decomposed.

Without the blueprint, a plan can still smuggle in generic defaults. With the blueprint, the plan must explain how to execute a specific product contract.

A Vertical Blueprint is not decorative planning. It is the artifact that makes an AI builder or coding agent produce this product, for this domain, with this stack, under these constraints.

## 9. Anti-genericity principle

An output is not acceptable merely because it works.

It must prove it belongs to this domain, this user, this workflow, this product, this stack, and this constraint set.

Anti-genericity is not visual novelty for its own sake. It is evidence that the product has understood its context. Real data, domain vocabulary, specific flows, explicit non-goals, stack rationale, error states, and failure modes matter more than surface polish.

A generated product that could belong to any startup belongs to none.

## 10. Responsibility of the AI/builder

The AI builder or coding agent has responsibilities.

It must not silently default to common templates. It must not invent product structure without marking assumptions. It must not skip relevant skills, plugins, context packs, MCP tools, or project profiles. It must not hide uncertainty. It must not produce a generic app when the request is underspecified.

When information is missing, the agent must produce a compact clarification pass or assumption ledger. When a choice affects architecture, data, security, privacy, cost, deployment, integrations, permissions, or scope, that choice must be explicit.

The agent is not allowed to convert ambiguity into fake confidence.

## 11. Responsibility of the developer/operator

Developers and operators have responsibilities too.

Even experienced developers can be lazy with AI: using the wrong context, skipping the right skill, ignoring project profiles, accepting default stacks, trusting generated architecture, or letting a polished demo stand in for validation.

Specification-Driven Coding requires the operator to select the right profile, load the right adapter, use the right skill or plugin, inspect architecture and security, verify the scorecard, and reject generic output.

AI does not remove engineering judgment. It makes poor judgment faster.

## 12. Small task mode

Specification-Driven Coding is not only for full projects.

It also applies to bug fixes, small features, UI changes, config fixes, documentation updates, security patches, dependency updates, and brownfield maintenance.

The targeted-change principle is:

```text
inspect before edit -> probable cause -> exact files -> minimal patch -> validation -> rollback
```

Small work does not need a full product blueprint. It still needs scope discipline, explicit assumptions, relevant validation, and a scorecard scaled to risk.

## 13. Multi-agent mode

Agents are not free-floating collaborators. They are governed roles.

A multi-agent system should define planner, architect, implementer, verifier, and safety/release gate responsibilities. Each agent needs a mandate, allowed inputs, required outputs, permitted tools, forbidden tools, stop conditions, reviewer, and quality gate.

No agent has unlimited authority. Tool calls, write permissions, destructive actions, external communication, sensitive data access, security remediation, legal decisions, medical decisions, financial decisions, and physical-world actions require explicit approval gates.

Multi-agent work without governance is just distributed ambiguity.

## 14. Evaluation is part of the product

Every significant output must return a scorecard.

The scorecard must evaluate:

- adherence to specification;
- anti-genericity;
- completeness;
- UX/domain fit;
- architecture;
- security;
- performance;
- tests;
- residual risks;
- next fixes.

Evaluation is not a final flourish. It is part of the product contract. If the output cannot be scored, it is not ready.

## 15. The specification must stay alive

Specification-Driven Coding does not treat the specification as a one-time pre-implementation document. The specification and Vertical Blueprint are living contracts.

If implementation diverges, the agent must not hide it. It must update the specification, update the Vertical Blueprint, fix the implementation/artifact, or accept a documented exception with rationale.

## 16. Final principle

Do not ask the AI to build from vibes.

Make the AI compile intent into a contract, specialize the contract into a blueprint, implement against it, and score the result.
