# Contributing

[English version ->](CONTRIBUTING.md)

Questa repository accetta contributi che migliorano il protocollo **Specification-Driven Coding** senza renderlo piu generico.

L'obiettivo non e aggiungere piu prompt, piu documentazione o piu complessita.  
L'obiettivo e rendere l'output AI piu specifico, piu verificabile e meno dipendente da default medi, template riciclati e assunzioni nascoste.

## Principio guida

Ogni contributo deve migliorare almeno una di queste qualita:

- specificita del dominio;
- chiarezza degli artifact;
- riduzione delle assunzioni implicite;
- qualita dei Vertical Blueprint;
- anti-genericita dell'output;
- sicurezza;
- testabilita;
- valutazione tramite scorecard;
- compatibilita con builder, coding agent o workflow multi-agent;
- riproducibilita tramite fixture, golden artifact o harness run.

Se un contributo aggiunge testo ma non migliora una di queste proprieta, probabilmente non appartiene alla repository.

## Tipi di contributo accettati

Sono benvenuti contributi per:

- nuovi project profile;
- nuovi Vertical Blueprint Contract;
- nuovi prompt operativi;
- nuove scorecard;
- nuove skill;
- nuovi adapter per builder o coding agent;
- nuove benchmark fixture;
- nuovi golden artifact;
- nuovi case study;
- miglioramenti a `tools/sdc.py`;
- miglioramenti a `tools/spec_lint.py`;
- miglioramenti a `tools/sdc_harness.py`;
- correzioni di naming, link, consistenza o pipeline;
- documentazione che rende il protocollo piu applicabile.

## Tipi di contributo rifiutati

I contributi non sono accettati se:

- rendono il metodo piu generico;
- aggiungono prompt vaghi;
- aggiungono template senza quality gate;
- introducono tool obbligatori non necessari;
- trasformano la repository in una lista di link;
- aggiungono framework o dipendenze senza rationale;
- duplicano contenuti esistenti;
- rimuovono vincoli di sicurezza, privacy o validazione;
- riducono l'importanza di blueprint, scorecard o anti-genericity;
- presentano output generico come accettabile solo perche funziona.

## Pipeline ufficiale

Ogni contributo deve rispettare la pipeline ufficiale:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

Il **Vertical Blueprint** viene prima del plan finale e dei task.

## Naming

Usa sempre il nome ufficiale della metodologia:

```text
Specification-Driven Coding
```

`spec-coding-manifesto` e consentito solo come slug della repository.

## Regole PR

### Project profile

Ogni nuovo project profile deve includere:

- quando usarlo;
- domande bloccanti;
- stack candidate;
- campi obbligatori;
- anti-pattern;
- acceptance gate;
- considerazioni di sicurezza/privacy;
- assunzioni di performance o deployment;
- focus atteso della scorecard.

### Blueprint

Ogni nuovo blueprint deve includere:

- role contract;
- domain intent;
- project profile;
- stack rationale;
- architecture/file contract;
- security/privacy contract;
- quality gate;
- validation;
- scorecard attesa.

### Prompt

Ogni nuovo prompt deve:

- ridurre l'ambiguita;
- dichiarare input e output;
- gestire richieste incomplete;
- usare assunzioni reversibili;
- evitare bloat;
- produrre artifact verificabili.

### Scorecard

Ogni nuova scorecard deve:

- usare criteri pesati;
- includere anti-genericity;
- includere domain fit;
- includere rischi residui;
- distinguere structural gate da semantic evaluation.

### Adapter/plugin

Ogni nuovo adapter deve spiegare:

- il tool o builder target;
- quando usarlo;
- quali file caricare;
- i limiti del tool;
- l'output contract richiesto;
- la validazione attesa.

### Entry nel catalogo extension

Ogni proposta di extension deve includere:

- `id`;
- `type`;
- `status`;
- `files`;
- `primary_use`;
- `requires`;
- `output_contract`;
- `known_limits`;
- comando di validazione.

Le extension sono solo metadati di discovery. Non devono introdurre esecuzione remota di codice, comportamento di install automatico, dipendenze nascoste, bundle generici o vincoli piu deboli su anti-genericity, scorecard, sicurezza, privacy o pipeline. Ogni file elencato deve esistere.

### Entry nel catalogo preset

Ogni proposta di preset deve includere:

- `id`;
- `project_profile`;
- `blueprints`;
- `prompts`;
- `scorecards`;
- `fixtures` quando disponibili;
- `best_for`;
- `quality_gates`;
- `known_limits`.

I preset devono rafforzare la specificita, non diluirla. Non devono applicare file automaticamente, nascondere dipendenze, bypassare la validazione o puntare a workflow generici. Ogni file e fixture elencati devono esistere.

### Benchmark fixture

Ogni nuova benchmark fixture deve includere:

- `raw-prompt.md`;
- `sdc-prompt.md`;
- `expected.json`;
- golden artifact:
  - `intake.md`;
  - `spec.md`;
  - `blueprint.md`;
  - `plan.md`;
  - `tasks.md`;
  - `scorecard.md`.

La fixture deve passare:

```bash
python3 tools/sdc_harness.py run --fixture <fixture-id>
```

## Checklist contributor

Prima di aprire una PR:

- [ ] Ho rispettato la pipeline ufficiale.
- [ ] Ho evitato frasi generiche.
- [ ] Ho aggiunto vincoli verificabili.
- [ ] Ho incluso esempi concreti.
- [ ] Ho dichiarato non-obiettivi o anti-pattern.
- [ ] Ho incluso quality gate.
- [ ] Ho aggiornato scorecard o benchmark quando necessario.
- [ ] Ho evitato nuove dipendenze non necessarie.
- [ ] Ho controllato link interni e path.
- [ ] Ho eseguito `python3 tools/spec_lint.py`.
- [ ] Ho eseguito `python3 tools/sdc.py doctor`.
- [ ] Ho eseguito `make harness`.

## Checklist maintainer

Prima del merge:

- [ ] Il contributo rende il protocollo piu specifico, non piu generico.
- [ ] Non introduce ambiguita nella pipeline.
- [ ] Non introduce provenance AI o linguaggio di authorship non autonomo.
- [ ] Non indebolisce privacy, sicurezza o validazione.
- [ ] Non duplica contenuti gia presenti.
- [ ] I comandi di validazione passano.
- [ ] Il contributo e coerente con manifesto, command model, blueprint e scorecard.

## Filosofia

Un buon contributo non aggiunge solo contenuto.  
Aggiunge **controllo operativo**.

Un buon contributo non rende l'AI piu libera di inventare.  
Rende l'AI piu capace di costruire prodotti specifici, verificabili e non generici.
