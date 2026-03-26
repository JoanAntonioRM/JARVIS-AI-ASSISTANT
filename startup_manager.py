import platform
from pathlib import Path


def set_startup(enabled: bool, app_name: str, exe_path: str) -> bool:
    """Enable/disable Windows startup via registry Run key."""
    if platform.system() != "Windows":
        return False
    try:
        import winreg
        key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE) as key:
            if enabled:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, f'"{exe_path}"')
            else:
                try:
                    winreg.DeleteValue(key, app_name)
                except FileNotFoundError:
                    pass
        return True
    except Exception:
        return False
