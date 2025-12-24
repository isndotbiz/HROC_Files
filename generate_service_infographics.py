#!/usr/bin/env python3
"""
Generate service card infographics with Nano Banana and upload to S3
"""

import os
import sys
import time
import requests
import boto3
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set FAL_KEY from environment for fal_client
fal_api_key = os.getenv('FAL_API_KEY')
if fal_api_key:
    os.environ['FAL_KEY'] = fal_api_key

# Try to import fal_client
try:
    import fal_client
except ImportError:
    print("[ERROR] fal-client not installed. Running: pip install fal-client")
    os.system("pip install fal-client")
    import fal_client

# S3 Configuration
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = 'us-west-2'
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_FOLDER = 'images/generated'

SERVICE_INFOGRAPHICS = {
    'service-overdose-prevention': 'Professional infographic showing Naloxone (Narcan) kit, fentanyl test strips, and overdose prevention statistics with bright colors and clear text, medical safety theme',
    'service-syringe-exchange': 'Clean infographic of sterile syringe exchange service showing disease prevention and harm reduction, professional healthcare design',
    'service-wound-care': 'Medical wound care infographic showing first aid supplies and professional care with healthcare worker, compassionate design',
    'service-health-screening': 'Healthcare screening infographic featuring blood pressure, glucose testing, and HIV/HCV resources with professional medical design',
    'service-peer-support': 'Peer support infographic showing diverse community members connecting with compassion, emotional support theme, warm colors',
    'service-housing-support': 'Housing and ID support infographic showing shelter, housing navigation, and community resources with hopeful design',
    'service-cultural-healing': 'Indigenous-informed cultural healing infographic with traditional symbols, healing circles, and ceremonial elements',
    'service-education-training': 'Educational training infographic showing naloxone training, workshops, and community education with learning symbols',
    'service-resource-navigation': 'Resource navigation infographic showing connection to food banks, legal aid, employment, benefits with interconnected network design',
}

class InfographicGenerator:
    def __init__(self):
        self.fal_key = os.getenv('FAL_API_KEY')
        if not self.fal_key:
            raise ValueError('FAL_API_KEY environment variable not set')

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

    def generate_infographic(self, filename, prompt):
        """Generate infographic with Nano Banana"""
        try:
            print(f"[IMG] Generating: {filename}")

            result = fal_client.subscribe(
                "fal-ai/nano-banana",
                arguments={
                    "prompt": f"Create a professional, clean infographic: {prompt}",
                    "model": "flux-pro",
                    "image_size": "landscape_16_9",
                    "num_inference_steps": 20,
                },
                with_logs=True,
                on_queue_update=self.log_update,
            )

            if result.get('images') and len(result['images']) > 0:
                image_url = result['images'][0]['url']

                # Download image
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Upload directly to S3
                    s3_key = f"{S3_FOLDER}/{filename}.png"
                    self.s3_client.put_object(
                        Bucket=S3_BUCKET,
                        Key=s3_key,
                        Body=response.content,
                        ContentType='image/png'
                    )
                    s3_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
                    print(f"   [OK] Uploaded to S3: {s3_url}")
                    self.generated.append((filename, s3_url))
                    return s3_url

            self.failed.append((filename, "No image returned"))
            return None

        except Exception as e:
            print(f"   [ERROR] {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} infographics")
        print(f"[ERROR] Failed: {len(self.failed)} infographics")

        if self.generated:
            print("\nGenerated Infographics:")
            for filename, url in self.generated:
                print(f"  - {filename}")
                print(f"    {url}")

        if self.failed:
            print("\nFailed Generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

        print("\nNext: Update index.html image URLs to point to S3 URLs above")

def main():
    try:
        print("=" * 70)
        print("GENERATE SERVICE INFOGRAPHICS WITH NANO BANANA")
        print("=" * 70)
        print(f"Generating {len(SERVICE_INFOGRAPHICS)} service infographics...\n")

        generator = InfographicGenerator()
        print("[OK] FAL API key detected")
        print("[OK] S3 connection configured\n")

        # Generate all infographics
        for filename, prompt in SERVICE_INFOGRAPHICS.items():
            generator.generate_infographic(filename, prompt)
            time.sleep(1)  # Rate limiting

        # Print summary
        generator.print_summary()

        return 0 if len(generator.failed) == 0 else 1

    except ValueError as e:
        print(f"[ERROR] {e}")
        print("\nSetup instructions:")
        print("  1. Create .env file with:")
        print("     FAL_API_KEY=your_key")
        print("     AWS_ACCESS_KEY_ID=your_key")
        print("     AWS_SECRET_ACCESS_KEY=your_key")
        return 1
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
