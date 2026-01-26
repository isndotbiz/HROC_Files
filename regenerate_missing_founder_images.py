#!/usr/bin/env python3
"""
Regenerate missing founder images that were deleted from S3
"""
import os
import requests
import time
from pathlib import Path
from PIL import Image
from io import BytesIO

FAL_KEY = os.environ.get('FAL_KEY')

if not FAL_KEY:
    print("❌ FAL_KEY not set!")
    exit(1)

# Create output directories
Path("HROC_Website_New/images/founders/l").mkdir(parents=True, exist_ok=True)
Path("HROC_Website_New/images/founders/j").mkdir(parents=True, exist_ok=True)

missing_images = [
    {
        'prompt': 'professional headshot photo of a woman with long dark hair, warm genuine smile, business professional blazer, natural window lighting, soft neutral background, compassionate approachable expression, direct eye contact, photorealistic, 4k quality',
        'filename': 'HROC_Website_New/images/founders/l/lilly_hero.webp'
    },
    {
        'prompt': 'professional photo of a woman with long dark hair presenting at a whiteboard, engaged expression, business professional attire, bright modern office, natural lighting, teaching moment, photorealistic, high quality',
        'filename': 'HROC_Website_New/images/founders/l/lilly_whiteboard.webp'
    },
    {
        'prompt': 'candid professional photo of a woman with long dark hair in yoga class, peaceful expression, athletic wear, natural light studio setting, wellness atmosphere, mindful pose, photorealistic',
        'filename': 'HROC_Website_New/images/founders/l/lilly_yoga.webp'
    },
    {
        'prompt': 'professional photo of a man with short dark hair and beard working with data analytics, focused expression, laptop and charts visible, modern office setting, business casual attire, natural lighting, photorealistic',
        'filename': 'HROC_Website_New/images/founders/j/jonathan_data.webp'
    }
]

print("🎨 Regenerating Missing Founder Images\n")

for i, config in enumerate(missing_images, 1):
    print(f"[{i}/{len(missing_images)}] Generating: {Path(config['filename']).name}...")

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

            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            img = Image.open(BytesIO(img_response.content))
            img.save(config['filename'], 'WEBP', quality=90)

            print(f"    ✅ Saved: {config['filename']}")
        else:
            print(f"    ❌ No images in response")

        time.sleep(2)

    except Exception as e:
        print(f"    ❌ Error: {e}")

print(f"\n✅ Image regeneration complete!")
