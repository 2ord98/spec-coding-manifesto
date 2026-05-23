# Metodologia

Specification-Driven Coding è un workflow per guidare modelli e app builder dalla richiesta grezza al prodotto verificabile.

Specification-Driven Coding is a workflow for guiding models and app builders from a raw request to a verifiable product.

La pipeline è scalabile. Prompt già strutturati possono usare un percorso compatto: mode detection -> consistency check -> assunzioni mancanti -> targeted blueprint o validation gate. Prompt fragili, builder deboli e generazione full-project ad alto rischio usano il percorso completo intake/spec/profile/blueprint.

The pipeline is scalable. Already-structured prompts may use a compact path: mode detection -> consistency check -> missing assumptions -> targeted blueprint or validation gate. Fragile prompts, weaker builders, and high-risk full-project generation use the full intake/spec/profile/blueprint path.

## Pipeline standard

```text
Raw request
  ↓
Intake
  ↓
Specification
  ↓
Project Profile Selection
  ↓
Vertical Blueprint Contract
  ↓
Plan tecnico
  ↓
Tasks atomici
  ↓
Implementation
  ↓
Evaluation Scorecard
  ↓
Release/Iteration
```

Il Vertical Blueprint precede plan e tasks perché è il contratto che determina stack, file tree, confini, ruolo dell’agente, sicurezza, output format e quality gates.

The Vertical Blueprint comes before plan and tasks because it is the contract that determines stack, file tree, boundaries, agent role, security, output format, and quality gates.

## English operational summary

1. Treat the raw request as input material, not an implementation order.
2. Produce intake with blocking questions, reversible assumptions, non-goals, and anti-genericity constraints.
3. Write a buildable specification connected to a project profile.
4. Compile the Vertical Blueprint before the final plan and tasks.
5. Generate plan and atomic tasks from the blueprint.
6. Implement only within the declared boundaries.
7. Evaluate with a scorecard and use the result for release, rollback, or iteration.

## 1. Raw intent

La richiesta iniziale può essere incompleta, emotiva, breve o caotica. Non va eseguita direttamente. Va interpretata come materiale grezzo.

The initial request may be incomplete, emotional, short, or chaotic. It must not be executed directly. Treat it as raw material.

## 2. Intake

L’agente legge questa repo come regola operativa. Non deve limitarsi a “rispondere al prompt”, ma deve compilare il prompt grezzo in un intake più forte:

```text
intent + domain + user + constraints + assumptions + project profile + blueprint
```

The agent reads this repository as operational discipline. It should not merely answer the prompt; it should compile the raw prompt into stronger intake.

## 3. Specification

È la richiesta riscritta in forma costruibile. Deve essere abbastanza specifica da guidare codice, design, dati, test e deployment.

This is the request rewritten into buildable form. It must be specific enough to guide code, design, data, tests, and deployment.

## 4. Project profile routing

Ogni progetto deve scegliere un profilo primario in `project-types/`. I progetti compositi possono usare massimo due profili primari.

Every project must choose a primary profile in `project-types/`. Composite projects may use at most two primary profiles.

## 5. Clarification pass

L’agente può fare massimo 5 domande bloccanti. Una domanda è bloccante solo se cambia architettura, modello dati, sicurezza, UX primaria, integrazioni o scope.

Tutto ciò che non è bloccante deve diventare assunzione esplicita.

Questo passaggio vive dentro intake/specification e produce un assumption ledger esplicito.

The agent may ask at most 5 blocking questions. Everything else must become an explicit assumption. This pass lives inside intake/specification and produces an assumption ledger.

## 6. Master specification

La specification chiarisce cosa deve essere vero: utenti, requisiti, non-obiettivi, dati, flussi, vincoli, rischi e acceptance criteria.

The specification defines what must be true: users, requirements, non-goals, data, flows, constraints, risks, and acceptance criteria.

## 7. Vertical Blueprint Contract

Il blueprint chiarisce come produrre il risultato: ruolo tecnico, stack, file tree, file obbligatori, codice richiesto, sicurezza stack-specifica, performance budget, fallback e test.

The blueprint defines how to produce the result: technical role, stack, file tree, required files, required code, stack-specific security, performance budget, fallback, and tests.

## 8. Plan e tasks

Il plan deriva dal blueprint e motiva l’ordine di implementazione. I task sono atomici, ordinati, testabili e collegati a specification e blueprint.

The plan derives from the blueprint and explains implementation order. Tasks are atomic, ordered, testable, and linked to specification and blueprint.

## 9. Implementation

Il codice deve rispettare specification, blueprint e tasks. In brownfield si cambia solo ciò che serve.

Code must respect specification, blueprint, and tasks. In brownfield work, change only what is required.

## 10. Evaluation Scorecard e Release/Iteration

Ogni output finale deve includere valutazione 0-100 con gap e prossime correzioni. La scorecard non è decorativa: è il gate di qualità che guida release, rollback o iterazione successiva.

Every final output must include a 0-100 evaluation with gaps and next fixes. The scorecard is not decorative: it is the quality gate that guides release, rollback, or the next iteration.

## 11. Continuous Specification Enforcement

La specification e il Vertical Blueprint restano contratti vivi. Se implementazione, task, scorecard o artifact divergono, l'agente deve scegliere esplicitamente: aggiornare la specification, aggiornare il Vertical Blueprint, correggere implementazione/artifact o accettare un'eccezione documentata.

The specification and Vertical Blueprint remain living contracts. If implementation, tasks, scorecards, or artifacts diverge, the agent must explicitly choose: update the specification, update the Vertical Blueprint, fix the implementation/artifact, or accept a documented exception.

```bash
python3 tools/sdc_enforce.py check --path benchmarks/golden/001-builder-habit-dashboard
```
