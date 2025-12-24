#!/usr/bin/env python3
"""
HROC Website Image Regeneration with FLUX 2
Uses direct HTTP API calls instead of fal_client library
"""

import os
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

FAL_API_KEY = os.getenv('FAL_API_KEY')

if not FAL_API_KEY:
    print("❌ FAL_API_KEY not found in .env file")
    exit(1)

# Directories
BASE_DIR = Path(__file__).parent / 'HROC_Website_New'
IMAGES_DIR = BASE_DIR / 'images' / 'generated'
GENERATED_DIR = BASE_DIR / 'generated_images'
SERVICE_ICONS_DIR = GENERATED_DIR / 'service_icons'
COMMUNITY_PHOTOS_DIR = GENERATED_DIR / 'community_photos'
HERO_BANNERS_DIR = GENERATED_DIR / 'hero_banners'
INFORMATIONAL_DIR = GENERATED_DIR / 'informational_graphics'
FOUNDERS_B_DIR = BASE_DIR / 'images' / 'founders' / 'b'
FOUNDERS_L_DIR = BASE_DIR / 'images' / 'founders' / 'l'
FOUNDERS_J_DIR = BASE_DIR / 'images' / 'founders' / 'j'

# Create directories
for dir_path in [SERVICE_ICONS_DIR, COMMUNITY_PHOTOS_DIR, HERO_BANNERS_DIR, INFORMATIONAL_DIR, FOUNDERS_B_DIR, FOUNDERS_L_DIR, FOUNDERS_J_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Prompts for each image category
IMAGE_PROMPTS = {
    # Service Icons
    (SERVICE_ICONS_DIR, "icon_01_naloxone_kit.png"): "Professional clean icon of naloxone kit and syringe, life-saving medication, white background, medical illustration style, bright colors, healthcare icon",
    (SERVICE_ICONS_DIR, "icon_02_syringe_exchange.png"): "Professional icon of sterile syringes and exchange services, healthcare icon style, clean design, medical illustration, blue and white colors",
    (SERVICE_ICONS_DIR, "icon_03_peer_support.png"): "Icon of two hands connecting or supporting each other, peer support and community care, empathy, professional healthcare icon",
    (SERVICE_ICONS_DIR, "icon_04_healthcare_navigation.png"): "Healthcare navigation icon showing person with medical professional, guidance, professional healthcare illustration",
    (SERVICE_ICONS_DIR, "icon_05_mobile_outreach.png"): "Icon of mobile RV outreach vehicle providing healthcare, street outreach, professional medical icon",
    (SERVICE_ICONS_DIR, "icon_06_education_training.png"): "Education and training icon with books or people learning, healthcare education, professional illustration",
    (SERVICE_ICONS_DIR, "icon_07_harm_reduction_supplies.png"): "Harm reduction supplies icon showing protective equipment, professional medical design",
    (SERVICE_ICONS_DIR, "icon_08_crisis_support.png"): "Crisis support icon showing emergency help and mental health support, professional healthcare illustration",
    (SERVICE_ICONS_DIR, "icon_09_cultural_competency.png"): "Indigenous cultural healing icon with traditional elements and community symbols",
    (SERVICE_ICONS_DIR, "icon_10_community_resources.png"): "Community resources and networks icon, professional healthcare illustration",
    (SERVICE_ICONS_DIR, "icon_11_safe_space.png"): "Safe space welcoming environment icon, community sanctuary, professional healthcare design",
    (SERVICE_ICONS_DIR, "icon_12_wellness_check.png"): "Wellness check icon showing health monitoring and preventive care, professional medical illustration",

    # Founders
    (FOUNDERS_B_DIR, "b_fluxmulti_01.png"): "Professional headshot photo of Indigenous woman named Bri, Secretary of harm reduction organization, warm smile, confident, kind eyes, studio lighting, professional photo, community leader",
    (FOUNDERS_L_DIR, "l1.png"): "Professional headshot photo of Indigenous woman named Lilly, Treasurer, warm compassionate expression, studio lighting, professional photo, community leader",
    (FOUNDERS_J_DIR, "j_fluxmulti_01.png"): "Professional headshot photo of Indigenous man named Jonathan, Chairman, serious confident expression, warm lighting, professional photo, leadership presence",

    # Community Photos
    (COMMUNITY_PHOTOS_DIR, "community_01_diverse_group_smiling.png"): "Diverse group of community members smiling together, outdoor setting, harm reduction outreach, warm community feeling, documentary style photography",
    (COMMUNITY_PHOTOS_DIR, "community_02_peer_counselor_listening.png"): "Peer counselor listening with compassion to someone, active listening, support, empathy, healthcare worker, documentary style",
    (COMMUNITY_PHOTOS_DIR, "community_03_elder_and_youth.png"): "Indigenous elder and young person together in intergenerational healing moment, cultural teaching, warm lighting, documentary",
    (COMMUNITY_PHOTOS_DIR, "community_04_volunteers_organizing.png"): "Team volunteers organizing harm reduction supplies and resources, community action, teamwork",
    (COMMUNITY_PHOTOS_DIR, "community_05_person_receiving_naloxone.png"): "Community member receiving naloxone training from healthcare worker, health education, outdoor street setting",
    (COMMUNITY_PHOTOS_DIR, "community_06_group_training_session.png"): "Group of people in harm reduction training session, overdose prevention workshop, education",
    (COMMUNITY_PHOTOS_DIR, "community_07_mobile_unit_service.png"): "Mobile healthcare RV unit providing community outreach services on street, street-level healthcare",
    (COMMUNITY_PHOTOS_DIR, "community_08_safe_space_interior.png"): "Welcoming safe interior space for community members, healing environment, supportive community center",
    (COMMUNITY_PHOTOS_DIR, "community_09_person_hope_expression.png"): "Community member showing hope and healing journey, wellness, positive feeling, documentary portrait",
    (COMMUNITY_PHOTOS_DIR, "community_10_hands_distributing_supplies.png"): "Hands distributing harm reduction supplies, syringe exchange, naloxone kits, direct service, care",

    # Hero Banners
    (HERO_BANNERS_DIR, "hero_01_mobile_outreach_vehicle.png"): "Professional photo of mobile RV healthcare outreach vehicle in urban community, helping people, bright daylight, street engagement",
    (HERO_BANNERS_DIR, "hero_02_community_engagement.png"): "Community members engaging with harm reduction workers on street, compassionate interaction, trust building, warm lighting",

    # Infographics
    (INFORMATIONAL_DIR, "impact_infographic_v1.png"): "Impact infographic showing statistics: naloxone distributions, lives saved, community members served, visual data design, professional layout",
    (INFORMATIONAL_DIR, "engagement_infographic_v1.png"): "Community engagement infographic featuring three founders, organizational structure, leadership visualization",
}

def generate_image_fal(prompt, output_path, max_retries=3):
    """Generate image via FAL API using HTTP requests"""
    url = "https://queue.fal.run/fal-ai/flux-2"

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "prompt": prompt,
        "image_size": "landscape_4_3",
        "num_inference_steps": 28,
        "guidance_scale": 2.5,
        "output_format": "png",
    }

    print(f"  Generating: {output_path.name}")
    print(f"  Prompt: {prompt[:70]}...")

    for attempt in range(max_retries):
        try:
            # Submit job
            response = requests.post(url, json=payload, headers=headers, timeout=30)

            if response.status_code != 200:
                print(f"  ⚠ API error (attempt {attempt + 1}/{max_retries}): {response.status_code}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                continue

            result = response.json()
            request_id = result.get('request_id')

            if not request_id:
                print(f"  ⚠ No request_id returned")
                continue

            print(f"  Request ID: {request_id}, waiting for processing...")

            # Poll for result
            status_url = f"https://queue.fal.run/fal-ai/flux-2/requests/{request_id}"
            max_wait = 300  # 5 minutes
            start_time = time.time()

            while time.time() - start_time < max_wait:
                status_response = requests.get(status_url, headers=headers, timeout=30)

                if status_response.status_code == 200:
                    status_result = status_response.json()

                    if status_result.get('status') == 'completed':
                        if 'result' in status_result and 'images' in status_result['result']:
                            image_url = status_result['result']['images'][0]['url']

                            # Download image
                            img_response = requests.get(image_url, timeout=30)
                            if img_response.status_code == 200:
                                output_path.write_bytes(img_response.content)
                                print(f"  ✓ Saved: {output_path.name}")
                                return True

                    elif status_result.get('status') == 'failed':
                        print(f"  ✗ Generation failed: {status_result.get('error', 'Unknown error')}")
                        break

                time.sleep(5)

        except requests.RequestException as e:
            print(f"  ✗ Request error: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(5)

    print(f"  ✗ Failed to generate after {max_retries} attempts")
    return False

def main():
    print("=" * 70)
    print("[ART] HROC Website - FLUX 2 Image Regeneration")
    print("=" * 70)
    print()

    total = len(IMAGE_PROMPTS)
    generated = 0
    failed = []

    for (output_dir, filename), prompt in IMAGE_PROMPTS.items():
        output_path = output_dir / filename

        if generate_image_fal(prompt, output_path):
            generated += 1
            time.sleep(3)  # Rate limiting
        else:
            failed.append(filename)

    print("\n" + "=" * 70)
    print(f"✅ Generation Complete: {generated}/{total} images")
    if failed:
        print(f"❌ Failed: {', '.join(failed[:5])}" + ("..." if len(failed) > 5 else ""))
    print("=" * 70)
    print()

if __name__ == "__main__":
    main()
