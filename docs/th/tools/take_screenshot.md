# `take_screenshot`

จับภาพหน้าจอ — เต็มจอ ระบุพิกัด หรือเลือก region แบบ interactive ผ่าน `slurp`

## Signature

```python
take_screenshot(region: str | None = None, output_path: str | None = None) -> str
```

## พารามิเตอร์

| ชื่อ | ประเภท | ค่าเริ่มต้น | คำอธิบาย |
|---|---|---|---|
| `region` | `str \| None` | `None` | `None` = เต็มจอ; `"select"` = เลือก interactive ด้วย `slurp`; ระบุพิกัด เช่น `"100,200 400x300"` (x,y widthxheight) |
| `output_path` | `str \| None` | `None` | ถ้าใส่ จะบันทึกที่ path นั้น; ถ้าไม่ใส่ คืนค่าเป็น base64 data URI |

## คืนค่า

- ถ้าใส่ `output_path` → `"Screenshot saved to {path}"`
- ถ้าไม่ใส่ → `"data:image/png;base64,..."`
- ถ้า error → `"Screenshot failed: {stderr}"` หรือ `"Selection cancelled."`

## ตัวอย่าง

**เต็มจอ บันทึกเป็นไฟล์**
```json
{ "output_path": "/tmp/shot.png" }
```

**เลือก region แบบ interactive**
```json
{ "region": "select" }
```

**ระบุพิกัด**
```json
{ "region": "0,0 1920x1080" }
```

## หมายเหตุ

- ต้องมี `grim` (และ `slurp` ถ้าใช้ `"select"`)
- ต้องรันใน Wayland session — env var `WAYLAND_DISPLAY` กับ `XDG_RUNTIME_DIR` ต้องส่งถึง server ด้วย

---

Part of [mcp-screenshot](../../../README.md) · © 2026 likezara™ · Kamaru
