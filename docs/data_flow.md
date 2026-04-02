
The pipeline starts from the command line via `main.py`.

### Example commands

#### Grants.gov
```bash
python main.py --source grants --url "https://simpler.grants.gov/opportunity/<id>" --out_dir ./out
```

#### NSF
```bash
python main.py --source nsf --keyword "AI" --out_dir ./out
```

---

## Current Processing Flow
   **1) Input Selection**

The CLI accepts a source type and source-specific input:

```--source grants``` + ```--url```

```--source nsf``` + ```--keyword```

This determines which ingestion path will be executed.

---

  **2) Source Retrieval**

Depending on the source, the pipeline retrieves either:

- HTML content (Grants.gov)
- JSON API response (NSF)

This is handled by source-specific logic.

---

  **3) Source-Specific Extraction / Normalization**

Each source is processed differently:

**Grants.gov**

The raw HTML page is parsed and relevant FOA-like fields are extracted.

**NSF**

The API response is already structured, so the selected award record is normalized into the same schema used by the Grants.gov pipeline.

---

**4) Shared Normalized Schema**

Both sources are transformed into a common schema:
```json
{
  "foa_id": "string",
  "title": "string",
  "agency": "string",
  "open_date": "YYYY-MM-DD",
  "close_date": "YYYY-MM-DD",
  "eligibility_text": "string",
  "program_description": "string",
  "award_range": "string",
  "source_url": "string",
  "tags": {
    "research_domains": [],
    "methods_approaches": [],
    "populations": [],
    "sponsor_themes": []
  }
}
```

---

**5) Semantic Tagging**

Once normalized, the record is passed into the tagging layer.

This applies deterministic semantic tags based on text matching against curated ontology-like keyword groups.

--

**6) Export**

The final record is exported to:

- **JSON**
- **CSV**

The outputs are written to the configured ```out/``` directory.

---

### Why this flow matters

Using a normalized intermediate schema makes it easier to:

- compare heterogeneous funding records
- extend to new sources
- add evaluation later
- support downstream search or matching workflows