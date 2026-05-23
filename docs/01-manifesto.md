# Specification-Driven Coding Manifesto

## 1. Il problema

Il vibe coding ha reso possibile trasformare intenzioni naturali in software funzionante. Ha accelerato prototipi, abbassato la barriera di ingresso e permesso a più persone di costruire prodotti digitali.

Il suo limite strutturale emerge quando il prompt è vago: l’AI riempie i vuoti con pattern medi. Il risultato può funzionare, ma tende ad assomigliare a molti altri risultati: stessa landing, stessa dashboard, stessi componenti, stesso stack, stesso modello dati implicito, stessi errori nascosti.

Il problema non è l’AI. Il problema è l’input non specifico trasformato direttamente in codice.

## 2. La tesi

Specification-Driven Coding è il passaggio da:

```text
prompt naturale → codice generato
```

a:

```text
raw request → intake → specification → project profile → vertical blueprint → plan → tasks → codice → scorecard → release/iteration
```

Non significa scrivere documentazione sterile. Significa rendere il prompt dell’utente un artefatto ingegneristico capace di guidare modelli, app builder e agenti senza lasciare decisioni critiche ai default statistici.

## 3. Definizione

**Specification-Driven Coding** è una modalità di sviluppo AI-native in cui una richiesta grezza viene trasformata in una specification viva, specifica per dominio, verificabile e vincolante prima di generare codice o prodotto.

In questa metodologia, `spec` significa **specification**. La specificità non è il nome tecnico: è il risultato. Una specification buona rende il codice specifico rispetto a utenti, dominio, stack, dati, qualità, sicurezza, performance e criteri di accettazione.

## 4. Il prompt non è un messaggio: è un contratto

Un prompt valido per Specification-Driven Coding deve contenere o derivare esplicitamente:

- intento;
- utente primario;
- dominio;
- contesto operativo;
- non-obiettivi;
- vincoli non negoziabili;
- project profile;
- stack o spazio decisionale;
- modello dati;
- integrazioni;
- sicurezza;
- performance budget;
- output/file contract;
- test;
- acceptance criteria;
- scorecard finale.

Quando questi elementi mancano, l’agente non deve produrre un’app generica. Deve costruire uno **Specification-Driven Prompt** dichiarando domande bloccanti e assunzioni reversibili.

## 5. Il Vertical Blueprint Contract

La specification chiarisce cosa deve essere vero. Il blueprint verticale chiarisce come l’AI deve produrre il risultato.

Nella pipeline ufficiale, il Vertical Blueprint viene prima del plan finale e dei tasks. Il motivo è operativo: senza blueprint non sono ancora vincolati stack, file tree, confini, sicurezza, output format, fallback e quality gates. Un piano scritto prima di questi contratti è ancora troppo libero.

Un **Vertical Blueprint Contract** definisce:

- ruolo tecnico dell’agente;
- dominio e contenuti specifici;
- architettura richiesta;
- stack motivato;
- struttura cartelle;
- file obbligatori;
- codice completo o patch attesa;
- vincoli di sicurezza specifici per stack;
- UX e motion direction;
- performance target e fallback;
- test minimi;
- criteri di accettazione;
- punteggio finale.

Questo layer supera il prompt lungo generico: non chiede solo “costruisci X”, ma impedisce all’AI di decidere il progetto con template medi.

## 6. Il ruolo del vibe coding

Il vibe coding resta utile per esplorare:

- idee;
- alternative UX;
- prototipi;
- proof of concept;
- prime bozze.

Specification-Driven Coding prende velocità, creatività e iterazione del vibe coding e le incanala in un sistema di vincoli. La fase esplorativa può essere libera; la fase costruttiva deve essere specifica.

## 7. Regola dell’intento esplicito

Ogni scelta importante deve essere esplicita o dichiarata come assunzione.

Sono scelte importanti:

- framework;
- runtime;
- database;
- auth;
- permessi;
- privacy;
- deployment;
- costi runtime;
- integrazioni;
- dati di esempio;
- UX primaria;
- design system;
- test;
- logging;
- failure mode.

Se l’AI sceglie una di queste cose perché “di solito si fa così”, la specification è incompleta.

## 8. Regola anti-genericità

L’output deve dimostrare di appartenere a quel progetto e non a un template medio.

Ogni progetto deve avere almeno:

- un utente primario nominabile;
- un problema specifico;
- una metrica di successo;
- un vincolo non negoziabile;
- una decisione di stack motivata;
- una direzione UX coerente con il dominio;
- dati realistici minimi;
- un failure mode previsto;
- una checklist di accettazione.

## 9. Regola delle assunzioni controllate

Non tutto può essere chiarito prima di iniziare. Ma ogni assunzione deve essere visibile.

Ogni assunzione importante deve dichiarare:

```text
Assunzione:
Perché è necessaria:
Impatto se sbagliata:
Quanto è reversibile:
Come verificarla:
```

Le domande all’utente devono essere poche e bloccanti. Per il resto, l’agente deve procedere con assunzioni esplicite, verificabili e facili da correggere.

## 10. Regola della verbosità utile

La risposta dell’agente deve essere abbastanza dettagliata da rendere verificabile il lavoro, ma non così lunga da nascondere decisioni critiche.

- Per task piccoli: patch breve, motivazione, rischi, test.
- Per progetti interi: specification, blueprint, file contract, piano, task, scorecard.
- Per sistemi complessi: architettura, failure mode, security, observability, valutazione.

La sintesi è utile solo quando non elimina informazioni necessarie alla verifica.

## 11. Regola della spec viva

La specification non si chiude quando parte l’implementazione.

Ogni modifica importante deve aggiornare almeno uno di questi artefatti:

- specification;
- blueprint;
- plan;
- tasks;
- data model;
- API contract;
- acceptance criteria;
- quality gate;
- scorecard.

Il codice non deve diventare l’unica fonte di verità.

## 12. Regola degli agenti limitati

Un agente non è un mago. È un ruolo con mandato, input, output, strumenti permessi, limiti, criteri di successo e reviewer.

Nei sistemi multi-agente, gli agenti devono essere progettati come componenti governati:

```text
planner → executor → verifier → safety/release gate
```

Nessun agente deve avere permessi illimitati. Tool calls, scrittura dati, automazioni distruttive e decisioni ad alto impatto richiedono gate espliciti.

## 13. Regola della valutazione finale

Ogni prodotto generato deve restituire una scorecard, non solo il codice.

La scorecard deve indicare:

- punteggio complessivo 0-100;
- aderenza alla specification;
- completezza;
- sicurezza;
- UX/domain fit;
- performance;
- test;
- rischi residui;
- prossime correzioni prioritarie.

Un output che non può essere valutato non è pronto.

## 14. Formula operativa

```text
Raw intent
+ context grounding
+ project profile
+ assumption ledger
+ project profile
+ vertical blueprint
+ output contract
+ quality gates
+ scorecard
= AI product generation without generic defaults
```

## 15. Principio finale

> Non chiedere all’AI di costruire un’app. Costruisci prima il modo corretto in cui l’AI deve capirla, vincolarla, implementarla e valutarla.
