#!/usr/bin/env python3
"""
HROC Website Complete Image Regeneration with FLUX 2
Generates all site images: service icons, founder photos, community photos, infographics
Automatically optimizes to WebP+PNG and uploads to S3
"""

import os
import sys
import json
import time
import base64
from pathlib import Path
from dotenv import load_dotenv
import fal_client
from PIL import Image
import io

# Load environment variables
load_dotenv()

FAL_API_KEY = os.getenv('FAL_API_KEY')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')

# Set FAL API key
if FAL_API_KEY:
    os.environ['FAL_KEY'] = FAL_API_KEY

# Directories
BASE_DIR = Path(__file__).parent / 'HROC_Website_New'
IMAGES_DIR = BASE_DIR / 'images' / 'generated'
GENERATED_DIR = BASE_DIR / 'generated_images'
SERVICE_ICONS_DIR = GENERATED_DIR / 'service_icons'
COMMUNITY_PHOTOS_DIR = GENERATED_DIR / 'community_photos'
HERO_BANNERS_DIR = GENERATED_DIR / 'hero_banners'
INFORMATIONAL_DIR = GENERATED_DIR / 'informational_graphics'
FOUNDERS_DIR = BASE_DIR / 'images' / 'founders'

# Create directories
for dir_path in [IMAGES_DIR, SERVICE_ICONS_DIR, COMMUNITY_PHOTOS_DIR, HERO_BANNERS_DIR, INFORMATIONAL_DIR, FOUNDERS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Image generation prompts
PROMPTS = {
    # Service Icons - Clean, professional, healthcare-focused
    "service_icons": {
        "icon_01_naloxone_kit.png": "Professional healthcare icon of naloxone kit, life-saving medication, bright clear background, medical illustration style, high quality, transparent background effect, icon design",
        "icon_02_syringe_exchange.png": "Healthcare service icon for sterile syringe exchange program, safe injection supplies, medical illustration, professional design, clean background",
        "icon_03_peer_support.png": "Icon representing peer support, two hands connected, community, empathy, healthcare illustration, professional medical icon style",
        "icon_04_healthcare_navigation.png": "Healthcare navigation icon, person with medical professional, guidance, community health icon, professional illustration",
        "icon_05_mobile_outreach.png": "Mobile RV outreach vehicle icon, mobile healthcare services, street outreach, professional medical illustration",
        "icon_06_education_training.png": "Education and training icon, knowledge sharing, workshops, professional healthcare education illustration",
        "icon_07_harm_reduction_supplies.png": "Harm reduction supplies icon, protective equipment, health safety, professional medical icon",
        "icon_08_crisis_support.png": "Crisis support icon, emergency help, mental health support, professional healthcare illustration",
        "icon_09_cultural_competency.png": "Indigenous healing and cultural competency icon, traditional knowledge, community wellness, cultural symbol",
        "icon_10_community_resources.png": "Community resources icon, networks, support systems, professional community health illustration",
        "icon_11_safe_space.png": "Safe space icon, welcoming environment, community sanctuary, professional healthcare illustration",
        "icon_12_wellness_check.png": "Wellness check icon, health monitoring, preventive care, professional medical illustration",
    },

    # Founder Photos - Professional headshots
    "founders": {
        "b_fluxmulti_01.png": "Professional headshot photograph of Indigenous woman, Bri, Secretary of healing harm reduction collective, confident expression, warm lighting, studio background, professional photo, compassionate eyes, community leader",
        "l1.png": "Professional headshot photograph of Indigenous woman, Lilly, Treasurer, traditional cultural background elements, warm studio lighting, professional photo, strong presence, community leader appearance",
        "j_fluxmulti_01.png": "Professional headshot photograph of Indigenous man, Jonathan, Chairman of healing collective, confident serious expression, warm lighting, studio background, professional photo, leadership presence",
    },

    # Community Impact Photos - Real-world scenarios
    "community_photos": {
        "community_01_diverse_group_smiling.png": "Diverse community members smiling together outdoors, harm reduction outreach, street engagement, warm community connection, documentary style photo",
        "community_02_peer_counselor_listening.png": "Peer counselor listening with compassion to community member, active listening, support, empathy, healthcare worker, documentary style photography",
        "community_03_elder_and_youth.png": "Indigenous elder and youth together in intergenerational healing, cultural teaching, community care, documentary style photo, warm lighting",
        "community_04_volunteers_organizing.png": "Team of volunteers organizing supplies and resources, community action, teamwork, harm reduction service setup",
        "community_05_person_receiving_naloxone.png": "Community member receiving naloxone training, health education, street outreach, mobile healthcare service",
        "community_06_group_training_session.png": "Group training session on harm reduction, overdose prevention, community education workshop, street engagement",
        "community_07_mobile_unit_service.png": "Mobile RV healthcare unit providing outreach services, street-level engagement, mobile harm reduction",
        "community_08_safe_space_interior.png": "Welcoming safe space interior for community members, healing environment, supportive atmosphere, community center",
        "community_09_person_hope_expression.png": "Community member expressing hope and healing, recovery journey, wellness, positive mental state, documentary portrait",
        "community_10_hands_distributing_supplies.png": "Hands distributing harm reduction supplies, syringe exchange, naloxone kits, direct service, community care",
        "community_11_street_outreach_team.png": "Street outreach team providing services in community, mobile healthcare, street-level engagement, neighborhood",
        "community_12_cultural_healing_circle.png": "Indigenous cultural healing circle gathering, community wellness, traditional practices, spiritual care, gathering",
    },

    # Hero Banners - Large impactful images
    "hero_banners": {
        "hero_01_mobile_outreach_vehicle.png": "Professional photograph of mobile RV healthcare outreach vehicle in urban community setting, helping people, street engagement, bright daylight",
        "hero_02_community_engagement.png": "Community members engaging with harm reduction workers, street outreach, trust building, compassionate healthcare interaction, warm lighting",
    },

    # Impact Infographics
    "informational_graphics": {
        "impact_infographic_v1.png": "Infographic showing harm reduction impact: naloxone distributions, lives saved, community members served, statistics, visual data design, professional layout",
        "engagement_infographic_v1.png": "Community engagement infographic featuring three founders: Bri (Secretary), Lilly (Treasurer), Jonathan (Chairman), organizational structure, leadership",
    },
}

def generate_image_with_flux2(prompt, output_path, image_size="landscape_4_3"):
    """Generate image using FLUX 2 via FAL"""
    try:
        print(f"  Generating: {output_path.name}")
        print(f"  Prompt: {prompt[:80]}...")

        result = fal_client.subscribe(
            "fal-ai/flux-2",
            arguments={
                "prompt": prompt,
                "image_size": image_size,
                "num_inference_steps": 28,
                "guidance_scale": 2.5,
                "output_format": "png",
            },
        )

        if result and 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']

            # Download and save image
            import urllib.request
            urllib.request.urlretrieve(image_url, str(output_path))
            print(f"  ✓ Saved: {output_path.name}")
            return True
        else:
            print(f"  ✗ Failed to generate image")
            return False

    except Exception as e:
        print(f"  ✗ Error generating {output_path.name}: {str(e)}")
        return False

def optimize_image_to_webp(png_path):
    """Convert PNG to WebP and optimize"""
    try:
        webp_path = png_path.with_suffix('.webp')

        # Open PNG and convert to WebP
        with Image.open(png_path) as img:
            # Convert RGBA to RGB if needed (WebP support)
            if img.mode == 'RGBA':
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background

            # Save as WebP with quality optimization
            img.save(webp_path, 'WEBP', quality=85, method=6)

        print(f"  ✓ WebP optimized: {webp_path.name}")
        return True
    except Exception as e:
        print(f"  ✗ Failed to optimize {png_path.name}: {str(e)}")
        return False

def main():
    print("=" * 60)
    print("🎨 HROC Website - FLUX 2 Image Regeneration")
    print("=" * 60)
    print()

    if not FAL_API_KEY:
        print("❌ FAL_API_KEY not found in .env file")
        sys.exit(1)

    total_images = 0
    generated_images = 0

    # Generate all image categories
    for category, images in PROMPTS.items():
        print(f"\n📁 {category.upper()}")
        print("-" * 60)

        if category == "service_icons":
            output_dir = SERVICE_ICONS_DIR
        elif category == "founders":
            output_dir = FOUNDERS_DIR / 'b' if 'b_' in list(images.keys())[0] else FOUNDERS_DIR / 'l' if 'l' in list(images.keys())[0] else FOUNDERS_DIR / 'j'
        elif category == "community_photos":
            output_dir = COMMUNITY_PHOTOS_DIR
        elif category == "hero_banners":
            output_dir = HERO_BANNERS_DIR
        elif category == "informational_graphics":
            output_dir = INFORMATIONAL_DIR

        output_dir.mkdir(parents=True, exist_ok=True)

        for filename, prompt in images.items():
            total_images += 1

            # Determine correct subdirectory for founders
            if category == "founders":
                if filename.startswith('b_'):
                    output_dir = FOUNDERS_DIR / 'b'
                elif filename.startswith('l'):
                    output_dir = FOUNDERS_DIR / 'l'
                elif filename.startswith('j_'):
                    output_dir = FOUNDERS_DIR / 'j'
                output_dir.mkdir(parents=True, exist_ok=True)

            output_path = output_dir / filename

            # Generate image
            if generate_image_with_flux2(prompt, output_path):
                generated_images += 1

                # Optimize to WebP
                optimize_image_to_webp(output_path)

                # Small delay to avoid rate limiting
                time.sleep(2)
            else:
                print(f"  ⚠ Skipping WebP optimization for {filename}")

    print("\n" + "=" * 60)
    print(f"✅ Generation Complete: {generated_images}/{total_images} images generated")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Run: python compress_and_optimize_images.py")
    print("  2. Run: python upload_to_s3.py")
    print("  3. Deploy updated HTML to live server")
    print()

if __name__ == "__main__":
    main()
