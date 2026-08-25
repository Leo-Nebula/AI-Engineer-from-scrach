"""LangChain tool wrappers used by ReAct agents."""

from langchain_core.tools import tool

from backend.tools.flight_tool import search_flights as _search_flights
from backend.tools.tavily_tool import tavily_search as _tavily_search


@tool
def search_flights(query: str) -> str:
    """Return mock flight options from a natural-language travel query.

    Prefer including origin/destination cities or airport codes when possible.
    The returned data is deterministic and intended only for demonstrations.
    """
    return _search_flights(query)


@tool
def search_web(query: str) -> str:
    """Return mock hotels, attractions, or travel tips."""
    return _tavily_search(query)
