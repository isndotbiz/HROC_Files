#!/usr/bin/env python3
"""
HROC Founder Image Generator
Uses fal.ai GPT Image 1.5 Edit API to generate:
1. Professional headshots for each founder (face-preserving crop)
2. Activity images (founders doing community activities together)

Prompting strategy based on OpenAI GPT Image 1.5 Prompting Guide:
- input_fidelity="high" for maximum face preservation
- Photography language (camera, lens, lighting) not generic AI terms
- Explicit face lock constraints repeated in every prompt
- First image = face reference for maximum texture fidelity
"""

import os
import sys
import json
import time
import urllib.request
import shutil
from pathlib import Path

# Load fal.ai API key
env_file = None
for p in [Path("/d/workspace/.env.local"), Path("D:/workspace/.env.local"), Path(os.path.expanduser("~")) / ".env.local"]:
    if p.exists():
        env_file = p
        break
if env_file is None:
    # Try reading via subprocess
    import subprocess
    result = subprocess.run(["cat", "/d/workspace/.env.local"], capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.splitlines():
            if line.startswith("FAL_KEY="):
                os.environ["FAL_KEY"] = line.split("=", 1)[1].strip()
                break
if env_file is not None and env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.startswith("FAL_KEY="):
            os.environ["FAL_KEY"] = line.split("=", 1)[1].strip()
            break

if "FAL_KEY" not in os.environ:
    print("ERROR: FAL_KEY not found. Set it in environment or /d/workspace/.env.local")
    sys.exit(1)

import fal_client

# S3 base URL
S3_BASE = "https://hroc-website-20251230043930.s3.us-east-1.amazonaws.com/images/founders"

# Output directories
OUTPUT_DIR = Path("D:/workspace/HROC_Files/images/generated_headshots")
ACTIVITY_DIR = Path("D:/workspace/HROC_Files/images/generated_activities")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
ACTIVITY_DIR.mkdir(parents=True, exist_ok=True)

# Founder portrait references (best face shots for each)
FOUNDERS = {
    "bri": {
        "portrait_url": f"{S3_BASE}/b/bri_portrait_1.webp",
        "name": "Bri",
        "title": "Secretary/COO",
        "description": "Indigenous woman, warm expression, natural beauty"
    },
    "lilly": {
        "portrait_url": f"{S3_BASE}/l/lilly_varied_03.webp",
        "name": "Lilly",
        "title": "Treasurer/CFO",
        "description": "Indigenous woman, thoughtful expression, cultural presence"
    },
    "jonathan": {
        "portrait_url": f"{S3_BASE}/j/jonathan_portrait_1.webp",
        "name": "Jonathan",
        "title": "Chairman/CEO",
        "description": "Professional man, confident expression, strategic presence"
    },
    "alicia": {
        "portrait_url": f"{S3_BASE}/a/alicia_portrait_1.webp",
        "name": "Alicia",
        "title": "Vice President/CPO",
        "description": "Young Indigenous woman, dynamic expression, compassionate presence"
    }
}

# Face preservation constraint block (included in EVERY prompt)
FACE_LOCK = """
CRITICAL PRESERVATION CONSTRAINTS:
- Do not change the subject's face, facial features, skin tone, body shape, or identity in any way
- Preserve their exact likeness, facial structure, expression style, hairstyle, and proportions from the reference image
- Match lighting direction and color temperature naturally on the face
- Maintain exact eye shape, nose structure, jawline, and skin texture from the reference
- Everything should feel grounded and authentic, as if captured in a real moment by a documentary photographer
"""


def download_image(url, filepath):
    """Download an image from URL to local filepath."""
    print(f"  Downloading: {url}")
    print(f"  To: {filepath}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        with open(filepath, "wb") as f:
            shutil.copyfileobj(response, f)
    print(f"  Done: {os.path.getsize(filepath)} bytes")


def generate_image(image_urls, prompt, output_path, quality="low"):
    """Call fal.ai GPT Image 1.5 Edit to generate an image."""
    print(f"\n--- Generating: {output_path.name} ---")
    print(f"  Quality: {quality}")
    print(f"  Input images: {len(image_urls)}")
    print(f"  Prompt preview: {prompt[:120]}...")

    try:
        result = fal_client.subscribe("fal-ai/gpt-image-1.5/edit", arguments={
            "prompt": prompt,
            "image_urls": image_urls,
            "quality": quality,
            "input_fidelity": "high",
            "image_size": "1024x1024",
            "num_images": 1,
            "output_format": "webp"
        })

        if result and "images" in result and len(result["images"]) > 0:
            image_url = result["images"][0]["url"]
            download_image(image_url, output_path)
            return True
        else:
            print(f"  ERROR: No images in result: {result}")
            return False

    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def generate_headshot(founder_key, founder_info):
    """Generate a professional headshot for a founder."""
    output_path = OUTPUT_DIR / f"{founder_key}_headshot.webp"

    # 3 prompt strategies, then blend the best elements

    # Strategy 1: Classic corporate headshot style
    prompt_1 = f"""Create a professional corporate headshot photograph of this exact person.
Shot with an 85mm portrait lens at f/2.8, studio lighting with soft key light at 45 degrees
and subtle fill light. Clean neutral gray backdrop. Head and shoulders framing, slight 3/4 turn.
Shallow depth of field isolating the subject. Professional attire appropriate for a nonprofit executive.
Catchlights visible in the eyes. Natural skin texture visible - pores, subtle lines.
{FACE_LOCK}"""

    # Strategy 2: Environmental portrait / warm editorial
    prompt_2 = f"""Create a warm editorial-style portrait photograph of this exact person for a
nonprofit organization's leadership page. Shot with a 50mm lens at f/2, natural window light
creating soft directional illumination. Warm color temperature. Head and upper body visible.
Genuine, approachable expression conveying compassion and leadership. Background subtly blurred
showing warm tones. Shot like a National Geographic portrait - authentic, intimate, dignified.
Natural skin texture, subtle film grain, no retouching.
{FACE_LOCK}"""

    # Strategy 3: Modern clean headshot
    prompt_3 = f"""Photograph this exact person in a clean, modern headshot style used by top
nonprofit organizations. 70mm lens, natural daylight from large diffused source. Minimal,
clean background with slight color wash. Tight crop from mid-chest up. Expression shows warmth,
determination, and genuine care. Professional yet approachable. Color grading: warm highlights,
neutral shadows. Skin shows real texture - this should look indistinguishable from an actual
photograph taken by a professional headshot photographer.
{FACE_LOCK}"""

    # BLENDED final prompt: combines the best elements from all three strategies
    blended_prompt = f"""Create a professional headshot photograph of this exact person for a nonprofit
organization's leadership page. This must look indistinguishable from an actual photograph.

Camera: 85mm portrait lens at f/2.8, creating shallow depth of field that isolates the subject.
Lighting: Soft directional natural window light as key light at 45 degrees, with subtle fill.
Warm color temperature evoking trust and approachability.
Framing: Head and shoulders, slight 3/4 body turn with face toward camera. Tight crop from mid-chest up.
Background: Clean, slightly warm-toned, naturally blurred.
Expression: Genuine warmth and confident leadership - approachable yet professional. Conveying compassion,
determination, and authentic care. Subtle, natural smile showing real character.
Technical: Natural skin texture fully visible - pores, subtle lines, real human detail. Catchlights in eyes.
Subtle film grain. No retouching, no airbrushing, no smoothing. Color grading with warm highlights
and neutral shadows. This should look exactly like a $500 professional headshot session.

{FACE_LOCK}"""

    print(f"\nGenerating headshot for {founder_info['name']}...")
    return generate_image(
        image_urls=[founder_info["portrait_url"]],
        prompt=blended_prompt,
        output_path=output_path,
        quality="low"
    )


# Activity scene definitions - each founder gets 3 unique activities
ACTIVITY_SCENES = {
    "bri": [
        {
            "name": "bri_yoga_session",
            "description": "Bri leading a community yoga session outdoors",
            "partners": ["lilly"],  # at least 2 founders in scene
        },
        {
            "name": "bri_turkey_distribution",
            "description": "Bri handing out turkeys at a community Thanksgiving event",
            "partners": ["jonathan", "alicia"],
        },
        {
            "name": "bri_healing_circle",
            "description": "Bri facilitating an Indigenous healing circle ceremony",
            "partners": ["lilly", "alicia"],
        },
    ],
    "lilly": [
        {
            "name": "lilly_community_garden",
            "description": "Lilly working in a community garden with volunteers",
            "partners": ["bri"],
        },
        {
            "name": "lilly_food_bank",
            "description": "Lilly organizing a food bank distribution event",
            "partners": ["jonathan", "bri"],
        },
        {
            "name": "lilly_wellness_workshop",
            "description": "Lilly leading a wellness and self-care workshop",
            "partners": ["alicia"],
        },
    ],
    "jonathan": [
        {
            "name": "jonathan_supply_distribution",
            "description": "Jonathan distributing harm reduction supplies from a mobile van",
            "partners": ["bri", "alicia"],
        },
        {
            "name": "jonathan_community_meal",
            "description": "Jonathan serving meals at a community dinner event",
            "partners": ["lilly"],
        },
        {
            "name": "jonathan_team_planning",
            "description": "Jonathan leading a team strategy session with other founders",
            "partners": ["bri", "lilly", "alicia"],
        },
    ],
    "alicia": [
        {
            "name": "alicia_outreach_van",
            "description": "Alicia doing street outreach from a harm reduction van",
            "partners": ["jonathan"],
        },
        {
            "name": "alicia_turkey_handout",
            "description": "Alicia handing out turkeys and supplies at a community event",
            "partners": ["bri", "lilly"],
        },
        {
            "name": "alicia_youth_workshop",
            "description": "Alicia facilitating a youth empowerment workshop",
            "partners": ["lilly", "jonathan"],
        },
    ],
}


def build_activity_prompt(founder_key, scene):
    """Build 3 prompt strategies and blend them for an activity scene."""
    founder = FOUNDERS[founder_key]
    partner_names = [FOUNDERS[p]["name"] for p in scene["partners"]]
    partners_str = " and ".join(partner_names)

    # Strategy 1: Documentary photography approach
    prompt_1 = f"""Photojournalistic documentary photograph capturing {founder['name']} {scene['description']}.
{founder['name']} is the primary subject (from reference Image 1), shown alongside {partners_str}
(from reference Images {', '.join(str(i+2) for i in range(len(scene['partners'])))}).
Shot with a 35mm lens at f/4, natural outdoor daylight, wide depth of field capturing the full scene.
Candid moment, authentic action, no posing. Documentary style like a Pulitzer-winning news photograph.
Natural color, available light only, slight motion capturing real activity.
{FACE_LOCK}"""

    # Strategy 2: Warm community narrative style
    prompt_2 = f"""Warm, authentic photograph of {founder['name']} {scene['description']} alongside
{partners_str}. Golden hour lighting creating warm, inviting atmosphere. Shot with 50mm lens,
moderate depth of field. Everyone engaged in genuine activity - laughing, working, connecting.
Composition tells a story of community, care, and collective action. Colors are warm and natural.
Feels like a photograph from a prestigious nonprofit's annual report - professional yet deeply human.
{FACE_LOCK}"""

    # Strategy 3: Action editorial style
    prompt_3 = f"""Editorial action photograph of {founder['name']} actively {scene['description']},
working alongside {partners_str}. Shot at eye level with a 40mm lens, f/3.5, creating an immersive
perspective that puts the viewer in the scene. Mixed natural and ambient lighting. Rich, authentic
color palette. The photograph captures genuine emotion - determination, joy, connection. Each person
is fully engaged in the activity. No one is looking at the camera. Real-world setting with authentic
environmental details. Magazine-quality but completely unstaged.
{FACE_LOCK}"""

    # BLENDED prompt combining best elements from all three
    partner_image_refs = "\n".join([
        f"Image {i+2}: Reference photo of {FOUNDERS[p]['name']} - preserve their exact facial features and identity."
        for i, p in enumerate(scene["partners"])
    ])

    blended = f"""Generate a photorealistic candid photograph of {founder['name']} {scene['description']},
alongside {partners_str}. This must look indistinguishable from a real photograph taken by a professional
documentary photographer.

Image 1: Reference photo of {founder['name']} (primary subject) - preserve their exact facial features and identity.
{partner_image_refs}

Scene: {scene['description']}. Authentic community setting with real environmental details - worn tables,
handmade signs, real grass, natural imperfections that make it believable.
Camera: 40mm lens at f/3.5, shot at eye level, moderate depth of field keeping all subjects in focus.
Lighting: Natural golden hour daylight mixed with warm ambient light. Soft shadows, warm color temperature.
Action: Everyone is genuinely engaged in the activity. Candid moment captured mid-action - no posing,
no looking at camera. {founder['name']} is the focal subject but others are clearly recognizable.
Emotion: Genuine joy, determination, and community connection visible in body language and expressions.
Style: Award-winning documentary photography. Magazine-quality but completely unstaged and authentic.
Natural skin texture on all subjects. Slight environmental context. Rich, warm color grading.

CRITICAL FACE PRESERVATION FOR ALL SUBJECTS:
- Every person in this image must have their exact face, facial features, skin tone, and identity preserved
  from their respective reference images
- Do not change any subject's facial structure, eye shape, nose, jawline, hairstyle, or skin texture
- Each person must be immediately recognizable as the person in their reference photo
- Match lighting naturally on all faces - consistent with the scene's ambient light
- All faces must show real human texture - pores, subtle lines, natural imperfections
- This photograph must be indistinguishable from reality - no AI artifacts, no uncanny valley, no plastic skin
"""

    return blended


def generate_activity_images(founder_key):
    """Generate 3 activity images for a founder."""
    founder = FOUNDERS[founder_key]
    scenes = ACTIVITY_SCENES[founder_key]

    for scene in scenes:
        output_path = ACTIVITY_DIR / f"{scene['name']}.webp"

        # Build image_urls: founder first (gets max fidelity), then partners
        image_urls = [founder["portrait_url"]]
        for partner_key in scene["partners"]:
            image_urls.append(FOUNDERS[partner_key]["portrait_url"])

        prompt = build_activity_prompt(founder_key, scene)

        print(f"\nGenerating activity: {scene['name']}")
        print(f"  Founder: {founder['name']}")
        print(f"  Partners: {[FOUNDERS[p]['name'] for p in scene['partners']]}")
        print(f"  Images: {len(image_urls)} reference photos")

        success = generate_image(
            image_urls=image_urls,
            prompt=prompt,
            output_path=output_path,
            quality="low"
        )

        if success:
            print(f"  SUCCESS: {scene['name']}")
        else:
            print(f"  FAILED: {scene['name']}")

        # Small delay between API calls
        time.sleep(2)


def main():
    print("=" * 60)
    print("HROC Founder Image Generator")
    print("=" * 60)
    print(f"Output directories:")
    print(f"  Headshots: {OUTPUT_DIR}")
    print(f"  Activities: {ACTIVITY_DIR}")
    print()

    # Phase 1: Generate headshots
    print("\n" + "=" * 60)
    print("PHASE 1: Generating Professional Headshots")
    print("=" * 60)

    for key, info in FOUNDERS.items():
        generate_headshot(key, info)
        time.sleep(2)

    # Phase 2: Generate activity images
    print("\n" + "=" * 60)
    print("PHASE 2: Generating Activity Images")
    print("=" * 60)

    for key in FOUNDERS:
        print(f"\n--- {FOUNDERS[key]['name']}'s Activity Images ---")
        generate_activity_images(key)

    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)
    print(f"\nHeadshots saved to: {OUTPUT_DIR}")
    print(f"Activity images saved to: {ACTIVITY_DIR}")
    print("\nNext steps:")
    print("  1. Review generated images")
    print("  2. Upload approved images to S3")
    print("  3. Update HTML references")


if __name__ == "__main__":
    main()
