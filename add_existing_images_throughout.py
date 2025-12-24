#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add existing service page images throughout content instead of all at bottom
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Image placement for each service using existing images (1, 2, 3)
IMAGE_PLACEMENTS = {
    'service-overdose-prevention': [
        {'image': 2, 'alt': 'Naloxone and harm reduction supplies', 'caption': 'Life-Saving Supplies', 'after': 'Overdose remains one of the leading'},
        {'image': 3, 'alt': 'Overdose prevention training', 'caption': 'Community Training', 'after': 'Program Components'},
        {'image': 1, 'alt': 'Mobile outreach services', 'caption': 'Mobile Access', 'after': 'How to Access'}
    ],
    'service-syringe-exchange': [
        {'image': 2, 'alt': 'Sterile injection equipment', 'caption': 'Quality Equipment', 'after': 'Evidence-based harm reduction'},
        {'image': 3, 'alt': 'Syringe exchange services', 'caption': 'Service Delivery', 'after': 'Services Offered'},
        {'image': 1, 'alt': 'Health screening and support', 'caption': 'Comprehensive Care', 'after': 'Impact & Access'}
    ],
    'service-wound-care': [
        {'image': 2, 'alt': 'Professional wound care', 'caption': 'Expert Care', 'after': 'Untreated wounds become'},
        {'image': 3, 'alt': 'Medical assessment', 'caption': 'Professional Assessment', 'after': 'Services Offered'},
        {'image': 1, 'alt': 'Mobile healthcare unit', 'caption': 'Accessible Services', 'after': 'How to Access'}
    ],
    'service-health-screening': [
        {'image': 2, 'alt': 'Health screening equipment', 'caption': 'Testing Services', 'after': 'Free health screenings'},
        {'image': 3, 'alt': 'Health education', 'caption': 'Health Education', 'after': 'Services Offered'},
        {'image': 1, 'alt': 'Community screening', 'caption': 'Community Health', 'after': 'Access & Support'}
    ],
    'service-peer-support': [
        {'image': 2, 'alt': 'Peer counseling', 'caption': 'Peer Support', 'after': 'Lived experience creates'},
        {'image': 3, 'alt': 'Support services', 'caption': 'Counseling & Support', 'after': 'Support We Provide'},
        {'image': 1, 'alt': 'Community gathering', 'caption': 'Community Connection', 'after': 'Get Support'}
    ],
    'service-housing-support': [
        {'image': 2, 'alt': 'Housing support services', 'caption': 'Housing Solutions', 'after': 'Housing is health care'},
        {'image': 3, 'alt': 'Transitional housing', 'caption': 'Housing Pathways', 'after': 'Support Offered'},
        {'image': 1, 'alt': 'Stable housing', 'caption': 'Permanent Housing', 'after': 'Access Housing Help'}
    ],
    'service-cultural-healing': [
        {'image': 2, 'alt': 'Indigenous healing circle', 'caption': 'Healing Circle', 'after': 'Our Indigenous roots'},
        {'image': 3, 'alt': 'Cultural gathering', 'caption': 'Cultural Connection', 'after': 'Healing Offered'},
        {'image': 1, 'alt': 'Nature-based healing', 'caption': 'Land-Based Healing', 'after': 'Join Us'}
    ],
    'service-education-training': [
        {'image': 2, 'alt': 'Training program', 'caption': 'Education & Training', 'after': 'Education empowers'},
        {'image': 3, 'alt': 'Community education', 'caption': 'Community Training', 'after': 'Training Topics'},
        {'image': 1, 'alt': 'Peer instruction', 'caption': 'Peer Training', 'after': 'Get Trained'}
    ],
    'service-resource-navigation': [
        {'image': 2, 'alt': 'Resource navigation', 'caption': 'Navigation Services', 'after': 'Systems are complex'},
        {'image': 3, 'alt': 'Resource support', 'caption': 'Resource Pathways', 'after': 'Resources Accessed'},
        {'image': 1, 'alt': 'Success stories', 'caption': 'Success & Support', 'after': 'Start Navigating'}
    ],
    'service-mobile-outreach': [
        {'image': 2, 'alt': 'Mobile outreach team', 'caption': 'Mobile Services', 'after': 'Our mobile outreach'},
        {'image': 3, 'alt': 'Community outreach', 'caption': 'Community Engagement', 'after': 'What We Bring'},
        {'image': 1, 'alt': 'Neighborhood services', 'caption': 'Accessible Services', 'after': 'Schedule a Visit'}
    ]
}

def create_image_html(image_num, service_name, alt_text, caption, layout='left', width='40%'):
    """Create HTML for floating image"""
    image_url = f"https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/{image_num}.png"

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

def find_paragraph_with_text(content, search_text):
    """Find paragraph containing search text and return insertion point"""
    # Look for paragraph containing the search text
    pattern = f'<p[^>]*>.*?{re.escape(search_text)}.*?</p>'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        return match.end()
    return -1

def update_service_page(html_path, service_name):
    """Update service page with images distributed throughout content"""
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get image placements for this service
    placements = IMAGE_PLACEMENTS.get(service_name, [])
    if not placements:
        return False

    # Remove old gallery section if it exists
    content = re.sub(
        r'<!-- Gallery of Related Images -->.*?</div>\s*(?=</section>)',
        '',
        content,
        flags=re.DOTALL
    )

    # Track modifications by keeping offset into account
    offset = 0
    widths = ['35%', '40%', '45%']

    for idx, placement in enumerate(placements):
        image_num = placement['image']
        alt_text = placement['alt']
        caption = placement['caption']
        search_text = placement['after']
        layout = 'left' if idx % 2 == 0 else 'right'
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
    print("Adding Existing Images Throughout Service Page Content")
    print("="*70 + "\n")

    service_files = list(Path('HROC_Website_New').glob('service-*.html'))

    updated = 0
    for file_path in sorted(service_files):
        service_name = file_path.stem

        # Skip if not in placements
        if service_name not in IMAGE_PLACEMENTS:
            continue

        print(f"Updating {file_path.name}...", end=' ')

        try:
            if update_service_page(file_path, service_name):
                print("✓ Images added")
                updated += 1
            else:
                print("(no changes)")
        except Exception as e:
            print(f"✗ Error: {str(e)}")

    print("\n" + "="*70)
    print(f"Updated {updated} service pages")
    print("="*70 + "\n")
    print("Next steps:")
    print("  1. Deploy: bash deploy_to_truenas.sh")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
