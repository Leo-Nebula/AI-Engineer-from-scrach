def tavily_search(query: str) -> str:
    """Return deterministic mock hotel, attraction, and travel-tip results."""
    topic = query.strip() or "the requested destination"
    return (
        f"Mock travel search results for: {topic}\n\n"
        "1. **Central City Hotel**\n"
        "   mock://travel/hotel\n"
        "   Mid-range hotel near public transport; sample rate: USD 95/night.\n\n"
        "2. **Old Town Walking Route**\n"
        "   mock://travel/attraction\n"
        "   Half-day route covering representative landmarks and a local market.\n\n"
        "3. **Local Travel Tips**\n"
        "   mock://travel/tips\n"
        "   Reserve popular attractions early and keep a 15% contingency budget."
    )
