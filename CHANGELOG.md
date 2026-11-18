# Changelog

## 0.1.0 — source-preserving distribution

- Archive the original user-provided UI source without changing any byte.
- Export its existing UI table by appending a single `return UI` statement (without rewriting source logic).
- Add standalone import examples, bilingual docs, byte-integrity checks, and GitHub CI.
- No UI functionality was removed, rewritten, or renamed; no game logic added.
- Runtime behavior still requires on-device testing.
