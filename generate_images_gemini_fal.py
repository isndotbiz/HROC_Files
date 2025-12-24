#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate diverse images for service pages using Gemini 3 Pro Image via fal-ai
"""
import sys
import io
import os
from pathlib import Path
import requests

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    import fal_client
except ImportError:
    print("Installing fal-client library...")
    os.system("pip install fal-client -q")
    import fal_client

# Image generation prompts for each service
IMAGE_SPECS = {
    'service-overdose-prevention': [
        {
            'num': 4,
            'prompt': 'Professional healthcare worker holding overdose prevention supplies: naloxone kits, fentanyl test strips, instruction materials. Medical setting, clear focus on life-saving equipment, compassionate care worker, photorealistic, bright lighting'
        },
        {
            'num': 5,
            'prompt': 'Diverse community members in peer health training session about overdose response. Small group actively learning and engaged. Inclusive setting, compassionate instruction, real diverse people, photorealistic, community center'
        },
        {
            'num': 6,
            'prompt': 'Mobile outreach van with healthcare services in Seattle urban neighborhood. Healthcare workers and community members accessing services outside. Daylight, street setting, photorealistic, professional'
        }
    ],
    'service-syringe-exchange': [
        {
            'num': 4,
            'prompt': 'Professional organized display of sterile injection supplies: syringes in various gauges, sterile containers, disposal boxes, harm reduction equipment. Clean medical setting, clear and organized, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Peer health worker in supportive one-on-one counseling with person seeking services. Compassionate listening and conversation, respectful healthcare setting. Real diverse people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Mobile health screening and syringe exchange station in community setting. Multiple people receiving services, health equipment visible, professional healthcare providers, inclusive environment, photorealistic'
        }
    ],
    'service-wound-care': [
        {
            'num': 4,
            'prompt': 'Healthcare provider performing professional wound assessment and care on patient. Clean technique, sterile environment, compassionate care demonstrated. Medical supplies visible, real setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Professional medical wound care supplies organized neatly: sterile gauze, bandages, antiseptic solutions, sterile gloves, dressings. Clean display, medical clinic setting, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Compassionate healthcare provider providing wound care treatment to community member. Treatment in progress, supportive healthcare environment, professional care, real diverse people, photorealistic'
        }
    ],
    'service-health-screening': [
        {
            'num': 4,
            'prompt': 'Health screening station with medical equipment: blood pressure cuff, pulse oximeter, rapid test kits, vital sign monitors, thermometer. Clean medical setting, professional equipment setup, photorealistic, bright'
        },
        {
            'num': 5,
            'prompt': 'Peer health worker explaining test results to person with compassion and clarity. Results discussion moment, health education, supportive and caring interaction. Diverse people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Community health screening event with multiple diverse people receiving health services. Mobile clinic setting, diverse participants getting screened, health workers providing care, inclusive environment, photorealistic'
        }
    ],
    'service-peer-support': [
        {
            'num': 4,
            'prompt': 'Two peer counselors in supportive one-on-one conversation. Engaged listening and emotional support, human connection. Real diverse people, intimate supportive healthcare setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Support circle gathering with peers sitting together in community space. People supporting each other, healing environment, community connection. Diverse group, real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Peer navigator helping person with resource navigation and future planning. Meeting reviewing documents together, problem-solving and support. Real diverse people, collaborative partnership, photorealistic'
        }
    ],
    'service-housing-support': [
        {
            'num': 4,
            'prompt': 'Visual representation showing housing support pathway: from emergency shelter to transitional housing to permanent supportive housing. Progression graphic, clear stages, hopeful imagery, infographic style, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Housing navigator meeting with person reviewing housing options and applications. Looking at documents and discussing solutions together. Supportive partnership, diverse people, office setting, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Person receiving keys and moving into stable housing with supportive team. Joyful moment celebrating housing stability, hopeful future, supportive community present, photorealistic'
        }
    ],
    'service-cultural-healing': [
        {
            'num': 4,
            'prompt': 'Indigenous healing circle with diverse people gathered respectfully in circle. Traditional healing elements, spiritual sacred space, community gathering. Real people, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Cultural community gathering and celebration event. Diverse indigenous and community members, traditional or cultural elements visible, celebration and healing. Inclusive space, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Land-based healing activity with community members in nature. People in natural outdoor setting, healing through connection to nature, community outdoor activity, photorealistic'
        }
    ],
    'service-education-training': [
        {
            'num': 4,
            'prompt': 'Trainer demonstrating naloxone use and overdose response techniques to community group. Hands-on demonstration, clear instruction, training materials visible. Community setting, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Interactive training session with diverse participants actively engaged in learning. People taking notes, asking questions, involved participation. Inclusive learning environment, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Certified peer trainers presenting and teaching at community event. Instructing group with enthusiasm, attendees engaged and learning. Diverse participants, professional training, photorealistic'
        }
    ],
    'service-resource-navigation': [
        {
            'num': 4,
            'prompt': 'Visual resource navigation map or flowchart showing pathways. Connections to housing, benefits, healthcare, food, employment resources. Infographic style, clear visual guide, helpful, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Navigator in one-on-one meeting discussing resource options and solutions with person. Collaborative problem-solving, reviewing options together, supportive conversation. Real diverse people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Person successfully accessing multiple resources with supportive team helping. Success story moment, person receiving help, team collaboration, hopeful positive outcome, photorealistic'
        }
    ],
    'service-mobile-outreach': [
        {
            'num': 4,
            'prompt': 'Mobile outreach team coordinating and loading supplies into van for community visits. Team coordination, equipment organization, professional preparation. Diverse team, photorealistic'
        },
        {
            'num': 5,
            'prompt': 'Mobile outreach team actively providing healthcare services in community location. Diverse healthcare providers, community setting, outreach services happening. Real people, photorealistic'
        },
        {
            'num': 6,
            'prompt': 'Mobile outreach unit van in Seattle neighborhood serving diverse community members. Van parked, people accessing services outside, diverse urban neighborhood, daytime, photorealistic'
        }
    ]
}

def on_queue_update(update):
    """Handle queue updates during generation"""
    if isinstance(update, fal_client.InProgress):
        for log in update.logs:
            print(f"      {log['message']}")

def generate_image(prompt, service_name, image_num):
    """Generate an image using Gemini/fal-ai"""
    try:
        print(f"    Generating image {image_num}...", end=' ', flush=True)

        result = fal_client.subscribe(
            "fal-ai/nano-banana-pro",
            arguments={
                "prompt": prompt,
                "num_images": 1,
                "aspect_ratio": "3:2",
                "output_format": "png",
                "resolution": "1K"
            },
            with_logs=True,
            on_queue_update=on_queue_update,
        )

        # Extract image URL from result
        if result and 'images' in result and len(result['images']) > 0:
            image_url = result['images'][0]['url']

            # Download the image
            img_response = requests.get(image_url, timeout=30)
            if img_response.status_code == 200:
                # Save to service folder
                service_path = Path('HROC_Website_New/generated_images') / service_name
                service_path.mkdir(parents=True, exist_ok=True)

                image_path = service_path / f'{image_num}.png'
                with open(image_path, 'wb') as f:
                    f.write(img_response.content)

                print(f"✓ Saved")
                return True

        print("✗ No image in result")
        return False

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

def main():
    print("\n" + "="*70)
    print("Generating Diverse Images with Gemini 3 Pro Image (fal-ai)")
    print("="*70 + "\n")

    # Check for API key
    api_key = os.getenv('FAL_KEY')
    if not api_key:
        print("⚠ FAL_KEY environment variable not set!")
        print("Please set: export FAL_KEY='your-key'")
        print("\nAlternatively, use image generation tools manually and place images in:")
        for service in IMAGE_SPECS.keys():
            print(f"  - HROC_Website_New/generated_images/{service}/ (images 4, 5, 6)")
        return

    total_generated = 0
    total_failed = 0

    for service_name, specs in IMAGE_SPECS.items():
        print(f"\n{service_name}:")
        for spec in specs:
            if generate_image(spec['prompt'], service_name, spec['num']):
                total_generated += 1
            else:
                total_failed += 1

    print("\n" + "="*70)
    print(f"Generated {total_generated} new images ({total_failed} failed)")
    print("="*70 + "\n")
    print("Next steps:")
    print("  1. Sync images to S3: aws s3 sync HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read")
    print("  2. Update HTML with: python add_images_to_content.py")
    print("  3. Deploy: bash deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
