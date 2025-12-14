#!/usr/bin/env python3
"""
Image Compression and Optimization Script
Converts all PNG images to WebP, compresses, and optimizes for web
"""

import os
from pathlib import Path
from PIL import Image
import shutil

BASE_DIR = Path(__file__).parent / 'HROC_Website_New'

def optimize_images_in_directory(directory, quality=85, method=6):
    """Optimize all PNG files in a directory to WebP"""
    png_files = list(directory.glob('**/*.png'))
    webp_count = 0
    png_compressed = 0

    for png_file in png_files:
        try:
            # Create WebP version
            webp_path = png_file.with_suffix('.webp')

            with Image.open(png_file) as img:
                # Handle transparency
                if img.mode == 'RGBA':
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[3])
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')

                # Save optimized WebP
                img.save(webp_path, 'WEBP', quality=quality, method=method)
                webp_count += 1
                print(f"[OK] {png_file.name} -> {webp_path.name} ({os.path.getsize(webp_path) / 1024:.1f}KB)")

            # Also recompress PNG for better compression
            with Image.open(png_file) as img:
                if img.mode == 'RGBA':
                    img.save(png_file, 'PNG', optimize=True)
                    png_compressed += 1
                    print(f"[OK] Optimized PNG: {png_file.name}")

        except Exception as e:
            print(f"[ERROR] Error processing {png_file.name}: {str(e)}")

    return webp_count, png_compressed

def main():
    print("=" * 60)
    print("[COMPRESS] Image Compression & Optimization")
    print("=" * 60)
    print()

    # Optimize images directory
    print("[DIR] Optimizing /images/generated/...")
    images_dir = BASE_DIR / 'images' / 'generated'
    if images_dir.exists():
        webp, png = optimize_images_in_directory(images_dir)
        print(f"  Generated {webp} WebP files, compressed {png} PNGs\n")

    # Optimize founders directory
    print("[DIR] Optimizing /images/founders/...")
    founders_dir = BASE_DIR / 'images' / 'founders'
    if founders_dir.exists():
        webp, png = optimize_images_in_directory(founders_dir)
        print(f"  Generated {webp} WebP files, compressed {png} PNGs\n")

    # Optimize generated_images directory
    print("[DIR] Optimizing /generated_images/...")
    generated_dir = BASE_DIR / 'generated_images'
    if generated_dir.exists():
        webp, png = optimize_images_in_directory(generated_dir)
        print(f"  Generated {webp} WebP files, compressed {png} PNGs\n")

    print("=" * 60)
    print("[OK] Optimization Complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
