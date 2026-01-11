#!/usr/bin/env python3
"""Quick test of FAL AI image generation."""

import os
import fal_client
import base64

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    raise ValueError("FAL_KEY environment variable required")

print("Testing FAL AI image generation...")
print(f"API Key: {FAL_KEY[:20]}...")

# Load test image
source_image = "j1.webp"
with open(source_image, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

data_uri = f"data:image/webp;base64,{image_data}"

print(f"\nLoaded source image: {source_image}")
print(f"Data URI length: {len(data_uri)} characters")

try:
    print("\nCalling fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait...")
    result = fal_client.run(
        "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
        arguments={
            "image_urls": [data_uri],
            "prompt": "Close-up portrait focusing on natural smile and eyes",
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
        }
    )
    print(f"Success! Result: {result}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {str(e)}")
    import traceback
    traceback.print_exc()
