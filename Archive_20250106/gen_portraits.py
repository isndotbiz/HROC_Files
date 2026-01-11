#!/usr/bin/env python3
import os, json, fal_client, base64, requests
from pathlib import Path

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    raise ValueError("FAL_KEY required")

OUTPUT_DIR = "generated_portrait_dataset"
Path(OUTPUT_DIR).mkdir(exist_ok=True)

def dl_img(url, path):
    try:
        with open(path, "wb") as f:
            f.write(requests.get(url, timeout=30).content)
        return True
    except: return False

def gen(src, prompt, model, out):
    try:
        with open(src, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        ext = src.split(".")[-1]
        uri = f"data:image/{ext};base64,{b64}"
        
        r = fal_client.run(model, arguments={
            "image_urls": [uri],
            "prompt": prompt,
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
        })
        
        if r and "images" in r and r["images"]:
            if dl_img(r["images"][0]["url"], out):
                print(f"✓ {Path(out).name}")
                return True
        return False
    except Exception as e:
        print(f"✗ {str(e)[:50]}")
        return False

srcs = ["j1.webp", "l1.webp", "b1.webp"]
models = {
    "close": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
    "upper": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
    "angles": "fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles",
    "full": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
}

close_prompts = [
    "Close-up portrait with natural smile and eyes. Studio lighting.",
    "Close-up portrait with serious expression and piercing eyes.",
    "Close-up portrait with contemplative look and facial details.",
    "Close-up portrait with genuine warmth and smile.",
    "Close-up portrait with dramatic expression.",
]

upper_prompts = [
    "Upper body portrait, confident standing pose, professional attire.",
    "Upper body portrait, relaxed posture, casual styling.",
    "Upper body portrait, dynamic pose, energetic.",
    "Upper body portrait, elegant pose, sophisticated styling.",
    "Upper body portrait, approachable pose, friendly.",
]

angle_prompts = [
    "Left profile view of the person.",
    "Three-quarter front-left angle view.",
    "Straight front view.",
    "Three-quarter front-right angle view.",
    "Right profile view.",
]

full_prompts = [
    "Full-body standing straight, neutral expression, formal outfit.",
    "Full-body dynamic standing pose, casual styling.",
    "Full-body seated pose, relaxed, contemporary outfit.",
    "Full-body standing with slight lean, business casual.",
    "Full-body standing professional stance, elegant styling.",
]

count = 0
for src in srcs:
    if not os.path.exists(src):
        print(f"Missing: {src}")
        continue
    
    stem = Path(src).stem
    print(f"\n{stem}:")
    
    for i, p in enumerate(close_prompts, 1):
        if gen(src, p, models["close"], f"{OUTPUT_DIR}/{stem}_close_{i}.webp"):
            count += 1
    
    for i, p in enumerate(upper_prompts, 1):
        if gen(src, p, models["upper"], f"{OUTPUT_DIR}/{stem}_upper_{i}.webp"):
            count += 1
    
    for i, p in enumerate(angle_prompts, 1):
        if gen(src, p, models["angles"], f"{OUTPUT_DIR}/{stem}_angle_{i}.webp"):
            count += 1
    
    for i, p in enumerate(full_prompts, 1):
        if gen(src, p, models["full"], f"{OUTPUT_DIR}/{stem}_full_{i}.webp"):
            count += 1

print(f"\nGenerated: {count} images")
