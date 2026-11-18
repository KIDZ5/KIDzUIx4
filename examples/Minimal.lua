-- KIDzUIx4 / minimal UI-only demonstration
-- Replace YOUR_USERNAME after uploading this repository to GitHub.
local UI = loadstring(game:HttpGet("https://raw.githubusercontent.com/YOUR_USERNAME/KIDzUIx4/main/dist/KIDzUIx4.lua"))()
local Window = UI:CreateWindow({
    Title = "KIDzUIx4 Demo",
    Subtitle = "Reusable UI library",
    Icon = "settings",
    Theme = "Dark",
    Config = false,
    Size = UDim2.fromOffset(790, 506),
})
local Tab = Window:AddTab({ Title = "Home", Icon = "house" })
local Section = Tab:AddSection({ Title = "Hello", Description = "UI-only example" })
Section:AddButton({ Title = "Say hello", Callback = function()
    print("KIDzUIx4 says hello")
end })
