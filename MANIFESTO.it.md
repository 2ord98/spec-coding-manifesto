# Manifesto di Specification-Driven Coding

[English version ->](MANIFESTO.md)

## 1. Il vero problema non e solo il prompt

I prompt vaghi sono una modalita di fallimento visibile, ma non esauriscono il problema.

Il problema piu profondo e il loop di generazione prodotto guidato dall'AI, che trasforma un'intenzione incompleta in software medio. Quando una richiesta lascia vuoti, modelli, app builder e workflow agentici riempiono quei vuoti con prior statistici, template di prodotto, pattern UI mediani, stack familiari, abitudini di planning superficiali e assunzioni nascoste.

Il risultato puo sembrare funzionale pur restando generico. Puo passare una demo e fallire il dominio.

Specification-Driven Coding esiste perche il fallimento e sistemico: intento debole, default del modello, template dei builder, memoria di progetto mancante, vincoli mancanti, skill o plugin saltati, selezione pigra dello stack e valutazione debole si sommano in prodotti plausibili ma non specifici.

E un livello di metodo e guida, non una fabbrica di progetti, un app generator o un sostituto del giudizio ingegneristico. I suoi strumenti scaffoldano workspace di specification e superfici di validazione; non producono prodotti finiti da soli.

## 2. Il vibe coding ha cambiato la velocita di creazione

Il vibe coding ha cambiato davvero la creazione di software. Ha reso i prototipi piu rapidi, l'esplorazione piu economica e la costruzione di software piu accessibile a chi sa esprimere un'idea prima ancora di saper specificare un'architettura.

Questo conta. L'esplorazione veloce e utile. L'iterazione in linguaggio naturale e utile. I prototipi usa-e-getta sono utili.

Il problema inizia quando la generazione esplorativa diventa costruzione di prodotto senza un contratto piu forte. Velocita senza specificita produce movimento, non necessariamente giudizio di prodotto.

## 3. Ma i prodotti vibe-coded convergono

Quando i sistemi AI riempiono l'intento mancante con pattern medi, i prodotti convergono.

Convergono verso le stesse landing page, le stesse dashboard, le stesse card arrotondate, gli stessi flussi di auth, lo stesso copy generato, gli stessi stack SaaS generici, la stessa finta lucidatura, gli stessi placeholder e lo stesso debole domain fit.

Convergono anche architetturalmente: framework di default, database di default, auth di default, assunzioni di deploy di default, pannelli admin di default, RAG di default, flussi multi-agent di default.

Non e solo un problema estetico. E un problema di prodotto e di ingegneria. Il software convergente nasconde decisioni mancanti dietro forme familiari. Sembra finito prima di essere stato capito.

## 4. La specification strutturata e il minimo

Specification-Driven Coding parte da un minimo pratico stabilito dai workflow di sviluppo guidati da specification: constitution, specification, clarification, checklist, technical plan, tasks, analysis, implementation, template, file di prompt per agenti e script di validazione.

Quel minimo e importante perche sposta lo sviluppo assistito dall'AI lontano dal prompting one-shot e verso artifact espliciti.

Specification-Driven Coding va oltre. Aggiunge raw-request intake, project profile selection, Vertical Blueprint Contract, builder ingestion, workflow targeted-change, scorecard, gate di anti-genericity, adapter cross-agent e una gestione piu forte dell'intento incompleto.

I workflow specification-first di base rendono piu disciplinato il passaggio da specification a implementazione. Specification-Driven Coding aggiunge i layer mancanti davanti e nel mezzo: come l'intento grezzo diventa una specification specifica per dominio e come quella specification diventa un execution contract abbastanza forte per app builder, coding agent e sistemi multi-agent.

## 5. Definizione

**Specification-Driven Coding** e un metodo di sviluppo AI-native che compila intenzione umana incompleta in construction contract espliciti, specifici per dominio e ingestibili dai tool prima della generazione del prodotto o dell'implementazione del codice.

In questa repository, `spec` significa **specification**. La specificita e l'esito: software ancorato a un utente reale, a un dominio, a un workflow, a uno stack motivato, a un modello dati, a vincoli, postura di sicurezza, test e criteri di valutazione.

La pipeline ufficiale e:

```text
Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration
```

## 6. La repo non e una collezione di prompt

Questa repository non e una collezione di prompt piu lunghi.

E un ingestion layer e un toolkit per AI builder, coding agent, app generator e workflow multi-agent. Il suo compito e costringere il sistema a chiedere, assumere, vincolare, specializzare, costruire, validare e valutare.

Un prompt piu lungo puo comunque restare generico. Un pacchetto forte di Specification-Driven Coding e diverso: lega intento, dominio, vincoli, stack, output file, safety, fallback, accettazione e valutazione prima che la generazione inizi.

Il metodo deve essere proporzionato. Quando un prompt e gia strutturato, specifico, vincolato e abbinato a uno strumento capace, Specification-Driven Coding dovrebbe agire come steering leggero: preservare le decisioni esistenti, controllare le assunzioni, esporre i gate mancanti e validare l'output. Quando il prompt e fragile, il builder tende ai template o il rischio di prodotto e alto, il metodo deve diventare piu rigido e richiedere il percorso completo intake, profile, blueprint, plan, tasks e scorecard.

## 7. Lo Specification-Driven Prompt

Uno Specification-Driven Prompt valido contiene o deriva:

