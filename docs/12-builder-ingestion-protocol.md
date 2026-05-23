# Builder Ingestion Protocol

Questa repo è progettata per essere caricata dentro AI builder, coding agent e sistemi multi-agente. Il builder deve usarla come instruction layer per trasformare input incompleti in prodotti Specification-Driven Coding.

Pipeline ufficiale: Raw request -> Intake -> Specification -> Project Profile Selection -> Vertical Blueprint -> Plan -> Tasks -> Implementation -> Evaluation Scorecard -> Release/Iteration.

Specification-Driven Coding non serve a scrivere prompt più lunghi in senso generico. Compila richieste incomplete in specification e vertical blueprint pronti per l’esecuzione, così builder e agenti costruiscono software esplicito, specifico per progetto e verificabile.

## Ruolo della repo

La repo non è un generatore di prompt cosmetici. È un compilatore metodologico.

```text
richiesta incompleta dell’utente
  + questa repo
  = Specification-Driven Prompt
  + Vertical Blueprint Contract
  + implementazione controllata
  + scorecard finale
```

## Regole per il builder

1. Non eseguire direttamente il prompt grezzo.
2. Normalizza intento, dominio, utente, vincoli e non-obiettivi.
3. Scegli un project profile primario.
4. Se la richiesta è piccola, usa `blueprints/12-targeted-change-blueprint.md`.
5. Se la richiesta è un progetto completo, usa `blueprints/02-full-project-blueprint.md`.
6. Se il dominio ha un blueprint verticale, usa quello.
7. Fai massimo 5 domande bloccanti.
8. Per dettagli non bloccanti, dichiara assunzioni reversibili.
9. Produci file, patch o progetto solo dopo un output contract verificabile.
10. Chiudi con scorecard e gap residui.

## Pacchetto minimo da produrre prima dell’implementazione

```markdown
# Builder Execution Packet

## Raw intent summary

## Specification-Driven Prompt

## Project profile

## Blocking questions

## Assumption ledger

## Vertical Blueprint Contract

## Output/file contract

## Implementation plan

## Acceptance gates

## Scorecard rubric
```

## Quando il builder non può fare domande

Se lo strumento è single-shot o non permette chiarimento, deve procedere così:

1. dichiarare le assunzioni;
2. scegliere opzioni conservative;
3. evitare decisioni irreversibili;
4. marcare i punti da validare dopo la prima generazione;
5. produrre comunque una prima versione specifica, non generica.

## Uso con app builder

Per strumenti come Emergent, Manus, Base44-style, Lovable, Bolt, v0, Replit o equivalenti:

```text
Leggi questa repo e comportati come compilatore Specification-Driven Coding.
Prima converti la mia richiesta in Builder Execution Packet.
Poi genera il prodotto rispettando il Vertical Blueprint Contract.
Non usare template generici se il dominio richiede scelte specifiche.
Alla fine valuta il risultato con scorecard 0-100.
```
