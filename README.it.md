# Specification-Driven Coding

[![Validate](https://github.com/2ord98/spec-coding-manifesto/actions/workflows/validate.yml/badge.svg)](https://github.com/2ord98/spec-coding-manifesto/actions/workflows/validate.yml)

[English version ->](README.md)

L'AI non ha bisogno di prompt più lunghi. Ha bisogno di contratti.

Specification-Driven Coding è un ingestion layer, execution contract e protocollo di Continuous Specification Enforcement per costruire software AI-native. Trasforma intenzioni incomplete in contratti di costruzione verificabili, specifici per dominio, eseguibili da AI builder e coding agent.

- Una pipeline, non un prompt template. Raw request -> intake -> specification -> project profile -> Vertical Blueprint -> plan -> tasks -> implementation -> evaluation scorecard -> release.
- Anti-genericità by design. Project profile, Vertical Blueprint e scorecard gate rifiutano artefatti che collassano nei pattern medi dell'AI.
- La specification è un contratto vivo. Continuous Specification Enforcement controlla specification, blueprint, plan, tasks e implementation. La deriva viene nominata, non nascosta.

## Quick Start

```bash
git clone https://github.com/2ord98/spec-coding-manifesto
cd spec-coding-manifesto
pip install -e .
sdc doctor
sdc demo run --fixture 001-builder-habit-dashboard
```

Nota: l'installazione è in modalità editable da checkout locale. Un pacchetto PyPI è previsto ma non ancora pubblicato — usa `pip install -e .` per ora.

Per uno smoke check piu rapido:

```bash
sdc doctor --quick
```

Differenza chiave: molti workflow si fermano alla specification. Questo la fa rispettare dall'intake alla release.

## Requisiti

- Python 3.11+
- Git

In modalità consumer project non sono richiesti `uv`, `pipx`, installazione editable, comando globale, configurazione `PATH` o configurazione shell-specific.

## Modalità consumer project

Per un progetto che vuole usare Specification-Driven Coding come toolkit incorporato, usa una checkout deterministica senza installazione:

```bash
cd my-project
git clone https://github.com/2ord98/spec-coding-manifesto.git .sdc
python3 .sdc/tools/sdc.py doctor --quick
python3 .sdc/tools/sdc.py init "my project" --type marketing-site-cms --out "$PWD/sdc-workspace"
```

`pip install -e .sdc` è opzionale, non richiesto. Se usato direttamente dentro un consumer project, l'installazione editable può creare metadati `.egg-info` locali; preferisci `python3 .sdc/tools/sdc.py ...` per uso deterministico senza installazione. Se è disponibile un comando globale `sdc`, cerca dalla directory corrente verso l'alto la `.sdc/tools/sdc.py` più vicina.

## Dove si colloca

Il vibe coding è veloce: entra un prompt, spesso esce software utilizzabile, e i default del modello diventano silenziosamente il prodotto. I workflow specification-first sono un passo avanti perché strutturano il percorso da richiesta a specification, plan e tasks. Però spesso si fermano agli artefatti, lasciando ad agenti e builder il compito di riempire i dettagli di dominio con i propri default. Le regole editor e le istruzioni per coding agent configurano il comportamento dell'agente, ma non compilano ciò che deve essere costruito in un contratto specifico di costruzione.

Specification-Driven Coding aggiunge gli strati mancanti: project profile che restringono lo spazio progettuale prima del planning, Vertical Blueprint che codificano il prodotto reale, scorecard che valutano gli artefatti con gate espliciti invece che con vibe, e Continuous Specification Enforcement che mantiene allineati specification, blueprint, plan, tasks e implementation mentre il progetto evolve.

I profile sono confini decisionali, non template. Ogni profile descrive una classe di software, il decision space consentito, vincoli anti-default, filtri di rischio, stack option, performance budget, security baseline e testing contract. Le verticali di mercato arrivano dalla raw request, non dai default del profile.

## Prova il demo

```bash
sdc demo run --fixture 001-builder-habit-dashboard
sdc demo run --fixture 001-builder-habit-dashboard --verbose
sdc demo run --fixture 001-builder-habit-dashboard --format markdown
sdc demo run --fixture 001-builder-habit-dashboard --format json
python3 tools/sdc_demo.py run --fixture 001-builder-habit-dashboard
```

Il demo legge artifact benchmark esistenti e mostra come un prompt grezzo vago diventa una chain di artifact Specification-Driven Coding. Non genera app, non chiama API esterne e non richiede un LLM.

La pipeline ufficiale è:

```text
Raw request
  → Intake
  → Specification
  → Project Profile Selection
  → Vertical Blueprint
  → Plan
  → Tasks
  → Implementation
  → Evaluation Scorecard
  → Release/Iteration
```

Il `Vertical Blueprint` viene prima di plan e tasks: è il contratto che blocca stack, file tree, confini, sicurezza, output format e quality gates prima che l’agente scomponga il lavoro.

Autore: **Lorenzo Cassiani**  
Repository slug: `spec-coding-manifesto`  
Nome metodologia: **Specification-Driven Coding**

## Tesi

Il problema principale del vibe coding non è la velocità. È l’ambiguità.

Quando l’utente scrive una richiesta incompleta, l’AI riempie i vuoti con pattern medi: stesso frontend, stessa dashboard, stesso stack, stessa architettura, stessi placeholder, stessa qualità apparente. Specification-Driven Coding usa il prompt grezzo solo come punto di partenza e lo trasforma in un contratto operativo:

```text
Raw request
  → Intake
  → Specification
  → Project Profile Selection
  → Vertical Blueprint
  → Plan
  → Tasks
  → Implementation
  → Evaluation Scorecard
  → Release/Iteration
```

## Definizione

**Specification-Driven Coding = coding guidato da specification esplicite, vive e verificabili.**

In questo progetto `spec` significa **specification**. La specificità è l’effetto pratico: una buona specification obbliga l’AI a costruire software ancorato a dominio, utenti, vincoli, stack, qualità e criteri di verifica.

## Differenza rispetto al vibe coding

| Modalità | Input | Output tipico | Rischio |
|---|---|---|---|
| Vibe coding | Prompt naturale, iterativo, spesso incompleto | Prototipo rapido | Genericità, decisioni implicite, debito tecnico |
| Toolkit specification-first | Artefatti ordinati di specification, planning, task list e implementazione | Processo strutturato | Può restare troppo feature-scoped |
| Specification-Driven Coding | Prompt trasformato + profilo progetto + blueprint + scorecard | Prodotto AI-guidato ma specifico | Più decisioni esplicite prima del codice |

## Come si usa con un AI builder

Carica o incolla questa repo nello strumento, poi usa un prompt di questo tipo:

```text
Usa questa repository come sistema operativo per Specification-Driven Coding.
Non limitarti a eseguire il mio prompt grezzo.
Prima trasformalo in uno Specification-Driven Prompt usando:
- AGENTS.md
- docs/04-prompt-construction-protocol.md
- docs/12-builder-ingestion-protocol.md
- docs/13-blueprint-compiler.md
- docs/14-vertical-blueprint-contracts.md
- docs/15-model-execution-principles.md
- docs/18-evaluation-scorecards.md
- il project profile più adatto in project-types/

Poi produci un Vertical Blueprint Contract e implementa solo ciò che il blueprint rende verificabile.
Se mancano dettagli, fai massimo 5 domande bloccanti; per il resto dichiara assunzioni reversibili e procedi.
Alla fine restituisci una scorecard 0-100 con gap e prossime correzioni.
```

## Cosa contiene questa repo

- `AGENTS.md`: istruzioni root per agenti e builder.
- `ai-adapters/`: adapter concisi per Codex, Claude Code, Copilot, Gemini CLI, Grok, Windsurf, agenti generici e app builder.
- `integrations/`: registry machine-readable degli adapter e delle superfici di integrazione della repo.
- `extensions/`: moduli opzionali e scopribili che estendono Specification-Driven Coding senza cambiare la pipeline ufficiale.
- `presets/`: bundle operativi scopribili che puntano a profili, blueprint, prompt, scorecard, fixture e gate esistenti.
- `MANIFESTO.it.md`: manifesto completo.
- `.specify/memory/constitution.md`: costituzione compatibile con flussi specification-first.
- `.specify/templates/overrides/`: template migliorati per spec, plan, tasks, research e acceptance.
- `docs/20-artifact-toolkit-model.md`: modello operativo di artefatti, comandi, template e validazione.
- `docs/21-command-model.md`: command model `/sdc.*` per usare la repo come toolkit operativo.
- `docs/25-english-public-index.md`: policy per documentazione pubblica English-first e companion italiane.
- `project-types/`: 20 profili progetto per evitare output generici. Ogni profile ha un profile-depth package con stack option, domain dictionary, security baseline, performance budget, testing contract e blueprint template.
- `blueprints/`: contratti verticali per progetti interi, task piccoli, web, mobile, WordPress, RAG e sistemi multi-agente.
- `prompts/`: prompt operativi per trasformare richieste incomplete in prompt e blueprint specifici.
- `agents/`: ruoli agentici e role prompt per prodotto, requirements, UX, platform, AI, security, QA, implementazione e release.
- `tools/sdc_signature.py`: contratti tipizzati stdlib-only, ispirati a DSPy, per future fasi compile e handoff.
- `skills/`: skill riusabili per attivare workflow specifici.
- `plugins/`: adapter per app builder, AGENTS.md, MCP, Cursor, Claude Code e flussi specification-first.
- `scorecards/`: rubriche di valutazione per prompt, blueprint, implementazione e sistemi multi-agente.
- `tools/`: script Python senza dipendenze per command surface, scaffold, lint e scoring euristico.
- `benchmarks/`: fixture, golden artifacts e report per harness riproducibile.
- `case-studies/`: studi comparativi raw prompt vs Specification-Driven Coding.
- `examples/`: esempi minimi di pacchetti Specification-Driven Coding.

## Workflow completo

```text
1. Leggi richiesta grezza
2. Produci intake con domande bloccanti o assunzioni reversibili
3. Scrivi specification verificabile
4. Seleziona project profile primario
5. Scrivi un Vertical Blueprint Contract
6. Definisci stack, file tree, dati, integrazioni, sicurezza, performance e test nel blueprint
7. Genera plan tecnico e task atomici dal blueprint
8. Implementa con scope controllato
9. Valuta con Evaluation Scorecard
10. Esegui release/iteration e aggiorna spec/blueprint se il codice diverge
```

## Regole fondative

> Se l’AI può scegliere una cosa importante senza che sia stata specificata o dichiarata come assunzione, il blueprint non è pronto.

> Un prompt incompleto non è un permesso per generare software generico. È un invito a costruire una specification migliore.

> Un prompt già ben strutturato non va ricostruito da zero. Va preservato, verificato e completato solo dove mancano decisioni critiche.

> Ogni prodotto AI deve restituire non solo output, ma anche una valutazione della propria aderenza alla specification.

## Validazione locale

Modalità contributor repository:

```bash
pip install -e .
sdc doctor
sdc doctor --quick
sdc list
sdc integration list
sdc integration list --format json
sdc extension list
sdc extension list --format json
sdc preset list
sdc preset list --format json
sdc demo list
sdc demo run --fixture 001-builder-habit-dashboard
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --workspace examples/enforcement-smoke
sdc enforce check --workspace examples/enforcement-smoke --format json
sdc init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
sdc harness run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py list
python3 tools/sdc.py integration list
python3 tools/sdc.py extension list
python3 tools/sdc.py preset list
python3 tools/sdc.py demo list
python3 tools/sdc.py demo run --fixture 001-builder-habit-dashboard
python3 tools/sdc.py enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc_enforce.py check --workspace examples/enforcement-smoke
python3 tools/sdc.py init "domain app" --type full-stack-saas --out /private/tmp/sdc-init-smoke
python3 tools/sdc.py harness run --fixture 001-builder-habit-dashboard
python3 tools/spec_lint.py
python3 tools/spec_scaffold.py --list
python3 tools/score_blueprint.py blueprints/02-full-project-blueprint.md
```

Uso senza installazione:

```bash
python3 -m sdc_cli doctor
python3 -m sdc_cli doctor --quick
python3 -m sdc_cli integration list
python3 -m sdc_cli extension list
python3 -m sdc_cli preset list
python3 -m sdc_cli demo run --fixture 001-builder-habit-dashboard
python3 -m sdc_cli enforce check --path benchmarks/golden/001-builder-habit-dashboard
python3 tools/sdc.py doctor
```

Modalità consumer senza installazione:

```bash
cd my-project
git clone https://github.com/2ord98/spec-coding-manifesto.git .sdc
python3 .sdc/tools/sdc.py doctor --quick
python3 .sdc/tools/sdc.py init "my project" --type marketing-site-cms --out "$PWD/sdc-workspace"
```

L'entrypoint `sdc` è pensato soprattutto per contributor mode e checkout `.sdc` incorporate. Questa release non impacchetta l'intera repository come tool remoto standalone e non installa automaticamente gli asset fuori dalla checkout.

`init` accetta sia `--name` sia una forma shorthand posizionale. Se `--type` manca, la CLI fallisce con un esempio esplicito invece di scaffoldingare in modo implicito.

`sdc compile` e `sdc handoff` sono comandi pianificati per una fase futura. Questo ciclo aggiunge la fondazione profile-depth e i contratti strutturali tipizzati che useranno, ma non implementa ancora quei comandi.

## Integrazioni, extension e preset

`integrations/catalog.json` descrive come tool, builder e agenti ingeriscono o usano la repository. `extensions/catalog.json` descrive moduli interni opzionali che estendono il metodo. `presets/catalog.json` descrive bundle operativi pronti per modalità comuni di Specification-Driven Coding.

Questi cataloghi sono solo metadati machine-readable per discovery. Non vengono installati automaticamente, non vengono applicati automaticamente e non sono un marketplace. Servono a sostenere contributi futuri senza indebolire anti-genericity, scorecard, sicurezza o pipeline ufficiale.

## Continuous Specification Enforcement

Specification-Driven Coding tratta specification e Vertical Blueprint come contratti vivi, non come file iniziali usa-e-getta. Se implementazione, task, scorecard o artifact divergono dal contratto, l'agente deve aggiornare la specification, aggiornare il Vertical Blueprint, correggere implementazione/artifact o accettare un'eccezione documentata.

```bash
sdc enforce check --path benchmarks/golden/001-builder-habit-dashboard
sdc enforce check --workspace examples/enforcement-smoke --format json
```

Lo strumento di enforcement è strutturale e usa solo stdlib. Segnala rischi di allineamento; non prova correttezza semantica.

## GitHub e Copilot

La repository include un layer GitHub leggero:

- `.github/copilot-instructions.md` fornisce a Copilot le regole repository-wide di Specification-Driven Coding.
- `.github/instructions/` aggiunge istruzioni Copilot path-specific per docs, file Python CLI, benchmark, blueprint, prompt, scorecard e skills.
- `.github/workflows/validate.yml` esegue la validazione in GitHub Actions.
- `.github/PULL_REQUEST_TEMPLATE.md` e `.github/ISSUE_TEMPLATE/` mantengono i contributi allineati a pipeline e validation gate.
- `.devcontainer/devcontainer.json` è opzionale per Codespaces/devcontainer e facilita i check locali.

L'integrazione GitHub non è obbligatoria. `AGENTS.md` resta l'entrypoint generico per agenti, e gli stessi artifact funzionano con altri coding agent, app builder, workflow MCP e uso CLI locale.

## Benchmark e harness

La repository include un harness strutturale riproducibile:

```bash
python3 tools/sdc_harness.py run --fixture 001-builder-habit-dashboard
python3 tools/sdc_harness.py run --fixture 002-b2b-leave-management
python3 tools/sdc_harness.py run --fixture 003-internal-pdf-rag-assistant
python3 tools/sdc_harness.py run --all
make harness
```

L'harness corrente valida completezza delle fixture, copertura dei golden artifact e forma della scorecard. `doctor` esegue tutte le fixture; `doctor --quick` mantiene il percorso smoke rapido sulla fixture `001`. E un gate, non una prova semantica definitiva della qualita del prodotto.

## Licenza

MIT. Vedi `LICENSE`.
