"""
install_and_run.py
One-shot installer + launcher.
- Installs requirements
- Installs Playwright browsers
- Runs main.py
"""
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def run(cmd, check=True):
    print(f"[Installer] {cmd}")
    return subprocess.run(cmd, check=check)


def main():
    # Ensure pip is available
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    run([sys.executable, "-m", "playwright", "install"], check=True)
    run([sys.executable, "main.py"], check=False)


if __name__ == "__main__":
    main()
