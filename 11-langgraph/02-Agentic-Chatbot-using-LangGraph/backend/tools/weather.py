from langchain_core.tools import tool

from backend.logger import get_logger

logger = get_logger(__name__)


@tool
def get_current_weather(location: str) -> str:
    """Return deterministic mock weather for a location."""
    logger.info("get_current_weather mock called | location=%s", location)
    normalized = location.strip().lower()
    presets = {
        "shanghai": (24, "Partly cloudy", 68, 14),
        "上海": (24, "Partly cloudy", 68, 14),
        "beijing": (27, "Sunny", 42, 11),
        "北京": (27, "Sunny", 42, 11),
        "london": (16, "Light rain", 81, 18),
        "tokyo": (25, "Cloudy", 72, 9),
        "dhaka": (30, "Scattered thunderstorms", 78, 10),
    }
    temperature, description, humidity, wind = presets.get(
        normalized,
        (22, "Partly cloudy", 60, 12),
    )
    return (
        f"Mock weather for {location}:\n"
        f"- Temperature: {temperature} C\n"
        f"- Conditions: {description}\n"
        f"- Humidity: {humidity}%\n"
        f"- Wind: {wind} km/h\n"
        "- Data source: local demonstration fixture (not real-time)"
    )
