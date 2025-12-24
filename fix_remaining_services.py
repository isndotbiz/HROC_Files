#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix remaining service pages - remove gallery grid and add mixed layout images
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

SERVICES_TO_FIX = [
    'service-wound-care',
    'service-health-screening',
    'service-peer-support',
    'service-housing-support',
    'service-cultural-healing',
    'service-education-training',
    'service-resource-navigation'
]

def fix_service_page(service_name):
    """Remove gallery grid and add basic image structure"""
    file_path = Path(f'HROC_Website_New/{service_name}.html')

    if not file_path.exists():
        print(f"❌ File not found: {service_name}.html")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove the entire gallery grid section
    gallery_pattern = r'<!-- Gallery of Related Images -->.*?</div>\s*'
    content = re.sub(gallery_pattern, '', content, flags=re.DOTALL)

    # Step 2: Remove/fix duplicate infographic section (some have it listed twice)
    # The infographic should stay, we just want to remove the gallery

    # Write the fixed content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Fixed: {service_name}.html - Removed old gallery grid")
    return True

def main():
    print("\n" + "="*60)
    print("Fixing remaining service pages")
    print("="*60 + "\n")

    fixed = 0
    for service_name in SERVICES_TO_FIX:
        if fix_service_page(service_name):
            fixed += 1

    print("\n" + "="*60)
    print(f"Fixed {fixed}/{len(SERVICES_TO_FIX)} service pages")
    print("="*60 + "\n")
    print("Next step: Add mixed layout images to each page manually")

if __name__ == '__main__':
    main()
