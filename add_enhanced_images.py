#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add enhanced images (4, 5, 6) throughout service page content
Integrates new diverse images with existing layout
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Enhanced image placements for new images (4, 5, 6)
ENHANCED_IMAGE_PLACEMENTS = {
    'service-overdose-prevention': [
        {'image': 4, 'alt': 'Healthcare worker with naloxone supplies', 'caption': 'Professional Preparation', 'after': 'Our Overdose Prevention program'},
        {'image': 5, 'alt': 'Community training and education', 'caption': 'Training & Education', 'after': 'Program Components'},
        {'image': 6, 'alt': 'Mobile outreach accessibility', 'caption': 'Mobile Access', 'after': 'Services are free, confidential'}
    ],
    'service-syringe-exchange': [
        {'image': 4, 'alt': 'Sterile supplies and equipment', 'caption': 'Sterile Equipment', 'after': 'We provide sterile syringes'},
        {'image': 5, 'alt': 'Health worker support', 'caption': 'Peer Health Workers', 'after': 'Services Offered'},
        {'image': 6, 'alt': 'Mobile clinic services', 'caption': 'Mobile Screening', 'after': 'Mobile outreach'}
    ],
    'service-wound-care': [
        {'image': 4, 'alt': 'Professional wound assessment', 'caption': 'Expert Assessment', 'after': 'We provide professional assessment'},
        {'image': 5, 'alt': 'Medical wound care supplies', 'caption': 'Medical Supplies', 'after': 'Services Offered'},
        {'image': 6, 'alt': 'Compassionate wound treatment', 'caption': 'Professional Treatment', 'after': 'Free, confidential, judgment-free'}
    ],
    'service-health-screening': [
        {'image': 4, 'alt': 'Health screening equipment', 'caption': 'Testing Equipment', 'after': 'Free health screenings'},
        {'image': 5, 'alt': 'Health results and education', 'caption': 'Health Education', 'after': 'Services Offered'},
        {'image': 6, 'alt': 'Community health events', 'caption': 'Community Screening', 'after': 'No insurance, ID, or appointment'}
    ],
    'service-peer-support': [
        {'image': 4, 'alt': 'Peer counseling support', 'caption': 'Counseling Support', 'after': 'Our peer counselors understand'},
        {'image': 5, 'alt': 'Support circles and groups', 'caption': 'Support Circles', 'after': 'Support We Provide'},
        {'image': 6, 'alt': 'Peer navigation assistance', 'caption': 'Navigation Support', 'after': 'Free, confidential, judgment-free'}
    ],
    'service-housing-support': [
        {'image': 4, 'alt': 'Housing pathways and options', 'caption': 'Housing Pathways', 'after': 'Housing is health care'},
        {'image': 5, 'alt': 'Housing navigation support', 'caption': 'Navigator Support', 'after': 'Support Offered'},
        {'image': 6, 'alt': 'Stable housing achievement', 'caption': 'Housing Stability', 'after': 'No one sleeps outside'}
    ],
    'service-cultural-healing': [
        {'image': 4, 'alt': 'Indigenous healing practices', 'caption': 'Healing Circle', 'after': 'Our Indigenous roots'},
        {'image': 5, 'alt': 'Cultural community gathering', 'caption': 'Cultural Connection', 'after': 'Healing Offered'},
        {'image': 6, 'alt': 'Land-based healing activities', 'caption': 'Nature Healing', 'after': 'Join Us'}
    ],
    'service-education-training': [
        {'image': 4, 'alt': 'Training demonstrations', 'caption': 'Hands-On Training', 'after': 'Education empowers change'},
        {'image': 5, 'alt': 'Interactive learning sessions', 'caption': 'Active Learning', 'after': 'Training Topics'},
        {'image': 6, 'alt': 'Peer trainers and educators', 'caption': 'Peer Training', 'after': 'Community training provided'}
    ],
    'service-resource-navigation': [
        {'image': 4, 'alt': 'Resource navigation pathways', 'caption': 'Resource Map', 'after': 'Systems are complex'},
        {'image': 5, 'alt': 'Navigation support meetings', 'caption': 'One-on-One Support', 'after': 'Resources Accessed'},
        {'image': 6, 'alt': 'Resource access success', 'caption': 'Success Stories', 'after': 'Don\'t navigate alone'}
    ],
    'service-mobile-outreach': [
        {'image': 4, 'alt': 'Mobile outreach preparation', 'caption': 'Team Coordination', 'after': 'Our mobile outreach brings'},
        {'image': 5, 'alt': 'Community outreach services', 'caption': 'Community Services', 'after': 'What We Bring'},
        {'image': 6, 'alt': 'Neighborhood accessibility', 'caption': 'Accessible Services', 'after': 'How to Schedule'}
    ]
}

