# Design Decisions and Tradeoffs

This document explains some of the key design decisions made in the current implementation.

---

## 1) Why use source-specific ingestion modules?

Different funding sources expose data differently.

For example:

- Grants.gov is handled through HTML page retrieval and extraction
- NSF is handled through structured API data

Because of this, source-specific logic is separated into dedicated modules rather than forcing all logic into a single parser.

### Benefit
This makes the code easier to maintain and extend.

### Tradeoff
There is some duplication between source adapters, but the separation improves clarity and future scalability.

---

## 2) Why normalize everything into a common schema?

The main challenge in FOA ingestion is inconsistency across sources.

A shared normalized schema makes it easier to:

- compare records
- apply shared tagging logic
- export consistently
- extend downstream use cases

### Benefit
One tagging/export layer can work across multiple sources.

### Tradeoff
Some source-specific nuance may be flattened or simplified during normalization.

---

## 3) Why use deterministic semantic tagging first?

The project currently uses deterministic tagging rather than embeddings or LLM-based classification.

### Benefit
This keeps the MVP:
- interpretable
- lightweight
- reproducible
- testable

### Tradeoff
This approach is less flexible than semantic similarity or model-based tagging and may miss nuanced phrasing.

---

## 4) Why export to JSON and CSV?

The project exports both formats because they serve different use cases.

### JSON
Useful for structured programmatic consumption and preserving nested semantic tags.

### CSV
Useful for manual inspection, spreadsheet workflows, and lightweight downstream analysis.

### Benefit
Both machine-readable and analyst-friendly outputs are supported.

### Tradeoff
CSV is less expressive for nested structures and may flatten some fields.

---

## 5) Why use a CLI-first workflow?

The current project is designed as a command-line pipeline rather than a UI-based system.

### Benefit
This keeps the MVP simple, reproducible, and easy to test.

### Tradeoff
It is less convenient for non-technical users compared to a dashboard or web interface.

---

## 6) Why not implement everything at once?

The project intentionally prioritizes a smaller, testable core before expanding into more advanced features such as:

- batch ingestion
- PDF parsing
- embeddings
- vector search
- evaluation dashboards

### Benefit
This reduces implementation risk and helps ensure the core pipeline works reliably first.

### Tradeoff
Some requested stretch capabilities are not yet implemented in the current version.