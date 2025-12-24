#!/usr/bin/env python3
"""
Generate gallery images for Community in Action and Our Impact Stories
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
S3_FOLDER = 'generated_images'

GALLERY_IMAGES = {
    # Community in Action - 3 images
    'community_photos/community_01_diverse_group_smiling': 'Photograph of a diverse group of community members smiling together, showing connection, trust, and solidarity in harm reduction work, warm and inclusive feeling, professional photography',
    'community_photos/community_02_peer_counselor_listening': 'Photo of a peer counselor listening with compassion to a community member, showing empathy and active listening, professional healthcare setting, warm lighting, genuine human connection',
    'community_photos/community_03_elder_and_youth': 'Photo of an elder and youth together in intergenerational healing moment, showing mentorship and cultural transmission, Indigenous community gathering, respectful and dignified',

    # Our Impact Stories - 5 images
    'hero_banners/hero_01_mobile_outreach_vehicle': 'Professional photo of a mobile outreach van/RV in a community, showing HROC mobile services in action, street setting, helping people, compassionate outreach team',
    'hero_banners/hero_02_community_engagement': 'Photo showing community engagement and trust building between HROC staff and community members, outdoor community event, partnership and collaboration',
    'hero_banners/hero_03_peer_support': 'Photo showing peer support in action, two people connecting with care, listening, mutual support, professional yet intimate setting',
    'hero_banners/hero_04_naloxone_training': 'Photo of naloxone training session with diverse community members learning life-saving skills, workshop setting, empowerment and education',
    'hero_banners/hero_05_hands_holding': 'Photo of hands holding together showing solidarity, community support, collective healing, diverse hands, symbolic of unity in harm reduction movement',
}

class GalleryImageGenerator:
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
        """Download image with retry logic"""
        for attempt in range(max_retries):
            try:
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

    def generate_gallery_image(self, filename, prompt):
        """Generate gallery image"""
        try:
            print(f"[IMG] Generating: {filename}")

            result = fal_client.subscribe(
                "fal-ai/nano-banana",
                arguments={
                    "prompt": f"{prompt}",
                    "model": "flux-pro",
                    "image_size": "landscape_16_9",
                    "num_inference_steps": 25,
                },
                with_logs=True,
                on_queue_update=self.log_update,
            )

            if result.get('images') and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                print(f"  [GEN] Generated image URL: {image_url}")

                image_content = self.download_image_with_retry(image_url)
                if image_content:
                    # Upload to S3 as PNG
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

            self.failed.append((filename, "No image or download failed"))
            return None

        except Exception as e:
            print(f"   [ERROR] {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("GALLERY IMAGE GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} images")
        print(f"[ERROR] Failed: {len(self.failed)} images")

        if self.generated:
            print("\nGenerated Images:")
            for filename, url in self.generated:
                print(f"  - {filename}")

        if self.failed:
            print("\nFailed Generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

def main():
    try:
        print("=" * 70)
        print("GENERATE GALLERY IMAGES")
        print("=" * 70)
        print(f"Generating {len(GALLERY_IMAGES)} gallery images...\n")

        generator = GalleryImageGenerator()
        print("[OK] S3 connection configured\n")

        for filename, prompt in GALLERY_IMAGES.items():
            generator.generate_gallery_image(filename, prompt)
            time.sleep(3)  # Delay between requests

        generator.print_summary()
        return 0 if len(generator.failed) == 0 else 1

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
