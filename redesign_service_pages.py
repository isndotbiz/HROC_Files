#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Redesign all service pages with mixed image/text layout and varied widths
"""
import sys
import io
import re
from pathlib import Path

# Fix UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Service pages to update (excluding the already done ones)
SERVICES = [
    'service-wound-care',
    'service-health-screening',
    'service-peer-support',
    'service-housing-support',
    'service-cultural-healing',
    'service-education-training',
    'service-resource-navigation'
]

def redesign_service_page(service_name):
    """Redesign a service page with mixed layout and varied image widths"""
    file_path = Path(f'HROC_Website_New/{service_name}.html')

    if not file_path.exists():
        print(f"File not found: {service_name}.html")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the old gallery grid at the bottom
    gallery_pattern = r'\s*<!-- Gallery of Related Images -->.*?</div>\s*'
    content = re.sub(gallery_pattern, '\n\n        ', content, flags=re.DOTALL)

    # Insert images throughout the page with varied widths
    # We'll insert them at strategic points after key sections

    # Pattern 1: After "Why ... Matters" section - insert first image (left, 36%)
    pattern1 = r'(          <p>.*?</p>\s*)(          <h2>(?:How to Access|What is|Program|Services Offered|Key))'

    image_html_left_36 = f'''
        </div>

        <!-- Image Left - 36% width -->
        <div class="service-image-left" style="width: 36%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/2.png" alt="Service Overview" loading="lazy">
          <figcaption>Service Overview</figcaption>
        </div>

        <div class="service-full-description">
          \\2'''

    if re.search(pattern1, content, re.DOTALL):
        content = re.sub(pattern1, image_html_left_36, content, flags=re.DOTALL, count=1)

    # Pattern 2: After first service section - insert second image (right, 44%)
    # Find and insert after "How to Access" intro
    pattern2 = r'(          <p>.*?mobile outreach.*?</p>\s*)(          <p>If you have a wound|          <p>To find our current|          <p>Accessing.*?simple)'

    image_html_right_44 = f'''
        </div>

        <!-- Image Right - 44% width -->
        <div class="service-image-right" style="width: 44%;">
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/3.png" alt="In Action" loading="lazy">
          <figcaption>In Action</figcaption>
        </div>

        <div class="service-full-description">
          \\2'''

    if re.search(pattern2, content, re.DOTALL):
        content = re.sub(pattern2, image_html_right_44, content, flags=re.DOTALL, count=1)

    # Pattern 3: After main content - insert third image (left, 40%)
    pattern3 = r'(          <p>.*?</p>\s*)(          <h2>(?:Get Involved|Community Impact|Contact|Additional Resources))