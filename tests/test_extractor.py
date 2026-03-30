from src.extractor import extract_fields


def test_extract_fields_basic():
    parsed_data = {
        "title": "Test FOA",
        "main_heading": "Test FOA Main Heading",
        "body_text": """
        Posted Date: February 19, 2026
        Closing: March 30, 2026
        Description
        This funding supports mental health treatment programs.
        Eligibility
        State governments and tribal governments
        Award Minimum $3,000,000
        """
    }

    result = extract_fields(parsed_data, "https://example.com/test-foa")

    assert result["title"] == "Test FOA Main Heading"
    assert result["open_date"] == "2026-02-19"
    assert result["close_date"] == "2026-03-30"
    assert result["agency"] in ["Unknown", "Grants.gov", "NSF", "NIH"]
    assert result["award_range"] != ""