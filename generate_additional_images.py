#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate additional diverse images for service pages and add them throughout the content
"""
import sys
import io
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Define new diverse image prompts for each service
IMAGE_PROMPTS = {
    'service-overdose-prevention': [
        'Image 4: Healthcare worker holding naloxone kits and fentanyl test strips, professional hands-on demonstration',
        'Image 5: Diverse community members in peer training session, taking notes and asking questions',
        'Image 6: Mobile outreach van parked in Seattle neighborhood, people accessing services'
    ],
    'service-syringe-exchange': [
        'Image 4: Sterile injection supplies displayed professionally - syringes, gauze, containers',
        'Image 5: Health worker conducting one-on-one counseling and education session',
        'Image 6: Mobile health screening station with multiple people receiving services'
    ],
    'service-wound-care': [
        'Image 4: Close-up of professional wound care and cleaning procedure',
        'Image 5: Medical supplies organized professionally - bandages, dressings, sterile gloves',
        'Image 6: Healthcare provider assessing and caring for patient wound'
    ],
    'service-health-screening': [
        'Image 4: Blood pressure cuff and vital sign monitoring equipment',
        'Image 5: Peer health worker explaining test results to person with compassion',
        'Image 6: Community members receiving health screenings at mobile clinic'
    ],
    'service-peer-support': [
        'Image 4: Two peer counselors in supportive conversation, engaged and caring',
        'Image 5: Support circle group in community gathering space',
        'Image 6: Peer navigator helping person with resource navigation planning'
    ],
    'service-housing-support': [
        'Image 4: Housing transition showing pathway from shelter to transitional to permanent housing',
        'Image 5: Housing navigator meeting with person reviewing housing options and applications',
        'Image 6: Person moving into stable housing with support and celebration'
    ],
    'service-cultural-healing': [
        'Image 4: Indigenous healing circle with people gathered in respectful space',
        'Image 5: Cultural gathering with traditional elements and community members',
        'Image 6: Land-based healing activity with nature and people in harmony'
    ],
    'service-education-training': [
        'Image 4: Trainer demonstrating naloxone use and overdose response techniques',
        'Image 5: Interactive training session with diverse participants engaged and learning',
        'Image 6: Peer trainers presenting at community event with enthusiastic attendees'
    ],
    'service-resource-navigation': [
        'Image 4: Resource navigation flowchart showing pathways to housing, benefits, healthcare',
        'Image 5: Navigator in one-on-one meeting discussing resource options and solutions',
        'Image 6: Person successfully accessing multiple resources with support team'
    ],
    'service-mobile-outreach': [
        'Image 4: Mobile outreach team loading supplies into van for community visit',
        'Image 5: Diverse team members providing services in community location',
        'Image 6: Mobile unit in different neighborhood serving multiple community members'
    ]
}

def print_image_generation_instructions():
    """Print instructions for generating images"""
    print("\n" + "="*70)
    print("IMAGE GENERATION INSTRUCTIONS")
    print("="*70 + "\n")

    print("Generate the following diverse images for enhanced service pages.\n")
    print("Each service should have varied imagery showing people, supplies, and activities.\n")

    for service, prompts in IMAGE_PROMPTS.items():
        print(f"\n{service}:")
        print(f"  Service folder: HROC_Website_New/generated_images/{service}/")
        for prompt in prompts:
            print(f"    • {prompt}")

    print("\n" + "="*70)
    print("After generating images:")
    print("  1. Save images as 4.png, 5.png, 6.png in each service folder")
    print("  2. Run add_images_to_content.py to update HTML pages")
    print("  3. Deploy to TrueNAS with deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    print_image_generation_instructions()
