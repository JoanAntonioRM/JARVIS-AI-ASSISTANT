import threading
import platform
from pathlib import Path


def start_tray(ui, settings, on_toggle_startup=None):
    if platform.system() != "Windows":
        return None
    try:
        import pystray
        from PIL import Image
    except Exception:
        return None

    base = Path(__file__).resolve().parent
    icon_path = base / "icon_jarvis.png"
    if not icon_path.exists():
        icon_path = base / "face.png"
    try:
        image = Image.open(icon_path) if icon_path.exists() else Image.new("RGB", (64, 64), "black")
    except Exception:
        image = Image.new("RGB", (64, 64), "black")

    def _open():
        try:
            ui.show()
        except Exception:
            pass

    def _exit():
        try:
            ui.root.destroy()
        except Exception:
            pass
        try:
            icon.stop()
        except Exception:
            pass

    def _toggle_startup(_item=None):
        settings["start_with_windows"] = not settings.get("start_with_windows", False)
        if on_toggle_startup:
            on_toggle_startup(settings["start_with_windows"])

    def _checked(_item):
        return bool(settings.get("start_with_windows", False))

    menu = pystray.Menu(
        pystray.MenuItem("Open", lambda: _open()),
        pystray.MenuItem("Start with Windows", _toggle_startup, checked=_checked),
        pystray.MenuItem("Exit", lambda: _exit())
    )

    icon = pystray.Icon("JARVIS", image, "JARVIS", menu)

    def _run():
        icon.run()

    t = threading.Thread(target=_run, daemon=True)
    t.start()
    return icon
