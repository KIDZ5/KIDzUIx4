-- KIDzUIx4 UI-only showcase / no automation or game-specific logic
-- Replace YOUR_USERNAME after your GitHub repository exists.
local UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/YOUR_USERNAME/KIDzUIx4/main/dist/KIDzUIx4.lua"))()

local Window = UI:CreateWindow({
    Title = "KIDzUIx4 Showcase",
    Subtitle = "UI Library Demo",
    Icon = "settings",
    Size = UDim2.fromOffset(790, 506),
    Theme = "Dark",
    Accent = "Default",
    Config = false,
})

local General = Window:AddGroup("General")
local Home = General:AddTab({Title = "Dashboard", Icon = "layout-dashboard"})
local Widgets = General:AddTab({Title = "Components", Icon = "sliders-horizontal"})
local SettingsGroup = Window:AddGroup("Settings")
local Appearance = SettingsGroup:AddTab({Title = "Appearance", Icon = "palette"})

local Intro = Home:AddSection({Title = "Welcome", Description = "A standalone library for reusable Roblox UIs"})
Intro:AddParagraph({Title = "Library only", Content = "No Auto Farm, no Macros, no game systems."})
Intro:AddButton({Title = "Show notification", ButtonText = "Notify", Icon = "bell", Callback = function()
    UI:Toast({Title = "KIDzUIx4", Description = "Your button works!", Duration = 4, Type = "Success"})
end})

local Demo = Widgets:AddSection({Title = "Widgets", Icon = "settings"})
Demo:AddToggle({Title = "Example toggle", Description = "Prints state", Default = false,
    Callback = function(value) print("Toggle:", value) end})
Demo:AddSlider({Title = "Example slider", Min = 1, Max = 10, Step = 1, Default = 4,
    Callback = function(value) print("Slider:", value) end})
Demo:AddDropdown({Title = "Example dropdown", Options = {"Option A", "Option B", "Option C"}, Default = "Option A",
    Callback = function(value) print("Dropdown:", value) end})
Demo:AddInput({Title = "Example input", Placeholder = "Type here...", Default = "",
    Callback = function(value) print("Input:", value) end})

local Look = Appearance:AddSection({Title = "Theme"})
Look:AddButton({Title = "Dark mode", Callback = function() UI:SetTheme("Dark") end})
Look:AddButton({Title = "Light mode", Callback = function() UI:SetTheme("Light") end})
Look:AddButton({Title = "White mode", Callback = function() UI:SetTheme("White") end})
