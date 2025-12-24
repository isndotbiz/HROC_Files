#!/usr/bin/env python3
"""
Generate 9 clean service images (NO TEXT OVERLAYS) for service cards
Professional photos/visuals that work as clean thumbnails
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
S3_FOLDER = 'images/generated/service-clean'

SERVICE_IMAGES = {
    'overdose-prevention': 'Professional clean photo of naloxone kits, overdose prevention supplies arranged professionally, medical aesthetic, white/neutral background, no text, professional photography style',
    'syringe-exchange': 'Professional clean photo of sterile syringes and harm reduction supplies neatly organized, neutral background, no text, medical professional style',
    'wound-care': 'Professional clean photo of wound care supplies, first aid materials, organized layout, white background, no text, healthcare aesthetic',
    'health-screening': 'Professional clean photo of health screening equipment like blood pressure cuff, stethoscope, organized on white background, no text, medical aesthetic',
    'peer-support': 'Warm professional photo of two people connecting in conversation, compassionate moment, neutral background, no text, genuine human connection',
    'housing-support': 'Professional photo representing housing support - could show housing documents, community resources, organized layout, white background, no text',
    'cultural-healing': 'Professional photo of cultural wellness elements - respectful, authentic, could show healing circle setup or cultural items, no text, respectful aesthetic',
    'education-training': 'Professional photo of educational materials - books, training materials, learning setup, neutral background, no text, professional education aesthetic',
    'resource-navigation': 'Professional photo of resource materials - community resources, guides, organized layout, white background, no text, helpful/supportive aesthetic',
}

class CleanServiceImageGenerator:
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

    def generate_image(self, service_name, prompt, max_retries=3):
        """Generate clean service image with retry logic"""
        for attempt in range(max_retries):
            try:
                print(f"[IMG] Generating: {service_name} (attempt {attempt + 1}/{max_retries})")

                result = fal_client.subscribe(
                    "fal-ai/flux-pro",
                    arguments={
                        "prompt": f"{prompt}. High quality, professional photography, clean composition.",
                        "image_size": "landscape_4_3",  # 1024x768 landscape for service cards
                        "num_inference_steps": 30,
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
                        s3_key = f"{S3_FOLDER}/service-{service_name}.png"
                        self.s3_client.put_object(
                            Bucket=S3_BUCKET,
                            Key=s3_key,
                            Body=image_content,
                            ContentType='image/png'
                        )
                        s3_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
                        print(f"   [OK] Uploaded to S3: {s3_url}")
                        self.generated.append((service_name, s3_url))
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

        self.failed.append((service_name, "All retry attempts exhausted"))
        return None

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("CLEAN SERVICE IMAGE GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} images")
        print(f"[ERROR] Failed: {len(self.failed)} images")

        if self.generated:
            print("\nGenerated Service Images:")
            for service_name, url in self.generated:
                print(f"  - service-{service_name}")
                print(f"    {url}")

        if self.failed:
            print("\nFailed Generations:")
            for service_name, error in self.failed:
                print(f"  - service-{service_name}: {error}")

def main():
    try:
        print("=" * 70)
        print("GENERATE CLEAN SERVICE IMAGES (NO TEXT)")
        print("=" * 70)
        print(f"Generating {len(SERVICE_IMAGES)} clean service images...\n")

        generator = CleanServiceImageGenerator()
        print("[OK] FAL API key detected")
        print("[OK] S3 connection configured\n")

        # Generate all images with robust retry
        for service_name, prompt in SERVICE_IMAGES.items():
            generator.generate_image(service_name, prompt, max_retries=3)
            time.sleep(2)  # Delay between requests

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
