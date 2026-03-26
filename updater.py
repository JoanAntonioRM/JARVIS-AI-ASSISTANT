import json
import urllib.request
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
APP_CONFIG = BASE_DIR / "config" / "app.json"


def _load_app_config():
    if APP_CONFIG.exists():
        return json.loads(APP_CONFIG.read_text(encoding="utf-8"))
    return {"version": "0.0.0", "repo": ""}


def _version_tuple(v: str):
    try:
        return tuple(int(x) for x in v.strip().lstrip('v').split('.'))
    except Exception:
        return (0, 0, 0)


def check_update_available():
    cfg = _load_app_config()
    repo = cfg.get("repo", "")
    current = cfg.get("version", "0.0.0")
    if not repo:
        return None

    url = f"https://api.github.com/repos/{repo}/releases/latest"
    req = urllib.request.Request(url, headers={"User-Agent": "jarvis-updater"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    latest = data.get("tag_name") or data.get("name") or "0.0.0"
    if _version_tuple(latest) > _version_tuple(current):
        return {
            "latest": latest,
            "assets": data.get("assets", []),
            "html_url": data.get("html_url"),
            "repo": repo
        }
    return None


def download_installer(info, installer_name: str = "jarvisinstall.exe"):
    assets = info.get("assets", []) or []
    url = None
    for a in assets:
        if a.get("name") == installer_name:
            url = a.get("browser_download_url")
            break
    if not url:
        return None

    dest = Path(os.getenv("TEMP", "/tmp")) / installer_name
    with urllib.request.urlopen(url) as resp:
        dest.write_bytes(resp.read())
    return dest
