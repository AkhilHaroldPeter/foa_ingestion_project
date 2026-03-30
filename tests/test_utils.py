from src.utils import clean_text, generate_foa_id, normalize_date


def test_clean_text():
    raw = "Hello   \n\n   World\t\t!"
    cleaned = clean_text(raw)
    assert "Hello" in cleaned
    assert "World" in cleaned


def test_generate_foa_id():
    url = "https://example.com/foa"
    foa_id = generate_foa_id(url)
    assert isinstance(foa_id, str)
    assert len(foa_id) == 10


def test_normalize_date():
    date_str = "March 30, 2026"
    normalized = normalize_date(date_str)
    assert normalized == "2026-03-30"