import re

from src.utils import clean_text, normalize_date, generate_foa_id

"""
Field extraction logic for FOA-style funding opportunity records.

This module contains functions responsible for extracting structured fields
from raw source content, especially HTML-based records such as Grants.gov
opportunity pages.

The goal of this layer is to convert semi-structured content into a clean,
normalized dictionary that can be used downstream for tagging and export.

Typical extracted fields include:
- title
- agency
- open / close dates
- eligibility text
- program description
- award range
- source URL
"""

def _extract_between(text: str, start_label: str, end_labels: list[str]) -> str:
    """
    Extract text between a start label and the earliest matching end label.
    """
    start_match = re.search(start_label, text, re.IGNORECASE)
    if not start_match:
        return ""

    start_idx = start_match.end()
    remaining = text[start_idx:]

    end_idx = len(remaining)
    for label in end_labels:
        match = re.search(label, remaining, re.IGNORECASE)
        if match:
            end_idx = min(end_idx, match.start())

    return clean_text(remaining[:end_idx])


def extract_fields(parsed_data: dict, source_url: str) -> dict:
    """
    Extract structured FOA fields from parsed HTML/text content.
    """
    title = parsed_data.get("main_heading") or parsed_data.get("title") or ""
    body_text = parsed_data.get("body_text", "")

    body_text = clean_text(body_text)

    # -----------------------------
    # Dates
    # -----------------------------
    posted_match = re.search(r"Posted date\s*:\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})", body_text, re.IGNORECASE)
    if not posted_match:
        posted_match = re.search(r"Posted Date\s*:\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})", body_text, re.IGNORECASE)

    closing_match = re.search(r"Closing\s*:\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})", body_text, re.IGNORECASE)

    open_date = normalize_date(posted_match.group(1)) if posted_match else ""
    close_date = normalize_date(closing_match.group(1)) if closing_match else ""

    # -----------------------------
    # Award range
    # -----------------------------
    award_match = re.search(r"Award Minimum\s*\$?([\d,]+)", body_text, re.IGNORECASE)
    award_range = f"${award_match.group(1)}" if award_match else ""

    # -----------------------------
    # Eligibility section
    # -----------------------------
    eligibility_text = _extract_between(
        body_text,
        r"Eligibility(?:\s+Eligible applicants)?",
        [
            r"Grantor contact information",
            r"Description",
            r"Documents",
            r"Application process",
            r"Award",
            r"Funding opportunity number",
        ]
    )

    # -----------------------------
    # Description section
    # -----------------------------
    program_description = _extract_between(
        body_text,
        r"Description",
        [
            r"Eligibility",
            r"Eligible applicants",
            r"Grantor contact information",
            r"Documents",
            r"Application process",
            r"Award",
            r"Funding opportunity number",
        ]
    )

    # Fallbacks if extraction is empty
    if not program_description:
        program_description = body_text[:1500]

    if not eligibility_text:
        eligibility_text = "Not clearly extracted from source page"

    return {
        "foa_id": generate_foa_id(source_url),
        "title": title,
        "agency": "Grants.gov",
        "open_date": open_date,
        "close_date": close_date,
        "eligibility_text": eligibility_text,
        "program_description": program_description,
        "award_range": award_range,
        "source_url": source_url,
        "tags": {}
    }