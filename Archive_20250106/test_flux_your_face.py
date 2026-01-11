#!/usr/bin/env python3
"""Test FLUX with your actual face at different angles."""
import os, base64, fal_client, requests
from pathlib import Path

os.environ['FAL_KEY'] = os.getenv('FAL_KEY')
Path('generated_portrait_dataset').mkdir(exist_ok=True)

src = "j1.webp"
model = 'fal-ai/flux-general'

# Test prompts that preserve YOUR face while changing angles
test_angles = [
    {
        "name": "your_left_45",
        "prompt": "Same person, head turned 45 degrees to the left, studio lighting, professional portrait, preserve facial features",
    },
    {
        "name": "your_right_45", 
        "prompt": "Same person, head turned 45 degrees to the right, studio lighting, professional portrait, preserve facial features",
    },
    {
        "name": "your_left_profile",
        "prompt": "Same person, left profile view 90 degrees, studio lighting, professional portrait, show full profile",
    },
    {
        "name": "your_right_profile",
        "prompt": "Same person, right profile view 90 degrees, studio lighting, professional portrait, show full profile",
    },
    {
        "name": "your_3quarter",
        "prompt": "Same person, 3/4 view angle, studio lighting, professional portrait, preserve all facial features",
    },
]

print("Testing FLUX.1 with YOUR FACE at different angles")
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
        print(f"  Prompt: {prompt[:70]}...")
        
        # Image-to-image with HIGH strength to preserve your face
        result = fal_client.run(
            'fal-ai/flux-general',
            arguments={
                'prompt': prompt,
                'image_url': uri,
                'image_size': 'portrait_4_3',
                'num_inference_steps': 30,
                'guidance_scale': 7.5,
                'strength': 0.85,  # HIGH: keeps more of your original face
                'seed': 100 + count,
            }
        )
        
        if result and 'images' in result and result['images']:
            img_data = requests.get(result['images'][0]['url'], timeout=30).content
            out_path = f'generated_portrait_dataset/your_{name}.webp'
            with open(out_path, 'wb') as f:
                f.write(img_data)
            print(f"  ✓ Saved: your_{name}.webp\n")
            count += 1
        else:
            print(f"  ✗ Failed - no images returned\n")
            
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:70]}\n")

print(f"\n✓ Generated {count}/5 test images (YOUR FACE at angles)")
