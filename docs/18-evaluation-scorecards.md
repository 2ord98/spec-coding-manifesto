# Evaluation Scorecards

Ogni output Specification-Driven Coding deve restituire una valutazione 0-100. La scorecard serve a rendere visibile quanto il prodotto aderisce alla specification e dove intervenire dopo.

I punteggi automatici presenti negli strumenti sono strutturali ed euristici. Per limiti e direzione futura, vedi `docs/18-scoring-and-evaluation-limits.md`.

## Scala

| Punteggio | Significato |
|---:|---|
| 90-100 | Pronto o quasi pronto; gap minori dichiarati |
| 75-89 | Buono, ma richiede correzioni puntuali |
| 60-74 | Prototipo utilizzabile ma non production-ready |
| 40-59 | Parziale; rischio alto di rework |
| 0-39 | Non aderente alla specification |

## Rubrica generale

| Area | Peso |
|---|---:|
| Aderenza all’intento | 15 |
| Specificità e anti-genericità | 15 |
| Architettura e stack rationale | 15 |
| Sicurezza, privacy e hardening | 15 |
| UX/domain fit | 10 |
| Completezza implementativa | 15 |
| Test, eval e osservabilità | 10 |
| Manutenibilità e deploy | 5 |
| **Totale** | **100** |

## Output richiesto

```markdown
# Final Scorecard

## Overall score

## Scores by area

| Area | Score | Reason |
|---|---:|---|

## Top 5 gaps

## Fix order

## Risks still open

## What changed from the original specification
```

## Regola

Se il punteggio è sotto 75, l’agente deve proporre la patch minima per superare il gate più importante.
