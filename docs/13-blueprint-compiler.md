# Blueprint Compiler

Il Blueprint Compiler è il livello che rende Specification-Driven Coding utilizzabile con coding agent, app builder, prompt-to-product builder, sistemi multi-agente e strumenti di prototipazione rapida.

Specification-Driven Coding compila richieste incomplete in specification e vertical blueprint pronti per l’esecuzione, guidando AI builder e agenti fuori dal vibe coding generico e verso costruzione software esplicita, specifica per progetto e verificabile.

## Scopo

Trasformare una richiesta incompleta in un **builder-ready blueprint**.

Il blueprint non è un prompt lungo. È una struttura di decisioni che impedisce al modello di generare output medi.

Pipeline ufficiale:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

## Input

```text
Richiesta utente + repo Specification-Driven Coding + eventuale codice/prodotto esistente
```

## Output

```text
Domande bloccanti, massimo 5
Assumption ledger con assunzioni reversibili
Specification-Driven Prompt o spec sintetica
Project profile
Blueprint verticale
Plan e task o slices
Quality gates
Scorecard target
```

## Pattern di scomposizione

Ogni blueprint deve usare questa sequenza:

1. **Role frame**: quale competenza deve assumere l’agente.
2. **Product frame**: cosa si sta costruendo e per chi.
3. **Domain frame**: contenuti, regole, dati e contesto reale.
4. **Architecture frame**: stack, componenti, confini, integrazioni.
5. **Interface frame**: UI, API, CLI, workflow o agent interface.
6. **Data frame**: entità, input, output, retention, privacy.
7. **Security frame**: auth, permessi, nonce/token, secret handling, threat model.
8. **Performance frame**: budget, fallback, lazy loading, caching, limiti runtime.
9. **Motion/UX frame**: quando applicabile, direzione visiva e interazioni non generiche.
10. **File contract**: albero cartelle, file obbligatori, file opzionali, output completo.
11. **Execution contract**: confini implementativi, ordine implementazione, fallback, stop conditions, human approval.
12. **Evaluation contract**: test, scorecard e audit finale.

## Modalità full project

Usare quando l’obiettivo è costruire un prodotto da zero.

Obbligatorio:

- file tree;
- file chiave;
- data model;
- acceptance criteria;
- security/privacy gates;
- deployment assumptions;
- integration assumptions;
- fallback behavior;
- scorecard.

## Modalità targeted change

Usare quando l’obiettivo è modificare un progetto esistente.

Obbligatorio:

- scope minimo;
- file potenzialmente toccati;
- regressioni da evitare;
- test prima/dopo;
- rollback;
- divieto di refactor non richiesti.

## Modalità app builder

Usare con strumenti che generano prodotto da prompt.

Obbligatorio:

- limitare default generici;
- specificare utente e dominio;
- imporre dati realistici;
- definire stack solo se lo strumento lo consente;
- chiedere output verificabile;
- chiedere scorecard.

## Modalità multi-agente

Usare quando il prodotto contiene o usa più agenti.

Obbligatorio:

- agent card per ogni agente;
- orchestratore;
- routing;
- memoria;
- tool permissions;
- audit log;
- human approval;
- failure modes;
- evaluation harness.

## Regole anti-genericità nel blueprint

Ogni blueprint deve dichiarare:

```text
Default da evitare:
Scelta distintiva obbligatoria:
Dati realistici minimi:
Pattern UX vietati:
Stack default esclusi:
Criterio di non-genericità:
```

## Stop conditions

L’agente deve fermarsi prima di implementare se:

- manca un vincolo di sicurezza essenziale;
- non è chiaro dove salvare dati sensibili;
- non è chiaro chi può fare cosa;
- il file contract è ambiguo;
- l’output richiesto viola una policy, una licenza o un vincolo legale;
- il progetto richiede accesso a sistemi reali senza approvazione umana.
