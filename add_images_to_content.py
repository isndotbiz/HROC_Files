#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add generated images throughout service page content using float layout
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Image placement strategy for each service
IMAGE_PLACEMENTS = {
    'service-overdose-prevention': [
        {'image': 2, 'alt': 'Naloxone and fentanyl test strips', 'caption': 'Life-Saving Supplies', 'after': 'Overdose remains one of the leading causes'},
        {'image': 4, 'alt': 'Healthcare worker with overdose prevention supplies', 'caption': 'Professional Care', 'after': 'Overdose prevention is peer-led prevention'},
        {'image': 5, 'alt': 'Community training session', 'caption': 'Community Education', 'after': 'Program Components'},
        {'image': 6, 'alt': 'Mobile outreach van', 'caption': 'Mobile Access', 'after': 'How to Access Services'}
    ],
    'service-syringe-exchange': [
        {'image': 2, 'alt': 'Sterile injection supplies', 'caption': 'Quality Equipment', 'after': 'Evidence-based harm reduction'},
        {'image': 4, 'alt': 'Sterile supplies display', 'caption': 'Professional Standards', 'after': 'Services Offered'},
        {'image': 5, 'alt': 'Health worker counseling', 'caption': 'Peer Support', 'after': 'Impact & Access'},
        {'image': 6, 'alt': 'Community mobile clinic', 'caption': 'Mobile Services', 'after': 'Research shows syringe exchange'}
    ],
    'service-wound-care': [
        {'image': 2, 'alt': 'Wound care assessment', 'caption': 'Professional Care', 'after': 'Untreated wounds become life-threatening'},
        {'image': 4, 'alt': 'Wound care procedure', 'caption': 'Expert Treatment', 'after': 'Services Offered'},
        {'image': 5, 'alt': 'Medical supplies organized', 'caption': 'Sterile Supplies', 'after': 'Infection Prevention'},
        {'image': 6, 'alt': 'Healthcare provider with patient', 'caption': 'Compassionate Care', 'after': 'How to Access'}
    ],
    'service-health-screening': [
        {'image': 2, 'alt': 'Health screening equipment', 'caption': 'Modern Testing', 'after': 'Free health screenings connect people'},
        {'image': 4, 'alt': 'Vital sign monitoring', 'caption': 'Health Assessment', 'after': 'Services Offered'},
        {'image': 5, 'alt': 'Health worker explaining results', 'caption': 'Health Education', 'after': 'Access & Support'},
        {'image': 6, 'alt': 'Community screening event', 'caption': 'Community Health', 'after': 'Peer navigators help connect'}
    ],
    'service-peer-support': [
        {'image': 2, 'alt': 'Peer counselors in conversation', 'caption': 'Understanding Support', 'after': 'Lived experience creates trust'},
        {'image': 4, 'alt': 'Supportive conversation', 'caption': 'One-on-One Support', 'after': 'Support We Provide'},
        {'image': 5, 'alt': 'Support circle gathering', 'caption': 'Healing Circles', 'after': 'Case Management'},
        {'image': 6, 'alt': 'Peer navigator helping', 'caption': 'Resource Navigation', 'after': 'Get Support'}
    ],
    'service-housing-support': [
        {'image': 2, 'alt': 'Housing pathway', 'caption': 'Path to Stability', 'after': 'Housing is health care'},
        {'image': 4, 'alt': 'Housing options visualization', 'caption': 'Housing Pathways', 'after': 'Support Offered'},
        {'image': 5, 'alt': 'Housing navigator meeting', 'caption': 'Professional Navigation', 'after': 'Case Management'},
        {'image': 6, 'alt': 'Person moving to stable housing', 'caption': 'Stable Housing', 'after': 'Access Housing Help'}
    ],
    'service-cultural-healing': [
        {'image': 2, 'alt': 'Indigenous healing circle', 'caption': 'Traditional Healing', 'after': 'Our Indigenous roots inform'},
        {'image': 4, 'alt': 'Healing circle gathering', 'caption': 'Community Circle', 'after': 'Healing Offered'},
        {'image': 5, 'alt': 'Cultural community event', 'caption': 'Cultural Connection', 'after': 'Arts & Expression'},
        {'image': 6, 'alt': 'Land-based healing activity', 'caption': 'Nature Connection', 'after': 'Join Us'}
    ],
    'service-education-training': [
        {'image': 2, 'alt': 'Overdose response training', 'caption': 'Education Matters', 'after': 'Education empowers change'},
        {'image': 4, 'alt': 'Training demonstration', 'caption': 'Hands-On Training', 'after': 'Training Topics'},
        {'image': 5, 'alt': 'Interactive training session', 'caption': 'Active Learning', 'after': 'Leadership Development'},
        {'image': 6, 'alt': 'Peer trainers presenting', 'caption': 'Peer Training', 'after': 'Get Trained'}
    ],
    'service-resource-navigation': [
        {'image': 2, 'alt': 'Resource navigation guide', 'caption': 'Resource Pathways', 'after': 'Systems are complex'},
        {'image': 4, 'alt': 'Resource flowchart', 'caption': 'Connected Resources', 'after': 'Resources Accessed'},
        {'image': 5, 'alt': 'Navigator meeting', 'caption': 'One-on-One Support', 'after': 'Healthcare Linkage'},
        {'image': 6, 'alt': 'Person accessing resources', 'caption': 'Success Stories', 'after': 'Start Navigating'}
    ],
    'service-mobile-outreach': [
        {'image': 2, 'alt': 'Mobile outreach team', 'caption': 'Team Coordination', 'after': 'Our mobile outreach brings'},
        {'image': 4, 'alt': 'Van preparation', 'caption': 'Service Preparation', 'after': 'Services in Every Neighborhood'},
        {'image': 5, 'alt': 'Outreach team providing services', 'caption': 'Community Engagement', 'after': 'What We Bring'},
        {'image': 6, 'alt': 'Mobile unit in neighborhood', 'caption': 'Accessible Services', 'after': 'How to Schedule'}
    ]
}

