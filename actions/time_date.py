# actions/time_date.py
# Returns current local time and date

from datetime import datetime


def time_date(parameters=None, response=None, player=None, session_memory=None) -> str:
    now = datetime.now()
    # Example: Wednesday, March 25, 2026 — 9:14 PM
    formatted = now.strftime("%A, %B %d, %Y — %I:%M %p")
    result = f"It is {formatted}."
    if player:
        try:
            player.write_log(f"[time] {result}")
        except Exception:
            pass
    return result
