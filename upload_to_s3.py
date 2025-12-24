#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

bucket_name = "hroc-outreach-assets-1765630540"
base_dir = Path(r"D:\workspace\HROC_Files\HROC_Website_New")

# Define what to upload
uploads = [
    ("images", "images/"),
    ("generated_images", "generated_images/"),
    ("lora_training", "lora_training/"),
    ("pdfs", "pdfs/"),
]

print(f"Uploading to S3 bucket: {bucket_name}\n")

total_files = 0
total_success = 0

for source_folder, s3_prefix in uploads:
    source_path = base_dir / source_folder

    if not source_path.exists():
        print(f"SKIP: {source_folder} (folder not found)")
        continue

    s3_path = f"s3://{bucket_name}/{s3_prefix}"

    print(f"Uploading {source_folder}/ to {s3_path}...")

    # Run aws s3 sync
    cmd = [
        "aws", "s3", "sync",
        str(source_path),
        s3_path,
        "--exclude", "*.webp",  # Skip WebP files since we have PNG now
        "--region", "us-west-2"
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            # Count files
            upload_output = result.stdout
            print(f"  Success!\n")
            total_success += 1
        else:
            print(f"  ERROR: {result.stderr}\n")
    except Exception as e:
        print(f"  ERROR: {str(e)}\n")

print(f"\n{'='*60}")
print(f"Upload Complete!")
print(f"Successfully uploaded: {total_success} folder(s)")
print(f"Bucket: {bucket_name}")
print(f"\nYou can access files at:")
print(f"  https://{bucket_name}.s3.us-west-2.amazonaws.com/images/...")
print(f"  https://{bucket_name}.s3.us-west-2.amazonaws.com/pdfs/...")
