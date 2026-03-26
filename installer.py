"""
installer.py -> build into jarvisinstall.exe
Downloads latest release assets and installs to AppData.
"""
import json
import os
import shutil
import subprocess
import urllib.request
import zipfile
from pathlib import Path

APP_DIR = Path(os.getenv("LOCALAPPDATA", Path.home())) / "JarvisAI"
CONFIG_DIR = APP_DIR / "config"

REPO = "JoanAntonioRM/JARVIS-AI-ASSISTANT"
ASSET_NAME = "jarvis.exe"


def _download(url: str, dest: Path):
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as resp:
        dest.write_bytes(resp.read())


def main():
    APP_DIR.mkdir(parents=True, exist_ok=True)

    # Get latest release info
    api = f"https://api.github.com/repos/{REPO}/releases/latest"
    data = json.loads(urllib.request.urlopen(api).read().decode("utf-8"))

    asset_url = None
    for a in data.get("assets", []):
        if a.get("name") == ASSET_NAME:
            asset_url = a.get("browser_download_url")
            break

    if not asset_url:
        raise SystemExit("No jarvis.exe asset found in latest release")

    exe_path = APP_DIR / "jarvis.exe"
    _download(asset_url, exe_path)

    # Write default config if missing
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    cfg = CONFIG_DIR / "settings.json"
    if not cfg.exists():
        cfg.write_text(json.dumps({"start_with_windows": False, "start_minimized": False}, indent=2), encoding="utf-8")

    # Launch JARVIS
    subprocess.Popen([str(exe_path)])


if __name__ == "__main__":
    main()
