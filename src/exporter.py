# import os
# import json
# import pandas as pd


# def export_json(foa_data: dict, out_dir: str):
#     output_path = os.path.join(out_dir, "foa.json")
#     with open(output_path, "w", encoding="utf-8") as f:
#         json.dump(foa_data, f, indent=4, ensure_ascii=False)


# def export_csv(foa_data: dict, out_dir: str):
#     flattened = {
#         "foa_id": foa_data.get("foa_id", ""),
#         "title": foa_data.get("title", ""),
#         "agency": foa_data.get("agency", ""),
#         "open_date": foa_data.get("open_date", ""),
#         "close_date": foa_data.get("close_date", ""),
#         "eligibility_text": foa_data.get("eligibility_text", ""),
#         "program_description": foa_data.get("program_description", ""),
#         "award_range": foa_data.get("award_range", ""),
#         "source_url": foa_data.get("source_url", ""),
#         "research_domains": ", ".join(foa_data.get("tags", {}).get("research_domains", [])),
#         "methods_approaches": ", ".join(foa_data.get("tags", {}).get("methods_approaches", [])),
#         "populations": ", ".join(foa_data.get("tags", {}).get("populations", [])),
#         "sponsor_themes": ", ".join(foa_data.get("tags", {}).get("sponsor_themes", []))
#     }

#     df = pd.DataFrame([flattened])
#     output_path = os.path.join(out_dir, "foa.csv")
#     df.to_csv(output_path, index=False)
# src/exporter.py

# import os
# import json
# import pandas as pd


# def export_outputs(foa_data: dict, out_dir: str):
#     """
#     Export normalized FOA data into:
#     - foa.json
#     - foa.csv
#     """

#     os.makedirs(out_dir, exist_ok=True)

#     # -------------------------
#     # Export JSON
#     # -------------------------
#     json_path = os.path.join(out_dir, "foa.json")
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(foa_data, f, indent=4, ensure_ascii=False)

#     # -------------------------
#     # Flatten tags for CSV
#     # -------------------------
#     csv_data = foa_data.copy()
#     tags = csv_data.pop("tags", {})

#     csv_data["research_domains"] = ", ".join(tags.get("research_domains", []))
#     csv_data["methods_approaches"] = ", ".join(tags.get("methods_approaches", []))
#     csv_data["populations"] = ", ".join(tags.get("populations", []))
#     csv_data["sponsor_themes"] = ", ".join(tags.get("sponsor_themes", []))

#     df = pd.DataFrame([csv_data])

#     csv_path = os.path.join(out_dir, "foa.csv")
#     df.to_csv(csv_path, index=False, encoding="utf-8")
# src/exporter.py

import os
import json
import pandas as pd


def export_outputs(foa_data: dict, out_dir: str, source_name: str = "foa"):
    """
    Export normalized FOA data into:
    - <source_name>_foa.json
    - <source_name>_foa.csv
    """

    os.makedirs(out_dir, exist_ok=True)

    json_path = os.path.join(out_dir, f"{source_name}_foa.json")
    csv_path = os.path.join(out_dir, f"{source_name}_foa.csv")

    # -------------------------
    # Export JSON
    # -------------------------
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(foa_data, f, indent=4, ensure_ascii=False)

    # -------------------------
    # Flatten tags for CSV
    # -------------------------
    csv_data = foa_data.copy()
    tags = csv_data.pop("tags", {})

    csv_data["research_domains"] = ", ".join(tags.get("research_domains", []))
    csv_data["methods_approaches"] = ", ".join(tags.get("methods_approaches", []))
    csv_data["populations"] = ", ".join(tags.get("populations", []))
    csv_data["sponsor_themes"] = ", ".join(tags.get("sponsor_themes", []))

    df = pd.DataFrame([csv_data])
    df.to_csv(csv_path, index=False, encoding="utf-8")