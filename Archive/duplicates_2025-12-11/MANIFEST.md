# Duplicate Files Archived - 2025-12-11

## Summary
- Moved full `ALL_PDFS/` folder to `Archive/duplicates_2025-12-11/ALL_PDFS/`.
- Canonical, site-facing copies now live in `HROC_Website_New/pdfs/`.
- No changes made to existing archive/markdown duplicates.

## Rationale
`ALL_PDFS/` contained exact duplicates of every PDF already placed under `HROC_Website_New/pdfs/`. To reduce clutter and avoid double-maintenance, the original bundle was archived.

## Locations
- Canonical: `HROC_Website_New/pdfs/` (used by documents.html)
- Archived duplicates: `Archive/duplicates_2025-12-11/ALL_PDFS/`

## Notes
- Other duplicate markdown files already live entirely under `Archive/` and were left untouched to avoid disturbing historical records.

## Dev/Test Scripts Archived (2025-12-11)
- Archived: `Archive/dev_scripts_2025-12-11/`
  - generate_test_images.py
  - image-generator/lora-train.js
  - image-generator/lora-train-bri.js
- Rationale: keep experimental generation scripts out of the active tree.

## Markdown Duplicates Consolidated
- Moved duplicate markdown set from `Archive/duplicates_by_hash/Archive/markdown_backup/` to `Archive/duplicates_2025-12-11/markdown_duplicates/from_duplicates_by_hash/`.
- Canonical markdown set remains in `Archive/markdown_backup/`.
- `Archive/duplicates_by_hash/manifest.txt` retained as provenance; redundant markdown folder removed from that tree.
