#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add mixed layout images with varied widths to service pages
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Image insertion patterns for each service
# Format: (service_name, insertions)
# Each insertion: (search_pattern, image_html)

def add_images_to_wound_care():
    """Add mixed layout images to wound-care page"""
    file_path = Path('HROC_Website_New/service-wound-care.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insertion 1: After "Why Wound Care Matters" - left image 36%
    insertion1 = '''        </div>

        <!-- Image Left - 36% width -->
        <div class="service-image-left" style="width: 36%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-wound-care/2.png" alt="Professional Wound Assessment" loading="lazy">
          <figcaption>Expert Assessment</figcaption>
        </div>

        <div class="service-full-description">'''

    content = content.replace(
        '        </div>\n\n          <h2>How to Access Wound Care Services</h2>',
        insertion1 + '\n          <h2>How to Access Wound Care Services</h2>'
    )

    # Insertion 2: After access info - right image 44%
    insertion2 = '''        </div>

        <!-- Image Right - 44% width -->
        <div class="service-image-right" style="width: 44%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-wound-care/3.png" alt="Care & Training" loading="lazy">
          <figcaption>Care & Training</figcaption>
        </div>

        <div class="service-full-description">'''

    content = content.replace(
        '          </p>\n\n          <h2>Wound Care Education & Prevention</h2>',
        '          </p>' + insertion2 + '\n          <h2>Wound Care Education & Prevention</h2>'
    )

    # Insertion 3: After education section - left image 40%
    insertion3 = '''        </div>

        <!-- Image Left - 40% width -->
        <div class="service-image-left" style="width: 40%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-gallery/1.png" alt="Comprehensive Support" loading="lazy">
          <figcaption>Comprehensive Support</figcaption>
        </div>

        <div class="service-full-description">'''

    content = content.replace(
        '        </div>\n\n        <!-- Service Infographic -->',
        insertion3 + '\n        </div>\n\n        <!-- Service Infographic -->'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Added images to: service-wound-care.html")

def add_generic_images(service_name, image_ids=[2, 3, 4, 5]):
    """Add generic images to service pages"""
    file_path = Path(f'HROC_Website_New/{service_name}.html')

    if not file_path.exists():
        print(f"❌ File not found: {service_name}.html")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    image_widths = ['36%', '44%', '40%', '48%']
    image_positions = ['left', 'right', 'left', 'right']

    # Insert images before the infographic section
    # Find the last major heading before infographic

    insertion = '''        </div>

        <!-- Image Left - 36% width -->
        <div class="service-image-left" style="width: 36%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service}/2.png" alt="Service Overview" loading="lazy">
          <figcaption>Service Overview</figcaption>
        </div>

        <!-- Image Right - 44% width -->
        <div class="service-image-right" style="width: 44%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service}/3.png" alt="In Action" loading="lazy">
          <figcaption>In Action</figcaption>
        </div>

        <!-- Image Left - 40% width -->
        <div class="service-image-left" style="width: 40%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-gallery/1.png" alt="Community Care" loading="lazy">
          <figcaption>Community Care</figcaption>
        </div>

        <!-- Image Right - 48% width -->
        <div class="service-image-right" style="width: 48%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-gallery/2.png" alt="Support Services" loading="lazy">
          <figcaption>Support Services</figcaption>
        </div>

        <div class="service-full-description">'''

    # Try to insert before infographic section
    if '<!-- Service Infographic -->' in content:
        content = content.replace(
            '        </div>\n\n        <!-- Service Infographic -->',
            insertion.format(service=service_name) + '\n        </div>\n\n        <!-- Service Infographic -->'
        )
    else:
        # Fallback: insert before the Call to Action or footer
        if '<!-- Call to Action -->' in content:
            content = content.replace(
                '        </div>\n\n        <!-- Call to Action -->',
                insertion.format(service=service_name) + '\n        </div>\n\n        <!-- Call to Action -->'
            )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Added images to: {service_name}.html")
    return True

def main():
    print("\n" + "="*60)
    print("Adding mixed layout images to service pages")
    print("="*60 + "\n")

    # Special handling for wound-care
    add_images_to_wound_care()

    # Generic handling for remaining services
    remaining_services = [
        'service-health-screening',
        'service-peer-support',
        'service-housing-support',
        'service-cultural-healing',
        'service-education-training',
        'service-resource-navigation'
    ]

    for service in remaining_services:
        add_generic_images(service)

    print("\n" + "="*60)
    print("Successfully added mixed layout images to all pages")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
