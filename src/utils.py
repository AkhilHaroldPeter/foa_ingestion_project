import re
import hashlib
from dateutil import parser as date_parser


def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"\r", " ", text)
    text = re.sub(r"\t", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ ]{2,}", " ", text)
    return text.strip()


def generate_foa_id(url: str) -> str:
    return hashlib.md5(url.encode()).hexdigest()[:10]


def normalize_date(date_str: str) -> str:
    try:
        dt = date_parser.parse(date_str, fuzzy=True)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return ""


def extract_with_regex(patterns: list, text: str) -> str:
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            return clean_text(match.group(1))
    return ""


def extract_section_text(section_keywords: list, text: str, max_chars: int = 1000) -> str:
    lines = text.split("\n")
    collected = []

    capture = False
    for line in lines:
        stripped = line.strip()

        if any(keyword.lower() in stripped.lower() for keyword in section_keywords):
            capture = True
            continue

        if capture:
            if stripped == "":
                break
            collected.append(stripped)

    result = " ".join(collected)
    return clean_text(result[:max_chars])