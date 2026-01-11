#!/usr/bin/env python3
"""Test FLUX Kontext - better for preserving facial identity."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

sources = ["j1.webp", "l1.webp", "b1.webp"]

# Test with Kontext Pro - designed for reference image preservation
angle_prompts = [
    ("left_45", "head turned 45 degrees to the left"),
    ("right_45", "head turned 45 degrees to the right"),
    ("left_profile", "left profile view"),
    ("right_profile", "right profile view"),
    ("3quarter", "3/4 view angle"),
]

print("Testing FLUX.1 Kontext Pro (better reference preservation)\n")
total_count = 0

for src in sources:
    if not os.path.exists(src):
        print(f"Missing: {src}")
        continue
    
    stem = Path(src).stem
    print(f"=== {stem} ===")
    
    with open(src, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    uri = f'data:image/webp;base64,{b64}'
    
    for angle_name, angle_desc in angle_prompts:
        try:
            print(f"  {angle_name}...", end=" ")
            
            # FLUX Kontext Pro - better for identity preservation
            result = fal_client.run(
                'fal-ai/flux-pro/v1.1-ultra',
                arguments={
                    'prompt': f"Professional portrait, {angle_desc}, studio lighting",
                    'image_url': uri,
                    'strength': 0.9,  # Very high - keep facial features
                }
            )
            
            if result and 'images' in result and result['images']:
                img_data = requests.get(result['images'][0]['url'], timeout=30).content
                out_path = f'generated_portrait_dataset/{stem}_kontext_{angle_name}.webp'
                with open(out_path, 'wb') as f:
                    f.write(img_data)
                print("✓")
                total_count += 1
            else:
                print("✗")
                
        except Exception as e:
            print(f"✗ Error")
    
    print()

print(f"\n✓ Generated {total_count}/15 test images with Kontext")
