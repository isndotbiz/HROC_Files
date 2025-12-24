#!/usr/bin/env python3
import re
from pathlib import Path

base_dir = Path(r"D:\workspace\HROC_Files\HROC_Website_New")
html_files = [
    base_dir / "index.html",
    base_dir / "documents.html",
]

bucket_name = "hroc-outreach-assets-1765630540"
s3_base_url = f"https://{bucket_name}.s3.us-west-2.amazonaws.com"

fixes = [
    # Fix service-*.png paths (they're actually in images/generated/)
    (
        f'{s3_base_url}/images/service-',
        f'{s3_base_url}/images/generated/service-'
    ),
    # Fix infographic paths (also in generated)
    (
        f'{s3_base_url}/images/infographic-',
        f'{s3_base_url}/images/generated/infographic-'
    ),
    # Fix photo/button/icon paths (also in generated)
    (
        f'{s3_base_url}/images/photo-',
        f'{s3_base_url}/images/generated/photo-'
    ),
    (
        f'{s3_base_url}/images/button-',
        f'{s3_base_url}/images/generated/button-'
    ),
    (
        f'{s3_base_url}/images/icon-',
        f'{s3_base_url}/images/generated/icon-'
    ),
    (
        f'{s3_base_url}/images/background-',
        f'{s3_base_url}/images/generated/background-'
    ),
]

for html_file in html_files:
    if not html_file.exists():
        print(f"SKIP: {html_file.name} (not found)")
        continue

    content = html_file.read_text(encoding='utf-8')
    original = content

    for old, new in fixes:
        content = content.replace(old, new)

    if content != original:
        html_file.write_text(content, encoding='utf-8')
        # Count changes
        changes = sum(1 for line in original.split('\n') if any(old in line for old, _ in fixes))
        print(f"OK: {html_file.name} - Fixed {changes} image paths")
    else:
        print(f"SKIP: {html_file.name} - No changes needed")

print("\nPath fixes complete!")
