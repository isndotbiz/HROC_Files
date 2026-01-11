#!/usr/bin/env python3
"""Test FLUX with all three people at different angles."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

sources = ["j1.webp", "l1.webp", "b1.webp"]

# Test 5 angles per person
angle_prompts = [
    ("left_45", "Head turned 45 degrees to the left, studio lighting, professional portrait, preserve facial features"),
    ("right_45", "Head turned 45 degrees to the right, studio lighting, professional portrait, preserve facial features"),
    ("left_profile", "Left profile view 90 degrees, studio lighting, professional portrait, sharp profile"),
    ("right_profile", "Right profile view 90 degrees, studio lighting, professional portrait, sharp profile"),
    ("3quarter", "3/4 view angle, studio lighting, professional portrait, preserve all facial features"),
]

print("Testing FLUX.1 with all three people at different angles\n")
total_count = 0

for src in sources:
    if not os.path.exists(src):
        print(f"Missing: {src}")
        continue
    
    stem = Path(src).stem
    print(f"=== Generating {stem} ===")
    
    with open(src, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    uri = f'data:image/webp;base64,{b64}'
    
    for angle_name, prompt in angle_prompts:
        try:
            print(f"  {angle_name}...", end=" ")
            
            result = fal_client.run(
                'fal-ai/flux-general',
                arguments={
                    'prompt': prompt,
                    'image_url': uri,
                    'image_size': 'portrait_4_3',
                    'num_inference_steps': 30,
                    'guidance_scale': 7.5,
                    'strength': 0.85,  # Preserve facial features
                    'seed': hash((stem, angle_name)) % 1000000,
                }
            )
            
            if result and 'images' in result and result['images']:
                img_data = requests.get(result['images'][0]['url'], timeout=30).content
                out_path = f'generated_portrait_dataset/{stem}_flux_{angle_name}.webp'
                with open(out_path, 'wb') as f:
                    f.write(img_data)
                print("✓")
                total_count += 1
            else:
                print("✗")
                
        except Exception as e:
            print(f"✗ {str(e)[:40]}")
    
    print()

print(f"\n✓ Generated {total_count}/15 test images")
print(f"Cost: ~${total_count * 0.075:.2f}")
