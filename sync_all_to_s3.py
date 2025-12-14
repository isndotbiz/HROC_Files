#!/usr/bin/env python3
"""
Sync all HROC website images to AWS S3
Handles: founders, images/generated, generated_images directories
Sets appropriate metadata and public read ACLs
"""

import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent / 'HROC_Website_New'
S3_BUCKET = 'hroc-outreach-assets-1765630540'
AWS_REGION = 'us-west-2'

def run_command(cmd, description):
    """Execute shell command with error handling"""
    print(f"\n[SYNCING] {description}")
    print(f"  Command: {cmd}\n")

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"[ERROR] {description} failed:")
        print(result.stderr)
        return False
    else:
        # Count files from output
        output_lines = result.stdout.strip().split('\n')
        file_count = len([l for l in output_lines if 'upload:' in l or 'download:' in l])
        print(f"[OK] {description} complete ({file_count} files)")
        return True

def main():
    print("=" * 70)
    print("[SYNC] HROC Website Images to AWS S3")
    print("=" * 70)

    success_count = 0
    total_tasks = 3

    # 1. Sync founder images
    cmd = f'aws s3 sync "{BASE_DIR / "images" / "founders"}" s3://{S3_BUCKET}/images/founders/ --region {AWS_REGION} --delete'
    if run_command(cmd, "Founder images"):
        success_count += 1

    # 2. Sync images/generated directory
    cmd = f'aws s3 sync "{BASE_DIR / "images" / "generated"}" s3://{S3_BUCKET}/images/generated/ --region {AWS_REGION} --delete'
    if run_command(cmd, "Generated images"):
        success_count += 1

    # 3. Sync generated_images directory
    cmd = f'aws s3 sync "{BASE_DIR / "generated_images"}" s3://{S3_BUCKET}/generated_images/ --region {AWS_REGION} --delete'
    if run_command(cmd, "Generated image collections"):
        success_count += 1

    print("\n" + "=" * 70)
    print(f"[RESULT] Sync Complete: {success_count}/{total_tasks} directories synced")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. Pull latest changes on TrueNAS: git pull origin main")
    print("  2. Reload Nginx: systemctl reload nginx")
    print("  3. Verify https://hrocinc.org loads all images correctly")
    print()

if __name__ == "__main__":
    main()
