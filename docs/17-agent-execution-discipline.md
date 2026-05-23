# Agent Execution Discipline

Gli agenti devono produrre risultati forti senza diventare prolissi, fragili o incontrollabili.

## Non assumere silenziosamente

Se una decisione cambia architettura, dati, sicurezza, privacy, costo o scope, non va assunta in silenzio.

Formato:

```markdown
## Assunzione
- Decisione:
- Perché serve:
- Rischio:
- Alternativa:
- Come verificarla:
```

## Verbosità controllata

Output completo non significa output enorme.

Preferire:

- spiegazioni brevi;
- file necessari;
- codice leggibile;
- commenti solo dove servono;
- task piccoli;
- verifiche esplicite.

Evitare:

- commenti riga per riga su codice ovvio;
- astrazioni non richieste;
- file “helper” senza uso reale;
- boilerplate decorativo;
- refactor non necessari;
- stack scelti per moda.

## Incrementalità

Per codice e prodotti complessi:

1. definire slice minima;
2. implementare;
3. verificare;
4. aggiornare spec/blueprint;
5. passare alla slice successiva.

## Brownfield discipline

In un progetto esistente:

- leggere struttura e convenzioni prima di modificare;
- cambiare solo ciò che serve;
- non rinominare file o componenti senza motivo;
- non introdurre nuove dipendenze se non indispensabili;
- preservare API pubbliche salvo richiesta esplicita;
- produrre diff minimo.

## Fail-safe

L’agente deve fermarsi e chiedere approvazione quando:

- deve usare secrets;
- deve cancellare dati;
- deve cambiare schema in modo distruttivo;
- deve fare deploy;
- deve inviare comunicazioni reali;
- deve eseguire tool write-capable non reversibili.
