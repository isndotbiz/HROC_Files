#!/usr/bin/env python3
"""
Comprehensive image verification and S3 sync script for HROC website
Ensures all images referenced in HTML files exist locally before syncing to S3
"""

import os
import sys
import subprocess
from pathlib import Path
from urllib.parse import urlparse

# Configuration
BASE_DIR = Path(__file__).parent / 'HROC_Website_New'
S3_BUCKET = 'hroc-website-20251230043930'
AWS_REGION = 'us-east-1'

# Image paths to check
IMAGE_DIRS = {
    'founders': BASE_DIR / 'images' / 'founders',
    'generated': BASE_DIR / 'images' / 'generated',
    'generated_images': BASE_DIR / 'generated_images',
}

# Image references from HTML
REQUIRED_IMAGES = {
    # Index.html service icons
    'images/generated/service-overdose-prevention.webp',
    'images/generated/service-syringe-exchange.webp',
    'images/generated/service-wound-care.webp',
    'images/generated/service-health-screening.webp',
    'images/generated/service-peer-support.webp',
    'images/generated/service-housing-support.webp',
    'images/generated/photo-healing-circle.webp',
    'images/generated/service-education-training.webp',
    'images/generated/service-resource-navigation.webp',
    # Community photos
    'generated_images/community_photos/community_01_diverse_group_smiling.webp',
    'generated_images/community_photos/community_02_peer_counselor_listening.webp',
    'generated_images/community_photos/community_03_elder_and_youth.webp',
    # Founder images
    'images/founders/bri_main.webp',
    'images/founders/lilly_main.webp',
    'images/founders/jonathan_main.webp',
    'images/founders/a/alicia_hero_real.webp',
    # Bri page images
    'images/founders/b/bri_professional_01_2.webp',
    'images/founders/b/bri_varied_03.webp',
    'images/founders/b/qwen_bri_02_business_casual_outdoor.webp',
    'images/founders/b/bri_varied_05.webp',
    'images/founders/b/qwen_bri_01_professional_office_laptop.webp',
    'images/founders/b/bri_professional_08_2.webp',
    # Lilly page images
    'images/founders/l/lilly_varied_03.webp',
    'images/founders/l/lilly_varied_02.webp',
    'images/founders/l/lilly_varied_05.webp',
    'images/founders/l/lilly_varied_08.webp',
    'images/founders/l/lilly_varied_07.webp',
    'images/founders/l/qwen_lilly_07_modern_office_desk.webp',
    # Jonathan page images
    'images/founders/j/jonathan_urban_outdoor_2.webp',
    'images/founders/j/jonathan_varied_01.webp',
    'images/founders/j/jonathan_varied_03.webp',
    'images/founders/j/jonathan_varied_05.webp',
    'images/founders/j/jonathan_varied_07.webp',
    # Alicia page images
    'images/founders/a/alicia_community_real.webp',
    'images/founders/a/alicia_whiteboard_real.webp',
    'images/founders/a/alicia_office_real.webp',
    'images/founders/a/alicia_varied_01_real.webp',
}

def verify_images():
    """Verify all required images exist locally"""
    print("=" * 80)
    print("[VERIFY] Checking for all required images...")
    print("=" * 80)
    
    missing_images = []
    found_count = 0
    
    for img_path in sorted(REQUIRED_IMAGES):
        full_path = BASE_DIR / img_path
        exists = full_path.exists()
        status = "✓" if exists else "✗"
        
        if exists:
            found_count += 1
            size_kb = full_path.stat().st_size / 1024
            print(f"  {status} {img_path} ({size_kb:.1f} KB)")
        else:
            missing_images.append(img_path)
            print(f"  {status} {img_path} [MISSING]")
    
    print("\n" + "=" * 80)
    print(f"[RESULT] Found {found_count}/{len(REQUIRED_IMAGES)} required images")
    print("=" * 80)
    
    if missing_images:
        print(f"\n[WARNING] Missing {len(missing_images)} images:")
        for img in missing_images:
            print(f"  - {img}")
        return False
    
    print("\n✓ All required images present locally!")
    return True

