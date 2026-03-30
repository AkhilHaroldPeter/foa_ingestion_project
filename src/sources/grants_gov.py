# src/sources/grants_gov.py

from src.parser import fetch_url_content, parse_html_content


def ingest_grants_gov(url: str) -> dict:
    """
    Fetch and parse a Grants.gov-style FOA HTML page.
    Returns parsed raw data for downstream extraction.
    """
    html = fetch_url_content(url)
    parsed_data = parse_html_content(html)
    return parsed_data