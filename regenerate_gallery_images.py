#!/usr/bin/env python3
"""
Regenerate gallery images for symmetrical layout
Creates 6 community photos and 6 impact story images total
"""

import os
import sys
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set FAL_KEY from environment for fal_client
fal_api_key = os.getenv('FAL_API_KEY')
if fal_api_key:
    os.environ['FAL_KEY'] = fal_api_key

# Try to import fal_client
try:
    import fal_client
except ImportError:
    print("Installing fal-client...")
    os.system("pip install fal-client")
    import fal_client

# Configuration
OUTPUT_DIRS = {
    'community': 'HROC_Website_New/generated_images/community_photos',
    'hero': 'HROC_Website_New/generated_images/hero_banners',
    'infographics': 'HROC_Website_New/generated_images/informational_graphics',
}

# Additional community photos (to make 6 total for symmetry)
ADDITIONAL_COMMUNITY_PROMPTS = {
    'community_16_harm_reduction_dignity': 'Respectful image of peer providing harm reduction services with full dignity, compassionate interaction, community setting, warm lighting, professional photography',
    'community_17_healing_circles': 'Community members in healing circle, cultural practice, outdoor natural setting, genuine connection, authentic representation, professional photography',
    'community_18_peer_mentorship': 'Peer mentor supporting someone, one-on-one connection, urban community space, genuine trust and support, warm lighting, professional photography',
}

# Hero banner images for impact stories (to make 6 total)
ADDITIONAL_HERO_PROMPTS = {
    'hero_08_community_celebration': 'Community celebration of success and healing, diverse people together, joyful atmosphere, urban community setting, professional photography, hopeful energy',
    'hero_09_youth_leadership': 'Youth peer leaders in action, empowerment and responsibility, community center setting, authentic leadership moment, professional photography, inspiring scene',
    'hero_10_culturally_centered_care': 'Indigenous-informed cultural healing practice in action, traditional elements, community gathering, authentic representation, professional photography, respectful documentation',
}

class GalleryImageGenerator:
    def __init__(self):
        self.fal_key = os.getenv('FAL_API_KEY')
        if not self.fal_key:
            raise ValueError('FAL_API_KEY environment variable not set')

        self.generated = []
        self.failed = []

    def ensure_output_dirs(self):
        """Create output directories"""
        for dir_path in OUTPUT_DIRS.values():
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        print("[OK] Output directories ready")

    def log_update(self, update):
        """Log queue updates"""
        if isinstance(update, fal_client.InProgress):
            for log in update.logs:
                print(f"  -> {log['message']}")

    def generate_flux_image(self, filename, prompt, category):
        """Generate single FLUX.2 image"""
        try:
            print(f"[IMG] Generating: {filename}")

            result = fal_client.subscribe(
                "fal-ai/flux-2",
                arguments={
                    "prompt": prompt,
                    "guidance_scale": 3.0,
                    "num_inference_steps": 28,
                    "image_size": "landscape_4_3",
                    "num_images": 1,
                    "acceleration": "regular",
                    "enable_safety_checker": True,
                    "output_format": "png"
                },
                with_logs=True,
                on_queue_update=self.log_update,
            )

            if result.get('images') and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                output_path = f"{OUTPUT_DIRS[category]}/{filename}.png"

                # Download image
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"   [OK] Saved to: {output_path}")
                    self.generated.append((filename, category))
                    return output_path

            self.failed.append((filename, "No image returned"))
            return None

        except Exception as e:
            print(f"   [ERROR] {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)
        print(f"[OK] Successfully generated: {len(self.generated)} assets")
        print(f"[ERROR] Failed to generate: {len(self.failed)} assets")

        if self.generated:
            print("\nGenerated images by category:")
            by_category = {}
            for filename, category in self.generated:
                by_category[category] = by_category.get(category, 0) + 1
            for category, count in by_category.items():
                print(f"  - {category}: {count}")

        if self.failed:
            print("\nFailed generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

        print("\nNext steps:")
        print("  1. Update index.html with new image references")
        print("  2. Commit changes to git")
        print("  3. Deploy to hrocinc.org")

def main():
    try:
        print("=" * 70)
        print("REGENERATE GALLERY IMAGES FOR SYMMETRICAL LAYOUT")
        print("=" * 70)
        print("This will generate:")
        print("  - 3 additional community photos (6 total for 2x3 grid)")
        print("  - 3 additional hero banners (6 total for impact stories)")
        print("=" * 70 + "\n")

        generator = GalleryImageGenerator()
        print("[OK] FAL API key detected\n")

        generator.ensure_output_dirs()

        # Generate additional community photos
        print("\n[GEN] Generating additional community photos...")
        for filename, prompt in ADDITIONAL_COMMUNITY_PROMPTS.items():
            generator.generate_flux_image(filename, prompt, 'community')
            time.sleep(1)

        # Generate additional hero banners
        print("\n[GEN] Generating additional hero banners...")
        for filename, prompt in ADDITIONAL_HERO_PROMPTS.items():
            generator.generate_flux_image(filename, prompt, 'hero')
            time.sleep(1)

        # Print summary
        generator.print_summary()

        return 0 if len(generator.failed) == 0 else 1

    except ValueError as e:
        print(f"[ERROR] {e}")
        print("\nSetup instructions:")
        print("  1. Create .env file in project root")
        print("  2. Add: FAL_KEY=your_api_key_here")
        print("  3. Get key from: https://fal.ai")
        return 1
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
