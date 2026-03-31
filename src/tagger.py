import re

"""
Rule-based semantic tagging for normalized FOA records.

This module applies deterministic ontology-aligned tags to funding
opportunity records based on their textual content.

The tagging system is designed to be:
- lightweight
- interpretable
- reproducible
- easy to extend

Current semantic tag groups include:
- research domains
- methods / approaches
- populations
- sponsor themes

Tagging is currently based on curated keyword and phrase matching.
"""

ONTOLOGY = {
    "research_domains": {
        "Artificial Intelligence": ["artificial intelligence", "machine learning", "deep learning"],
        "Public Health": ["public health", "healthcare", "clinical", "disease", "mental health", "substance use"],
        "Education": ["education", "student", "learning", "curriculum"],
        "Climate & Environment": ["climate", "environment", "sustainability", "ecology"]
    },
    "methods_approaches": {
        "Survey Research": ["survey", "questionnaire"],
        "Simulation": ["simulation", "simulated"],
        "Data Analysis": ["data analysis", "analytics", "modeling"],
        "Intervention Study": ["intervention", "program evaluation", "treatment services", "treatment"]
    },
    "populations": {
        "Children": ["children", "youth", "adolescent"],
        "Students": ["students", "undergraduate", "graduate"],
        "Rural Communities": ["rural"],
        "Underserved Populations": ["underserved", "low-income", "marginalized"]
    },
    "sponsor_themes": {
        "Innovation": ["innovation", "innovative"],
        "Workforce Development": ["workforce", "training", "career development"],
        "Equity": ["equity", "inclusion", "diversity"],
        "Infrastructure": ["infrastructure", "capacity building", "technology modernization", "housing access"]
    }
}


def contains_phrase(text: str, phrase: str) -> bool:
    return phrase.lower() in text.lower()


def apply_tags(foa_data: dict) -> dict:
    """
    Apply deterministic semantic tags to a normalized FOA record.

    Tags are assigned by checking the record text against curated keyword
    groups mapped to ontology-aligned categories.
    """    
    combined_text = " ".join([
        foa_data.get("title", ""),
        foa_data.get("eligibility_text", ""),
        foa_data.get("program_description", "")
    ]).lower()

    tags = {
        "research_domains": [],
        "methods_approaches": [],
        "populations": [],
        "sponsor_themes": []
    }

    for category, label_map in ONTOLOGY.items():
        for label, keywords in label_map.items():
            if any(contains_phrase(combined_text, keyword) for keyword in keywords):
                tags[category].append(label)

    foa_data["tags"] = tags
    return foa_data