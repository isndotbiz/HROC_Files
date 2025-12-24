#!/usr/bin/env python3
"""
Upload generated images to AWS S3 bucket
"""

import os
import sys
from pathlib import Path
import boto3
from botocore.exceptions import ClientError

# Configuration
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_REGION = 'us-west-2'
LOCAL_IMAGES_DIR = 'HROC_Website_New/generated_images'

def upload_images_to_s3():
    """Upload all generated images to S3 bucket"""

    # Initialize S3 client
    try:
        s3_client = boto3.client('s3', region_name=S3_REGION)
    except Exception as e:
        print(f"ERROR: Could not initialize S3 client: {str(e)}")
        print("Please ensure AWS credentials are configured (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)")
        sys.exit(1)

    # Find all generated images
    images_dir = Path(LOCAL_IMAGES_DIR)
    if not images_dir.exists():
        print(f"ERROR: Generated images directory not found: {LOCAL_IMAGES_DIR}")
        sys.exit(1)

    image_files = list(images_dir.rglob('*.png')) + list(images_dir.rglob('*.jpg'))

    if not image_files:
        print(f"ERROR: No images found in {LOCAL_IMAGES_DIR}")
        sys.exit(1)

    print(f"\nFound {len(image_files)} images to upload to S3")
    print("="*60)

    uploaded_count = 0
    failed_count = 0

    for image_path in sorted(image_files):
        relative_path = image_path.relative_to('HROC_Website_New')
        s3_key = f"images/{relative_path}".replace("\\", "/")

        try:
            print(f"Uploading: {s3_key}")

            # Determine content type
            content_type = 'image/png' if image_path.suffix.lower() == '.png' else 'image/jpeg'

            # Upload with public read access
            s3_client.upload_file(
                str(image_path),
                S3_BUCKET,
                s3_key,
                ExtraArgs={
                    'ContentType': content_type,
                    'ACL': 'public-read',
                    'CacheControl': 'max-age=31536000'  # Cache for 1 year
                }
            )

            url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{s3_key}"
            print(f"  ✓ Uploaded to: {url}")
            uploaded_count += 1

        except ClientError as e:
            print(f"  ✗ Upload failed: {str(e)}")
            failed_count += 1
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")
            failed_count += 1

    print("\n" + "="*60)
    print("Upload Summary")
    print("="*60)
    print(f"Successfully Uploaded: {uploaded_count}")
    print(f"Failed: {failed_count}")
    print(f"Total: {uploaded_count + failed_count}")
    print("="*60)

    if failed_count > 0:
        print("\nNote: Check your AWS credentials and S3 bucket permissions")
        return False

    return True

if __name__ == "__main__":
    print("\n" + "="*60)
    print("Upload Generated Images to S3")
    print("="*60)

    if upload_images_to_s3():
        print("\n✓ Images uploaded successfully!")
        print("Next: Run update_html_images.py to update image references in HTML")
    else:
        print("\n✗ Some images failed to upload")
        sys.exit(1)
