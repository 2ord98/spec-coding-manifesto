# Agents

Questi file definiscono ruoli agentici limitati. Non sono persone: sono modalità operative per coding agents.

Uso:

1. scegli ruolo;
2. leggi mandate/input/output;
3. esegui solo quel compito;
4. passa al reviewer/gate successivo.

## Role prompts

`agents/*.md` sono role card. `agents/role-prompts/*.md` sono wrapper operativi domain-agnostic per usare quei ruoli con coding agent e CLI target.

I role prompt non duplicano il manifesto, non generano app e non sostituiscono spec, Vertical Blueprint, plan, tasks o scorecard. Servono a restringere il comportamento dell'agente dentro un mandato verificabile.
