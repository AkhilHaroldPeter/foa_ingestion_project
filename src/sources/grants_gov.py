from src.parser import fetch_url_content, parse_html_content

"""
Source-specific ingestion logic for Grants.gov opportunity pages.

This module handles retrieval and source-specific preprocessing for
Grants.gov funding opportunity records.

Because Grants.gov opportunities are ingested from public HTML pages,
this module focuses on:
- fetching page content
- parsing source HTML
- preparing content for structured extraction

This source adapter is intentionally isolated so that source-specific
logic does not leak into the rest of the pipeline.
"""


def ingest_grants_gov(url: str) -> dict:
    """
    Fetch and parse a Grants.gov-style FOA HTML page.
    Returns parsed raw data for downstream extraction.
    """
    html = fetch_url_content(url)
    parsed_data = parse_html_content(html)
    return parsed_data