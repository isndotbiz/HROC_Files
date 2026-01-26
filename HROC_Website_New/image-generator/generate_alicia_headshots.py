#!/usr/bin/env python3
"""
Generate professional headshots for Alicia using OpenAI image editing and fal.ai
Source image: /mnt/d/1.jpg
"""
import os
import requests
import time
from pathlib import Path
from PIL import Image
import base64
from io import BytesIO

# API Keys from environment (set via 1Password CLI)
FAL_KEY = os.environ.get('FAL_KEY')
OPENAI_KEY = os.environ.get('OPENAI_KEY')

if not FAL_KEY or not OPENAI_KEY:
    print("❌ API keys not set!")
    print("Run: export FAL_KEY=$(op read 'op://TrueNAS Infrastructure/FAL API Key/credential')")
    print("Run: export OPENAI_KEY=$(op read 'op://TrueNAS Infrastructure/OpenAI API Key/credential')")
    exit(1)

# Paths
SOURCE_IMAGE = Path("/mnt/d/1.jpg")
OUTPUT_DIR = Path("../images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Generating Professional Headshots for Alicia\n")
print(f"📸 Source image: {SOURCE_IMAGE}")
print(f"📁 Output directory: {OUTPUT_DIR}\n")

# Verify source image exists
if not SOURCE_IMAGE.exists():
    print(f"❌ Source image not found: {SOURCE_IMAGE}")
    exit(1)

# Convert source to PNG for OpenAI (required format)
source_img = Image.open(SOURCE_IMAGE)
source_png = BytesIO()
source_img.save(source_png, format='PNG')
source_png.seek(0)

# Generate variations using OpenAI image editing/variations
print("🖼️  Using OpenAI to create image variations at different angles...\n")

openai_variations = [
    {
        'prompt': 'Professional headshot of a young Indigenous woman in her late 20s with warm smile, looking directly at camera, business professional attire, natural lighting, office background',
        'filename': 'alicia_openai_01_direct.webp'
    },
    {
        'prompt': 'Professional headshot of a young Indigenous woman in her late 20s, slight angle to the left, thoughtful expression, business casual attire, soft natural lighting, neutral background',
        'filename': 'alicia_openai_02_left.webp'
    },
    {
        'prompt': 'Professional headshot of a young Indigenous woman in her late 20s, slight angle to the right, confident smile, business professional blazer, natural daylight, clean background',
        'filename': 'alicia_openai_03_right.webp'
    }
]

for i, config in enumerate(openai_variations, 1):
    print(f"  [{i}/3] Generating: {config['filename']}...")

    try:
        # Use DALL-E 3 for image generation based on reference
        response = requests.post(
            'https://api.openai.com/v1/images/generations',
            headers={
                'Authorization': f'Bearer {OPENAI_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'dall-e-3',
                'prompt': config['prompt'],
                'n': 1,
                'size': '1024x1792',  # Portrait orientation
                'quality': 'hd',
                'style': 'natural'
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        image_url = result['data'][0]['url']

        # Download and convert to WebP
        img_response = requests.get(image_url, timeout=30)
        img_response.raise_for_status()

        img = Image.open(BytesIO(img_response.content))
        output_path = OUTPUT_DIR / config['filename']
        img.save(output_path, 'WEBP', quality=90)

        print(f"      ✅ Saved: {config['filename']}")
        time.sleep(2)  # Rate limiting

    except Exception as e:
        print(f"      ❌ Error: {e}")

# Generate additional professional headshots using fal.ai
print("\n🎨 Using fal.ai to create additional professional headshots...\n")

fal_prompts = [
    {
        'prompt': 'professional corporate headshot photo of a young Indigenous woman in her late 20s, warm genuine smile, business professional blazer, natural window lighting, soft neutral background, approachable confident expression, direct eye contact, photorealistic, 4k quality',
        'filename': 'alicia_main.webp'
    },
    {
        'prompt': 'candid professional photo of a young Indigenous woman in her late 20s, thoughtful slight smile, looking slightly to the left, outdoor setting with soft bokeh background, natural daylight, genuine relaxed expression, business casual attire, photorealistic',
        'filename': 'alicia_hero.webp'
    },
    {
        'prompt': 'professional portrait of a young Indigenous woman in her late 20s, confident warm expression, presenting at whiteboard, bright office environment, engaged leadership presence, business casual attire, photorealistic, high quality',
        'filename': 'alicia_whiteboard.webp'
    },
    {
        'prompt': 'professional photo of a young Indigenous woman in her late 20s working at laptop, focused expression, modern office setting, natural lighting through windows, business professional attire, photorealistic',
        'filename': 'alicia_office.webp'
    },
    {
        'prompt': 'candid professional photo of a young Indigenous woman in her late 20s at community event, genuine warm smile, interacting with community members, outdoor natural setting, approachable demeanor, business casual attire, photorealistic',
        'filename': 'alicia_community.webp'
    }
]

for i, config in enumerate(fal_prompts, 1):
    print(f"  [{i}/{len(fal_prompts)}] Generating: {config['filename']}...")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/flux/dev",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": config['prompt'],
                "image_size": {
                    "width": 1024,
                    "height": 1280
                },
                "num_inference_steps": 28,
                "guidance_scale": 3.5,
                "num_images": 1,
                "enable_safety_checker": False
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        images = result.get('images', [])
        if images:
            image_url = images[0].get('url')

            # Download and save as WebP
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            img = Image.open(BytesIO(img_response.content))
            output_path = OUTPUT_DIR / config['filename']
            img.save(output_path, 'WEBP', quality=90)

            print(f"      ✅ Saved: {config['filename']}")
        else:
            print(f"      ❌ No images in response")

        time.sleep(2)  # Rate limiting

    except Exception as e:
        print(f"      ❌ Error: {e}")

print(f"\n✅ Image generation complete!")
print(f"📁 Images saved to: {OUTPUT_DIR}")
print(f"\nNext steps:")
print(f"  1. Review images in {OUTPUT_DIR}")
print(f"  2. Upload to S3 bucket")
print(f"  3. Create alicia.html page")
print(f"  4. Add Alicia to index.html founders section")
