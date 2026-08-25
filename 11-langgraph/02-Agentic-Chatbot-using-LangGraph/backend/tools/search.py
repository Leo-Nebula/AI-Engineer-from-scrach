from langchain_core.tools import tool


@tool
def search_tool(query: str) -> str:
    """Return deterministic mock search results for chatbot demonstrations."""
    topic = query.strip() or "the requested topic"
    return (
        f"Mock search results for: {topic}\n"
        f"1. Overview: Background and key concepts for {topic}. (mock://search/overview)\n"
        f"2. Update: Representative recent developments in {topic}. (mock://search/update)\n"
        "3. Guide: Practical considerations and common risks. (mock://search/guide)"
    )
