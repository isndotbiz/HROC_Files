#!/usr/bin/env python3
"""Upload Bri images to S3 bucket."""
import boto3
import os
from pathlib import Path

# AWS credentials from environment variables
# Set these in your .env.local or shell before running
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
BUCKET_NAME = os.environ.get("AWS_S3_BUCKET", "hroc-website-20251230043930")

# Initialize S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Images to upload
images_dir = Path("/Users/jonathanmallinger/Workspace/HROC_Files/HROC_Website_New/images/founders/b")
images = [
    "qwen_bri_01_professional_office_laptop.webp",
    "qwen_bri_02_business_casual_outdoor.webp",
    "qwen_bri_07_modern_office_desk.webp",
    "bri_professional_01_2.webp",
    "bri_set2_professional_10_2.webp",
    "bri_professional_08_2.webp"
]

print("Uploading images to S3...\n")
for image_name in images:
    local_path = images_dir / image_name
    s3_key = f"images/founders/b/{image_name}"

    try:
        print(f"Uploading {image_name}...", end=" ")
        s3_client.upload_file(
            str(local_path),
            BUCKET_NAME,
            s3_key,
            ExtraArgs={
                'ContentType': 'image/webp'
            }
        )
        print("✓")
    except Exception as e:
        print(f"✗ Error: {e}")

print(f"\n✓ Upload complete! Images available at:")
print(f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/images/founders/b/")
