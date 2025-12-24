#!/usr/bin/env python3
"""
Generate optimized service card images with Nano Banana (no text overlay)
Small, clean images - perfect for service cards
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
S3_FOLDER = 'images/generated/service-cards'

SERVICE_CARDS = {
    'service-card-naloxone': 'Clean, professional image of naloxone kit and overdose prevention supplies on white background, minimalist design, no text',
    'service-card-syringe-services': 'Clean syringe exchange supplies and harm reduction kits, organized layout on white background, minimalist, no text',
    'service-card-peer-support': 'Two people connecting with care and support, warm, compassionate moment, professional photography style, white background, no text',
    'service-card-health-navigation': 'Healthcare resources and navigation support visual, clean design with medical elements, white background, no text',
    'service-card-mobile-outreach': 'Mobile outreach van/vehicle, professional street setting, helping community, white background, no text',
    'service-card-education': 'Educational materials, training, workshops setting, learning environment, professional design, white background, no text',
    'service-card-harm-reduction': 'Harm reduction supplies and resources display, organized, professional, white background, no text',
    'service-card-crisis-support': 'Crisis support and emergency assistance visual, compassionate design, support symbols, white background, no text',
    'service-card-wellness': 'Wellness and health check visual, holistic health elements, professional design, white background, no text',
}

class ServiceCardGenerator:
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

    def generate_service_card(self, filename, prompt, max_retries=3):
        """Generate service card image with retry logic"""
        for attempt in range(max_retries):
            try:
                print(f"[IMG] Generating: {filename} (attempt {attempt + 1}/{max_retries})")

                result = fal_client.subscribe(
                    "fal-ai/nano-banana",
                    arguments={
                        "prompt": f"{prompt}. Image size should be square. Professional quality, clean aesthetic.",
                        "model": "flux-pro",
                        "image_size": "square_hd",  # 1024x1024 square for service cards
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
        print("SERVICE CARD GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} service cards")
        print(f"[ERROR] Failed: {len(self.failed)} service cards")

        if self.generated:
            print("\nGenerated Service Cards:")
            for filename, url in self.generated:
                print(f"  - {filename}")
                print(f"    {url}")

        if self.failed:
            print("\nFailed Generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

def main():
    try:
        print("=" * 70)
        print("GENERATE OPTIMIZED SERVICE CARD IMAGES")
        print("=" * 70)
        print(f"Generating {len(SERVICE_CARDS)} service card images...\n")

        generator = ServiceCardGenerator()
        print("[OK] FAL API key detected")
        print("[OK] S3 connection configured\n")

        # Generate all service cards with robust retry
        for filename, prompt in SERVICE_CARDS.items():
            generator.generate_service_card(filename, prompt, max_retries=3)
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
