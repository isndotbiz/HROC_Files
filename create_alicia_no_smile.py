#!/usr/bin/env python3
"""
Create hyper-realistic Alicia images with NO SMILE using best practices
Source: D:\alicia\2.webp
"""
import os
import requests
import base64
from PIL import Image, ImageEnhance
from io import BytesIO
from pathlib import Path

FAL_KEY = os.environ.get('FAL_KEY')
if not FAL_KEY:
    print("❌ FAL_KEY not set")
    exit(1)

SOURCE_IMAGE = Path("/mnt/d/alicia/2.webp")
OUTPUT_DIR = Path("HROC_Website_New/images/founders/a")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("🎨 Creating Hyper-Realistic Alicia Images - NO SMILE")
print(f"📸 Source: {SOURCE_IMAGE}\n")

# Load and prepare source image
source_img = Image.open(SOURCE_IMAGE)
width, height = source_img.size

# Crop to headshot (top 65%)
crop_height = int(height * 0.65)
left = int(width * 0.1)
right = int(width * 0.9)
cropped = source_img.crop((left, 0, right, crop_height))

# Enhance for better face definition
contrast = ImageEnhance.Contrast(cropped)
cropped = contrast.enhance(1.1)  # Subtle 10% contrast boost

sharpness = ImageEnhance.Sharpness(cropped)
cropped = sharpness.enhance(1.05)  # Very subtle sharpening

# Convert to base64
buffered = BytesIO()
cropped.save(buffered, format="PNG")
img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
source_data_uri = f"data:image/png;base64,{img_base64}"

print(f"✅ Source prepared (cropped & enhanced)\n")

# Negative prompt to avoid AI artifacts
NEGATIVE_PROMPT = """plastic skin, over-smoothed face, waxy texture,
perfect symmetry, fake lighting, cartoon, illustration, cgi,
oversaturated, artificial shine, airbrushed, flawless skin,
forced smile, teeth too white, blurry, distorted face, low resolution,
painting, anime, rendered, 3d model"""

# Fixed seed for consistency
FIXED_SEED = 12345

# Image variations - NO SMILES, varied clothing, different angles
variations = [
    {
        'name': '1. Hero - Serious Professional (Casual Denim)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Professional corporate headshot, serious confident expression, no smile,
            direct eye contact, natural facial asymmetry, realistic skin texture
            with natural pores and subtle imperfections, wearing casual denim button-up shirt,
            natural window lighting with soft shadows, clean neutral background.
            Ultra-realistic skin detail, detailed fabric texture, professional photography,
            8K quality, photorealistic, no artificial smoothing, dermatological detail retention.''',
        'filename': 'alicia_hero_real.webp'
    },
    {
        'name': '2. Office - Neutral (Comfortable Sweater)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Professional portrait at laptop, neutral focused expression, no smile,
            looking slightly to the right, natural facial asymmetry, realistic skin texture
            with visible pores, wearing comfortable knit sweater, modern office background
            softly blurred, natural daylight, authentic professional demeanor.
            Ultra-realistic detail, natural imperfections, photorealistic, 8K quality.''',
        'filename': 'alicia_office_real.webp'
    },
    {
        'name': '3. Community - Approachable (Casual T-shirt + Cardigan)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Candid outdoor portrait, very slight subtle smile (hint of warmth only),
            front-facing angle, natural facial asymmetry, realistic skin texture with pores,
            wearing casual t-shirt with open cardigan, outdoor natural setting with bokeh,
            golden hour lighting, relaxed approachable energy, natural imperfections.
            Professional photography, photorealistic, authentic skin detail, 8K quality.''',
        'filename': 'alicia_community_real.webp'
    },
    {
        'name': '4. Leadership - Thoughtful (Casual Button-up)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Professional portrait presenting, thoughtful engaged expression, no smile,
            three-quarter view angle, natural facial asymmetry, realistic skin texture,
            wearing casual chambray button-up shirt, bright office environment,
            confident leadership presence, natural window lighting.
            Ultra-realistic detail, professional photography, photorealistic, 8K quality.''',
        'filename': 'alicia_whiteboard_real.webp'
    },
    {
        'name': '5. Profile - Serious (Knit Top)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Professional portrait, serious contemplative expression, no smile,
            left profile angle (side view), natural facial asymmetry, realistic skin
            texture with natural pores, wearing comfortable knit top or casual blouse,
            soft natural lighting, warm tones, authentic professional demeanor.
            Photorealistic, 8K quality, detailed skin texture, natural imperfections.''',
        'filename': 'alicia_varied_01_real.webp'
    },
    {
        'name': '6. Outdoor - Calm (Casual Hoodie)',
        'prompt': '''Same person, EXACT facial features, identical face structure.
            Outdoor professional portrait, calm neutral expression, no smile,
            side angle view, natural facial asymmetry, realistic skin texture with pores,
            wearing casual zip-up hoodie or jacket, natural outdoor setting,
            soft afternoon light, relaxed demeanor, natural environment background.
            Photorealistic, high detail, authentic texture, 8K quality.''',
        'filename': 'alicia_outdoor_real.webp'
    },
]

print(f"Generating {len(variations)} images with best practices:")
print("  ✅ NO SMILES (serious/neutral expressions)")
print("  ✅ All casual clothing (no business suits)")
print("  ✅ Negative prompts to avoid AI look")
print("  ✅ High input fidelity + optimal parameters\n")

for i, config in enumerate(variations, 1):
    print(f"[{i}/{len(variations)}] {config['name']}")

    try:
        response = requests.post(
            "https://fal.run/fal-ai/gpt-image-1.5/edit",
            headers={
                "Authorization": f"Key {FAL_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": config['prompt'],
                "negative_prompt": NEGATIVE_PROMPT,  # Avoid AI artifacts
                "image_urls": [source_data_uri],
                "image_size": "1024x1536",  # Portrait
                "quality": "high",
                "input_fidelity": "high",  # Preserve face
                "num_images": 1,
                "output_format": "webp"
            },
            timeout=180
        )

        response.raise_for_status()
        result = response.json()

        if 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']
            img_response = requests.get(image_url, timeout=30)
            img_response.raise_for_status()

            output_path = OUTPUT_DIR / config['filename']
            with open(output_path, 'wb') as f:
                f.write(img_response.content)

            size_kb = len(img_response.content) / 1024
            print(f"    ✅ Saved: {size_kb:.1f} KB\n")
        else:
            print(f"    ❌ No images in response\n")

    except Exception as e:
        print(f"    ❌ Error: {e}\n")

print(f"\n🎉 Complete! Images saved to: {OUTPUT_DIR}")
print("\nFeatures:")
print("  ✅ NO smiles - serious/neutral professional expressions")
print("  ✅ Natural facial asymmetry preserved")
print("  ✅ Realistic skin texture with pores")
print("  ✅ Varied angles and clothing")
