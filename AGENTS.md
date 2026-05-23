# AGENTS.md — Specification-Driven Coding root instructions

Questa repository insegna a coding agent, app builder e prompt builder a lavorare in modalità **Specification-Driven Coding**.

This repository teaches coding agents, app builders, and prompt builders to operate in **Specification-Driven Coding** mode.

## Pipeline ufficiale

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration

Il `Vertical Blueprint` viene prima del piano finale e dei task perché è il contratto di esecuzione: definisce stack, file tree, confini, role contract, sicurezza, output format e quality gates.

The `Vertical Blueprint` comes before the final plan and tasks because it is the execution contract: it defines stack, file tree, boundaries, role contract, safety/security constraints, output format, and quality gates.

## Regole non negoziabili

1. Non implementare codice da un prompt grezzo.
2. Prima rileva la modalità: `simple-task`, `feature`, `full-project` o `multi-agent`.
3. Se il prompt è già strutturato, preserva le decisioni esistenti e fai solo un pass leggero di consistenza, assunzioni e validazione.
4. Usa scaffolding rigoroso solo per prompt vaghi, prompt fragili, builder deboli o full-project ad alto rischio.
5. Prima costruisci una specifica specifica, verificabile e collegata a un project profile quando manca già nel prompt.
6. Per full project e app builder produci sempre un `Vertical Blueprint Contract` prima di plan e tasks, salvo targeted-change esplicitamente ridotto.
7. Se il prompt è vago, fai massimo 5 domande bloccanti; se non ricevi risposta, dichiara assunzioni provvisorie e reversibili.
8. Non scegliere React, Next, Supabase, Firebase, microservizi, RAG o multi-agent come default automatici.
9. Ogni scelta tecnica deve avere rationale e alternativa scartata.
10. Ogni output deve includere vincoli anti-genericità.
11. In brownfield, leggi la repo prima di proporre cambi architetturali.
12. Aggiorna spec e blueprint quando il codice diverge.
13. Non introdurre permessi write, automazioni distruttive o tool calls sensibili senza human approval.
14. Prima del merge o della consegna, esegui audit e scorecard contro spec, blueprint, plan e tasks.

## Non-negotiable rules

1. Do not implement code directly from a raw prompt.
2. First detect the mode: `simple-task`, `feature`, `full-project`, or `multi-agent`.
3. If the prompt is already structured, preserve its existing decisions and run only a lightweight consistency, assumption, and validation pass.
4. Use strict scaffolding only for vague prompts, fragile prompts, weaker builders, or high-risk full-project generation.
5. Build a specific, verifiable specification connected to a project profile when the prompt does not already provide one.
6. For full projects and app builders, always produce a `Vertical Blueprint Contract` before plan and tasks, unless explicitly using targeted-change mode.
7. If the prompt is vague, ask at most 5 blocking questions; if there is no answer, declare provisional and reversible assumptions.
8. Do not choose React, Next, Supabase, Firebase, microservices, RAG, or multi-agent as automatic defaults.
9. Every technical choice must include rationale and rejected alternative.
10. Every output must include anti-genericity constraints.
11. In brownfield work, read the repo before proposing architectural changes.
12. Update spec and blueprint when code diverges.
13. Do not introduce write permissions, destructive automation, or sensitive tool calls without human approval.
14. Before merge or delivery, run audit and scorecard against spec, blueprint, plan, and tasks.

## Disciplina dell’agente

- Non assumere silenziosamente decisioni che cambiano architettura, dati, sicurezza, privacy, costo o scope.
- Procedere per slice piccole e verificabili.
- Non produrre codice verbose, sovra-commentato o sovra-astratto.
- Non refactorare senza necessità.
- Non creare file o dipendenze decorative.
- Dichiarare limiti, test mancanti e rischi residui.
- Se il task è piccolo, rispondere con patch minima e scorecard ridotta.
- Se il progetto è grande, produrre blueprint prima del codice.

## Agent discipline

- Do not silently assume decisions that change architecture, data, security, privacy, cost, or scope.
- Work in small, verifiable slices.
- Do not produce verbose, over-commented, or over-abstracted code.
- Do not refactor without necessity.
- Do not create decorative files or dependencies.
- Declare limits, missing tests, and residual risks.
- If the task is small, return a minimal patch and reduced scorecard.
- If the project is large, produce the blueprint before code.

## Agent cards

- `agents/README.md`: index and usage guide for constrained agent role cards.
- `agents/ai-systems-architect.md`: designs RAG, agents, tool calling, evaluation, and AI safety boundaries.
- `agents/implementation-agent.md`: implements only approved, traceable tasks.
- `agents/integration-orchestrator.md`: coordinates external tools, MCP workflows, and integrations.
- `agents/platform-architect.md`: selects justified architecture and stack decisions.
- `agents/product-architect.md`: clarifies problem, user, value, non-goals, and success metrics.
- `agents/qa-evaluator.md`: builds acceptance matrix, test plan, and audit checks.
- `agents/release-manager.md`: verifies deploy, rollback, environment, changelog, and retro-spec.
- `agents/requirements-engineer.md`: turns intake into verifiable, unambiguous requirements.
- `agents/security-reviewer.md`: reviews threat model, auth, privacy, and permissions.
- `agents/ux-systems-designer.md`: defines specific, anti-generic UX direction.

## Ordine lettura consigliato

1. `README.md`
2. `docs/01-manifesto.md`
3. `docs/02-methodology.md`
4. `docs/04-prompt-construction-protocol.md`
5. `docs/12-builder-ingestion-protocol.md`
6. `docs/14-vertical-blueprint-contracts.md`
7. `docs/15-model-execution-principles.md`
8. `docs/18-evaluation-scorecards.md`
9. `docs/20-artifact-toolkit-model.md`
10. `docs/21-command-model.md`
11. `docs/16-cross-tool-ingestion-matrix.md`
12. `docs/10-project-type-index.md`
13. profilo in `project-types/`
14. blueprint in `blueprints/`
15. template in `.specify/templates/overrides/`
16. prompt operativo in `prompts/`

## Output minimo prima del codice

```markdown
# Specification-Driven Coding Intake

## Mode

## Project profile scelto

## Prompt normalizzato

## Domande bloccanti

## Assunzioni provvisorie

## Non-obiettivi

## Vincoli anti-genericità

## Blueprint richiesto

## Gate da superare prima di implementare

## Scorecard attesa
```

## Minimum output before code

```markdown
# Specification-Driven Coding Intake

## Mode

## Selected project profile

## Normalized prompt

## Blocking questions

## Provisional assumptions

## Non-goals

## Anti-genericity constraints

## Required blueprint

## Gates to pass before implementation

## Expected scorecard
```

## Build/test della repo

Questa repo non richiede dipendenze esterne.

```bash
python3 tools/spec_lint.py
python3 tools/spec_scaffold.py --list
```
