import json
import csv
from pathlib import Path

INPUT_FILE = Path("data/processed/jd_master.jsonl")
OUTPUT_FILE = Path("data/exports/jd_master.csv")

FIELDNAMES = [
    "entry_id",
    "date_added",
    "company",
    "role_title_raw",
    "role_title_standardized",
    "industry",
    "location",
    "work_mode",
    "seniority",
    "employment_type",
    "salary",
    "inferred_job_family",
    "inferred_specialization",
    "inferred_role_focus",
    "skills_tools",
    "skills_technical",
    "skills_business_terms",
    "skills_governance_terms",
    "skills_soft",
    "required_skills",
    "preferred_skills",
    "similarity_tags",
    "notes",
]

def normalize_value(value):
    if isinstance(value, list):
        return " | ".join(str(item) for item in value)
    if value is None:
        return ""
    return str(value)

def main():
    rows = []

    with INPUT_FILE.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {line_number}: {e}")

            row = {}
            for field in FIELDNAMES:
                row[field] = normalize_value(record.get(field, ""))
            rows.append(row)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV created: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
