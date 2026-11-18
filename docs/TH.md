# วิธีใช้ KIDzUIx4 (ภาษาไทย)

นี่คือ **UI Library เปล่า** ไม่ได้ใส่ระบบฟาร์ม หรือสคริปต์สำหรับเกมใด ๆ และยังไม่มีหน้าต่างปรากฏจนกว่าโปรเจกต์จะสั่ง `CreateWindow`.

## วิธีอัป GitHub

1. สร้าง Repository ชื่อ **KIDzUIx4** ใน GitHub (แนะนำ **Private** ก่อนจนกว่าจะตรวจสิทธิ์เผยแพร่ซอร์สต้นฉบับ)
2. แตกไฟล์ ZIP และอัปโหลด **ไฟล์ข้างในโฟลเดอร์ `KIDzUIx4/`** ไปที่ราก Repository
3. ตรวจว่ามี `dist/KIDzUIx4.lua` อยู่บน Branch `main`
4. เปลี่ยน `YOUR_USERNAME` ในโค้ดตัวอย่างเป็นชื่อบัญชีจริง
5. เรียก `loadstring(game:HttpGet(...))()` เพื่อรับตัวแปร UI แล้วสร้างหน้าต่าง

**หมายเหตุ:** ลิงก์ raw จะไม่เปิดใช้งานจนกว่าคุณจะอัปโหลดไฟล์สำเร็จ

## ตัวอย่างสั้น

```lua
local UI = loadstring(game:HttpGet(
    "https://raw.githubusercontent.com/YOUR_USERNAME/KIDzUIx4/main/dist/KIDzUIx4.lua"
))()

local Window = UI:CreateWindow({
    Title = "KIDz Test",
    Subtitle = "UI only",
    Size = UDim2.fromOffset(790, 506),
    Theme = "Dark",
    Config = false,
})

local Tab = Window:AddTab({Title = "General", Icon = "settings"})
local Section = Tab:AddSection({Title = "Example"})
Section:AddButton({Title = "Click me", Callback = function()
    print("Button clicked")
end})
```

ถ้าสั่งรันตัว Library เพียงไฟล์เดียวแล้วไม่เห็น UI ถือว่า **ปกติ** เพราะไฟล์นี้เป็น Library ไม่ใช่ Demo

## คำศัพท์

- `UI` = Library ที่ถูกโหลดเข้ามา
- `Window` = หน้าต่างหลัก
- `Tab` = เมนูด้านซ้าย
- `Section` = กลุ่มปุ่มในการตั้งค่า
- `Callback` = ฟังก์ชันที่ทำงานตอนผู้ใช้กด/เปลี่ยนค่า
- `UI:Unload()` = ทำความสะอาด/ปิดหน้าต่างที่ Library สร้างไว้

## เรื่องการคงต้นฉบับ

เก็บต้นฉบับครบตามจำนวนไบต์เดิม ไม่มีการลบแม้แต่บรรทัดเดียว โค้ด Library เพิ่มเพียง `return UI` หลังบรรทัดสุดท้ายเพื่อให้โหลดจากโปรเจกต์อื่นได้ และมีไฟล์ต้นฉบับไม่แก้ไขอยู่ใน `original/`.

**ยังรับรองไม่ได้ว่า runtime 100%** เพราะไม่ได้ทดสอบจริงใน Roblox/Potassium ทุกองค์ประกอบ และต้องตรวจสิทธิ์ก่อนเผยแพร่โค้ดที่ได้จากบุคคลอื่น
