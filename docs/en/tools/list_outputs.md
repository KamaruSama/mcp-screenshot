# `list_outputs`

List the available Wayland outputs (monitors) detected on the system.

## Signature

```python
list_outputs() -> str
```

## Parameters

None.

## Returns

A plain-text listing of monitors, formatted by whichever tool succeeds first:

1. `wlr-randr` — full mode list per output
2. `grim -l` — compact fallback
3. Error string if neither is available

## Example

```
HDMI-A-1 "Samsung U28E590 ..."
  Enabled: yes
  Position: 0,0
  Transform: normal
  Scale: 1.000000
  ...
```

## Notes

- Install `wlr-randr` for richer output: `sudo pacman -S wlr-randr`.
- Works under Sway, Hyprland, and other wlroots-based compositors.

---

Part of [mcp-screenshot](../../../README.md) · © 2026 likezara™ · Kamaru
