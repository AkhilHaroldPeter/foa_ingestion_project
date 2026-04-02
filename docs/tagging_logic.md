
# Semantic Tagging Logic

This document explains how semantic tagging is currently implemented in the project.

---

## Current Approach

The project currently uses a **deterministic rule-based semantic tagging strategy**.

This means tags are assigned by checking FOA text against predefined keyword or phrase groups mapped to semantic categories.

The goal of this approach is to keep the tagging system:

- interpretable
- reproducible
- easy to test
- easy to extend

---

## Current Semantic Categories

The tagging system currently supports the following top-level categories:

- `research_domains`
- `methods_approaches`
- `populations`
- `sponsor_themes`

---

## Tagging Inputs

Tags are assigned based on available text fields such as:

- title
- program description
- eligibility text
- other extracted descriptive content

The exact behavior depends on how the current `tagger.py` logic combines and checks record text.

---

## Why Rule-Based Tagging Was Chosen

For the current MVP, rule-based tagging was chosen because it offers:

### 1) Transparency
It is easy to explain why a tag was assigned.

### 2) Reproducibility
The same input produces the same output.

### 3) Testability
The logic can be unit tested directly.

### 4) Low Complexity
It avoids introducing heavier dependencies too early.

---

## Tradeoff

Rule-based tagging is useful for an MVP, but it has known limitations:

- it depends on keyword coverage
- it may miss semantically similar wording
- it can underperform on ambiguous or domain-specific phrasing

Because of this, it should be treated as a strong baseline rather than a final semantic classification system.

---

## Possible Future Extensions

Future versions of the tagging layer could include:

- expanded ontology coverage
- synonym-aware matching
- embedding-based similarity
- confidence scoring
- hybrid rule + semantic retrieval workflows

These are not currently implemented in the project, but the tagging layer is modular enough to support them later.