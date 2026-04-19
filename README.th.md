# mcp-screenshot

**MCP server สำหรับจับภาพหน้าจอ Linux / Wayland ผ่าน `grim` และ `slurp`**

ให้ 2 เครื่องมือสำหรับจับภาพเต็มจอ เลือก region หรือเลือกแบบ interactive — คืนค่าเป็น base64 หรือบันทึกลงไฟล์

📖 **[Read in English →](README.md)**

---

## เครื่องมือ

| เครื่องมือ | หน้าที่ |
|---|---|
| [`take_screenshot`](docs/th/tools/take_screenshot.md) | จับภาพหน้าจอ (เต็มจอ / ระบุพิกัด / เลือกแบบ interactive) |
| [`list_outputs`](docs/th/tools/list_outputs.md) | ลิสต์จอ (Wayland outputs) ที่มี |

---

## ระบบที่ต้องมี

- **Wayland** compositor (Sway, Hyprland ฯลฯ)
- `grim` — เครื่องมือจับภาพ
- `slurp` — ตัวเลือก region แบบ interactive
- `wlr-randr` *(ไม่บังคับ)* — สำหรับ `list_outputs`

ติดตั้งบน Arch Linux:
```bash
sudo pacman -S grim slurp wlr-randr
```

## ติดตั้ง

```bash
claude mcp add screenshot -s user \
  --env WAYLAND_DISPLAY=wayland-1 \
  --env XDG_RUNTIME_DIR=/run/user/1000 \
  -- /path/to/mcp-screenshot/.venv/bin/python /path/to/mcp-screenshot/server.py
```

สร้าง venv ครั้งเดียว:
```bash
cd /path/to/mcp-screenshot
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp
```

---

## สนับสนุนผู้พัฒนา ❤

- **Ko-fi:** https://ko-fi.com/kamaru

---

## ติดต่อ

- **Portfolio / ทั่วไป:** k.kamarux@gmail.com
- **เชิงพาณิชย์ / ลิขสิทธิ์:** contact@likezara.com

---

Copyright © 2026 **likezara™**. สงวนลิขสิทธิ์
พัฒนาโดย **Kamaru** (นามปากกา)
