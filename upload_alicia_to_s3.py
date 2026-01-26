#!/usr/bin/env python3
"""Upload Alicia images to S3 bucket."""
import boto3
import os
from pathlib import Path

# AWS credentials from environment variables
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
images_dir = Path("/home/jdmal/workspace/HROC_Files/HROC_Website_New/images/founders/a")
images = [
    "alicia_main.webp",
    "alicia_hero.webp",
    "alicia_whiteboard.webp",
    "alicia_office.webp",
    "alicia_community.webp"
]

print("Uploading Alicia's images to S3...\n")
for image_name in images:
    local_path = images_dir / image_name
    s3_key = f"images/founders/a/{image_name}"

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
print(f"https://{BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/images/founders/a/")
