# Byte-level preservation report

Reference upload: `Reaper X New UI(2).txt`

- Original size: **442,747 bytes**
- Original SHA-256: `b4cfc7170e8a0e119f7d18547bb906da1792b7f6ec17fc8e984aec07cf57058c`
- Original line endings: CRLF
- Original code structure: starts `local UI = (function()`; ends `end)()`
- Export patch: `\r\nreturn UI\r\n` appended to end, **no replacements, no deletions**
- Exported library size: **442,760 bytes**
- Exported SHA-256: `93a70d4dde95dfc549a56c3a484da751fa596b3ff201bee5adc0d37873f9f94f`
- Archive original: `original/Reaper_X_New_UI__unaltered.txt`
- Distributable: `dist/KIDzUIx4.lua`

The archive is an exact byte copy of the original upload; the `src` and `dist` copies contain that exact source as a byte-prefix plus the 13-byte export patch. This is checkable with `python scripts/build.py --check`.

**What this proves:** no byte in the uploaded source was removed or altered, and the built library returns its existing local `UI` table to callers.

**What this does NOT prove:** in-game compatibility, successful dynamic font/icon downloads, all widgets behaving correctly, compliance with third-party licensing, or security of external network resources.


## GitHub Actions line-ending compatibility

Git and GitHub may normalize CRLF to LF when the repository is uploaded or checked out.
The fixed `scripts/build.py` checks a **canonical LF SHA-256** while preserving
the original UI code in full. Only CRLF/LF differences are tolerated.
A changed, missing, or replaced code character still makes the check fail.

The exact byte-level report above applies to the initial downloadable ZIP;
a GitHub checkout that normalized newlines is text-identical but not byte-identical.
