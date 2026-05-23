# Mobile App Blueprint

Usa questo blueprint per app iOS, Android, Expo, Flutter, SwiftUI, Jetpack Compose o mobile-first.

## Role contract

Agisci come mobile product architect. Tratta il mobile come esperienza nativa, non come sito ridotto.

## Required decisions

- piattaforma target;
- navigazione;
- schermate;
- offline/cache;
- permessi;
- notifiche;
- storage locale;
- sincronizzazione;
- accessibilità;
- store readiness;
- analytics/privacy.

## Stack guidance

- Expo/React Native: MVP cross-platform rapido, ecosystem ampio;
- Flutter: UI consistente e performance cross-platform;
- SwiftUI/Kotlin/Compose: esperienza nativa profonda;
- backend separato se dati, auth o sync sono non banali.

## Output contract

```text
Screens:
Navigation map:
Data model:
API contract:
State management:
Offline strategy:
Permission strategy:
Test plan:
Build/run commands:
```

## Anti-genericity

Ogni app deve includere gesture, stati vuoti, microcopy e flussi coerenti con il dominio. Non basta generare una tab bar standard.
