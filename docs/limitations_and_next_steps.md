# Limitations and Next Steps

This document outlines the current limitations of the project and realistic next steps for future development.

---

## Current Limitations

### 1) Single-record CLI workflow
The current CLI is primarily designed around one input at a time:

- one Grants.gov URL
- one NSF keyword query

This is sufficient for the MVP, but not yet a full batch ingestion system.

---

### 2) Source coverage is limited
The current implementation supports:

- Grants.gov
- NSF Awards API

Other useful sources such as NIH, agency PDFs, or institutional funding pages are not yet supported.

---

### 3) HTML extraction is source-format dependent
The Grants.gov extraction logic is tied to the current structure of the source page.

If the source layout changes, extraction logic may need to be updated.

---

### 4) No PDF ingestion yet
Although PDF support is a logical next step for FOA ingestion, it is not currently implemented.

---

### 5) Semantic tagging is rule-based only
The current tagging system is deterministic and keyword-based.

This is useful for interpretability and testing, but it is not yet a semantic similarity or model-based classification system.

---

### 6) Evaluation is not yet fully implemented
The current project includes unit tests for functionality, but not yet a dedicated tagging evaluation dataset with precision / recall style measurement.

---

## Recommended Next Steps

### Near-Term Improvements
- Add batch ingestion support
- Improve output organization for multiple records
- Expand semantic keyword coverage
- Improve logging and validation

### Medium-Term Improvements
- Add NIH or another public funding source
- Add PDF ingestion support
- Add tagging evaluation dataset
- Improve schema robustness across edge cases

### Longer-Term Improvements
- Add embedding-based semantic similarity
- Add lightweight search or filtering interface
- Add vector indexing for retrieval workflows
- Add database-backed storage or update tracking

---

## Guiding Principle

The project is currently positioned as a **clean, testable MVP**.

The next steps should prioritize:

1. reliability  
2. source coverage  
3. evaluation  
4. semantic depth  

in that order.