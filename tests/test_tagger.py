from src.tagger import apply_tags


def test_apply_tags_public_health():
    sample_foa = {
        "title": "Mental Health and Treatment Services Funding",
        "eligibility_text": "State governments and local agencies",
        "program_description": "Supports mental health and substance use treatment services.",
        "tags": {}
    }

    result = apply_tags(sample_foa)

    assert "Public Health" in result["tags"]["research_domains"]
    assert "Intervention Study" in result["tags"]["methods_approaches"]