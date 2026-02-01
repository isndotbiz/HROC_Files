"""
HROC Founder Headshot Generator — fal.ai GPT Image 1.5 Edit
Face identity preservation is the #1 priority.
Usage: python generate_headshots.py
Requires: FAL_KEY environment variable set
"""

import base64
import os
import sys
import requests
from pathlib import Path

try:
    import fal_client
except ImportError:
    print("Install fal SDK: pip install fal-client")
    sys.exit(1)

# Load keys from .env.local if not already set
if not os.environ.get("FAL_KEY"):
    env_local = Path("D:/workspace/.env.local")
    if not env_local.exists():
        env_local = Path("/d/workspace/.env.local")
    if env_local.exists():
        for line in env_local.read_text().splitlines():
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            os.environ[key.strip()] = val.strip()

if not os.environ.get("FAL_KEY"):
    print("ERROR: FAL_KEY not found. Set it or add to D:/workspace/.env.local")
    sys.exit(1)


def image_to_data_uri(path: Path) -> str:
    """Convert a local image file to a base64 data URI."""
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode()
    return f"data:image/png;base64,{b64}"


# Face-first constraint block
FACE_LOCK = """\
CRITICAL — FACE IDENTITY LOCK: The face in the output image MUST be pixel-level \
identical to the face in the input image. Preserve every facial feature exactly: \
eye shape, eye color, iris pattern, eyebrow shape, nose shape, nostril width, lip \
shape, lip thickness, jawline, chin shape, cheekbone structure, forehead shape, \
ear shape, skin tone, freckles, moles, blemishes, wrinkles, facial hair pattern, \
smile lines, and overall facial geometry. The face must be recognizable as the \
exact same person — not a similar-looking person, THE SAME person. If in doubt, \
change NOTHING about the face. Treat the face region as a locked mask that cannot \
be modified."""

# Uniform studio setup
STUDIO = """\
Background: Seamless warm-neutral studio paper (#E8E0D8 to #D5CCC3 gradient), \
softly lit by a large softbox at camera-left (45 degrees), white fill card at \
camera-right. Background falls to smooth creamy bokeh, no hard edges or horizon line.

Lighting: Soft directional key light from camera-left, gentle modeling shadows \
under cheekbone and jaw. Subtle specular highlights on nose bridge and cheekbones. \
Fill ratio approximately 2:1. Natural 5200K white balance. Rectangular softbox \
catchlights visible in both eyes.

Camera: Canon EOS R5, 85mm f/1.4L, ISO 200, shallow depth of field. \
Shoulder-up framing, centered composition."""

# Realism enforcement
REALISM = """\
Realism: Visible skin pore texture, natural under-eye shadows, micro fly-away hairs \
along hairline, subtle skin color variation (no uniform color cast). No airbrushing, \
no frequency separation, no beauty-filter smoothing, no plastic skin. Natural lip \
color. The output must be indistinguishable from an unretouched DSLR photograph of \
a real human being.

Body proportions: Anatomically correct human proportions — normal shoulder width \
relative to head size, natural neck length, realistic collar bone and shoulder \
positioning. No elongation, no compression, no uncanny distortion.

Hard constraints: No text, no logos, no watermarks. Do not alter the subject's \
expression or pose. Do not change clothing or accessories."""

FOUNDERS = {
    "alicia": {
        "input": "a1.png",
        "prompt": f"""{FACE_LOCK}

{STUDIO}

Subject: This exact woman with straight dark-brown hair parted at center, wearing a \
white sleeveless top. Her face, expression, head angle, and pose must remain \
absolutely unchanged. Only the background and lighting quality may change.

{REALISM}""",
    },
    "bri": {
        "input": "b1.png",
        "prompt": f"""{FACE_LOCK}

{STUDIO}

Subject: This exact woman with wavy brown hair, wearing a white crew-neck t-shirt \
and gold pendant necklace. Her face, expression, head angle, and pose must remain \
absolutely unchanged. Only the background and lighting quality may change. Keep the \
gold pendant necklace exactly as-is.

{REALISM}""",
    },
    "jonathan": {
        "input": "j1.png",
        "prompt": f"""{FACE_LOCK}

{STUDIO}

Subject: This exact man with short reddish-brown hair, short beard stubble, blue \
eyes, wearing a navy henley shirt and gold chain necklace. His face, facial hair, \
expression, head angle, and pose must remain absolutely unchanged. Only the \
background and lighting quality may change. Preserve the exact beard stubble \
pattern and density.

{REALISM}""",
    },
    "lilly": {
        "input": "l1.png",
        "prompt": f"""{FACE_LOCK}

{STUDIO}

Subject: This exact woman with wavy dark-brown shoulder-length hair, green eyes, \
wearing a black tank top, with a small dark mole below the collarbone. Her face, \
expression, head angle, and pose must remain absolutely unchanged. Only the \
background and lighting quality may change. Preserve the green eye color and iris \
detail exactly.

{REALISM}""",
    },
}

OUTPUT_DIR = Path(__file__).parent / "output"


def generate_headshot(name: str, cfg: dict) -> None:
    input_path = Path(__file__).parent / cfg["input"]
    if not input_path.exists():
        print(f"  SKIP: {input_path} not found")
        return

    print(f"\nGenerating {name} headshot from {cfg['input']} via fal.ai GPT-Image-1.5/edit...")

    # Convert local image to data URI for fal.ai
    data_uri = image_to_data_uri(input_path)

    result = fal_client.subscribe(
        "fal-ai/gpt-image-1.5/edit",
        arguments={
            "prompt": cfg["prompt"],
            "image_urls": [data_uri],
            "image_size": "1024x1024",
            "quality": "high",
            "input_fidelity": "high",
            "num_images": 1,
            "output_format": "png",
        },
    )

    # Download the result image
    images = result.get("images", [])
    if not images:
        print(f"  ERROR: No images returned for {name}")
        return

    image_url = images[0]["url"]
    resp = requests.get(image_url)
    resp.raise_for_status()

    out_path = OUTPUT_DIR / f"{name}_headshot.png"
    out_path.write_bytes(resp.content)
    print(f"  Saved: {out_path} ({len(resp.content)} bytes)")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("=" * 60)
    print("HROC Founder Headshot Generator")
    print("Model: fal-ai/gpt-image-1.5/edit")
    print("Face identity preservation = #1 priority")
    print("=" * 60)

    for name, cfg in FOUNDERS.items():
        try:
            generate_headshot(name, cfg)
        except Exception as e:
            print(f"  ERROR for {name}: {e}")

    print(f"\n{'=' * 60}")
    print(f"Done. Output directory: {OUTPUT_DIR}/")
    print("IMPORTANT: Visually compare each output face to the input.")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
