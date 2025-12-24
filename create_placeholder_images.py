#!/usr/bin/env python3
"""
Create placeholder images for gallery sections
These will be replaced with real FLUX.2 images later
"""

from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# Colors matching HROC brand
MAGENTA = (233, 30, 140)
CYAN = (0, 212, 232)
LIGHT_GRAY = (248, 249, 250)
DARK_GRAY = (51, 51, 51)

OUTPUT_DIRS = {
    'community': 'HROC_Website_New/generated_images/community_photos',
    'hero': 'HROC_Website_New/generated_images/hero_banners',
}

PLACEHOLDER_IMAGES = {
    'community': [
        ('community_16_harm_reduction_dignity', 'Dignity in Action'),
        ('community_17_healing_circles', 'Healing Circles'),
        ('community_18_peer_mentorship', 'Peer Mentorship'),
    ],
    'hero': [
        ('hero_08_community_celebration', 'Community Celebration'),
        ('hero_09_youth_leadership', 'Youth Leadership'),
        ('hero_10_culturally_centered_care', 'Cultural Healing'),
    ],
}

def create_placeholder_image(filename, title, category):
    """Create a gradient placeholder image"""
    # Create image with gradient
    if category == 'hero':
        width, height = 1024, 768
    else:
        width, height = 768, 768
    img = Image.new('RGB', (width, height), color=LIGHT_GRAY)
    draw = ImageDraw.Draw(img)

    # Draw gradient background
    for y in range(img.size[1]):
        r = int(MAGENTA[0] + (255 - MAGENTA[0]) * (y / img.size[1]))
        g = int(MAGENTA[1] + (255 - MAGENTA[1]) * (y / img.size[1]))
        b = int(MAGENTA[2] + (255 - MAGENTA[2]) * (y / img.size[1]))
        draw.rectangle([(0, y), (img.size[0], y+1)], fill=(r, g, b))

    # Draw text
    text_y = img.size[1] // 2 - 20
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        font = ImageFont.load_default()
        font_small = font

    draw.text((img.size[0]//2, text_y), title, fill='white', anchor='mm', font=font)
    draw.text((img.size[0]//2, text_y + 60), f'[PLACEHOLDER - Replace with FLUX.2]',
              fill='white', anchor='mm', font=font_small)

    # Save image
    output_path = f"{OUTPUT_DIRS[category]}/{filename}.png"
    img.save(output_path)
    print(f"[OK] Created placeholder: {output_path}")
    return output_path

def main():
    print("=" * 70)
    print("CREATE PLACEHOLDER IMAGES")
    print("=" * 70 + "\n")

    # Create directories
    for dir_path in OUTPUT_DIRS.values():
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    # Create placeholder images
    for category, images in PLACEHOLDER_IMAGES.items():
        print(f"\n[GEN] Creating {category} placeholders...")
        for filename, title in images:
            create_placeholder_image(filename, title, category)

    print("\n" + "=" * 70)
    print("COMPLETE")
    print("=" * 70)
    print("\nNote: These are placeholder images.")
    print("Replace them with real FLUX.2 images when API key is available:")
    print("  python regenerate_gallery_images.py")
    print("\nUpdate index.html with:")
    print("  - 6 community photos (2x3 grid)")
    print("  - 6 impact story images (2x3 grid)")

if __name__ == "__main__":
    main()
