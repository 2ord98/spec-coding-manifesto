# Cursor Plugin Guidance

Use `sdc handoff --target cursor` for editor-scoped changes.

- Prefer `.cursor/rules` Project Rules.
- Treat `.cursorrules` as legacy compatibility only.
- Preserve existing code unless the artifacts require changes.
- Return changed files and validation evidence.
