# actions/weather_report.py

import webbrowser
from urllib.parse import quote_plus


def weather_action(
    parameters: dict,
    player=None,
    session_memory=None
):
    """
    Weather report action.
    Opens a Google weather search and gives a short spoken confirmation.
    """

    city = parameters.get("city")
    time = parameters.get("time")

    def _load_default_city() -> str:
        try:
            from pathlib import Path
            import json
            base_dir = Path(__file__).resolve().parent.parent
            cfg_path = base_dir / "config" / "api_keys.json"
            if cfg_path.exists():
                data = json.loads(cfg_path.read_text(encoding="utf-8"))
                if isinstance(data, dict) and data.get("default_city"):
                    return str(data.get("default_city")).strip()
        except Exception:
            pass
        return "Laval"

    if not city or not isinstance(city, str):
        city = _load_default_city()
    else:
        city = city.strip()
        if city.lower() in ("my city", "here", "local", "current location"):
            city = _load_default_city()

    if not time or not isinstance(time, str):
        time = "today"
    else:
        time = time.strip()

    search_query = f"weather in {city} {time}"
    encoded_query = quote_plus(search_query)
    url = f"https://www.google.com/search?q={encoded_query}"

    try:
        webbrowser.open(url)
    except Exception:
        msg = f"Sir, I couldn't open the browser for the weather report."
        _speak_and_log(msg, player)
        return msg

    msg = f"Showing the weather for {city}, {time}, sir."
    _speak_and_log(msg, player)

    if session_memory:
        try:
            session_memory.set_last_search(
                query=search_query,
                response=msg
            )
        except Exception:
            pass  

    return msg


def _speak_and_log(message: str, player=None):
    if player:
        try:
            player.write_log(f"JARVIS: {message}")
        except Exception:
            pass