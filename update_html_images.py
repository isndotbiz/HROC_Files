#!/usr/bin/env python3
"""
Update HTML files to reference newly generated images in S3
"""

import re
from pathlib import Path

# Configuration
S3_BUCKET = 'hroc-outreach-assets-1765630540'
S3_REGION = 'us-west-2'
S3_BASE_URL = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com"

# Image mappings for each service page
SERVICE_IMAGE_MAPPING = {
    'service-overdose-prevention': {
        'primary': 'generated_images/service-overdose-prevention/1.png',
        'gallery': [
            'generated_images/service-overdose-prevention/2.png',
            'generated_images/service-overdose-prevention/3.png',
            'generated_images/service-gallery-image/1.png',
        ]
    },
    'service-syringe-exchange': {
        'primary': 'generated_images/service-syringe-exchange/1.png',
        'gallery': [
            'generated_images/service-syringe-exchange/2.png',
            'generated_images/service-syringe-exchange/3.png',
            'generated_images/service-gallery-image/2.png',
        ]
    },
    'service-wound-care': {
        'primary': 'generated_images/service-wound-care/1.png',
        'gallery': [
            'generated_images/service-wound-care/2.png',
            'generated_images/service-wound-care/3.png',
            'generated_images/service-gallery-image/3.png',
        ]
    },
    'service-health-screening': {
        'primary': 'generated_images/service-health-screening/1.png',
        'gallery': [
            'generated_images/service-health-screening/2.png',
            'generated_images/service-health-screening/3.png',
            'generated_images/service-gallery-image/4.png',
        ]
    },
    'service-peer-support': {
        'primary': 'generated_images/service-peer-support/1.png',
        'gallery': [
            'generated_images/service-peer-support/2.png',
            'generated_images/service-peer-support/3.png',
            'generated_images/service-gallery-image/5.png',
        ]
    },
    'service-housing-support': {
        'primary': 'generated_images/service-housing-support/1.png',
        'gallery': [
            'generated_images/service-housing-support/2.png',
            'generated_images/service-housing-support/3.png',
            'generated_images/service-gallery-image/1.png',
        ]
    },
    'service-cultural-healing': {
        'primary': 'generated_images/service-cultural-healing/1.png',
        'gallery': [
            'generated_images/service-cultural-healing/2.png',
            'generated_images/service-cultural-healing/3.png',
            'generated_images/service-gallery-image/2.png',
        ]
    },
    'service-education-training': {
        'primary': 'generated_images/service-education-training/1.png',
        'gallery': [
            'generated_images/service-education-training/2.png',
            'generated_images/service-education-training/3.png',
            'generated_images/service-gallery-image/3.png',
        ]
    },
    'service-resource-navigation': {
        'primary': 'generated_images/service-resource-navigation/1.png',
        'gallery': [
            'generated_images/service-resource-navigation/2.png',
            'generated_images/service-resource-navigation/3.png',
            'generated_images/service-gallery-image/4.png',
        ]
    }
}

def update_service_pages():
    """Update all service pages with new image references"""

    html_dir = Path('HROC_Website_New')
    updated_count = 0

    for service_name, images in SERVICE_IMAGE_MAPPING.items():
        html_file = html_dir / f"{service_name}.html"

        if not html_file.exists():
            print(f"⚠ File not found: {service_name}.html")
            continue

        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Update primary image
        primary_url = f"{S3_BASE_URL}/images/{images['primary']}"
        # Replace the primary service image
        content = re.sub(
            r'<div class="service-primary-image">.*?<img[^>]*src="[^"]*"',
            f'<div class="service-primary-image"><img src="{primary_url}"',
            content,
            flags=re.DOTALL
        )

        # Update gallery images
        gallery_images = images['gallery']
        photo_items = re.findall(r'<figure class="photo-item">.*?</figure>', content, re.DOTALL)

        for idx, photo_item in enumerate(photo_items[:len(gallery_images)]):
            old_url_match = re.search(r'src="([^"]*)"', photo_item)
            if old_url_match:
                new_url = f"{S3_BASE_URL}/images/{gallery_images[idx]}"
                content = content.replace(
                    photo_item,
                    photo_item.replace(old_url_match.group(1), new_url)
                )

        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated: {service_name}.html")
            updated_count += 1
        else:
            print(f"⚠ No changes needed: {service_name}.html")

    return updated_count

