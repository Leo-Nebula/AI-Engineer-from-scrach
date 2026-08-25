from langchain.tools import tool


@tool
def web_search(query: str) -> str:
    """Return deterministic mock search results for an Agent workflow demo."""
    topic = query.strip() or "the requested topic"
    return "\n----\n".join(
        [
            (
                f"Title: Mock overview of {topic}\n"
                "URL: mock://research/overview\n"
                f"Snippet: A concise background summary and key terminology for {topic}."
            ),
            (
                f"Title: Mock recent developments in {topic}\n"
                "URL: mock://research/developments\n"
                f"Snippet: Representative developments, trade-offs, and open questions about {topic}."
            ),
            (
                f"Title: Mock practical guide to {topic}\n"
                "URL: mock://research/practical-guide\n"
                f"Snippet: Common implementation patterns, risks, and evaluation criteria for {topic}."
            ),
        ]
    )


@tool
def scrape_url(url: str) -> str:
    """Return mock article content without making a network request."""
    return (
        f"Mock article content for {url}. "
        "This source explains the topic background, presents representative evidence, "
        "compares benefits and limitations, and recommends validating claims against "
        "authoritative sources before production use."
    )