- intento;
- utente primario;
- dominio;
- non-obiettivi;
- vincoli;
- assunzioni;
- project profile;
- stack rationale;
- modello dati;
- direzione UX;
- file/output contract;
- integrazioni;
- sicurezza;
- performance;
- test;
- acceptance criteria;
- scorecard.

Quando questi elementi mancano, l'agente o il builder non deve riempirli silenziosamente con default. Deve fare un pass compatto di domande bloccanti o produrre un assumption ledger visibile con rationale, impatto, reversibilita e verifica.

## 8. Il Vertical Blueprint Contract

Il Vertical Blueprint Contract e l'estensione chiave oltre lo sviluppo di base guidato da specification.

Viene prima del plan finale e dei tasks perche definisce l'execution contract. Vincola ruolo, stack, file tree, architettura, output format, confini di implementazione, fallback, quality gate e comportamento specifico per dominio prima che il lavoro venga scomposto.

Senza blueprint, un plan puo ancora introdurre default generici di nascosto. Con il blueprint, il plan deve spiegare come eseguire un contratto di prodotto specifico.

Un Vertical Blueprint non e planning decorativo. E l'artifact che fa produrre a un AI builder o a un coding agent questo prodotto, per questo dominio, con questo stack, sotto questi vincoli.

## 9. Principio di anti-genericity

Un output non e accettabile solo perche funziona.

Deve dimostrare di appartenere a questo dominio, a questo utente, a questo workflow, a questo prodotto, a questo stack e a questo insieme di vincoli.

L'anti-genericity non e novita visiva fine a se stessa. E la prova che il prodotto ha capito il suo contesto. Dati reali, vocabolario di dominio, flussi specifici, non-obiettivi espliciti, stack rationale, stati d'errore e failure mode contano piu della semplice lucidatura.

Un prodotto generato che potrebbe appartenere a qualsiasi startup non appartiene a nessuna.

## 10. Responsabilita dell'AI/builder

L'AI builder o il coding agent hanno responsabilita.

Non devono defaultare silenziosamente a template comuni. Non devono inventare la struttura di prodotto senza marcare le assunzioni. Non devono saltare skill, plugin, context pack, tool MCP o project profile rilevanti. Non devono nascondere l'incertezza. Non devono produrre un'app generica quando la richiesta e sottospecificata.

Quando mancano informazioni, l'agente deve produrre un pass di chiarimento compatto o un assumption ledger. Quando una scelta impatta architettura, dati, sicurezza, privacy, costo, deploy, integrazioni, permessi o scope, quella scelta deve essere esplicita.

All'agente non e permesso trasformare l'ambiguita in falsa confidenza.

## 11. Responsabilita del developer/operator

Anche developer e operator hanno responsabilita.

Anche developer esperti possono essere pigri con l'AI: usare il contesto sbagliato, saltare la skill giusta, ignorare i project profile, accettare stack di default, fidarsi dell'architettura generata o scambiare una demo lucidata per validazione.

Specification-Driven Coding richiede all'operatore di selezionare il profilo giusto, caricare l'adapter giusto, usare la skill o il plugin giusto, ispezionare architettura e sicurezza, verificare la scorecard e rifiutare output generico.

L'AI non rimuove il giudizio ingegneristico. Rende piu veloce il cattivo giudizio.

## 12. Modalita small task

Specification-Driven Coding non e solo per full project.

Si applica anche a bug fix, piccole feature, cambi UI, fix di config, aggiornamenti documentali, patch di sicurezza, dependency update e manutenzione brownfield.

Il principio targeted-change e:

```text
inspect before edit -> probable cause -> exact files -> minimal patch -> validation -> rollback
```

Il lavoro piccolo non richiede per forza un blueprint completo di prodotto. Richiede comunque disciplina di scope, assunzioni esplicite, validazione rilevante e una scorecard scalata sul rischio.

## 13. Modalita multi-agent

Gli agenti non sono collaboratori liberi. Sono ruoli governati.

Un sistema multi-agent dovrebbe definire planner, architect, implementer, verifier e safety/release gate. Ogni agente ha bisogno di un mandato, input consentiti, output richiesti, tool permessi, tool vietati, stop condition, reviewer e quality gate.

Nessun agente ha autorita illimitata. Tool call, permessi di scrittura, azioni distruttive, comunicazione esterna, accesso a dati sensibili, remediation di sicurezza, decisioni legali, mediche, finanziarie e azioni nel mondo fisico richiedono gate di approvazione espliciti.

Lavoro multi-agent senza governance significa solo ambiguita distribuita.

## 14. La valutazione e parte del prodotto

Ogni output significativo deve restituire una scorecard.

La scorecard deve valutare:

- aderenza alla specification;
- anti-genericity;
- completezza;
- UX/domain fit;
- architettura;
- sicurezza;
- performance;
- test;
- rischi residui;
- next fixes.

La valutazione non e un abbellimento finale. E parte del contratto di prodotto. Se l'output non puo essere valutato, non e pronto.

## 15. La specification deve restare viva

Specification-Driven Coding non tratta la specification come documento iniziale usa-e-getta. Specification e Vertical Blueprint sono contratti vivi.

Se l'implementazione diverge, l'agente non deve nasconderlo. Deve aggiornare la specification, aggiornare il Vertical Blueprint, correggere implementazione/artifact o accettare un'eccezione documentata con rationale.

## 16. Principio finale

Non chiedere all'AI di costruire da vibes.

Fai compilare all'AI l'intento in un contratto, specializzare il contratto in un blueprint, implementare contro quel blueprint e valutare il risultato.