def update_index_html():
    """Update index.html with new impact story and service thumbnail images"""

    index_file = Path('HROC_Website_New/index.html')

    if not index_file.exists():
        print("ERROR: index.html not found")
        return False

    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Update impact story images
    impact_stories = [
        {
            'pattern': r'<img[^>]*alt="[^"]*First Founder[^"]*"[^>]*src="[^"]*"',
            'new_image': f"{S3_BASE_URL}/images/generated_images/impact-story-hero-1.png"
        },
        {
            'pattern': r'<img[^>]*alt="[^"]*Second Founder[^"]*"[^>]*src="[^"]*"',
            'new_image': f"{S3_BASE_URL}/images/generated_images/impact-story-hero-2.png"
        },
        {
            'pattern': r'<img[^>]*alt="[^"]*Third Founder[^"]*"[^>]*src="[^"]*"',
            'new_image': f"{S3_BASE_URL}/images/generated_images/impact-story-hero-3.png"
        }
    ]

    for story in impact_stories:
        match = re.search(story['pattern'], content)
        if match:
            old_img_tag = match.group(0)
            new_img_tag = re.sub(
                r'src="[^"]*"',
                f'src="{story["new_image"]}"',
                old_img_tag
            )
            content = content.replace(old_img_tag, new_img_tag)

    # Update service thumbnail images in "Our Services" section
    # This will replace placeholder images with generated service images
    service_thumbnails = {
        'overdose-prevention': f"{S3_BASE_URL}/images/generated_images/service-overdose-prevention/1.png",
        'syringe-exchange': f"{S3_BASE_URL}/images/generated_images/service-syringe-exchange/1.png",
        'wound-care': f"{S3_BASE_URL}/images/generated_images/service-wound-care/1.png",
        'health-screening': f"{S3_BASE_URL}/images/generated_images/service-health-screening/1.png",
        'peer-support': f"{S3_BASE_URL}/images/generated_images/service-peer-support/1.png",
        'housing-support': f"{S3_BASE_URL}/images/generated_images/service-housing-support/1.png",
        'cultural-healing': f"{S3_BASE_URL}/images/generated_images/service-cultural-healing/1.png",
        'education-training': f"{S3_BASE_URL}/images/generated_images/service-education-training/1.png",
        'resource-navigation': f"{S3_BASE_URL}/images/generated_images/service-resource-navigation/1.png",
    }

    for service_name, image_url in service_thumbnails.items():
        # Find service card and update its image
        pattern = f'<a href="service-{service_name}.html"[^>]*>.*?<img[^>]*src="[^"]*"'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            old_tag = match.group(0)
            new_tag = re.sub(r'src="[^"]*"', f'src="{image_url}"', old_tag)
            content = content.replace(old_tag, new_tag)

    if content != original_content:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ Updated: index.html")
        return True
    else:
        print("⚠ No changes needed: index.html")
        return False

def main():
    print("\n" + "="*60)
    print("Update HTML Image References")
    print("="*60 + "\n")

    # Update service pages
    print("Updating service pages...")
    service_count = update_service_pages()

    print("\nUpdating index.html...")
    index_updated = update_index_html()

    print("\n" + "="*60)
    print("Summary")
    print("="*60)
    print(f"Service pages updated: {service_count}")
    print(f"Index page updated: {'Yes' if index_updated else 'No'}")
    print("="*60)

    print("\n✓ HTML files updated successfully!")
    print("Next steps:")
    print("1. Deploy updated HTML files to TrueNAS")
    print("2. Verify all images load correctly in browser")

if __name__ == "__main__":
    main()
