# Architecture Overview

This project is structured as a lightweight, modular ingestion and normalization pipeline for Funding Opportunity Announcement (FOA)-like records.

The current implementation focuses on a clear separation of concerns so that each layer of the pipeline can be extended independently.

---

## High-Level Pipeline

The pipeline currently follows this flow:

1. **Source Ingestion**
   - Retrieve raw content from a supported source
   - Example sources:
     - Grants.gov (HTML page)
     - NSF Awards API (structured JSON)

2. **Parsing / Extraction**
   - Extract source-specific fields
   - Normalize them into a shared internal structure

3. **Semantic Tagging**
   - Apply deterministic ontology-aligned semantic tags

4. **Export**
   - Save normalized outputs as:
     - JSON
     - CSV

---

## Current Project Structure

```bash
foa_ingestion_project/
│
├── main.py
├── README.md
├── requirements.txt
│
├── out/
│   ├── grants_foa.csv
│   ├── grants_foa.json
│   ├── nsf_foa.csv
│   └── nsf_foa.json
│
├── src/
│   ├── extractor.py
│   ├── exporter.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── tagger.py
│   ├── utils.py
│   └── sources/
│       ├── grants_gov.py
│       └── nsf_api.py
│
└── tests/
    ├── test_extractor.py
    ├── test_nsf_api.py
    ├── test_tagger.py
    └── test_utils.py
```


---    

## Module Responsibilities
```main.py```

Acts as the CLI entry point.
It routes execution based on the requested source and coordinates the full ingestion workflow.

```src/fetcher.py```

Handles raw HTTP retrieval for source content.

```src/parser.py```

Contains parsing-related logic used to prepare raw content for extraction.

```src/extractor.py```

Extracts structured metadata from raw or parsed source content.

```src/sources/grants_gov.py```

Contains source-specific handling for Grants.gov opportunity pages.

```src/sources/nsf_api.py```

Contains source-specific retrieval and normalization logic for the NSF Awards API.

```src/tagger.py```

Applies deterministic semantic tags to normalized records.

```src/exporter.py```

Writes processed records to JSON and CSV.

```src/utils.py```

Contains reusable helpers such as text cleaning, date normalization, and FOA ID generation.



## Design Goal

The architecture is intentionally lightweight and modular so that future enhancements can be added without rewriting the full pipeline.

This makes it easier to extend the project later for:

- additional funding sources
- batch ingestion
- PDF parsing
- evaluation workflows
- semantic similarity or embedding-based enrichment
