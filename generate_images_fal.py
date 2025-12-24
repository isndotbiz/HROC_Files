#!/usr/bin/env python3
"""
HROC Website Image Generation Script
Generates images for all services and impact stories using FAL.ai API
Theme: Warm, inclusive, community-focused visuals with "nanao banana" aesthetic
"""

import os
import sys
import json
import base64
import requests
from pathlib import Path
import time

# Configuration
FAL_API_KEY = os.getenv('FAL_API_KEY', '')
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_REGION = 'us-west-2'

# Image generation prompts for each service and section
PROMPTS = {
    # Service Pages
    'service-overdose-prevention': [
        "Warm, inclusive illustration of harm reduction educator showing naloxone administration training to community members, Indigenous-led health education, compassionate care, diverse participants, safe community space, professional medical illustration style with warm earth tones and community focus, nanao banana creative style",
        "Infographic showing overdose prevention resources: naloxone kit, fentanyl test strips, emergency numbers, colorful educational graphics with icons, warm aesthetic, health information design, diverse representation",
        "Community outreach scene: mobile harm reduction vehicle with medical professionals and community members, outdoor setting, trust-building moment, welcoming environment, realistic illustration style with warm lighting"
    ],
    'service-syringe-exchange': [
        "Professional illustration of sterile injection equipment exchange program: clean supplies, engaged community members, safe healthcare setting, compassionate care providers, diverse participants, warm color palette with health focus, nanao banana style",
        "Educational infographic on harm reduction and disease prevention: icons for HIV prevention, Hepatitis C info, safe injection practices, colorful graphics with clear messaging, inclusive design",
        "Community health worker distributing supplies with respect and dignity: warm interaction, trust-building moment, professional setting, diverse representation, positive atmosphere"
    ],
    'service-wound-care': [
        "Compassionate healthcare scene: wound care assessment with diverse participants, medical professional showing care technique, clean supplies, healing-focused environment, warm earth tones, inclusive representation, nanao banana style",
        "Medical infographic for wound care: proper cleaning technique, infection prevention steps, when to seek help, clear healthcare icons, educational design, warm aesthetic",
        "Community health moment: experienced healthcare provider with patient, trust and dignity, clean medical setting, diverse participants, positive care interaction"
    ],
    'service-health-screening': [
        "Mobile health clinic scene: blood pressure screening, friendly healthcare workers, diverse community members receiving care, professional medical setting, warm lighting, inclusive atmosphere, nanao banana style",
        "Health screening infographic: blood pressure ranges, glucose testing, HIV/HCV information, health indicators icons, educational graphics, colorful design with clear information",
        "Community health fair scene: multiple screening stations, diverse healthcare workers and participants, welcoming environment, health resources available, positive engagement"
    ],
    'service-peer-support': [
        "Circle of support illustration: diverse peers in supportive conversation, crisis support moment, recovery-focused dialogue, warm community setting, healing circle aesthetic, professional design, nanao banana style",
        "Peer support journey infographic: crisis support, treatment navigation, recovery milestones, mentorship, colorful hopeful design with clear pathways and support indicators",
        "Mentorship moment: experienced peer supporting someone in recovery, trust-building interaction, hope-focused, diverse representation, positive healing environment"
    ],
    'service-housing-support': [
        "Housing navigation illustration: diverse individuals with support workers exploring housing options, dignified representation, community center setting, planning moment, warm aesthetic, inclusive design, nanao banana style",
        "Housing support infographic: navigation process, ID assistance, benefits access, housing resources, timeline graphic, colorful informative design with clear steps",
        "Success story moment: individual with housing support worker, moving boxes, new home, hope and stability, positive transformation, diverse representation"
    ],
    'service-cultural-healing': [
        "Indigenous healing circle illustration: diverse participants in sacred gathering, traditional practices, cultural respect, healing plants, spiritual atmosphere, warm earth tones, authentic representation, nanao banana style",
        "Cultural healing infographic: healing circle components, traditional practices, community benefits, cultural elements, respectful design with Indigenous art aesthetics",
        "Community ceremony moment: traditional healing practice, diverse participants, cultural connection, sacred space, respect and dignity, positive spiritual energy"
    ],
    'service-education-training': [
        "Training workshop scene: naloxone training demonstration, diverse participants learning, engaged educators, practical skills focus, professional workshop setting, warm atmosphere, nanao banana style",
        "Training infographic: naloxone administration steps, workshop components, harm reduction education topics, learning pathway, clear icons and instructions, educational design",
        "Hands-on training moment: instructor demonstrating technique, engaged learners, practice session, supportive learning environment, diverse participants, positive knowledge transfer"
    ],
    'service-resource-navigation': [
        "Resource navigation illustration: navigator helping individual understand healthcare and benefits options, supportive meeting, organized information, community resource network, warm professional setting, nanao banana style",
        "Navigation infographic: benefits programs (SSI, SSDI, Medicaid), healthcare resources, legal aid, treatment options, system flowchart, colorful informative design",
        "Success navigation moment: navigator and client at healthcare appointment together, advocacy and support, overcoming barriers, positive outcome, diverse representation, hopeful atmosphere"
    ],

    # Impact Story Images
    'impact-story-hero-1': [
        "Powerful community portrait: diverse individual who has accessed multiple HROC services, transformation visible, hope and stability, warm lighting, respectful portraiture, diverse representation, authentic community member, professional photography style with nanao banana aesthetic",
    ],
    'impact-story-hero-2': [
        "Community transformation image: group of individuals at HROC event, celebration of progress, diverse participants, community connection, hopeful atmosphere, warm lighting, candid joyful moment, professional photography, nanao banana style",
    ],
    'impact-story-hero-3': [
        "Healing journey visual: individual in moment of growth and progress, surrounded by support systems, stability indicators, warm environment, hope-focused, diverse representation, authentic moment, professional image, nanao banana aesthetic",
    ],

    # Gallery images for service pages
    'service-gallery-image': [
        "Community health worker providing compassionate care to diverse individual in mobile outreach setting, trust moment, harm reduction, warm lighting, professional healthcare interaction",
        "Group community members in supportive circle, peer support moment, recovery-focused, positive atmosphere, diverse participation, healing environment",
        "Healthcare provider and patient in dignified health interaction, respectful medical moment, trust-building, warm professional setting, diverse representation",
        "Community gathering for HROC service, diverse participants, supportive environment, collective healing, positive energy, welcoming atmosphere",
        "Mobile outreach vehicle with community members accessing services, professional setting, welcoming environment, accessible healthcare moment",
    ]
}

