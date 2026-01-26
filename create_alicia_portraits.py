#!/usr/bin/env python3
"""
Create portrait-style headshots of Alicia using D:\alicia\2.webp
Normal casual clothing only - NO business suits
"""
import os
import requests
import base64
from PIL import Image
from io import BytesIO
from pathlib import Path

FAL_KEY = os.environ.get('FAL_KEY')
if not FAL_KEY:
    print("❌ FAL_KEY environment variable not set")
    exit(1)

SOURCE_IMAGE = Path("/mnt/d/alicia/2.webp")
OUTPUT_DIR = Path("HROC_Website_New/images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Creating Portrait Headshots of Alicia")
print(f"📸 Source: {SOURCE_IMAGE}\n")

# Load and encode source image
img = Image.open(SOURCE_IMAGE)
buffered = BytesIO()
img.save(buffered, format="PNG")
img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
image_data_uri = f"data:image/png;base64,{img_base64}"

print(f"✅ Source image loaded ({len(img_base64)} chars)\n")

# Portrait variations - ONLY casual/normal clothing
portraits = [
    {
        "filename": "alicia_hero_real.webp",
        "prompt": "Professional portrait headshot of a young Indigenous woman in her late 20s, warm genuine smile, wearing a casual denim button-up shirt, natural window lighting, soft neutral background, direct eye contact, approachable confident expression, photorealistic, 8k, high detail texture, natural skin tones",
        "desc": "1. Main Hero Portrait - Casual denim shirt"
    },
    {
        "filename": "alicia_office_real.webp",
        "prompt": "Portrait of a young Indigenous woman in her late 20s, slight smile, wearing a comfortable sweater, looking slightly to the right, modern office background softly blurred, natural daylight, genuine relaxed expression, photorealistic, detailed facial features, realistic texture",
        "desc": "2. Office Portrait - Cozy sweater, looking right"
    },
    {
        "filename": "alicia_community_real.webp",
        "prompt": "Candid portrait of a young Indigenous woman in her late 20s, bright warm smile, wearing a casual t-shirt with cardigan, outdoor natural setting with soft bokeh, golden hour lighting, approachable demeanor, head and shoulders composition, photorealistic, hyper-realistic skin texture",
        "desc": "3. Community Portrait - Casual t-shirt + cardigan"
    },
    {
        "filename": "alicia_whiteboard_real.webp",
        "prompt": "Professional portrait of a young Indigenous woman in her late 20s, confident expression, wearing a casual chambray or linen button-up, three-quarter view angle, bright office environment, engaged leadership presence, photorealistic, high resolution, detailed texture",
        "desc": "4. Leadership Portrait - Casual button-up, 3/4 view"
    },
    {
        "filename": "alicia_varied_01_real.webp",
        "prompt": "Portrait of a young Indigenous woman in her late 20s, thoughtful gentle smile, wearing a comfortable knit top or casual blouse, slight left profile angle, soft natural lighting, warm tones, genuine authentic expression, photorealistic, 8k quality, realistic hair and skin detail",
        "desc": "5. Profile Portrait - Comfortable knit top, left angle"
    },
    {
        "filename": "alicia_outdoor_real.webp",
        "prompt": "Outdoor portrait of a young Indigenous woman in her late 20s, relaxed smile, wearing a casual hoodie or zip-up jacket, side angle view, natural outdoor setting, soft afternoon light, approachable friendly demeanor, photorealistic, high detail, natural environment",
        "desc": "6. Outdoor Portrait - Casual hoodie/jacket, side view"
    },
]

print(f"Generating {len(portraits)} portrait headshots...")
print("Note: All casual/normal clothing - NO business suits\n")

for i, config in enumerate(portraits, 1):
    print(f"[{i}/{len(portraits)}] {config['desc']}")

    try:
        # Use GPT-Image-1.5 Edit API
        response = requests.post(
            "https://fal.run/fal-ai/gpt-image-1.5/edit",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": config['prompt'],
                "image_urls": [image_data_uri],
                "image_size": "1024x1536",  # Portrait orientation
                "quality": "high",
                "input_fidelity": "high",
                "num_images": 1,
                "output_format": "webp"
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']

            # Download the generated image
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            # Save as WebP
            output_path = OUTPUT_DIR / config['filename']
            with open(output_path, 'wb') as f:
                f.write(img_response.content)

            size_kb = len(img_response.content) / 1024
            print(f"    ✅ Saved: {size_kb:.1f} KB\n")
        else:
            print(f"    ❌ No images in response\n")

    except Exception as e:
        print(f"    ❌ Error: {e}\n")

print(f"\n🎉 Generation complete!")
print(f"📁 {OUTPUT_DIR}")
print(f"\nGenerated {len(portraits)} portrait headshots with casual clothing")
