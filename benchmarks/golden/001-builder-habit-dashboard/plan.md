# Plan: local-first habit dashboard

## Slice 1: domain model

Define habit and completion data structures with local-first storage.
Record that health routines are sensitive personal data, not medical advice.

## Slice 2: core workflow

Implement create, complete, edit, and delete a habit.
Keep the account system out of scope unless explicit sync requirements appear.

## Slice 3: progress view

Implement today and weekly progress views.
Avoid paid analytics and use only local completions to calculate progress.

## Slice 4: states and recovery

Implement empty state, error state, and undo/reset behavior.

## Slice 5: validation

Validate accessibility, privacy, testability, anti-genericity, and scorecard readiness.
Verify acceptance criteria for create, complete, edit, delete, weekly progress, privacy, and stack rationale.

## Stack rationale

Use local-first implementation for the `dashboard-admin-bi` profile and document why account, database, analytics, and heavier backend defaults were rejected.
