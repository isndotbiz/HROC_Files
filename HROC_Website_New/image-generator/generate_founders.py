#!/usr/bin/env python3
"""
Generate professional founder photos using fal.ai
"""
import os
import requests
import time
from pathlib import Path

FAL_KEY = os.environ.get('FAL_KEY')

if not FAL_KEY:
    print("❌ FAL_KEY environment variable not set!")
    exit(1)

# Output directory
OUTPUT_DIR = Path("../images/founders")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Founder configurations - 3 photos each with different angles/expressions
founders = {
    'bri': {
        'name': 'Bri',
        'prompts': [
            'professional headshot photo of an Indigenous woman with glasses, warm genuine smile, business casual blouse, natural window lighting, soft neutral background, approachable confident expression, direct eye contact, photorealistic, 4k quality',
            'candid professional photo of an Indigenous woman with glasses, thoughtful slight smile, looking slightly to the left, outdoor setting with soft bokeh background, natural daylight, genuine relaxed expression, business casual attire, photorealistic',
            'professional portrait of an Indigenous woman with glasses, serious kind expression, hands clasped, solid gray background, direct confident gaze, executive presence, business professional attire, photorealistic, high quality'
        ]
    },
    'lilly': {
        'name': 'Lilly',
        'prompts': [
            'professional headshot photo of a woman with long dark hair, warm genuine smile, business professional blazer, natural lighting, soft neutral background, compassionate approachable expression, direct eye contact, photorealistic, 4k quality',
            'candid professional photo of a woman with long dark hair, thoughtful expression looking slightly to the right, outdoor natural setting with soft background blur, natural daylight, relaxed professional demeanor, business casual attire, photorealistic',
            'professional portrait of a woman with long dark hair, confident warm smile, hands visible, neutral gray background, direct engaging gaze, executive leadership presence, business professional attire, photorealistic, high quality'
        ]
    },
    'jonathan': {
        'name': 'Jonathan',
        'prompts': [
            'professional headshot photo of a man with short dark hair and neat beard, friendly warm smile, business casual button-up shirt, natural window lighting, soft neutral background, approachable professional expression, direct eye contact, photorealistic, 4k quality',
            'candid professional photo of a man with short dark hair and beard, slight smile looking to the left thoughtfully, outdoor setting with natural bokeh, natural daylight, genuine relaxed expression, business casual attire, photorealistic',
            'professional portrait of a man with short dark hair and beard, confident strategic expression, arms crossed professionally, solid gray background, direct purposeful gaze, leadership presence, business professional attire, photorealistic, high quality'
        ]
    }
}

def generate_image(prompt, filename):
    """Generate image using fal.ai flux-dev model (faster and more cost-effective)"""

    url = "https://fal.run/fal-ai/flux/dev"

    headers = {
        "Authorization": f"Key {FAL_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_size": {
            "width": 1024,
            "height": 1280
        },
        "num_inference_steps": 28,
        "guidance_scale": 3.5,
        "num_images": 1,
        "enable_safety_checker": False
    }

    print(f"  Generating: {filename}...")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()

        # flux-dev returns images directly
        images = result.get('images', [])

        if images:
            image_url = images[0].get('url')

            # Download image
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            # Save as WebP
            output_path = OUTPUT_DIR / filename
            with open(output_path, 'wb') as f:
                f.write(img_response.content)

            # Convert to WebP if needed (already should be, but just in case)
            from PIL import Image
            from io import BytesIO

            img = Image.open(BytesIO(img_response.content))
            img.save(output_path, 'WEBP', quality=90)

            print(f"  ✅ Saved: {filename}")
            return True
        else:
            print(f"  ❌ No images in response for {filename}")
            return False

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

# Generate images
print("🎨 Generating Professional Founder Photos\n")

total = 0
success = 0

for founder_key, config in founders.items():
    print(f"📸 {config['name']}:")

    for i, prompt in enumerate(config['prompts'], 1):
        filename = f"{founder_key}_professional_{i:02d}.webp"
        total += 1

        if generate_image(prompt, filename):
            success += 1

        # Rate limiting - be nice to the API
        time.sleep(2)

    print()

print(f"📊 Summary: {success}/{total} images generated successfully")

if success == total:
    print("✅ All images generated!")
else:
    print(f"⚠️  {total - success} images failed")
