#!/usr/bin/env python3
"""Test FLUX.1 with ControlNet for angled portraits."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

src = "j1.webp"
model = 'fal-ai/flux-general'

# Test 5 different angle prompts with ControlNet pose guidance
test_angles = [
    {
        "name": "test_left_45",
        "prompt": "Professional portrait, person looking 45 degrees to the left, studio lighting, clear face, sharp focus",
    },
    {
        "name": "test_right_45", 
        "prompt": "Professional portrait, person looking 45 degrees to the right, studio lighting, clear face, sharp focus",
    },
    {
        "name": "test_left_profile",
        "prompt": "Professional portrait, person in left profile view 90 degrees, studio lighting, sharp facial details",
    },
    {
        "name": "test_right_profile",
        "prompt": "Professional portrait, person in right profile view 90 degrees, studio lighting, sharp facial details",
    },
    {
        "name": "test_3quarter_left",
        "prompt": "Professional portrait, person at 3/4 angle looking left, studio lighting, elegant pose, clear features",
    },
]

print("Testing FLUX.1 [dev] with ControlNet for angled portraits")
print(f"Source: {src}\n")

with open(src, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode()
uri = f'data:image/webp;base64,{b64}'

count = 0
for test in test_angles:
    name = test["name"]
    prompt = test["prompt"]
    
    try:
        print(f"Generating: {name}")
        print(f"  Prompt: {prompt[:60]}...")
        
        # Use FLUX with image-to-image for better control
        result = fal_client.run(
            'fal-ai/flux-general',
            arguments={
                'prompt': prompt,
                'image_url': uri,
                'image_size': 'portrait_4_3',  # 1024x1280
                'num_inference_steps': 30,
                'guidance_scale': 7.5,
                'strength': 0.7,  # Balance between prompt and reference
                'seed': 42 + count,
            }
        )
        
        if result and 'images' in result and result['images']:
            img_data = requests.get(result['images'][0]['url'], timeout=30).content
            out_path = f'generated_portrait_dataset/flux_{name}.webp'
            with open(out_path, 'wb') as f:
                f.write(img_data)
            print(f"  ✓ Saved: flux_{name}.webp\n")
            count += 1
        else:
            print(f"  ✗ Failed - no images returned\n")
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:70]}\n")

print(f"\n✓ Generated {count}/5 test images")
print("Check the flux_test_*.webp files to verify quality and angles")
