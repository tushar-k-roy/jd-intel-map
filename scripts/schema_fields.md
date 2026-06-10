# JD JSON Schema

Each line in `data/processed/jd_master.jsonl` should be one JSON object.

Required keys:

- entry_id
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

Rules:
- Always keep all keys
- Use null or "NOT_MENTIONED" for missing values
- Multi-value fields should be arrays in JSON
- If internal joining is needed later, use `;`
