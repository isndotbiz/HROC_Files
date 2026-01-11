#!/usr/bin/env python3
"""Test multiple-angles model for better head turns."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

src = "j1.webp"
model = 'fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles'

# Better angle prompts for head turns
test_prompts = [
    "Head turned 45 degrees left",
    "Head turned 45 degrees right",
    "Head turned 90 degrees left, full left profile",
    "Head turned 90 degrees right, full right profile",
    "Head turned 60 degrees left",
]

print(f"Testing {model}")
print(f"Testing on: {src}\n")

with open(src, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()

for i, prompt in enumerate(test_prompts, 1):
    try:
        print(f"Test {i}: {prompt}...")
        r = fal_client.run(model, arguments={
            'image_urls': [f'data:image/webp;base64,{b64}'],
            'prompt': prompt,
            'num_inference_steps': 30,
            'guidance_scale': 7.5,
        })
        
        if r and 'images' in r and r['images']:
            img_data = requests.get(r['images'][0]['url'], timeout=30).content
            out_path = f'generated_portrait_dataset/j1_test_angle_{i}.webp'
            with open(out_path, 'wb') as f:
                f.write(img_data)
            print(f"  ✓ Saved: j1_test_angle_{i}.webp\n")
        else:
            print(f"  ✗ No images returned\n")
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:60]}\n")

print("Test complete! Check the 5 test images to verify angles.")
