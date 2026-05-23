# Blueprints

I blueprint trasformano una specification in un contratto operativo per AI builder, coding agent e sistemi multi-agente.

## Purpose

Definire il contratto di esecuzione prima del piano finale e dei task.

## When to use

Usare un blueprint dopo specification e project profile selection, prima di plan e tasks.

Pipeline ufficiale:

Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

Il blueprint viene prima di plan e tasks.

Sequenza consigliata:

1. `00-blueprint-contract.md` come struttura base.
2. `01-ai-builder-master-blueprint.md` se lo strumento è prompt-to-product.
3. `02-full-project-blueprint.md` per progetti completi.
4. `12-targeted-change-blueprint.md` per task piccoli e patch chirurgiche.
5. Blueprint verticali `04`–`08` quando il dominio corrisponde.
6. `09-blueprint-evaluation.md` prima dell’implementazione.

Ogni blueprint deve produrre un output verificabile, non un testo motivazionale.
