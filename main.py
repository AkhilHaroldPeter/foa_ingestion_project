import os
import argparse

from src.extractor import extract_fields
from src.tagger import apply_tags
from src.exporter import export_outputs

from src.sources.grants_gov import ingest_grants_gov
from src.sources.nsf_api import fetch_nsf_awards, normalize_nsf_award

"""
Main entry point for the FOA ingestion and semantic tagging pipeline.

This script acts as the command-line interface for the project. It allows
the user to run ingestion workflows for supported funding opportunity
sources, normalize the extracted data into a common schema, apply
deterministic semantic tags, and export the final outputs as JSON and CSV.

Currently supported sources:
* Grants.gov (HTML-based ingestion)
* NSF Awards API (structured JSON ingestion)

Example usage:
    python main.py --source grants --url "<FOA_URL>" --out_dir ./out
    python main.py --source nsf --keyword "AI" --out_dir ./out
"""

def main():
    """
    Parse CLI arguments and run the selected ingestion workflow.

    Based on the requested source, this function triggers the appropriate
    ingestion pipeline, applies semantic tagging, and exports the processed
    output to the specified directory.
    """
    parser = argparse.ArgumentParser(description="FOA Ingestion + Semantic Tagging Pipeline")

    parser.add_argument(
        "--source",
        required=True,
        choices=["grants", "nsf"],
        help="Data source to ingest from: grants or nsf"
    )

    parser.add_argument(
        "--url",
        help="FOA URL for Grants.gov-style HTML ingestion"
    )

    parser.add_argument(
        "--keyword",
        help="Keyword for NSF API search"
    )

    parser.add_argument(
        "--out_dir",
        required=True,
        help="Directory to store output files"
    )

    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    if args.source == "grants":
        if not args.url:
            raise ValueError("For --source grants, you must provide --url")

        print("[INFO] Fetching Grants.gov URL...")
        parsed_data = ingest_grants_gov(args.url)

        print("[INFO] Extracting structured fields...")
        foa_data = extract_fields(parsed_data, args.url)

        print("[INFO] Applying semantic tags...")
        tagged_data = apply_tags(foa_data)

        print("[INFO] Exporting outputs...")
        # export_outputs(tagged_data, args.out_dir)
        export_outputs(tagged_data, args.out_dir, source_name=args.source)

        print(f"[SUCCESS] Grants.gov files created successfully in: {args.out_dir}")

    elif args.source == "nsf":
        if not args.keyword:
            raise ValueError("For --source nsf, you must provide --keyword")

        print("[INFO] Fetching NSF API data...")
        awards = fetch_nsf_awards(args.keyword, limit=1)

        if not awards:
            raise ValueError("No NSF awards found for the given keyword.")

        print("[INFO] Normalizing NSF award record...")
        foa_data = normalize_nsf_award(awards[0], keyword=args.keyword)

        print("[INFO] Applying semantic tags...")
        tagged_data = apply_tags(foa_data)

        print("[INFO] Exporting outputs...")
        # export_outputs(tagged_data, args.out_dir)
        export_outputs(tagged_data, args.out_dir, source_name=args.source)

        print(f"[SUCCESS] NSF files created successfully in: {args.out_dir}")


if __name__ == "__main__":
    main()