def create_image_html(image_num, alt_text, caption, layout='left', width='40%'):
    """Create HTML for floating image"""
    image_url = f"https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{{service}}/{image_num}.png"

    if layout == 'left':
        return f'''<figure class="service-image-left" style="width: {width}; float: left; margin: 0 20px 15px 0; clear: left;">
            <img src="{image_url}" alt="{alt_text}" loading="lazy" style="width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <figcaption style="font-size: 14px; color: #666; margin-top: 8px; text-align: center;"><em>{caption}</em></figcaption>
          </figure>'''
    else:  # right
        return f'''<figure class="service-image-right" style="width: {width}; float: right; margin: 0 0 15px 20px; clear: right;">
            <img src="{image_url}" alt="{alt_text}" loading="lazy" style="width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
            <figcaption style="font-size: 14px; color: #666; margin-top: 8px; text-align: center;"><em>{caption}</em></figcaption>
          </figure>'''

def update_service_page(html_path, service_name):
    """Update service page with images distributed throughout content"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get image placements for this service
    placements = IMAGE_PLACEMENTS.get(service_name, [])
    if not placements:
        print(f"  No image placements defined for {service_name}")
        return False

    # Remove old gallery section if it exists
    content = re.sub(
        r'<!-- Gallery of Related Images -->.*?</div>\s*(?=</section>)',
        '',
        content,
        flags=re.DOTALL
    )

    # Add images throughout content
    images_added = 0
    widths = ['35%', '40%', '45%', '48%']

    for idx, placement in enumerate(placements):
        image_num = placement['image']
        alt_text = placement['alt']
        caption = placement['caption']
        search_text = placement['after']
        layout = 'left' if idx % 2 == 0 else 'right'
        width = widths[idx % len(widths)]

        # Create image HTML
        image_html = create_image_html(image_num, alt_text, caption, layout, width)
        image_html = image_html.replace('{service}', service_name)

        # Find insertion point - after the search_text in the content
        # Look for the first paragraph containing search_text
        pattern = f'([pP]><.*?{re.escape(search_text)}.*?</p>)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            insertion_point = match.end()
            content = content[:insertion_point] + '\n\n' + image_html + '\n\n' + content[insertion_point:]
            images_added += 1

    if images_added > 0:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True

    return False

def main():
    print("\n" + "="*70)
    print("Adding Images Throughout Service Page Content")
    print("="*70 + "\n")

    service_files = list(Path('HROC_Website_New').glob('service-*.html'))

    updated = 0
    for file_path in sorted(service_files):
        service_name = file_path.stem
        print(f"Updating {file_path.name}...", end=' ')

        if update_service_page(file_path, service_name):
            print("✓ Added images")
            updated += 1
        else:
            print("(no changes)")

    print("\n" + "="*70)
    print(f"Updated {updated} service pages")
    print("="*70 + "\n")
    print("Next steps:")
    print("  1. Sync images to S3: aws s3 sync HROC_Website_New/generated_images s3://hroc-outreach-assets/images/generated_images --region us-west-2 --acl public-read")
    print("  2. Deploy: bash deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
