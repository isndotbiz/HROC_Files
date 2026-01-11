#!/usr/bin/env python3
"""
Generate a dataset of portrait images using FAL AI Qwen image edit models.
Creates 20 images per source image across 4 categories:
- 5 close-ups (facial expressions and features)
- 5 upper body shots
- 5 different angles
- 5 full-body images
"""

import os
import json
import fal_client
import base64
import requests
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

# Configuration
SOURCE_IMAGES = ["j1.webp", "l1.webp", "b1.webp"]
OUTPUT_DIR = "generated_portrait_dataset"
FAL_KEY = os.getenv("FAL_KEY")

# Ensure API key is set
if not FAL_KEY:
    raise ValueError("FAL_KEY environment variable is required. Set it with: export FAL_KEY='your_key'")

# Create output directory
Path(OUTPUT_DIR).mkdir(exist_ok=True)

# Model configurations for different shot types
SHOT_CONFIGURATIONS = {
    "close_ups": {
        "model": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
        "count": 5,
        "prompt_template": "Close-up portrait focusing on {feature}. Professional photography, studio lighting, clear facial details.",
        "features": [
            "natural smile and eyes",
            "serious expression with piercing eyes",
            "contemplative look with detailed facial features",
            "genuine warmth with focus on smile",
            "dramatic expression highlighting facial structure"
        ]
    },
    "upper_body": {
        "model": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
        "count": 5,
        "prompt_template": "Upper body portrait shot. Professional styling and posture. Focus on {style}. Studio photography.",
        "styles": [
            "confident standing pose with professional attire",
            "relaxed posture with casual styling",
            "dynamic pose showing movement and energy",
            "elegant pose with sophisticated styling",
            "approachable pose with friendly demeanor"
        ]
    },
    "multiple_angles": {
        "model": "fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles",
        "count": 5,
        "prompt_template": "Create {angle} view of the person. Professional portrait lighting, clear facial features.",
        "angles": [
            "a left profile view",
            "a three-quarter front-left angle",
            "a straight front view",
            "a three-quarter front-right angle",
            "a right profile view"
        ]
    },
    "full_body": {
        "model": "fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait",
        "count": 5,
        "prompt_template": "Full-body portrait. {pose} overall silhouette and style visible. Professional photography.",
        "poses": [
            "Standing straight, neutral expression, formal outfit",
            "Dynamic standing pose, engaging expression, casual styling",
            "Seated pose, relaxed demeanor, contemporary outfit",
            "Standing with slight lean, confident expression, business casual",
            "Full-length standing, professional stance, elegant styling"
        ]
    }
}

def download_image(url: str, output_path: str) -> bool:
    """Download image from URL and save locally."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"    Error downloading image: {str(e)}")
        return False

def generate_image(source_image: str, prompt: str, model: str, output_path: str = None) -> dict:
    """Generate an image using FAL AI."""
    try:
        # Read source image and convert to base64
        with open(source_image, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        
        # Determine image type
        ext = os.path.splitext(source_image)[1].lower().lstrip(".")
        if ext == "webp":
            data_uri = f"data:image/webp;base64,{image_data}"
        elif ext == "jpg" or ext == "jpeg":
            data_uri = f"data:image/jpeg;base64,{image_data}"
        elif ext == "png":
            data_uri = f"data:image/png;base64,{image_data}"
        else:
            data_uri = f"data:image/{ext};base64,{image_data}"
        
        # Call FAL AI model
        result = fal_client.run(
            model,
            arguments={
                "image_urls": [data_uri],
                "prompt": prompt,
                "num_inference_steps": 30,
                "guidance_scale": 7.5,
            }
        )
        
        # Download generated image if output path provided
        if output_path and result and "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            if download_image(image_url, output_path):
                print(f"    ✓ Generated: {os.path.basename(output_path)}")
                return {"success": True, "url": image_url, "path": output_path}
        
        return {"success": False, "error": "No images returned"}
    except Exception as e:
        print(f"    Error: {str(e)}")
        return {"success": False, "error": str(e)}

def process_source_image(source_image: str) -> dict:
    """Process a single source image and generate all variations."""
    print(f"\n{'='*60}")
    print(f"Processing: {source_image}")
    print(f"{'='*60}")
    
    source_name = Path(source_image).stem
    results = {
        "source": source_image,
        "generated_at": datetime.now().isoformat(),
        "shots": {}
    }
    
    for shot_type, config in SHOT_CONFIGURATIONS.items():
        print(f"\n>>> Generating {config['count']} {shot_type}...")
        results["shots"][shot_type] = []
        
        prompt_list = None
        if shot_type == "close_ups":
            prompt_list = config["features"]
        elif shot_type == "upper_body":
            prompt_list = config["styles"]
        elif shot_type == "multiple_angles":
            prompt_list = config["angles"]
        elif shot_type == "full_body":
            prompt_list = config["poses"]
        
        for idx, detail in enumerate(prompt_list, 1):
            prompt = config["prompt_template"].format(
                feature=detail if shot_type == "close_ups" else None,
                style=detail if shot_type == "upper_body" else None,
                angle=detail if shot_type == "multiple_angles" else None,
                pose=detail if shot_type == "full_body" else None
            ).strip()
            
            output_filename = f"{source_name}_{shot_type}_{idx}.webp"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            
            result = generate_image(source_image, prompt, config["model"], output_path)
            
            # Save result metadata
            results["shots"][shot_type].append({
                "id": idx,
                "prompt": prompt,
                "filename": output_filename,
                "status": "success" if result["success"] else "failed",
                "error": result.get("error") if not result["success"] else None
            })
    
    return results

def main():
    """Main function to generate dataset."""
    print("FAL AI Portrait Dataset Generator")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Using API Key: {FAL_KEY[:10]}...")
    
    all_results = {
        "generated_at": datetime.now().isoformat(),
        "total_images": 0,
        "failed_images": 0,
        "sources": {}
    }
    
    for source_image in SOURCE_IMAGES:
        source_path = os.path.join(".", source_image)
        if os.path.exists(source_path):
            result = process_source_image(source_path)
            all_results["sources"][source_image] = result
            
            # Count generated images
            for shot_type, shots in result["shots"].items():
                for shot in shots:
                    if shot["status"] == "success":
                        all_results["total_images"] += 1
                    else:
                        all_results["failed_images"] += 1
        else:
            print(f"Warning: Source image not found: {source_image}")
    
    # Save summary
    summary_path = os.path.join(OUTPUT_DIR, "generation_summary.json")
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"✓ Dataset generation complete!")
    print(f"Total images generated: {all_results['total_images']}")
    if all_results['failed_images'] > 0:
        print(f"Failed generations: {all_results['failed_images']}")
    print(f"Output directory: {OUTPUT_DIR}/")
    print(f"Summary saved: {summary_path}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
