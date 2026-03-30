# tests/test_nsf_api.py

from src.sources.nsf_api import normalize_nsf_award


def test_normalize_nsf_award():
    sample_record = {
        "title": "AI for Scientific Discovery",
        "abstractText": "This project supports machine learning research for scientific applications.",
        "agency": "NSF",
        "date": "2026-01-15",
        "expDate": "2027-01-15",
        "estimatedTotalAmt": "500000"
    }

    result = normalize_nsf_award(sample_record, keyword="AI")

    assert result["title"] == "AI for Scientific Discovery"
    assert result["agency"] == "NSF"
    assert result["open_date"] == "2026-01-15"
    assert result["close_date"] == "2027-01-15"
    assert result["award_range"] == "$500000"
    assert "machine learning" in result["program_description"].lower()