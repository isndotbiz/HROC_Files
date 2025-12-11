#!/usr/bin/env python3
"""
Generate 5 test images per person (Jonathan, Bri, Lilly) using Qwen image editing model.
Uses existing training images as input for consistent face generation.
"""

import os
import sys
import replicate
import base64
import time
from pathlib import Path

# API token from environment
api_token = os.environ.get("REPLICATE_API_TOKEN")
if not api_token:
    print("ERROR: REPLICATE_API_TOKEN not set")
    print("Run: export REPLICATE_API_TOKEN=<your_token_here>")
    sys.exit(1)

def image_to_data_uri(image_path):
    """Convert image file to base64 data URI"""
    with open(image_path, "rb") as f:
        data = f.read()

    # Determine mime type from extension
    ext = Path(image_path).suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp"
    }
    mime_type = mime_types.get(ext, "image/png")

    b64_data = base64.b64encode(data).decode("utf-8")
    return f"data:{mime_type};base64,{b64_data}"

# Base paths
base_path = Path("/Users/jonathanmallinger/Workspace/HROC_Files/HROC_Website_New/lora_training")

# Person configs with training images and test prompts
people = {
    "jonathan": {
        "training_images": ["IMG_0113.png", "IMG_1243.png"],
        "tests": [
            "frontal headshot view, professional business casual attire",
            "3/4 view facing left, casual t-shirt, relaxed pose",
            "side profile view, business casual button-up shirt",
            "looking down slightly, casual outfit",
            "full body standing frontal view, professional casual mix"
        ]
    },
    "bri": {
        "training_images": ["bri_professional_01.png", "IMG_1215.png"],
        "tests": [
            "frontal headshot view, professional business casual attire",
            "3/4 view facing right, casual feminine clothing",
            "side profile view, business casual blazer and blouse",
            "looking down slightly, casual feminine outfit",
            "full body standing frontal view, professional casual mix"
        ]
    },
    "lilly": {
        "training_images": ["465168804_28361199616812436_5751942585475638287_n.jpg", "lilly_professional_01.png"],
        "tests": [
            "frontal headshot view, professional business casual attire",
            "3/4 view facing left, casual feminine clothing",
            "side profile view, business casual blazer and blouse",
            "looking down slightly, casual feminine outfit",
            "full body standing frontal view, professional casual mix"
        ]
    }
}

def generate_test_images():
    """Generate 5 test images per person"""
    import urllib.request

    for person_name, config in people.items():
        person_path = base_path / person_name
        output_path = person_path / "test_outputs"
        output_path.mkdir(exist_ok=True)

        # Use first training image as input
        training_img = config["training_images"][0]
        input_img_path = person_path / training_img

        if not input_img_path.exists():
            print(f"ERROR: Training image not found: {input_img_path}")
            continue

        print(f"\nGenerating {len(config['tests'])} test images for {person_name.upper()}")
        print(f"Input image: {training_img}")
        print(f"Output folder: {output_path}")

        # Convert image to data URI
        print(f"Preparing image...")
        image_uri = image_to_data_uri(str(input_img_path))

        for idx, test_prompt in enumerate(config["tests"], 1):
            try:
                print(f"  [{idx}/5] Generating with prompt: '{test_prompt[:50]}...'")

                output = replicate.run(
                    "qwen/qwen-image-edit-plus-lora",
                    input={
                        "image": [image_uri],
                        "prompt": test_prompt,
                        "lora_scale": 1.25,
                        "lora_weights": "dx8152/qwen-edit-2509-multiple-angles"
                    }
                )

                # Save output files
                for output_idx, item in enumerate(output):
                    output_file = output_path / f"{person_name}_test_{idx:02d}_{output_idx}.webp"

                    # If item is a URL string, download it
                    if isinstance(item, str):
                        print(f"    Downloading from URL...")
                        urllib.request.urlretrieve(item, str(output_file))
                        print(f"    Saved: {output_file}")
                    # If item is a File object, read it
                    elif hasattr(item, 'read'):
                        with open(output_file, "wb") as f:
                            f.write(item.read())
                        print(f"    Saved: {output_file}")
                    else:
                        print(f"    Note: Unexpected output type: {type(item)}")

            except Exception as e:
                error_str = str(e)
                # Handle rate limiting with backoff
                if "429" in error_str or "throttled" in error_str.lower():
                    print(f"  RATE LIMIT - Waiting 15 seconds...")
                    time.sleep(15)
                else:
                    print(f"  ERROR on test {idx}: {error_str}")
                continue

        print(f"Completed {person_name}!")

if __name__ == "__main__":
    print("=" * 70)
    print("QWEN IMAGE EDITING - TEST IMAGE GENERATION")
    print("=" * 70)
    print(f"API Token: {api_token[:20]}...***")
    print(f"Base path: {base_path}")
    print(f"Generating 15 test images total (5 per person)")
    print("=" * 70)

    generate_test_images()

    print("\n" + "=" * 70)
    print("IMAGE GENERATION COMPLETE")
    print("=" * 70)
