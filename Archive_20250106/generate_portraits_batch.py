#!/usr/bin/env python3
"""
Batch portrait image generator using FAL AI.
Generates images in smaller batches to avoid timeouts.
"""

import os
import json
import fal_client
import base64
import requests
from pathlib import Path
from datetime import datetime

FAL_KEY = os.getenv("FAL_KEY")
if not FAL_KEY:
    raise ValueError("FAL_KEY environment variable required")

OUTPUT_DIR = "generated_portrait_dataset"
Path(OUTPUT_DIR).mkdir(exist_ok=True)

def download_image(url: str, output_path: str) -> bool:
    """Download image from URL and save locally."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading: {str(e)}")
        return False

def generate_image(source_image: str, prompt: str, model: str, output_path: str) -> dict:
    """Generate a single image."""
    try:
        with open(source_image, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        
        ext = os.path.splitext(source_image)[1].lower().lstrip(".")
        data_uri = f"data:image/{ext};base64,{image_data}"
        
        print(f"  Calling FAL AI... ({prompt[:40]}...)")
        result = fal_client.run(
            model,
            arguments={
                "image_urls": [data_uri],
                "prompt": prompt,
                "num_inference_steps": 30,
                "guidance_scale": 7.5,
            }
        )
        
        if result and "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            if download_image(image_url, output_path):
                print(f"  ✓ Saved: {os.path.basename(output_path)}")
                return {"success": True, "url": image_url}
        
        return {"success": False, "error": "No images in response"}
    except Exception as e:
        print(f"  Error: {str(e)}")
        return {"success": False, "error": str(e)}

# Configuration
sources = ["j1.webp", "l1.webp", "b1.webp"]
models = {
    "face": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
    "angles": "fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles"
}

# Close-ups
close_ups = [
    "Close-up portrait focusing on natural smile and eyes. Professional photography, studio lighting.",
    "Close-up portrait with serious expression and piercing eyes. Professional photography.",
    "Close-up portrait with contemplative look and detailed facial features. Professional photography.",
    "Close-up portrait with genuine warmth and smile. Professional photography, studio lighting.",
    "Close-up portrait with dramatic expression. Professional photography, studio lighting."
]

# Upper body
upper_body = [
    "Upper body portrait with confident standing pose and professional attire. Studio photography.",
    "Upper body portrait with relaxed posture and casual styling. Studio photography.",
    "Upper body portrait with dynamic pose showing movement and energy. Studio photography.",
    "Upper body portrait with elegant pose and sophisticated styling. Studio photography.",
    "Upper body portrait with approachable pose and friendly demeanor. Studio photography."
]

# Multiple angles
angles = [
    "Create a left profile view of the person. Professional portrait lighting.",
    "Create a three-quarter front-left angle view. Professional portrait lighting.",
    "Create a straight front view. Professional portrait lighting.",
    "Create a three-quarter front-right angle view. Professional portrait lighting.",
    "Create a right profile view. Professional portrait lighting."
]

# Full body
full_body = [
    "Full-body portrait standing straight with neutral expression in formal outfit. Professional photography.",
    "Full-body portrait with dynamic standing pose in casual styling. Professional photography.",
    "Full-body portrait seated with relaxed demeanor in contemporary outfit. Professional photography.",
    "Full-body portrait standing with slight lean in business casual outfit. Professional photography.",
    "Full-body portrait full-length standing with professional stance in elegant styling. Professional photography."
]

def batch_generate(source_image: str, shot_type: str, prompts: list, model: str) -> list:
    """Generate a batch of images for one category."""
    source_name = Path(source_image).stem
    results = []
    
    for idx, prompt in enumerate(prompts, 1):
        output_filename = f"{source_name}_{shot_type}_{idx}.webp"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        result = generate_image(source_image, prompt, model, output_path)
        results.append({
            "filename": output_filename,
            "success": result["success"],
            "prompt": prompt
        })
    
    return results

print("FAL AI Portrait Dataset Generator")
print(f"Output directory: {OUTPUT_DIR}/\n")

# Generate batch by batch
all_results = {}

for source in sources:
    if not os.path.exists(source):
        print(f"Error: Source image not found: {source}")
        continue
    
    source_name = Path(source).stem
    print(f"\n{'='*60}")
    print(f"Processing: {source} ({source_name})")
    print(f"{'='*60}")
    
    all_results[source] = {}
    
    # Close-ups
    print(f"\n1. Generating close-ups...")
    all_results[source]["close_ups"] = batch_generate(
        source, "close_ups", close_ups, models["face"]
    )
    successful = sum(1 for r in all_results[source]["close_ups"] if r["success"])
    print(f"  Result: {successful}/{len(close_ups)} successful")
    
    # Upper body
    print(f"\n2. Generating upper body shots...")
    all_results[source]["upper_body"] = batch_generate(
        source, "upper_body", upper_body, models["face"]
    )
    successful = sum(1 for r in all_results[source]["upper_body"] if r["success"])
    print(f"  Result: {successful}/{len(upper_body)} successful")
    
    # Angles
    print(f"\n3. Generating multiple angles...")
    all_results[source]["angles"] = batch_generate(
        source, "angles", angles, models["angles"]
    )
    successful = sum(1 for r in all_results[source]["angles"] if r["success"])
    print(f"  Result: {successful}/{len(angles)} successful")
    
    # Full body
    print(f"\n4. Generating full-body shots...")
    all_results[source]["full_body"] = batch_generate(
        source, "full_body", full_body, models["face"]
    )
    successful = sum(1 for r in all_results[source]["full_body"] if r["success"])
    print(f"  Result: {successful}/{len(full_body)} successful")

# Summary
print(f"\n{'='*60}")
print("GENERATION SUMMARY")
print(f"{'='*60}")

total_successful = 0
total_failed = 0

for source, categories in all_results.items():
    source_name = Path(source).stem
    for category, results in categories.items():
        successful = sum(1 for r in results if r["success"])
        failed = sum(1 for r in results if not r["success"])
        total_successful += successful
        total_failed += failed
        print(f"{source_name} - {category}: {successful}/{len(results)}")

print(f"\nTotal: {total_successful} successful, {total_failed} failed")
print(f"Output directory: {OUTPUT_DIR}/")

# Save results
summary_path = os.path.join(OUTPUT_DIR, "generation_results.json")
with open(summary_path, "w") as f:
    json.dump({
        "generated_at": datetime.now().isoformat(),
        "total_successful": total_successful,
        "total_failed": total_failed,
        "results": all_results
    }, f, indent=2)
print(f"Results saved: {summary_path}\n")
