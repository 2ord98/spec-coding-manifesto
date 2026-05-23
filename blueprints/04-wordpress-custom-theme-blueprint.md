# WordPress Custom Theme Blueprint

Usa questo blueprint quando la richiesta riguarda un tema WordPress custom, senza page builder pesanti, con PHP nativo e frontend moderno.

## Role contract

Agisci come WordPress custom theme architect e senior full-stack developer. Genera un tema modulare, sicuro, scalabile e pronto per Git/CI-CD.

## Product intent

Trasforma la richiesta in un sito specifico per dominio. Per hospitality, ristorazione, cocktail bar, eventi o retail premium, definisci contenuti reali minimi senza copiare branding, testi proprietari o asset di realtà esistenti.

## Stack contract

- PHP 8.x
- WordPress custom theme
- CPT e tassonomie native
- Custom fields sicuri
- Vanilla JS dove basta
- GSAP/ScrollTrigger solo se motivati
- Three.js/WebGL solo con fallback e reduced-motion
- CSS modulare senza page builder pesanti

## File tree minimo

```text
/themes/<theme-slug>/
  style.css
  functions.php
  front-page.php
  header.php
  footer.php
  page-contatti.php
  single-<cpt>.php
  archive-<cpt>.php
  template-parts/
    hero.php
    cards-experiences.php
    menu-filter.php
    location-grid.php
    booking-form.php
  assets/
    css/main.css
    js/motion-engine.js
    js/ajax-menu.js
    js/booking-form.js
    img/.gitkeep
  inc/
    cpt.php
    taxonomies.php
    ajax.php
    security.php
    maintenance.php
    helpers.php
```

## Content architecture

Definisci CPT, tassonomie, custom fields, relazioni, contenuti seed realistici, campi obbligatori e regole di ordinamento.

## WordPress security contract

Obbligatorio:

- nonce nei form;
- `check_ajax_referer` o `check_admin_referer`;
- sanitizzazione input: `sanitize_text_field`, `sanitize_email`, `wp_kses_post`, funzioni specifiche;
- escaping output: `esc_html`, `esc_attr`, `esc_url`, `wp_kses_post` dove appropriato;
- `wp_send_json_success` / `wp_send_json_error`;
- niente API key hardcoded;
- segreti via env/config sicura;
- rimozione versione WordPress dagli header;
- restrizione endpoint utenti pubblici;
- permessi e capabilities per azioni admin;
- HTTP 503 per maintenance mode.

## Motion/performance contract

Per canvas, WebGL o animazioni avanzate:

```text
Target: motion fluido su desktop moderno.
Fallback mobile: reduced motion, canvas opzionale, no blocco rendering.
Budget: script differiti, lazy-loading media, nessuna mappa bloccante.
Misura: Lighthouse, profiler browser, smoke test mobile.
```

Non dichiarare “60 FPS garantiti” senza fallback e metodo di misura.

## AJAX/REST contract

Per filtri menu, prenotazioni o form: endpoint dichiarato, nonce, validazione server-side, risposta JSON coerente, error states UI, abuso prevedibile, nessun dato sensibile nel frontend.

## Output richiesto

Generare albero cartelle, `functions.php` completo o modulare con `inc/*`, template principale, JS motion/AJAX richiesto, CSS base, istruzioni installazione tema e scorecard finale.

## Anti-pattern

- page builder come scorciatoia non richiesta;
- plugin pesanti per logica core;
- chiavi API nei template;
- animazioni senza fallback;
- CPT senza campi e tassonomie coerenti;
- HTML non semantico;
- codice “commentato riga per riga” senza necessità.
