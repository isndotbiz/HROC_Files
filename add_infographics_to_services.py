#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add infographic sections to all service pages
"""
import sys
import io
import re
from pathlib import Path

# Fix UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Service-infographic mapping
SERVICES = {
    'service-syringe-exchange': {
        'index': 2,
        'title': 'Harm Reduction Essentials Guide'
    },
    'service-wound-care': {
        'index': 2,
        'title': 'Wound Care Guide'
    },
    'service-health-screening': {
        'index': 2,
        'title': 'Health Screening Reference'
    },
    'service-peer-support': {
        'index': 2,
        'title': 'Peer Support Resources'
    },
    'service-housing-support': {
        'index': 2,
        'title': 'Housing Navigation Guide'
    },
    'service-cultural-healing': {
        'index': 2,
        'title': 'Cultural Healing Framework'
    },
    'service-education-training': {
        'index': 2,
        'title': 'Training Program Overview'
    },
    'service-resource-navigation': {
        'index': 2,
        'title': 'Resource Navigation Pathways'
    }
}

def add_infographic(service_name, title):
    """Add infographic section to service page"""
    file_path = Path(f'HROC_Website_New/{service_name}.html')

    if not file_path.exists():
        print(f"File not found: {service_name}.html")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if infographic section already exists
    if 'service-infographic-section' in content:
        print(f"Infographic already exists in {service_name}.html")
        return True

    # Pattern to find where to insert the infographic
    # Looking for the closing </div> of service-full-description before Program Components
    # More flexible pattern that handles variable whitespace
    pattern = r'(          <p>.*?</p>)\s+(          <h2>Program Components</h2>)'

    if not re.search(pattern, content, re.DOTALL):
        print(f"Could not find insertion point in {service_name}.html")
        return False

    # Replacement: add infographic section between last <p> and <h2>Program Components</h2>
    infographic_html = f'''

        <!-- Service Infographic -->
        <div class="service-infographic-section">
          <h2>{title}</h2>
          <img src="https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{service_name}/2.png" alt="{service_name.replace('-', ' ').title()} Educational Guide and Reference" loading="lazy">
        </div>

        <!-- Continue Service Description -->
        '''

    # Replace the pattern with content + infographic + h2
    def replacer(match):
        return match.group(1) + infographic_html + match.group(2)

    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Updated: {service_name}.html")
    return True

def main():
    print("\n" + "="*60)
    print("Adding Infographics to Service Pages")
    print("="*60 + "\n")

    updated = 0
    for service_name, config in SERVICES.items():
        if add_infographic(service_name, config['title']):
            updated += 1

    print("\n" + "="*60)
    print(f"Updated {updated}/{len(SERVICES)} service pages")
    print("="*60)

if __name__ == '__main__':
    main()