def create_image_html(image_num, service_name, alt_text, caption, layout='left', width='40%'):
    """Create HTML for floating image"""
    image_url = f"https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/{image_num}.png"

    if layout == 'left':
        return f'''<figure class="service-image-left" style="width: {width}; float: left; margin: 0 20px 15px 0; clear: left;">
            <img src="{image_url}" alt="{alt_text}" loading="lazy" style="width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <figcaption style="font-size: 13px; color: #666; margin-top: 8px; text-align: center;"><em>{caption}</em></figcaption>
          </figure>'''
    else:  # right
        return f'''<figure class="service-image-right" style="width: {width}; float: right; margin: 0 0 15px 20px; clear: right;">
            <img src="{image_url}" alt="{alt_text}" loading="lazy" style="width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <figcaption style="font-size: 13px; color: #666; margin-top: 8px; text-align: center;"><em>{caption}</em></figcaption>
          </figure>'''

def find_paragraph_with_text(content, search_text):
    """Find paragraph containing search text and return insertion point"""
    # More flexible search - case insensitive
    pattern = f'<p[^>]*>.*?{re.escape(search_text)}.*?</p>'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        return match.end()
    return -1

def update_service_page_enhanced(html_path, service_name):
    """Update service page with enhanced images distributed throughout content"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get image placements for this service
    placements = ENHANCED_IMAGE_PLACEMENTS.get(service_name, [])
    if not placements:
        return False

    # Track modifications with offset
    offset = 0
    widths = ['38%', '42%', '45%']

    for idx, placement in enumerate(placements):
        image_num = placement['image']
        alt_text = placement['alt']
        caption = placement['caption']
        search_text = placement['after']
        layout = 'right' if idx % 2 == 0 else 'left'  # Alternate from existing
        width = widths[idx % len(widths)]

        # Create image HTML
        image_html = create_image_html(image_num, service_name, alt_text, caption, layout, width)

        # Find insertion point
        insertion_point = find_paragraph_with_text(content, search_text)

        if insertion_point > 0:
            # Adjust for previous insertions
            insertion_point_adjusted = insertion_point + offset
            # Insert image after the paragraph
            content = content[:insertion_point_adjusted] + '\n\n' + image_html + '\n\n' + content[insertion_point_adjusted:]
            offset += len('\n\n' + image_html + '\n\n')

    # Write updated content
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    print("\n" + "="*70)
    print("Adding Enhanced Images (4, 5, 6) Throughout Service Pages")
    print("="*70 + "\n")

    service_files = list(Path('HROC_Website_New').glob('service-*.html'))

    updated = 0
    missing_images = []

    for file_path in sorted(service_files):
        service_name = file_path.stem

        # Skip if not in placements
        if service_name not in ENHANCED_IMAGE_PLACEMENTS:
            continue

        # Check if images 4, 5, 6 exist
        service_image_dir = Path('HROC_Website_New/generated_images') / service_name
        missing = []
        for img_num in [4, 5, 6]:
            if not (service_image_dir / f'{img_num}.png').exists():
                missing.append(img_num)

        if missing:
            missing_images.append((service_name, missing))
            print(f"⚠ {file_path.name}: Missing images {missing} - Skipping")
            continue

        print(f"Updating {file_path.name}...", end=' ')

        try:
            if update_service_page_enhanced(file_path, service_name):
                print("✓ Enhanced images added")
                updated += 1
            else:
                print("(no changes)")
        except Exception as e:
            print(f"✗ Error: {str(e)}")

    print("\n" + "="*70)
    print(f"Updated {updated} service pages")
    if missing_images:
        print(f"\nMissing images in {len(missing_images)} services:")
        for service, images in missing_images:
            print(f"  - {service}: images {images}")
    print("="*70 + "\n")
    print("Next steps:")
    if updated > 0:
        print("  1. Sync images to S3: aws s3 sync HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read")
        print("  2. Deploy: bash deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
