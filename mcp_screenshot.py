"""
================================================================================
 Screenshot MCP Server
================================================================================

 A Model Context Protocol server for taking Linux / Wayland screenshots
 via `grim` (screenshot) and `slurp` (interactive region selection).

 Transport : stdio
 Tools     : take_screenshot, list_outputs
 Deps      : grim, slurp (system binaries); wlr-randr (optional)

--------------------------------------------------------------------------------
 Copyright © 2026 likezara™. All rights reserved.
 Developed by Kamaru (pen name).
--------------------------------------------------------------------------------
"""

from __future__ import annotations

import base64
import subprocess
import tempfile
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("screenshot")


@mcp.tool()
def take_screenshot(
    region: str | None = None, output_path: str | None = None
) -> str:
    """Take a screenshot of the Linux desktop.

    Args:
        region: Optional region to capture. Use "select" to interactively
                pick a region with slurp, or pass geometry like "100,200 400x300".
                If omitted, captures the full screen.
        output_path: Optional path to save the screenshot. If omitted, saves to
                     a temp file and returns the image as base64.
    """
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        path = output_path or tmp.name

    cmd = ["grim"]

    if region == "select":
        try:
            geometry = subprocess.check_output(["slurp"], text=True).strip()
            cmd += ["-g", geometry]
        except subprocess.CalledProcessError:
            return "Selection cancelled."
    elif region:
        cmd += ["-g", region]

    cmd.append(path)

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return f"Screenshot failed: {e.stderr}"

    if output_path:
        return f"Screenshot saved to {output_path}"

    data = Path(path).read_bytes()
    encoded = base64.standard_b64encode(data).decode()
    Path(path).unlink(missing_ok=True)
    return f"data:image/png;base64,{encoded}"


@mcp.tool()
def list_outputs() -> str:
    """List available Wayland outputs (monitors)."""
    try:
        result = subprocess.run(
            ["wlr-randr"], capture_output=True, text=True, check=True
        )
        return result.stdout
    except FileNotFoundError:
        try:
            result = subprocess.run(
                ["grim", "-l"], capture_output=True, text=True
            )
            return result.stdout or "Could not list outputs."
        except Exception:
            return "wlr-randr not found and grim -l failed."


def main():
    """Entry point for  console script."""
    mcp.run()


if __name__ == "__main__":
    main()