def get_all_local_images():
    """Get all webp images currently in the image directories"""
    local_images = {}
    
    for dir_name, dir_path in IMAGE_DIRS.items():
        if dir_path.exists():
            local_images[dir_name] = []
            for webp_file in dir_path.rglob('*.webp'):
                relative_path = webp_file.relative_to(BASE_DIR)
                local_images[dir_name].append(str(relative_path))
    
    return local_images

def list_local_images():
    """List all local images"""
    print("\n" + "=" * 80)
    print("[INFO] All local images by category:")
    print("=" * 80)
    
    local_images = get_all_local_images()
    total = 0
    
    for category, images in sorted(local_images.items()):
        print(f"\n  {category.upper()} ({len(images)} files):")
        for img in sorted(images):
            total += 1
            full_path = BASE_DIR / img
            size_kb = full_path.stat().st_size / 1024
            print(f"    - {img} ({size_kb:.1f} KB)")
    
    print(f"\n  TOTAL: {total} images")
    return total

def sync_to_s3():
    """Sync all images to S3"""
    print("\n" + "=" * 80)
    print("[SYNC] Starting S3 synchronization...")
    print("=" * 80)
    
    commands = [
        {
            'name': 'Founder images',
            'src': BASE_DIR / 'images' / 'founders',
            'dest': f's3://{S3_BUCKET}/images/founders/'
        },
        {
            'name': 'Generated service images',
            'src': BASE_DIR / 'images' / 'generated',
            'dest': f's3://{S3_BUCKET}/images/generated/'
        },
        {
            'name': 'Generated image collections',
            'src': BASE_DIR / 'generated_images',
            'dest': f's3://{S3_BUCKET}/generated_images/'
        },
    ]
    
    success_count = 0
    
    for cmd in commands:
        print(f"\n[SYNC] {cmd['name']}...")
        print(f"  Source: {cmd['src']}")
        print(f"  Destination: {cmd['dest']}")
        
        # Build AWS CLI command with delete to clean up old files
        aws_cmd = (
            f'aws s3 sync "{cmd["src"]}" "{cmd["dest"]}" '
            f'--region {AWS_REGION} --delete'
        )
        
        try:
            result = subprocess.run(aws_cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Count uploads from output
                upload_count = result.stdout.count('upload:')
                delete_count = result.stdout.count('delete:')
                print(f"  ✓ Success ({upload_count} uploaded, {delete_count} deleted)")
                success_count += 1
            else:
                print(f"  ✗ Failed")
                print(f"  Error: {result.stderr}")
                return False
                
        except Exception as e:
            print(f"  ✗ Exception: {e}")
            return False
    
    print("\n" + "=" * 80)
    print(f"[RESULT] S3 Sync Complete: {success_count}/{len(commands)} successful")
    print("=" * 80)
    
    return success_count == len(commands)

def main():
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " HROC Website Image Verification & S3 Sync".center(78) + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Step 1: Verify required images
    if not verify_images():
        print("\n[ERROR] Missing required images. Fix before syncing.")
        sys.exit(1)
    
    # Step 2: List all local images
    total_images = list_local_images()
    
    # Step 3: Sync to S3
    if not sync_to_s3():
        print("\n[ERROR] S3 sync failed!")
        sys.exit(1)
    
    # Success!
    print("\n" + "=" * 80)
    print("[SUCCESS] All images verified and synced to S3!")
    print("=" * 80)
    print("\nNext steps:")
    print("  1. Verify images load at https://hrocinc.org")
    print("  2. Check all founder pages (bri.html, lilly.html, jonathan.html, alicia.html)")
    print("  3. Commit changes: git add -A && git commit -m 'Verify and sync all images'")
    print("  4. Push to GitHub: git push origin main")
    print()

if __name__ == "__main__":
    main()
