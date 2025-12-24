#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate additional diverse images for service pages using FAL API
"""
import sys
import io
import os
import time
import requests
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# FAL API configuration
FAL_API_KEY = os.getenv('FAL_API_KEY', '')
FAL_API_URL = 'https://queue.fal.run/fal-ai/flux-pro/v1/turbo'

# Image generation prompts
IMAGE_SPECS = {
    'service-overdose-prevention': [
        {
            'num': 4,
            'prompt': 'Professional healthcare worker holding overdose prevention supplies: naloxone kits, fentanyl test strips, instruction materials. Medical setting, clear focus on life-saving equipment, compassionate care worker, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Diverse community members in peer health training session. Small group actively learning about overdose response. Engaged participants, inclusive setting, compassionate instruction, real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Mobile outreach van labeled with harm reduction services parked in Seattle urban neighborhood. Healthcare workers and community members accessing services outside. Daylight, real street setting, photorealistic'
        }
    ],
    'service-syringe-exchange': [
        {
            'num': 4,
            'prompt': 'Professional display of sterile injection supplies: syringes in various gauges, sterile containers, disposal boxes, harm reduction equipment. Clean, organized, medical setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Peer health worker in one-on-one counseling with person seeking services. Supportive conversation, compassionate listening, respectful setting. Real people, diverse, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Mobile health screening station in community setting. Multiple people receiving services, health screening equipment visible, professional healthcare providers, inclusive environment, photorealistic'
        }
    ],
    'service-wound-care': [
        {
            'num': 4,
            'prompt': 'Healthcare provider performing professional wound assessment and care. Clean technique, sterile environment, compassionate care. Medical supplies visible, real setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Professional medical supplies for wound care organized neatly: sterile gauze, bandages, dressings, gloves, cleaning supplies. Clean display, medical setting, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Compassionate healthcare provider providing wound care to community member. Treatment in progress, supportive environment, professional care, real people, photorealistic'
        }
    ],
    'service-health-screening': [
        {
            'num': 4,
            'prompt': 'Health screening station with equipment: blood pressure cuff, pulse oximeter, rapid test kits, vital sign monitors. Clean medical setting, professional setup, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Peer health worker explaining test results to person with compassion and clarity. Results discussion, education moment, supportive interaction, diverse people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Community health screening event with multiple people receiving services. Mobile clinic setting, diverse participants, health workers providing care, inclusive environment, photorealistic'
        }
    ],
    'service-peer-support': [
        {
            'num': 4,
            'prompt': 'Two peer counselors in supportive one-on-one conversation. Engaged listening, compassionate support, connection. Real diverse people, intimate supportive setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Support circle or group gathering with peers in community space. People sitting in circle, supportive community, healing environment. Diverse group, real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Peer navigator helping person with resource navigation and planning. Meeting over documents, problem-solving together, supportive partnership. Real people, collaborative, photorealistic'
        }
    ],
    'service-housing-support': [
        {
            'num': 4,
            'prompt': 'Visual representation of housing pathway: shelter to transitional to permanent supportive housing. Infographic style showing progression, clear stages, hopeful imagery, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Housing navigator meeting with person reviewing housing options. Looking at documents, applications, discussing solutions. Supportive partnership, diverse people, office setting, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Person receiving keys and moving into stable housing with support team. Joyful moment, stable housing, supportive community, hope and celebration, photorealistic'
        }
    ],
    'service-cultural-healing': [
        {
            'num': 4,
            'prompt': 'Indigenous healing circle with people gathered respectfully. Traditional healing elements, spiritual space, people in circle, community gathering, real people, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Cultural gathering and community event. Diverse indigenous and community members, traditional or cultural elements, celebration, inclusive space, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Land-based healing activity with people in nature. Community members in natural setting, healing through connection to nature, outdoor activity, photorealistic'
        }
    ],
    'service-education-training': [
        {
            'num': 4,
            'prompt': 'Trainer demonstrating naloxone use and overdose response techniques. Hands-on instruction, clear demonstration, training materials, community setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Interactive training session with diverse participants actively engaged and learning. People taking notes, asking questions, involved participation, inclusive environment, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Peer trainers presenting at community event. Certified trainers instructing group, enthusiastic attendees, community education, diverse participants, photorealistic'
        }
    ],
    'service-resource-navigation': [
        {
            'num': 4,
            'prompt': 'Visual resource navigation map or flowchart. Showing pathways to housing, benefits, healthcare, food, employment. Infographic style, clear connections, helpful visual guide, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Navigator in one-on-one meeting discussing resource options and solutions. Collaborative problem-solving, going through options, supportive conversation, real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Person successfully accessing multiple resources with support team. Success story, person receiving help, team collaboration, hopeful outcome, photorealistic'
        }
    ],
    'service-mobile-outreach': [
        {
            'num': 4,
            'prompt': 'Mobile outreach team loading supplies and preparing van for community visits. Team coordination, equipment organization, professional preparation, diverse team, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Mobile outreach team providing services in community location. Diverse healthcare providers, community setting, outreach services happening, real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Mobile outreach unit in different Seattle neighborhood serving community members. Van parked, people accessing services, diverse neighborhood setting, daytime, photorealistic'
        }
    ]
}

def generate_image(prompt, service_name, image_num):
    """Generate an image using FAL API"""
    if not FAL_API_KEY:
        print(f"  ⚠ FAL_API_KEY not set. Skipping image generation.")
        return False

    try:
        headers = {
            'Authorization': f'Key {FAL_API_KEY}',
            'Content-Type': 'application/json'
        }

        payload = {
            'prompt': prompt,
            'image_size': {
                'width': 1024,
                'height': 768
            },
            'num_inference_steps': 28,
            'guidance_scale': 3.5
        }

        print(f"    Generating image {image_num}...", end=' ', flush=True)

        response = requests.post(FAL_API_URL, json=payload, headers=headers, timeout=120)

        if response.status_code == 200:
            data = response.json()

            # Check if request_id is present (queued) or image_url (completed)
            if 'image' in data and 'url' in data['image']:
                image_url = data['image']['url']

                # Download the image
                img_response = requests.get(image_url, timeout=30)
                if img_response.status_code == 200:
                    # Save to service folder
                    service_path = Path('HROC_Website_New/generated_images') / service_name
                    service_path.mkdir(parents=True, exist_ok=True)

                    image_path = service_path / f'{image_num}.png'
                    with open(image_path, 'wb') as f:
                        f.write(img_response.content)

                    print(f"✓ Saved as {image_path.name}")
                    return True

            print("⚠ Image generation queued (may take longer)")
            return False

        else:
            print(f"✗ API error: {response.status_code}")
            return False

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def main():
    print("\n" + "="*70)
    print("Generating Additional Diverse Images for Service Pages")
    print("="*70 + "\n")

    if not FAL_API_KEY:
        print("⚠ FAL_API_KEY environment variable not set!")
        print("Please set: export FAL_API_KEY='your-key'")
        print("\nAlternatively, use image generation tools manually and place images in:")
        for service in IMAGE_SPECS.keys():
            print(f"  - HROC_Website_New/generated_images/{service}/ (images 4, 5, 6)")
        return

    total_generated = 0

    for service_name, specs in IMAGE_SPECS.items():
        print(f"\n{service_name}:")
        for spec in specs:
            if generate_image(spec['prompt'], service_name, spec['num']):
                total_generated += 1
            time.sleep(2)  # Rate limiting

    print("\n" + "="*70)
    print(f"Generated {total_generated} new images")
    print("="*70 + "\n")
    print("Next steps:")
    print("  1. Run: python add_images_to_content.py")
    print("  2. Deploy: bash deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
