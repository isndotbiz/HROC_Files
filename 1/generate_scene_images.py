"""
HROC Founder Scene Image Generator — fal.ai GPT Image 1.5 Edit
Generates all gallery/scene images for each founder's page.
Face identity preservation is the #1 priority.
"""

import base64
import os
import sys
import requests
from pathlib import Path
from PIL import Image

try:
    import fal_client
except ImportError:
    print("Install fal SDK: pip install fal-client")
    sys.exit(1)

# Load keys from .env.local if not already set
if not os.environ.get("FAL_KEY"):
    env_local = Path("/home/jdmal/workspace/.env.local")
    if not env_local.exists():
        env_local = Path("/home/jdmal/workspace/.env.local")
    if env_local.exists():
        for line in env_local.read_text().splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ[key.strip()] = val.strip()


def image_to_data_uri(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f"data:image/png;base64,{b64}"


FACE_LOCK = """\
CRITICAL — FACE IDENTITY LOCK: The face in the output MUST be identical to the \
input image face. Preserve every facial feature exactly: eye shape, eye color, \
iris pattern, eyebrow shape, nose shape, nostril width, lip shape, lip thickness, \
jawline, chin shape, cheekbone structure, forehead shape, skin tone, freckles, \
moles, blemishes, wrinkles, facial hair pattern, and overall facial geometry. \
The face must be THE SAME person. Treat the face as a locked mask. \
Natural skin pore texture, no airbrushing, no beauty filter. \
Anatomically correct body proportions. No text, no logos, no watermarks."""

# Scene images for each founder. Each entry:
#   s3_key: target S3 filename (under images/founders/{letter}/)
#   alt: the alt text from the HTML (describes the scene)
#   scene: detailed scene prompt

SCENES = {
    "bri": {
        "input": "b1.png",
        "letter": "b",
        "images": [
            {
                "s3_key": "bri_professional_01_2.webp",
                "alt": "Bri - HROC Secretary",
                "scene": "Professional three-quarter portrait in a modern nonprofit office. "
                         "Same woman, same face. Wearing a smart casual blazer over a white top. "
                         "Warm natural window light from the left. Blurred office background with "
                         "bookshelves and plants. Confident, approachable expression. "
                         "Shot on Canon EOS R5, 85mm f/1.8, shallow depth of field. "
                         "Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "bri_varied_03.webp",
                "alt": "Bri in business casual outdoor setting",
                "scene": "Same woman, same face. Standing outdoors in a Pacific Northwest urban "
                         "park setting. Business casual attire — light jacket, professional but "
                         "relaxed. Soft overcast daylight, lush green trees blurred in background. "
                         "Natural, relaxed posture. Three-quarter body shot from waist up. "
                         "Shot on Canon EOS R5, 70mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "qwen_bri_02_business_casual_outdoor.webp",
                "alt": "Bri working in the community",
                "scene": "Same woman, same face. Engaged in conversation with community members "
                         "at an outdoor community event. Warm, compassionate expression. Casual "
                         "professional clothing. Soft golden hour light. Blurred people and event "
                         "tents in background. Waist-up framing. Shot on Canon EOS R5, 50mm f/1.8. "
                         "Photorealistic, documentary photography style, natural skin texture.",
            },
            {
                "s3_key": "bri_varied_05.webp",
                "alt": "Bri in modern office setting",
                "scene": "Same woman, same face. Sitting at a modern desk in a bright, contemporary "
                         "office. Working on a laptop, looking up at camera with a warm smile. "
                         "Clean white desk, minimalist decor, large windows with natural light. "
                         "Upper body framing. Shot on Canon EOS R5, 50mm f/2.0. "
                         "Photorealistic, natural skin texture, corporate editorial style.",
            },
            {
                "s3_key": "qwen_bri_01_professional_office_laptop.webp",
                "alt": "Bri demonstrating leadership",
                "scene": "Same woman, same face. Standing at the head of a conference table, "
                         "gesturing while presenting to colleagues (blurred). Professional attire. "
                         "Modern glass-walled meeting room. Confident leadership posture. "
                         "Soft overhead and window lighting. Three-quarter body shot. "
                         "Shot on Canon EOS R5, 35mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "bri_professional_08_2.webp",
                "alt": "Bri's vision for HROC",
                "scene": "Same woman, same face. Thoughtful portrait looking slightly off-camera "
                         "with a visionary expression. Standing near a large window with soft "
                         "natural light creating a gentle rim light on hair. Warm neutral background. "
                         "Wearing professional attire. Upper body framing. "
                         "Shot on Canon EOS R5, 85mm f/1.4. Photorealistic, cinematic lighting, "
                         "natural skin texture.",
            },
        ],
    },
    "jonathan": {
        "input": "j1.png",
        "letter": "j",
        "images": [
            {
                "s3_key": "jonathan_urban_outdoor_2.webp",
                "alt": "Jonathan - HROC Chairman",
                "scene": "Professional three-quarter portrait in an urban outdoor setting. "
                         "Same man, same face, same short beard stubble, same blue eyes. "
                         "Wearing a dark professional jacket. City architecture softly blurred "
                         "in background. Confident, direct gaze. Natural overcast daylight. "
                         "Shot on Canon EOS R5, 85mm f/1.8. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "jonathan_varied_01.webp",
                "alt": "Jonathan - Technology Leadership",
                "scene": "Same man, same face, same stubble, same blue eyes. Standing in a modern "
                         "tech workspace with multiple monitors showing data dashboards (blurred). "
                         "Dark professional attire. Cool ambient office lighting with warm accents. "
                         "Confident posture, arms crossed. Upper body shot. "
                         "Shot on Canon EOS R5, 50mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "jonathan_varied_03.webp",
                "alt": "Jonathan - Systems Thinking",
                "scene": "Same man, same face, same stubble, same blue eyes. Sitting at a desk "
                         "reviewing architectural diagrams and documents. Focused, analytical "
                         "expression. Modern minimalist office. Soft directional window light. "
                         "Upper body framing, slight lean forward. Shot on Canon EOS R5, 50mm f/1.8. "
                         "Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "jonathan_varied_05.webp",
                "alt": "Jonathan with data and analytics",
                "scene": "Same man, same face, same stubble, same blue eyes. Standing in front of "
                         "a large monitor or screen showing analytics data (blurred). Pointing or "
                         "gesturing at the screen. Dark professional attire. Modern office with "
                         "cool blue ambient light. Three-quarter body shot. "
                         "Shot on Canon EOS R5, 35mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "jonathan_varied_07.webp",
                "alt": "Jonathan - Strategic Vision",
                "scene": "Same man, same face, same stubble, same blue eyes. Thoughtful portrait "
                         "near a large window overlooking a Pacific Northwest cityscape (blurred). "
                         "Soft natural window light creating gentle rim lighting. Looking slightly "
                         "off-camera with a visionary, contemplative expression. Dark attire. "
                         "Upper body framing. Shot on Canon EOS R5, 85mm f/1.4. "
                         "Photorealistic, cinematic, natural skin texture.",
            },
        ],
    },
    "lilly": {
        "input": "l1.png",
        "letter": "l",
        "images": [
            {
                "s3_key": "lilly_varied_03.webp",
                "alt": "Lilly - HROC Treasurer",
                "scene": "Professional three-quarter portrait in a warm, welcoming office. "
                         "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "Wearing smart professional attire. Soft natural window light. "
                         "Bookshelves and warm decor blurred in background. Confident expression. "
                         "Shot on Canon EOS R5, 85mm f/1.8. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "lilly_varied_02.webp",
                "alt": "Lilly in thoughtful leadership moment",
                "scene": "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "Seated in a comfortable chair in a meeting room, listening intently. "
                         "Thoughtful, engaged expression. Soft ambient lighting. Professional "
                         "attire. Upper body shot, slight head tilt. "
                         "Shot on Canon EOS R5, 50mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "lilly_varied_05.webp",
                "alt": "Lilly giving presentation at whiteboard",
                "scene": "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "Standing at a whiteboard with notes and diagrams, mid-presentation. "
                         "Gesturing with one hand, engaged and passionate expression. "
                         "Bright modern meeting room. Professional casual attire. "
                         "Three-quarter body shot. Shot on Canon EOS R5, 35mm f/2.0. "
                         "Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "lilly_varied_08.webp",
                "alt": "Lilly in yoga class",
                "scene": "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "In a peaceful yoga studio, seated in a meditation pose on a yoga mat. "
                         "Wearing comfortable athletic wear. Soft warm studio lighting. "
                         "Wooden floors, plants in background (blurred). Calm, centered expression. "
                         "Full body or three-quarter shot. Shot on Canon EOS R5, 50mm f/2.0. "
                         "Photorealistic, natural skin texture, serene atmosphere.",
            },
            {
                "s3_key": "lilly_varied_07.webp",
                "alt": "Lilly building community resilience",
                "scene": "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "Outdoors at a community gathering, engaged in warm conversation with "
                         "diverse community members (blurred). Pacific Northwest park setting "
                         "with green trees. Casual but professional clothing. Warm expression. "
                         "Waist-up framing. Shot on Canon EOS R5, 50mm f/1.8. "
                         "Photorealistic, documentary style, natural skin texture.",
            },
            {
                "s3_key": "qwen_lilly_07_modern_office_desk.webp",
                "alt": "Lilly's vision for cultural reclamation",
                "scene": "Same woman, same face, same wavy dark-brown hair, same green eyes. "
                         "Seated at a modern desk with cultural artifacts and books visible. "
                         "Looking directly at camera with a warm, visionary expression. "
                         "Soft warm lighting, rich earth-toned decor in background. "
                         "Professional attire. Upper body framing. "
                         "Shot on Canon EOS R5, 85mm f/1.4. Photorealistic, natural skin texture.",
            },
        ],
    },
    "alicia": {
        "input": "a1.png",
        "letter": "a",
        "images": [
            {
                "s3_key": "alicia_community_real.webp",
                "alt": "Alicia working with community members",
                "scene": "Same woman, same face, same straight dark-brown hair. "
                         "Outdoors at a community outreach event, talking with diverse community "
                         "members (blurred). Casual professional clothing. Warm, empathetic "
                         "expression. Golden hour soft light. Park or community center exterior. "
                         "Waist-up framing. Shot on Canon EOS R5, 50mm f/1.8. "
                         "Photorealistic, documentary style, natural skin texture.",
            },
            {
                "s3_key": "alicia_whiteboard_real.webp",
                "alt": "Alicia leading program planning session",
                "scene": "Same woman, same face, same straight dark-brown hair. "
                         "Standing at a whiteboard covered in program plans and sticky notes. "
                         "Leading a planning session, gesturing with a marker. Engaged, focused "
                         "expression. Bright modern office meeting room. Professional casual attire. "
                         "Three-quarter body shot. Shot on Canon EOS R5, 35mm f/2.0. "
                         "Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "alicia_office_real.webp",
                "alt": "Alicia working on program development",
                "scene": "Same woman, same face, same straight dark-brown hair. "
                         "Seated at a desk with documents and a laptop, reviewing program materials. "
                         "Focused, thoughtful expression. Modern nonprofit office with warm natural "
                         "light from window. Professional attire. Upper body framing. "
                         "Shot on Canon EOS R5, 50mm f/2.0. Photorealistic, natural skin texture.",
            },
            {
                "s3_key": "alicia_varied_01_real.webp",
                "alt": "Alicia connecting with community",
                "scene": "Same woman, same face, same straight dark-brown hair. "
                         "Informal setting, sitting with a small group at a community center table. "
                         "Warm, open body language, listening attentively. Casual professional "
                         "clothing. Soft indoor lighting, community space with notice boards "
                         "blurred in background. Waist-up framing. Shot on Canon EOS R5, 50mm f/1.8. "
                         "Photorealistic, natural skin texture, candid feel.",
            },
        ],
    },
}

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output" / "scenes"
S3_BUCKET = "hroc-website-20251230043930"
S3_PREFIX = "images/founders"


def generate_image(founder: str, cfg: dict, scene: dict) -> Path | None:
    input_path = BASE_DIR / cfg["input"]
    data_uri = image_to_data_uri(input_path)

    full_prompt = f"""{FACE_LOCK}

{scene['scene']}"""

    print(f"  Generating: {scene['s3_key']} — \"{scene['alt']}\"")

    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "prompt": full_prompt,
            "image_urls": [data_uri],
            "image_size": "1024x1024",
            "quality": "high",
            "input_fidelity": "high",
            "num_images": 1,
            "output_format": "png",
        },
    )

    images = result.get("images", [])
    if not images:
        print(f"    ERROR: No images returned")
        return None

    resp = requests.get(images[0]["url"])
    resp.raise_for_status()

    # Save as PNG first
    png_path = OUTPUT_DIR / cfg["letter"] / f"{Path(scene['s3_key']).stem}.png"
    png_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.write_bytes(resp.content)

    # Convert to WebP
    webp_path = OUTPUT_DIR / cfg["letter"] / scene["s3_key"]
    img = Image.open(png_path)
    img.save(webp_path, "WEBP", quality=90)
    png_path.unlink()  # remove temp PNG

    print(f"    Saved: {webp_path} ({webp_path.stat().st_size} bytes)")
    return webp_path


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total = sum(len(f["images"]) for f in SCENES.values())
    done = 0
    failed = []

    print("=" * 60)
    print("HROC Founder Scene Image Generator")
    print(f"Model: fal-ai/gpt-image-1.5/edit")
    print(f"Total images to generate: {total}")
    print("=" * 60)

    for founder, cfg in SCENES.items():
        print(f"\n--- {founder.upper()} ({len(cfg['images'])} images) ---")
        for scene in cfg["images"]:
            done += 1
            try:
                result = generate_image(founder, cfg, scene)
                if result is None:
                    failed.append(f"{founder}/{scene['s3_key']}")
            except Exception as e:
                print(f"    ERROR: {e}")
                failed.append(f"{founder}/{scene['s3_key']}")
            print(f"    Progress: {done}/{total}")

    print(f"\n{'=' * 60}")
    print(f"Generation complete. {done - len(failed)}/{total} succeeded.")
    if failed:
        print(f"Failed: {failed}")
    print(f"Output: {OUTPUT_DIR}/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
