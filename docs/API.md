# KIDzUIx4 API (mapped from the supplied original)

The library is an original shadcn-style API preserved **without renaming methods**. The `KIDzUIx4` name is the distribution name, not a new API or a rewrite.

## Import

```lua
local UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/YOUR_USERNAME/KIDzUIx4/main/dist/KIDzUIx4.lua"))()
```

## Library (`UI`) methods confirmed in source

- `UI:CreateWindow(options)` -> window
- `UI:SetTheme(theme)`
- `UI:SetAccent(accent)`
- `UI:SetColor(token, color)` and `UI:ResetColor(token)`
- `UI:ResetTheme()`
- `UI:ExportTheme()` and `UI:ImportTheme(json)`
- `UI:AddTheme(name, colors, base)`
- `UI:GetColor(token)`
- `UI:Icon(name)` and `UI:LoadIcons(source)`
- `UI:Toast(options)`, `UI:Notify(options)`, `UI:Promise(callback, options)`
- `UI:Unload()`

## Window

```lua
local window = UI:CreateWindow({
    Title = "Example",
    Subtitle = "UI only",
    Icon = "settings",
    Size = UDim2.fromOffset(790, 506),
    Theme = "Dark", -- also supports Light and White
    Accent = "Default", -- original palette options retained
    Config = false, -- disable on-disk config for a simple demonstration
})
local tab = window:AddTab({Title = "General", Icon = "settings"})
-- OR group by sidebar category:
local group = window:AddGroup("General")
local tab2 = group:AddTab({Title = "Settings", Icon = "settings"})
```

Observed public methods include `window:AddGroup()`, `window:AddTab()`, `window:SelectTab()`, `window:GetFlag()`, `window:SetFlag()`, `window:SetToggleKey()`, `window:SetVisible()`, `window:SetSidebarCollapsed()`, `window:SetGlass()`, `window:Dialog()`, `window:Confirm()`, `window:Destroy()`.

## Tab + Section

```lua
local section = tab:AddSection({Title = "Main", Description = "Example UI components"})
section:AddLabel("Some text")
section:AddParagraph("About", "Description")
section:AddButton({Title = "Press", Callback = function() print("pressed") end})
section:AddToggle({Title = "Enabled", Default = false, Callback = function(value) print(value) end})
section:AddSlider({Title = "Speed", Min = 0, Max = 100, Step = 1, Default = 40, Callback = function(value) print(value) end})
section:AddDropdown({Title = "Mode", Options = {"Normal", "Fast"}, Default = "Normal", Callback = function(value) print(value) end})
```

Source also implements `section:AddBadge()`, `section:AddInput()`, `section:AddColorPicker()`, `section:AddTable()`, `section:AddKeybind()`, and `section:AddRow()` with internal support for row-level toggles/dropdowns/etc. Feature details are unmodified from the supplied original and are not exhaustively specified here; consult the source for exact option shapes.

## Important notes

- The library has no game-specific features. Example actions print or show UI notifications only.
- It is **not API-compatible** with the new independent KIDzUIx4 demo design or with KIDzUIx3 by default.
- The library source is complete as delivered, but **runtime compatibility has not been certified**.
