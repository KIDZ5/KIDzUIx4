# KIDzUIx4 — UI Library (source-preserving edition)

A **standalone Luau user-interface library**, packaged from the exact uploaded `Reaper X New UI(2).txt`. Intended to be imported into other projects. **It does not contain Anime Adventures automation, farming, macros, or game logic.**

> **Preservation rule:** All **442,747 original bytes** are kept intact and in the same order. The distributable adds only `return UI` *after* the original text so that `loadstring(...)()` can return the UI library table. No original methods, themes, UI widgets, internals, file helpers, or icons were removed or renamed. The exact uploaded source is also available as an archive. This is a packaging adaptation; no in-game runtime verification has been performed.

## Get started

Upload the **contents** of this repository folder to GitHub as repository `KIDzUIx4` (choose your account/organization). Then import the published `dist/KIDzUIx4.lua` from a runtime that supports `loadstring` and `game:HttpGet`:

```lua
local UI = loadstring(game:HttpGet(
    "https://raw.githubusercontent.com/YOUR_USERNAME/KIDzUIx4/main/dist/KIDzUIx4.lua"
))()

local window = UI:CreateWindow({
    Title = "My Project",
    Subtitle = "Powered by KIDzUIx4",
    Theme = "Dark",
    Size = UDim2.fromOffset(790, 506),
    Config = false,
})

local tab = window:AddTab({ Title = "Main", Icon = "settings" })
local section = tab:AddSection({ Title = "Controls", Icon = "settings" })

section:AddToggle({
    Title = "Demo toggle",
    Default = false,
    Callback = function(value)
        print("Enabled:", value)
    end,
})
```

**Do not run `dist/KIDzUIx4.lua` as a standalone demo** — it deliberately creates **no window** until your project calls `UI:CreateWindow(...)`. The library's `return UI` value is its API. See [`examples/Showcase.lua`](examples/Showcase.lua) for a working demonstration to run *after* publishing or adapting the loader URL.

For best reproducibility, use a fixed release tag or commit SHA instead of tracking mutable `main`. Only execute remotely loaded code you trust.

## Repository layout

```text
KIDzUIx4/
├── dist/KIDzUIx4.lua                    # Import this (all original code + return UI)
├── src/KIDzUIx4.luau                   # Development copy, byte-identical to dist
├── original/Reaper_X_New_UI__unaltered.txt  # Exact uploaded bytes
├── examples/Showcase.lua               # Demo only; NOT part of the library
├── examples/Minimal.lua                # Minimal import and window
├── docs/API.md                         # Grounded methods and usage
├── docs/TH.md                          # Thai user guide
├── docs/PRESERVATION.md                # Preservation proof + limitations
├── NOTICE.md                           # Origin / licensing / external URLs
├── scripts/build.py                    # Byte-preserving rebuild / verify
└── .github/workflows/verify.yml        # CI integrity check
```

## Development / rebuild

This distribution intentionally **does not split the obfuscated/decompiled original into multiple source modules**: doing so would risk removing behavior or changing semantics. Both `src/` and `dist/` carry the complete source unchanged plus the single export statement.

To verify or recreate distribution using only Python 3:

```bash
python scripts/build.py --check
python scripts/build.py
```

The script checks the archived original file against its recorded SHA-256 and ensures that `src/` and `dist/` differ from the original **only by the export line**.

## Compatibility / limitations

- Original code is **Roblox Luau**. Execution requires a compatible client environment. Its icon/font download paths and filesystem helpers are retained as supplied; no functionality is silently removed.
- The source tries `gethui()` and `CoreGui` before falling back to `PlayerGui`. This may require adapting the UI parent for normal Roblox Studio LocalScripts, where CoreGui access is restricted. Such adaptation is intentionally **not** included in the preserved distribution.
- Static file-integrity checks pass; **in-game widget behavior, platform compatibility, and all original features are not yet validated at runtime**.
- This is **not** the existing KIDzUIx3 implementation and does not inherit its API. The internal original library version identifier and names are preserved.

## Source permissions

A license for the supplied Reaper X/shadcn-derived source has **not** been established. **Check redistribution and licensing rights before making this repository public.** Do not assume that an MIT license from another KIDzUIx repository covers this code. More in [`NOTICE.md`](NOTICE.md).
