# JD JSON Schema

Each line in `data/processed/jd_master.jsonl` should be one JSON object.
## Required keys

- entry_id
- date_posted
- date_added
- company
- role_title_raw
- role_title_standardized
- industry
- location
- work_mode
- seniority
- employment_type
- salary
- inferred_job_family
- inferred_specialization
- inferred_role_focus
- skills_tools
- skills_technical
- skills_business_terms
- skills_governance_terms
- skills_soft
- required_skills
- preferred_skills
- similarity_tags
- notes

## Field rules

- `entry_id`
  - Must be numeric-only, stored as a string (e.g. `"1"`, `"2"`, `"3"`).
  - Acts as the primary key for each JD record.

- `date_posted`
  - Date when the job was posted on LinkedIn/company site.
  - Format: `YYYY-MM-DD` if known.
  - Use `"NOT_MENTIONED"` if the exact posting date cannot be determined.

- `date_added`
  - Date when you copied/logged this JD into your personal dataset.
  - Format: `YYYY-MM-DD`.

## General rules

- Always keep **all** keys in every record.
- For missing/unknown values, use `null` or `"NOT_MENTIONED"` (but do not drop the key).
- Multi-value fields (`skills_*`, `required_skills`, `preferred_skills`, `similarity_tags`) **must be arrays** of strings in JSON.
- If you need internal grouping inside a string, use `;` as the separator (e.g. `"SQL;joins;aggregations"`).
- Downstream exports (e.g. CSV) may join array values using `" | "` or other separators, but the source JSONL should keep them as arrays.
