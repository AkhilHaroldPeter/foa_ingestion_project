import requests
from src.utils import clean_text, generate_foa_id, normalize_date


def fetch_nsf_awards(keyword: str, limit: int = 1) -> list:
    """
    Fetch NSF awards data using keyword search.
    Returns a list of raw NSF award records.
    """
    url = f"https://api.nsf.gov/services/v1/awards.json?keyword={keyword}"

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    awards = data.get("response", {}).get("award", [])
    return awards[:limit]


def normalize_nsf_award(record: dict, keyword: str = "NSF") -> dict:
    """
    Convert a raw NSF API record into the common normalized FOA schema.
    """
    title = clean_text(record.get("title", ""))
    abstract = clean_text(record.get("abstractText", ""))
    agency = clean_text(record.get("agency", "NSF")) or "NSF"

    open_date = normalize_date(record.get("date", ""))
    close_date = normalize_date(record.get("expDate", ""))

    award_amt = record.get("estimatedTotalAmt", "")
    if award_amt:
        award_range = f"${award_amt}"
    else:
        award_range = ""

    source_url = record.get(
        "awardeeCity",
        f"https://api.nsf.gov/services/v1/awards.json?keyword={keyword}"
    )

    normalized = {
        "foa_id": generate_foa_id(title + abstract),
        "title": title,
        "agency": agency,
        "open_date": open_date,
        "close_date": close_date,
        "eligibility_text": "Not specified in NSF API record",
        "program_description": abstract,
        "award_range": award_range,
        "source_url": f"https://api.nsf.gov/services/v1/awards.json?keyword={keyword}",
        "tags": {
            "research_domains": [],
            "methods_approaches": [],
            "populations": [],
            "sponsor_themes": []
        }
    }

    return normalized