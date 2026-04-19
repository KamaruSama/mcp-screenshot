# `take_screenshot`

Capture the desktop — full screen, a specific geometry, or an interactive region selection via `slurp`.

## Signature

```python
take_screenshot(region: str | None = None, output_path: str | None = None) -> str
```

## Parameters

| Name | Type | Default | Description |
|---|---|---|---|
| `region` | `str \| None` | `None` | `None` for full screen; `"select"` to pick interactively with `slurp`; or geometry string like `"100,200 400x300"` (x,y widthxheight) |
| `output_path` | `str \| None` | `None` | If set, save to this file and return a message. If omitted, return the PNG inline as a base64 data URI |

## Returns

- If `output_path` set → `"Screenshot saved to {path}"`
- If `output_path` omitted → `"data:image/png;base64,..."` (data URI)
- On error → `"Screenshot failed: {stderr}"` or `"Selection cancelled."`

## Examples

**Full screen to file**
```json
{ "output_path": "/tmp/shot.png" }
```

**Interactive crop, inline**
```json
{ "region": "select" }
```

**Fixed geometry**
```json
{ "region": "0,0 1920x1080" }
```

## Notes

- Requires `grim` and (for `"select"`) `slurp`.
- Must run in a Wayland session; `WAYLAND_DISPLAY` and `XDG_RUNTIME_DIR` env vars need to reach the server.

---

Part of [mcp-screenshot](../../../README.md) · © 2026 likezara™ · Kamaru
