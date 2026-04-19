# `list_outputs`

ลิสต์จอ (Wayland outputs) ทั้งหมดที่ระบบรู้จัก

## Signature

```python
list_outputs() -> str
```

## พารามิเตอร์

ไม่มี

## คืนค่า

text ธรรมดาแสดงรายการจอ — เลือกเครื่องมือตามลำดับ:

1. `wlr-randr` — รายละเอียดเต็ม
2. `grim -l` — fallback แบบย่อ
3. error string ถ้าทั้งคู่ไม่มี

## ตัวอย่าง

```
HDMI-A-1 "Samsung U28E590 ..."
  Enabled: yes
  Position: 0,0
  ...
```

## หมายเหตุ

- ติดตั้ง `wlr-randr` ได้ผลลัพธ์ละเอียดกว่า: `sudo pacman -S wlr-randr`
- ใช้ได้กับ Sway, Hyprland และ compositor อื่นๆ ที่ใช้ wlroots

---

Part of [mcp-screenshot](../../../README.md) · © 2026 likezara™ · Kamaru
