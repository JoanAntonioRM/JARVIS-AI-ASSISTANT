# actions/take_note.py
# Append important notes to a text file on Desktop

from datetime import datetime
from pathlib import Path


def take_note(parameters=None, response=None, player=None, session_memory=None) -> str:
    params = parameters or {}
    text = (params.get("text") or params.get("note") or "").strip()
    if not text:
        return "Please provide the note text, sir."

    desktop = Path.home() / "Desktop"
    desktop.mkdir(parents=True, exist_ok=True)
    notes_file = desktop / "Jarvis_Notes.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"[{timestamp}] {text}\n"
    try:
        with open(notes_file, "a", encoding="utf-8") as f:
            f.write(entry)
        result = f"Note saved to {notes_file}."
    except Exception as e:
        result = f"Failed to save note: {e}"

    if player:
        try:
            player.write_log(f"[note] {text[:50]}")
        except Exception:
            pass

    return result
