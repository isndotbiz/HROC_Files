#!/usr/bin/env python3
"""
Use fal.ai GPT-Image-1.5 Edit API to create professional images of Alicia
using her actual face from /mnt/d/1.jpg in different professional situations.
"""
import os
import requests
import time
from pathlib import Path
from PIL import Image
from io import BytesIO
import base64

FAL_KEY = os.environ.get('FAL_KEY')

if not FAL_KEY:
    print("❌ FAL_KEY not set!")
    exit(1)

# Source image
SOURCE_IMAGE = Path("/mnt/d/1.jpg")
OUTPUT_DIR = Path("HROC_Website_New/images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Creating Professional Images of Alicia using GPT-Image-1.5 Edit\n")
print(f"📸 Source image: {SOURCE_IMAGE}\n")

# Convert source image to base64 data URI
with open(SOURCE_IMAGE, 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data).decode('utf-8')
    source_data_uri = f"data:image/jpeg;base64,{base64_data}"

print(f"✅ Source image encoded ({len(base64_data)} chars)\n")

# Professional situations matching other founders
activities = [
    {
        'name': 'Professional Headshot (Hero)',
        'prompt': 'Same person, professional corporate headshot. Warm genuine smile, business professional blazer, natural window lighting, clean neutral background, confident expression, direct eye contact. High quality professional photography.',
        'filename': 'alicia_hero_real.webp'
    },
    {
        'name': 'Office - Working at Laptop',
        'prompt': 'Same person working at laptop in modern bright office. Focused expression, contemporary workspace, large windows with natural daylight, business professional attire, desk with notebook and coffee. Professional office photography.',
        'filename': 'alicia_office_real.webp'
    },
    {
        'name': 'Whiteboard Presentation',
        'prompt': 'Same person presenting at whiteboard in conference room. Confident teaching expression, pointing at whiteboard with notes, bright office, business blazer, leadership moment. Professional photography.',
        'filename': 'alicia_whiteboard_real.webp'
    },
    {
        'name': 'Outdoor Professional',
        'prompt': 'Same person outdoors, candid professional photo. Slight warm smile, natural daylight, soft bokeh greenery background, business casual blazer, relaxed approachable demeanor. Natural professional photography.',
        'filename': 'alicia_outdoor_real.webp'
    },
    {
        'name': 'Community Engagement',
        'prompt': 'Same person at community event outdoors. Genuine warm smile, natural setting with people blurred in background, friendly expression, business casual attire. Candid community photography.',
        'filename': 'alicia_community_real.webp'
    },
    {
        'name': 'Thoughtful Professional',
        'prompt': 'Same person, professional headshot. Thoughtful confident expression, looking slightly left, natural soft lighting, business professional attire, neutral background. High quality photography.',
        'filename': 'alicia_varied_01_real.webp'
    }
]

print(f"Generating {len(activities)} images using GPT-Image-1.5 Edit API...\n")

for i, activity in enumerate(activities, 1):
    print(f"[{i}/{len(activities)}] {activity['name']}")

    try:
        # Use GPT-Image-1.5 Edit API
        response = requests.post(
            "https://fal.run/fal-ai/gpt-image-1.5/edit",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": activity['prompt'],
                "image_urls": [source_data_uri],  # Data URI works
                "image_size": "auto",
                "quality": "high",
                "input_fidelity": "high",
                "num_images": 1,
                "output_format": "webp"
            },
            timeout=180
        )

        response.raise_for_status()
        result = response.json()

        # Handle the response
        if 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0].get('url')

            # Download
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            # Save
            img = Image.open(BytesIO(img_response.content))
            output_path = OUTPUT_DIR / activity['filename']
            img.save(output_path, 'WEBP', quality=95)

            size = output_path.stat().st_size / 1024
            print(f"    ✅ Saved: {activity['filename']} ({size:.1f} KB)\n")

        else:
            print(f"    ❌ No images in response\n")

        time.sleep(4)

    except Exception as e:
        print(f"    ❌ Error: {str(e)[:200]}\n")
        time.sleep(4)

print(f"\n✅ Image generation complete!")
print(f"📁 Output: {OUTPUT_DIR}")
