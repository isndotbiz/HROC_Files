#!/usr/bin/env python3
"""
Create photorealistic images of Alicia using her face from source image
in the same activities as other founders: office work, whiteboard, outdoor, etc.
"""
import os
import requests
import time
import base64
from pathlib import Path
from PIL import Image
from io import BytesIO

FAL_KEY = os.environ.get('FAL_KEY')

if not FAL_KEY:
    print("❌ FAL_KEY not set!")
    exit(1)

# Source image
SOURCE_IMAGE = Path("/mnt/d/1.jpg")
OUTPUT_DIR = Path("HROC_Website_New/images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Creating Photorealistic Images of Alicia\n")
print(f"📸 Source image: {SOURCE_IMAGE}\n")

# Read and encode source image
with open(SOURCE_IMAGE, 'rb') as f:
    source_image_data = base64.b64encode(f.read()).decode('utf-8')

# Activities matching other founders
activities = [
    {
        'name': 'Hero - Professional Headshot',
        'prompt': 'professional corporate headshot, young Indigenous woman in late 20s, warm genuine smile, business professional blazer, natural window lighting, soft neutral background, approachable confident expression, direct eye contact with camera, photorealistic, high quality, 4k',
        'filename': 'alicia_hero_real.webp'
    },
    {
        'name': 'Office Work - At Laptop',
        'prompt': 'professional photo of young Indigenous woman working at laptop, focused engaged expression, modern bright office setting, natural daylight through windows, business professional attire, desk with notebook and coffee, photorealistic, high quality',
        'filename': 'alicia_office_real.webp'
    },
    {
        'name': 'Whiteboard Presentation',
        'prompt': 'professional photo of young Indigenous woman presenting at whiteboard, confident teaching expression, pointing at whiteboard with strategy notes, bright modern office, business professional attire, engaged leadership moment, photorealistic, high quality',
        'filename': 'alicia_whiteboard_real.webp'
    },
    {
        'name': 'Outdoor Professional',
        'prompt': 'candid professional photo of young Indigenous woman outdoors, slight warm smile, natural daylight, soft bokeh background with greenery, business casual blazer, relaxed approachable demeanor, photorealistic, high quality',
        'filename': 'alicia_outdoor_real.webp'
    },
    {
        'name': 'Community Engagement',
        'prompt': 'professional photo of young Indigenous woman at community event, genuine warm smile, interacting with community members, outdoor natural setting, friendly approachable expression, business casual attire, photorealistic, high quality',
        'filename': 'alicia_community_real.webp'
    },
    {
        'name': 'Varied Professional 1',
        'prompt': 'professional headshot of young Indigenous woman, thoughtful confident expression, looking slightly to the left, natural lighting, business professional attire, neutral background, photorealistic, high quality',
        'filename': 'alicia_varied_01.webp'
    }
]

print(f"Generating {len(activities)} photorealistic images using fal.ai image-to-image...\n")

for i, activity in enumerate(activities, 1):
    print(f"[{i}/{len(activities)}] {activity['name']}...")
    print(f"    Generating: {activity['filename']}")

    try:
        # Use fal.ai flux-dev with image reference for more realistic results
        response = requests.post(
            "https://fal.run/fal-ai/flux-lora",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": f"{activity['prompt']}, maintaining consistent facial features and identity",
                "image_url": f"data:image/jpeg;base64,{source_image_data}",
                "strength": 0.75,  # Use source image as strong reference
                "image_size": {
                    "width": 1024,
                    "height": 1280
                },
                "num_inference_steps": 35,
                "guidance_scale": 4.0,
                "num_images": 1,
                "enable_safety_checker": False
            },
            timeout=180
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
            output_path = OUTPUT_DIR / activity['filename']
            img.save(output_path, 'WEBP', quality=95)

            print(f"    ✅ Saved: {activity['filename']}\n")
        else:
            print(f"    ❌ No images in response\n")

        time.sleep(3)  # Rate limiting

    except Exception as e:
        print(f"    ❌ Error: {e}\n")
        # Try with flux-dev instead
        try:
            print("    Retrying with flux-dev...")
            response = requests.post(
                "https://fal.run/fal-ai/flux/dev",
                headers={
                    "Authorization": f"Key {FAL_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "prompt": f"photorealistic portrait photo based on reference, young Indigenous woman in late 20s with long dark hair. Activity: {activity['prompt']}",
                    "image_size": {
                        "width": 1024,
                        "height": 1280
                    },
                    "num_inference_steps": 30,
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
                output_path = OUTPUT_DIR / activity['filename']
                img.save(output_path, 'WEBP', quality=95)

                print(f"    ✅ Saved (fallback): {activity['filename']}\n")
            else:
                print(f"    ❌ Fallback also failed\n")

        except Exception as e2:
            print(f"    ❌ Fallback error: {e2}\n")

        time.sleep(3)

print(f"\n✅ Image generation complete!")
print(f"📁 Images saved to: {OUTPUT_DIR}")