def generate_image_with_fal(prompt: str, output_path: str) -> bool:
    """
    Generate image using FAL.ai API
    Uses the FLUX model for high-quality, detailed images
    """
    if not FAL_API_KEY:
        print(f"ERROR: FAL_API_KEY environment variable not set")
        print(f"Please set your FAL.ai API key: export FAL_API_KEY='your-key-here'")
        return False

    try:
        # FAL.ai API endpoint for image generation
        # Using FLUX model for quality outputs
        url = "https://api.fal.ai/v1/gen/flux-pro/text-to-image"

        headers = {
            "Authorization": f"Key {FAL_API_KEY}",
            "Content-Type": "application/json"
        }

        # Enhanced prompt with consistent theme
        enhanced_prompt = f"{prompt} | Professional illustration, warm inclusive aesthetic, community-focused, diverse representation, high quality, clear details, suitable for nonprofit website"

        payload = {
            "prompt": enhanced_prompt,
            "image_size": "landscape_16_9",
            "num_images": 1,
            "enable_safety_checker": True,
        }

        print(f"Generating: {output_path}")
        print(f"Prompt: {enhanced_prompt[:100]}...")

        response = requests.post(url, headers=headers, json=payload, timeout=120)

        if response.status_code == 200:
            result = response.json()
            image_url = result.get('images', [{}])[0].get('url')

            if image_url:
                # Download image
                img_response = requests.get(image_url, timeout=30)
                if img_response.status_code == 200:
                    # Create directory if needed
                    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
                    with open(output_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"✓ Saved: {output_path}")
                    return True
            else:
                print(f"✗ No image URL in response")
                return False
        else:
            print(f"✗ API Error {response.status_code}: {response.text}")
            return False

    except Exception as e:
        print(f"✗ Error generating image: {str(e)}")
        return False

def generate_all_images():
    """Generate all images for HROC website"""

    output_base = "HROC_Website_New/generated_images"
    Path(output_base).mkdir(parents=True, exist_ok=True)

    total_images = 0
    successful_images = 0

    # Generate service images
    for service_name, prompt_list in PROMPTS.items():
        if service_name.startswith('service-') and not service_name.startswith('service-gallery'):
            for idx, prompt in enumerate(prompt_list):
                output_path = f"{output_base}/{service_name}/{idx + 1}.png"
                if generate_image_with_fal(prompt, output_path):
                    successful_images += 1
                total_images += 1
                time.sleep(2)  # Rate limit

    # Generate impact story images
    for story_name, prompt_list in PROMPTS.items():
        if story_name.startswith('impact-story'):
            for idx, prompt in enumerate(prompt_list):
                output_path = f"{output_base}/{story_name}.png"
                if generate_image_with_fal(prompt, output_path):
                    successful_images += 1
                total_images += 1
                time.sleep(2)

    # Generate gallery images
    if 'service-gallery-image' in PROMPTS:
        for idx, prompt in enumerate(PROMPTS['service-gallery-image']):
            output_path = f"{output_base}/service-gallery/{idx + 1}.png"
            if generate_image_with_fal(prompt, output_path):
                successful_images += 1
            total_images += 1
            time.sleep(2)

    print("\n" + "="*60)
    print(f"Image Generation Summary")
    print("="*60)
    print(f"Total Images Processed: {total_images}")
    print(f"Successfully Generated: {successful_images}")
    print(f"Failed: {total_images - successful_images}")
    print(f"Success Rate: {(successful_images/total_images*100):.1f}%" if total_images > 0 else "N/A")
    print("="*60)

    return successful_images, total_images

if __name__ == "__main__":
    print("\n" + "="*60)
    print("HROC Website Image Generation")
    print("Using FAL.ai with 'nanao banana' aesthetic theme")
    print("="*60 + "\n")

    successful, total = generate_all_images()

    if successful > 0:
        print("\n✓ Images generated successfully!")
        print("Next steps:")
        print("1. Review generated images in HROC_Website_New/generated_images/")
        print("2. Run: python3 upload_images_to_s3.py")
        print("3. Run: python3 update_html_images.py")
        print("4. Deploy to TrueNAS")
    else:
        print("\n✗ No images generated. Please check FAL_API_KEY and try again.")
        sys.exit(1)
