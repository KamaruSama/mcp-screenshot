# mcp-screenshot

<!-- mcp-name: io.github.KamaruSama/mcp-screenshot -->

**MCP server for taking Linux / Wayland screenshots via `grim` and `slurp`.**

Exposes 2 tools to capture the full screen, a selected region, or an interactive crop — returned inline as base64 or saved to disk.

📖 **[อ่านภาษาไทย →](README.th.md)**

---

## Tools

| Tool | Purpose |
|---|---|
| [`take_screenshot`](docs/en/tools/take_screenshot.md) | Capture screen (full / geometry / interactive select) |
| [`list_outputs`](docs/en/tools/list_outputs.md) | List available Wayland outputs / monitors |

---

## Requirements

- **Wayland** compositor (Sway, Hyprland, etc.)
- `grim` — screenshot tool
- `slurp` — interactive region selector
- `wlr-randr` *(optional)* — for `list_outputs`

Install on Arch Linux:
```bash
sudo pacman -S grim slurp wlr-randr
```

## Install

```bash
claude mcp add screenshot -s user \
  --env WAYLAND_DISPLAY=wayland-1 \
  --env XDG_RUNTIME_DIR=/run/user/1000 \
  -- /path/to/mcp-screenshot/.venv/bin/python /path/to/mcp-screenshot/server.py
```

Build the venv once:
```bash
cd /path/to/mcp-screenshot
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python mcp
```

---

## Support the project ❤

- **Ko-fi:** https://ko-fi.com/kamaru

---

## Contact

- **Portfolio / general:** k.kamarux@gmail.com
- **Commercial / licensing:** contact@likezara.com

---

Copyright © 2026 **likezara™**. All rights reserved.
Developed by **Kamaru** (pen name).
