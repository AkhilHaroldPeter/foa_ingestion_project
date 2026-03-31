import requests
from bs4 import BeautifulSoup

from src.utils import clean_text

"""
Parsing helpers for preparing raw source content for extraction.

This module contains parsing-related utilities used to clean, organize, and
prepare source content before structured extraction is performed.

Depending on the source, this may include:
- HTML parsing
- text normalization
- section isolation
- field preparation for downstream processing

This layer helps keep raw source handling separate from field extraction
logic.
"""

def fetch_url_content(url: str) -> str:
    """
    Fetch raw HTML content from a URL.
    """
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.text


def parse_html_content(html: str) -> dict:
    """
    Parse HTML content into a simplified structured dictionary.
    Returns title, main heading, and cleaned body text.
    """
    soup = BeautifulSoup(html, "lxml")

    page_title = clean_text(soup.title.get_text()) if soup.title else ""

    h1 = soup.find("h1")
    main_heading = clean_text(h1.get_text()) if h1 else page_title

    body_text = clean_text(soup.get_text(separator=" "))

    return {
        "title": page_title,
        "main_heading": main_heading,
        "body_text": body_text
    }