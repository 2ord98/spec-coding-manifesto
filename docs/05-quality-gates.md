# Quality Gates

I gate impediscono che un output plausibile venga scambiato per un output corretto.

## Gate 1 — Specificità

Passa se:

- utente primario definito;
- problema definito;
- non-obiettivi definiti;
- modalità operativa scelta;
- project profile scelto;
- almeno un vincolo non negoziabile presente.

## Gate 2 — Non genericità

Passa se:

- UI e architettura sono motivate dal dominio;
- stack non scelto per abitudine;
- dati di esempio sono realistici;
- copy e naming non sono placeholder;
- il risultato non somiglia a un template SaaS generico;
- esiste almeno una scelta distintiva verificabile.

## Gate 3 — Blueprint

Passa se:

- ruolo tecnico definito;
- file tree previsto;
- file obbligatori elencati;
- output format dichiarato;
- sicurezza stack-specifica definita;
- performance budget presente;
- test/verifiche richiesti.

## Gate 4 — Contratti

Passa se:

- API/data contracts definiti quando necessari;
- acceptance criteria testabili;
- error states definiti;
- edge cases presenti;
- criteri di rifiuto/out-of-scope presenti per AI systems;
- tool calls e permessi definiti nei sistemi agentici.

## Gate 5 — Sicurezza e privacy

Passa se:

- auth/permissions definite;
- dati sensibili identificati;
- secret handling specificato;
- logging non espone PII;
- azioni distruttive gated;
- richieste esterne validate.

## Gate 6 — Implementabilità

Passa se:

- task atomici;
- ordine dipendenze chiaro;
- build/test commands definiti;
- deploy target definito;
- rollback o fallback considerato;
- assunzioni residue non bloccanti.

## Gate 7 — Testabilità

Passa se:

- almeno un test o verifica per requisito critico;
- dati di prova realistici;
- criteri di fallimento espliciti;
- controlli manuali dichiarati dove i test automatici non bastano.

## Gate 8 — Scorecard

Passa se il risultato finale include punteggi su:

- aderenza alla spec;
- specificità;
- architettura;
- sicurezza/privacy;
- performance;
- UX/accessibilità;
- testabilità;
- manutenibilità;
- rischio residuo.

## Gate 9 — Audit finale

Passa se:

- ogni feature implementata mappa un requisito;
- ogni requisito critico ha test o verifica;
- decisioni implicite emerse sono documentate;
- spec e blueprint sono aggiornati dopo implementazione.

## Soglie consigliate

| Contesto | Soglia minima |
|---|---:|
| Throwaway prototype | 60/100 |
| Demo interna | 70/100 |
| MVP pubblico | 80/100 |
| Production | 88/100 |
| Enterprise / regulated | 92/100 |

Un punteggio sotto soglia non vieta la consegna, ma obbliga a dichiarare rischi, gap e priorità di correzione.
