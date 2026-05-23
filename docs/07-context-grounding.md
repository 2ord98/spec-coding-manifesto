# Context Grounding

Specification-Driven Coding richiede che l’agente separi ciò che sa da ciò che deve verificare.

## Greenfield

Per progetti da zero:

- verificare versioni e vincoli di framework se cambiano rapidamente;
- scegliere stack in base a profilo progetto;
- evitare boilerplate eccessivo;
- costruire dati seed realistici.

## Brownfield

Per repo esistenti:

- leggere struttura progetto prima di proporre cambi;
- identificare pattern esistenti;
- non introdurre librerie senza motivazione;
- non cambiare architettura senza approvazione;
- aggiungere test nel formato già usato.

## Evidence log

Ogni piano deve includere:

```markdown
## Evidence log
- Fonte/elemento osservato:
- Decisione supportata:
- Rischio residuo:
```

## Tooling

Usare ricerca web, file search, grep, test suite, documentazione ufficiale o issue tracker solo quando servono a ridurre un’incertezza specifica.
