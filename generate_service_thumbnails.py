#!/usr/bin/env python3
"""
Generate 9 small service thumbnail images with Nano Banana (NOT infographics)
Clean, simple professional images for service categories on main page
"""

import os
import sys
import time
import requests
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set FAL_KEY from environment
fal_api_key = os.getenv('FAL_API_KEY')
if fal_api_key:
    os.environ['FAL_KEY'] = fal_api_key

# Import fal_client
try:
    import fal_client
except ImportError:
    print("[ERROR] fal-client not installed")
    sys.exit(1)

# S3 Configuration
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = 'us-west-2'
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_FOLDER = 'images/generated/service-thumbnails'

SERVICE_THUMBNAILS = {
    'service-thumb-overdose-prevention': 'Professional photo of naloxone kits and overdose prevention supplies, clean white background, medical aesthetic, square format',
    'service-thumb-syringe-exchange': 'Clean professional image of syringe exchange supplies and harm reduction kits organized on white background',
    'service-thumb-peer-support': 'Compassionate moment of peer support, two people connecting warmly, professional photography, white background',
    'service-thumb-health-screening': 'Medical healthcare resources and health screening visualization, clean professional design on white background',
    'service-thumb-mobile-outreach': 'Mobile outreach van or vehicle providing services in community setting, professional street photography',
    'service-thumb-education-training': 'Educational materials and training workshop setting, learning environment, professional clean design',
    'service-thumb-harm-reduction': 'Harm reduction supplies professionally displayed and organized on white background',
    'service-thumb-crisis-support': 'Crisis support and emergency assistance visual, compassionate and supportive design, professional',
    'service-thumb-cultural-healing': 'Cultural healing and Indigenous wellness visual, respectful and authentic design, professional aesthetic',
}

class ServiceThumbnailGenerator:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        self.generated = []
        self.failed = []

    def log_update(self, update):
        """Log queue updates"""
        if isinstance(update, fal_client.InProgress):
            for log in update.logs:
                print(f"  -> {log['message']}")

    def download_image_with_retry(self, image_url, max_retries=5):
        """Download image with exponential backoff retry"""
        for attempt in range(max_retries):
            try:
                print(f"  [DL] Downloading image (attempt {attempt + 1}/{max_retries})...")
                response = requests.get(image_url, timeout=30)
                if response.status_code == 200:
                    return response.content
                else:
                    print(f"  [DL] HTTP {response.status_code}, retrying...")
            except Exception as e:
                print(f"  [DL] Download failed: {str(e)}")
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"  [DL] Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
        return None

    def generate_thumbnail(self, filename, prompt, max_retries=3):
        """Generate service thumbnail image with retry logic"""
        for attempt in range(max_retries):
            try:
                print(f"[IMG] Generating: {filename} (attempt {attempt + 1}/{max_retries})")

                result = fal_client.subscribe(
                    "fal-ai/nano-banana",
                    arguments={
                        "prompt": f"{prompt}. Square format. Professional quality, clean aesthetic, no text.",
                        "model": "flux-pro",
                        "image_size": "square",  # 512x512 square for thumbnails
                        "num_inference_steps": 25,
                    },
                    with_logs=True,
                    on_queue_update=self.log_update,
                )

                if result.get('images') and len(result['images']) > 0:
                    image_url = result['images'][0]['url']
                    print(f"  [GEN] Generated image URL: {image_url}")

                    # Download with retry
                    image_content = self.download_image_with_retry(image_url)
                    if image_content:
                        # Upload to S3
                        s3_key = f"{S3_FOLDER}/{filename}.png"
                        self.s3_client.put_object(
                            Bucket=S3_BUCKET,
                            Key=s3_key,
                            Body=image_content,
                            ContentType='image/png'
                        )
                        s3_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
                        print(f"   [OK] Uploaded to S3: {s3_url}")
                        self.generated.append((filename, s3_url))
                        return s3_url
                    else:
                        print(f"  [DL] Failed to download image after retries")
                else:
                    print(f"  [GEN] No image returned from FAL")

            except Exception as e:
                print(f"   [ERROR] Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    wait_time = 3 ** attempt
                    print(f"   [RETRY] Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)

        self.failed.append((filename, "All retry attempts exhausted"))
        return None

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("SERVICE THUMBNAIL GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} thumbnails")
        print(f"[ERROR] Failed: {len(self.failed)} thumbnails")

        if self.generated:
            print("\nGenerated Service Thumbnails:")
            for filename, url in self.generated:
                print(f"  - {filename}")
                print(f"    {url}")

        if self.failed:
            print("\nFailed Generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

def main():
    try:
        print("=== " * 20)
        print("GENERATE SERVICE THUMBNAIL IMAGES")
        print("=" * 60)
        print(f"Generating {len(SERVICE_THUMBNAILS)} service thumbnail images...\n")

        generator = ServiceThumbnailGenerator()
        print("[OK] FAL API key detected")
        print("[OK] S3 connection configured\n")

        # Generate all thumbnails with robust retry
        for filename, prompt in SERVICE_THUMBNAILS.items():
            generator.generate_thumbnail(filename, prompt, max_retries=3)
            time.sleep(3)  # Delay between requests

        # Print summary
        generator.print_summary()

        return 0 if len(generator.failed) == 0 else 1

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
