#!/usr/bin/env python3
"""Generate 10 turned angles (left/right) for each character."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

srcs = ["j1.webp", "l1.webp", "b1.webp"]

# 10 specific turned angles - no center
angle_prompts = [
    "Head turned 30 degrees to the right",
    "Head turned 60 degrees to the right", 
    "Head turned 75 degrees to the right, near profile",
    "Head turned 45 degrees to the left",
    "Head turned 80 degrees to the left, almost profile",
    "Head turned 15 degrees to the right, slight angle",
    "Head turned 50 degrees to the left",
    "Head turned 70 degrees to the right, close to profile",
    "Head turned 25 degrees to the left, subtle turn",
    "Head turned 55 degrees to the right",
]

model = 'fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles'
count = 0

for src in srcs:
    if not os.path.exists(src):
        print(f"Missing: {src}")
        continue
    
    stem = Path(src).stem
    print(f"\n{stem} - Generating turned angles...")
    
    with open(src, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    
    for i, prompt in enumerate(angle_prompts, 1):
        try:
            r = fal_client.run(model, arguments={
                'image_urls': [f'data:image/webp;base64,{b64}'],
                'prompt': prompt,
                'num_inference_steps': 30,
                'guidance_scale': 7.5,
            })
            
            if r and 'images' in r and r['images']:
                img_data = requests.get(r['images'][0]['url'], timeout=30).content
                out_path = f'generated_portrait_dataset/{stem}_turned_{i:02d}.webp'
                with open(out_path, 'wb') as f:
                    f.write(img_data)
                print(f"  ✓ turned_{i:02d} - {prompt}")
                count += 1
            else:
                print(f"  ✗ turned_{i:02d} - Failed")
        except Exception as e:
            print(f"  ✗ turned_{i:02d} - {str(e)[:40]}")

print(f"\n✓ Generated {count} turned angle images")
