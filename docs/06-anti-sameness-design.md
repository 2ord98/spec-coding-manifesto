# Anti-Sameness Design

Gli AI app builder tendono a produrre output medi quando il prompt non contiene differenziazione. Specification-Driven Coding impone una fase anti-sameness.

## Checklist anti-genericità

Prima di implementare, l’agente deve rispondere:

1. Quale pattern comune rischiamo di ripetere?
2. Quale scelta visiva o strutturale rende il progetto specifico?
3. Quale parte del dominio deve emergere nella UI?
4. Quale stack default va evitato?
5. Quale dato di esempio dimostra realismo?
6. Quale micro-interazione è propria di questo caso?
7. Quale decisione non deve essere lasciata all’AI?

## Regole UI

- Vietati hero generici con “Unlock your potential”.
- Vietate card feature senza relazione al dominio.
- Vietati dashboard chart casuali.
- Vietati nomi tipo “TaskFlow”, “DataHub”, “AI Assistant” salvo richiesti.
- Ogni schermata deve avere scopo operativo.

## Regole architettura

- React non è default universale.
- Supabase/Firebase non sono default universali.
- Microservizi non sono default.
- RAG non è default per ogni chat.
- Multi-agent non è default per ogni automazione.

## Output richiesto

Ogni spec deve includere una sezione:

```markdown
## Anti-genericity constraints
- Pattern da evitare:
- Scelta distintiva:
- Dati realistici richiesti:
- Stack default esclusi:
- Criterio di accettazione non-generico:
```
