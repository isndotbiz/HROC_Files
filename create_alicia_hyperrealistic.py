#!/usr/bin/env python3
"""
Create hyper-realistic professional images of Alicia using GPT-Image-1.5 Edit
Source: D:\1.webp (cropped to headshot format)
Varied clothing, different angles, high texture detail
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
SOURCE_IMAGE = Path("/mnt/d/1.webp")
OUTPUT_DIR = Path("HROC_Website_New/images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Creating Hyper-Realistic Professional Images of Alicia\n")
print(f"📸 Source: {SOURCE_IMAGE}\n")

# Crop source image to headshot format (similar to other founders)
print("✂️  Cropping source to headshot format...")
source_img = Image.open(SOURCE_IMAGE)
width, height = source_img.size

# Crop to upper portion for headshot (top 60% with centered crop)
crop_height = int(height * 0.65)
# Center crop horizontally
left = int(width * 0.1)
right = int(width * 0.9)
cropped = source_img.crop((left, 0, right, crop_height))

# Save cropped version
cropped_path = Path("/tmp/alicia_cropped.webp")
cropped.save(cropped_path, 'WEBP', quality=95)
print(f"✅ Cropped to {cropped.size[0]}x{cropped.size[1]}\n")

# Convert to base64 data URI
with open(cropped_path, 'rb') as f:
    image_data = f.read()
    base64_data = base64.b64encode(image_data).decode('utf-8')
    source_data_uri = f"data:image/webp;base64,{base64_data}"

# Varied professional situations - ONLY 1 BUSINESS SUIT
# Matching variety seen in other founders (casual, outdoor, yoga, etc.)
activities = [
    {
        'name': '1. Professional Headshot - BUSINESS SUIT',
        'prompt': 'Same person, hyper-realistic professional corporate headshot. Warm genuine smile, wearing sharp business suit with professional blazer, natural window lighting with soft shadows, clean neutral background, confident approachable expression, direct eye contact. Ultra-realistic skin texture, detailed fabric texture, professional photography, 8K quality, photorealistic.',
        'filename': 'alicia_hero_real.webp'
    },
    {
        'name': '2. Office Casual - Looking Right',
        'prompt': 'Same person in modern office, looking slightly to the right. Casual professional attire (blouse, no jacket), working at laptop, focused thoughtful expression, bright office with windows, natural daylight, desk with plants. Hyper-realistic skin texture, detailed fabric, sharp focus, 8K photorealistic.',
        'filename': 'alicia_office_real.webp'
    },
    {
        'name': '3. Outdoor Casual - Side Angle',
        'prompt': 'Same person outdoors at 45-degree angle, looking to the left. Wearing casual comfortable clothing (sweater or cardigan), warm natural smile, golden hour lighting, soft bokeh background with trees and greenery, relaxed demeanor. Hyper-realistic skin texture, natural hair detail, photorealistic outdoor photography.',
        'filename': 'alicia_outdoor_real.webp'
    },
    {
        'name': '4. Community Casual - Front Angle',
        'prompt': 'Same person at community gathering, facing camera. Wearing casual everyday clothing (t-shirt or casual top), genuine warm smile, outdoor natural setting, soft focus people in background, friendly approachable energy. Hyper-realistic texture, natural lighting, candid photorealistic style.',
        'filename': 'alicia_community_real.webp'
    },
    {
        'name': '5. Business Casual - Three-Quarter View',
        'prompt': 'Same person in business casual attire (nice blouse, cardigan), three-quarter view looking over shoulder. Confident warm expression, standing near whiteboard or in meeting room, bright modern space, professional but approachable. Hyper-realistic facial detail, fabric texture, photorealistic.',
        'filename': 'alicia_whiteboard_real.webp'
    },
    {
        'name': '6. Casual Professional - Left Profile',
        'prompt': 'Same person in profile view (left side), wearing casual professional clothing. Thoughtful serene expression, natural soft lighting, neutral background, elegant simple style. Hyper-realistic skin detail, natural hair texture, high-end portrait photography, photorealistic.',
        'filename': 'alicia_varied_01_real.webp'
    }
]

print(f"Generating {len(activities)} hyper-realistic images...\n")
print("Note: Only 1 business suit, rest are casual/business casual\n")

for i, activity in enumerate(activities, 1):
    print(f"[{i}/{len(activities)}] {activity['name']}")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/gpt-image-1.5/edit",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": activity['prompt'],
                "image_urls": [source_data_uri],
                "image_size": "1024x1536",  # Portrait orientation like other founders
                "quality": "high",
                "input_fidelity": "high",  # Preserve actual face
                "num_images": 1,
                "output_format": "webp"
            },
            timeout=180
        )

        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0].get('url')

            # Download
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            # Save as high quality WebP
            img = Image.open(BytesIO(img_response.content))
            output_path = OUTPUT_DIR / activity['filename']
            img.save(output_path, 'WEBP', quality=98)  # Higher quality for realism

            size = output_path.stat().st_size / 1024
            print(f"    ✅ Saved: {size:.1f} KB\n")
        else:
            print(f"    ❌ Failed\n")

        time.sleep(5)  # Longer delay for high quality generation

    except Exception as e:
        print(f"    ❌ Error: {str(e)[:150]}\n")
        time.sleep(5)

print(f"\n🎉 Generation complete!")
print(f"📁 {OUTPUT_DIR}\n")

print("Summary:")
for activity in activities:
    filepath = OUTPUT_DIR / activity['filename']
    if filepath.exists():
        size = filepath.stat().st_size / 1024
        print(f"  ✓ {activity['filename']} ({size:.1f} KB)")
