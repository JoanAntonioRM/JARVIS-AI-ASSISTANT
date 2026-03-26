import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SETTINGS_PATH = BASE_DIR / "config" / "settings.json"

DEFAULTS = {
    "start_with_windows": False,
    "start_minimized": False
}


def load_settings() -> dict:
    if not SETTINGS_PATH.exists():
        return DEFAULTS.copy()
    try:
        data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            merged = DEFAULTS.copy()
            merged.update({k: data.get(k, v) for k, v in DEFAULTS.items()})
            return merged
    except Exception:
        pass
    return DEFAULTS.copy()


def save_settings(settings: dict) -> None:
    SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = DEFAULTS.copy()
    data.update({k: settings.get(k, v) for k, v in DEFAULTS.items()})
    SETTINGS_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
