#!/usr/bin/env python3
import os
import re
from pathlib import Path

bucket_name = "hroc-outreach-assets-1765630540"
s3_base_url = f"https://{bucket_name}.s3.us-west-2.amazonaws.com"

base_dir = Path(r"D:\workspace\HROC_Files\HROC_Website_New")
html_files = [
    base_dir / "index.html",
    base_dir / "documents.html",
    base_dir / "generated_images" / "image_gallery.html",
]

def update_html_file(file_path):
    """Update image and PDF references in HTML file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # Replace WebP image paths with PNG from S3
        # Pattern: src="path/to/image.webp" or href="path/to/file.pdf"

        # Handle relative paths like "images/..." -> S3 URL with .png
        content = re.sub(
            r'(src|href)="(images/[^"]+)\.webp"',
            lambda m: f'{m.group(1)}="{s3_base_url}/images/{Path(m.group(2)).name}.png"',
            content
        )

        # Handle generated_images paths
        content = re.sub(
            r'(src|href)="(generated_images/[^"]+)\.webp"',
            lambda m: f'{m.group(1)}="{s3_base_url}/generated_images/{m.group(2).replace(os.sep, "/")}.png"',
            content
        )

        # Handle service_icons paths
        content = re.sub(
            r'(src|href)="(service_icons/[^"]+)\.webp"',
            lambda m: f'{m.group(1)}="{s3_base_url}/service_icons/{Path(m.group(2)).name}.png"',
            content
        )

        # Handle hero_banners paths
        content = re.sub(
            r'(src|href)="(hero_banners/[^"]+)\.webp"',
            lambda m: f'{m.group(1)}="{s3_base_url}/hero_banners/{Path(m.group(2)).name}.png"',
            content
        )

        # Handle PDF references
        content = re.sub(
            r'(href)="(pdfs/[^"]+\.pdf)"',
            lambda m: f'{m.group(1)}="{s3_base_url}/pdfs/{m.group(2).replace(os.sep, "/")}"',
            content
        )

        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            return True, "Updated"
        else:
            return False, "No changes needed"
    except Exception as e:
        return False, f"Error: {str(e)}"

print(f"Updating HTML files to use S3 URLs...\n")
print(f"S3 Base URL: {s3_base_url}\n")

for html_file in html_files:
    if html_file.exists():
        success, message = update_html_file(html_file)
        status = "OK" if success else "SKIP"
        print(f"{status}: {html_file.name} - {message}")
    else:
        print(f"SKIP: {html_file.name} (not found)")

print(f"\n{'='*60}")
print(f"HTML Update Complete!")
print(f"All relative image paths now point to S3 bucket")
