#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image

base_dir = Path(r"D:\workspace\HROC_Files\HROC_Website_New")
webp_files = list(base_dir.rglob("*.webp"))

print(f"Found {len(webp_files)} WebP files to convert...")
successful = 0
failed = 0
errors = []

for webp_file in webp_files:
    try:
        # Create output filename
        png_file = webp_file.with_suffix('.png')

        # Skip if PNG already exists
        if png_file.exists():
            print(f"SKIP: {png_file.name} (already exists)")
            continue

        # Open and convert
        img = Image.open(webp_file)
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            rgb_img.save(png_file, 'PNG', quality=95)
        else:
            img.save(png_file, 'PNG', quality=95)

        print(f"OK: {webp_file.name} > {png_file.name}")
        successful += 1
    except Exception as e:
        failed += 1
        error_msg = f"ERROR: {webp_file.name}: {str(e)}"
        print(error_msg)
        errors.append(error_msg)

print(f"\n{'='*60}")
print(f"Conversion Complete!")
print(f"Successfully converted: {successful}")
print(f"Failed: {failed}")
print(f"Total WebP files: {len(webp_files)}")
if errors:
    print(f"\nErrors:")
    for error in errors:
        print(f"  {error}")
