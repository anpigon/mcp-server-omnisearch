from fastmcp import FastMCP
from urllib.parse import quote
import requests
import os

mcp = FastMCP("Omnisearch")

OBSIDIAN_VAULT_PATH = "/Users/anpigon/ObsidianVault/2ndbrain"


@mcp.tool()
def obsidian_notes_search(query: str):
    """Search Obsidian notes and return absolute paths to the matching notes.
    The returned paths can be used with the read_file tool to view the note contents."""
    try:
        search_url: str = "http://localhost:51361/search?q={query}"
        response = requests.get(search_url.format(query=quote(query)))
        response.raise_for_status()  # Raise an exception for bad status codes
        json_response = response.json()
        return [
            os.path.join(OBSIDIAN_VAULT_PATH, item["path"].lstrip("/"))
            for item in json_response
        ]
    except Exception:
        return []
