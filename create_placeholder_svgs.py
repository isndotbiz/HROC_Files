#!/usr/bin/env python3
"""
Create and upload placeholder SVG images for failed infographics
"""

import os
import boto3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# S3 Configuration
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = 'us-west-2'
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_FOLDER = 'images/generated'

# Placeholder SVGs with service-specific colors
PLACEHOLDER_SVGS = {
    'service-wound-care': {
        'color': '#e74c3c',
        'icon': '🩹',
        'title': 'Wound Care'
    },
    'service-health-screening': {
        'color': '#3498db',
        'icon': '🩺',
        'title': 'Health Screening'
    },
    'service-peer-support': {
        'color': '#9b59b6',
        'icon': '🤝',
        'title': 'Peer Support'
    },
    'service-housing-support': {
        'color': '#f39c12',
        'icon': '🏠',
        'title': 'Housing Support'
    },
    'service-cultural-healing': {
        'color': '#16a085',
        'icon': '🌿',
        'title': 'Cultural Healing'
    },
    'service-education-training': {
        'color': '#2980b9',
        'icon': '📚',
        'title': 'Education & Training'
    },
    'service-resource-navigation': {
        'color': '#c0392b',
        'icon': '🌐',
        'title': 'Resource Navigation'
    },
}

def create_placeholder_svg(title, color):
    """Create an SVG placeholder"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color};stop-opacity:0.1" />
            <stop offset="100%" style="stop-color:{color};stop-opacity:0.3" />
        </linearGradient>
    </defs>
    <rect width="1920" height="1080" fill="url(#grad)"/>
    <rect width="1920" height="1080" fill="white" opacity="0.7"/>
    <circle cx="960" cy="540" r="200" fill="{color}" opacity="0.2"/>
    <circle cx="960" cy="540" r="150" fill="{color}" opacity="0.3"/>
    <circle cx="960" cy="540" r="100" fill="{color}" opacity="0.4"/>
    <text x="960" y="480" font-size="120" font-family="Arial, sans-serif" text-anchor="middle" fill="{color}" font-weight="bold">{title}</text>
    <text x="960" y="620" font-size="36" font-family="Arial, sans-serif" text-anchor="middle" fill="#666666">Placeholder Image</text>
</svg>'''
    return svg

def main():
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )

        print("=" * 70)
        print("CREATE PLACEHOLDER SVG IMAGES")
        print("=" * 70)
        print(f"Creating {len(PLACEHOLDER_SVGS)} placeholder SVGs...\n")

        generated = []
        failed = []

        for filename, info in PLACEHOLDER_SVGS.items():
            try:
                print(f"[SVG] Creating: {filename}")
                svg_content = create_placeholder_svg(info['title'], info['color'])

                s3_key = f"{S3_FOLDER}/{filename}.png"
                s3_client.put_object(
                    Bucket=S3_BUCKET,
                    Key=s3_key,
                    Body=svg_content.encode('utf-8'),
                    ContentType='image/svg+xml'
                )

                s3_url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"
                print(f"   [OK] Uploaded to S3: {s3_url}")
                generated.append((filename, s3_url))

            except Exception as e:
                print(f"   [ERROR] {str(e)}")
                failed.append((filename, str(e)))

        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully created: {len(generated)} placeholders")
        print(f"[ERROR] Failed: {len(failed)} placeholders")

        if generated:
            print("\nCreated Placeholders:")
            for filename, url in generated:
                print(f"  - {filename}: {url}")

        if failed:
            print("\nFailed Creations:")
            for filename, error in failed:
                print(f"  - {filename}: {error}")

        return 0 if len(failed) == 0 else 1

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
