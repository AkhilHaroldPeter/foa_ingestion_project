import requests

"""
Utilities for fetching raw source content from public FOA pages
"""

def fetch_url(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; FOAIngestionBot/1.0)"
    }

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    return response.text