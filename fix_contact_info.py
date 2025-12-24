#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix contact information across all service pages
"""
import sys
import io
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Old contact info to replace
OLD_CONTACTS = {
    'admin@hrocinc.org': ['admin@healingrootsoutreachcollective.org'],
    '2536789186': ['2536789186', '+12536789186', '(253) 678-9186'],
    'Pierce County, WA': ['King & Pierce Counties, Washington', 'King and Pierce Counties, WA'],
}

# New contact info
NEW_EMAIL = 'admin@hrocinc.org'
NEW_PHONE = '253-881-7377'
NEW_PHONE_FORMATTED = '(253) 881-7377'
NEW_PHONE_LINK = '+12538817377'
NEW_ADDRESS = '2122 S 272ND ST APT B111, Kent, WA 98032'
NEW_SERVICE_AREA = 'King and Pierce Counties, Washington'

def fix_contact_in_file(file_path):
    """Fix contact information in a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace old emails
    content = content.replace('admin@healingrootsoutreachcollective.org', NEW_EMAIL)
    content = content.replace('admin@hrocinc.org', NEW_EMAIL)  # Ensure consistent

    # Replace old phone numbers (be careful with tel: and SMS links)
    content = re.sub(r'href=["\']tel:\+?12536789186["\']', f'href="tel:{NEW_PHONE_LINK}"', content)
    content = re.sub(r'href=["\']sms:\+?12536789186["\']', f'href="sms:{NEW_PHONE_LINK}"', content)
    content = content.replace('+12536789186', NEW_PHONE_LINK)
    content = content.replace('(253) 678-9186', NEW_PHONE_FORMATTED)
    content = content.replace('2536789186', NEW_PHONE.replace('-', ''))

    # Fix service area descriptions
    content = content.replace('King & Pierce Counties, Washington', NEW_SERVICE_AREA)
    content = content.replace('King and Pierce Counties, WA', NEW_SERVICE_AREA)
    content = content.replace('King & Pierce Counties, WA', NEW_SERVICE_AREA)
    content = content.replace('Pierce County, WA', NEW_SERVICE_AREA)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("\n" + "="*70)
    print("Fixing contact information across all service pages")
    print("="*70 + "\n")

    print(f"New Contact Info:")
    print(f"  Email: {NEW_EMAIL}")
    print(f"  Phone: {NEW_PHONE}")
    print(f"  Address: {NEW_ADDRESS}")
    print(f"  Service Area: {NEW_SERVICE_AREA}\n")

    service_files = list(Path('HROC_Website_New').glob('service-*.html'))

    fixed = 0
    for file_path in sorted(service_files):
        if fix_contact_in_file(file_path):
            print(f"✓ Fixed: {file_path.name}")
            fixed += 1
        else:
            print(f"  (no changes needed): {file_path.name}")

    print("\n" + "="*70)
    print(f"Fixed {fixed} service pages")
    print("="*70 + "\n")

if __name__ == '__main__':
    main()
