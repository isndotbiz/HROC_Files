import os, base64, fal_client, requests
from pathlib import Path

Path('generated_portrait_dataset').mkdir(exist_ok=True)

src = "l1.webp"
with open(src, 'rb') as f:
    uri = f'data:image/webp;base64,{base64.b64encode(f.read()).decode()}'

print("Creating l1 examples...\n")

# LEFT
try:
    print("LEFT 45°...", end=" ")
    r = fal_client.run('fal-ai/flux-pro/v1.1-ultra', arguments={
        'prompt': 'professional portrait, head turned 45 degrees to the left, studio lighting',
        'image_url': uri, 'strength': 0.9,
    })
    if r and 'images' in r:
        with open('generated_portrait_dataset/l1_LEFT.webp', 'wb') as f:
            f.write(requests.get(r['images'][0]['url'], timeout=30).content)
        print("✓")
except: print("✗")

# RIGHT
try:
    print("RIGHT 45°...", end=" ")
    r = fal_client.run('fal-ai/flux-pro/v1.1-ultra', arguments={
        'prompt': 'professional portrait, head turned 45 degrees to the right, studio lighting',
        'image_url': uri, 'strength': 0.9,
    })
    if r and 'images' in r:
        with open('generated_portrait_dataset/l1_RIGHT.webp', 'wb') as f:
            f.write(requests.get(r['images'][0]['url'], timeout=30).content)
        print("✓")
except: print("✗")

print("\nReady to review!")
