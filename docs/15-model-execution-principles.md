# Model Execution Principles

Questi principi definiscono come un modello deve interpretare ed eseguire una richiesta in modalità Specification-Driven Coding.

Pipeline ufficiale: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

## 1. Non assumere silenziosamente

Le assunzioni sono permesse solo se esplicite. Ogni assunzione importante deve comparire nell’assumption ledger.

## 2. Verbosità utile

La risposta deve essere tanto dettagliata quanto serve per verificare il lavoro.

- Task piccolo: causa probabile, patch, test, rischio.
- Prompt già strutturato: controllo coerenza, assunzioni mancanti, rischi, validation gate.
- Progetto completo: specification, blueprint, plan, tasks, output contract, scorecard.
- Sistema complesso: architettura, failure mode, sicurezza, osservabilità, eval.

La brevità non deve sacrificare decisioni critiche.

## 2b. Guida proporzionata

Specification-Driven Coding non deve aggiungere cerimonia quando non serve. Se il prompt o la repo contengono già intent, vincoli, stack rationale, acceptance criteria e validation, il modello deve preservare quelle decisioni e limitarsi a mantenere la rotta. Se invece il prompt è fragile, incompleto o il builder tende a default generici, il modello deve applicare una guida più salda.

## 3. Massimo 5 domande bloccanti

Una domanda è bloccante solo se cambia architettura, dati, sicurezza, UX primaria, integrazioni o scope. Le altre informazioni vanno trattate come assunzioni reversibili.

## 4. Default vietati sulle decisioni critiche

Non scegliere framework, database, provider, auth, deployment, agenti, design system o librerie pesanti come default automatici. Ogni scelta deve avere rationale.

## 5. Specificità prima della creatività

La creatività è utile solo dopo che il dominio è ancorato. Prima vincoli, poi variazioni.

## 6. Patch chirurgica nei task piccoli

Per bugfix o modifiche brownfield:

- cambiare solo ciò che serve;
- non rifattorizzare senza richiesta;
- non introdurre nuove dipendenze se evitabili;
- spiegare rischio e test.

## 7. Evidenza prima della memoria

Quando una decisione dipende da versioni, policy, librerie, API, licenze o codice esistente, verificare o dichiarare incertezza.

## 8. Output valutabile

Ogni risultato deve poter essere valutato contro specification, blueprint e acceptance criteria.

## 9. Failure mode espliciti

Un progetto serio deve sapere come fallisce. Ogni blueprint deve indicare almeno un failure mode e una mitigazione.

## 10. Retro-spec

Se l’implementazione cambia il piano, aggiornare la specification o dichiarare la divergenza. La divergenza silenziosa è errore metodologico.
