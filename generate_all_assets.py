#!/usr/bin/env python3
"""
HROC Complete Asset Generation - FLUX.2 Images + Nano Banana Infographics
Regenerates all images and creates professional infographics using FAL AI
"""

import os
import sys
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import fal_client
try:
    import fal_client
except ImportError:
    print("Installing fal-client...")
    os.system("pip install fal-client")
    import fal_client

# Configuration
OUTPUT_DIRS = {
    'hero': 'HROC_Website_New/generated_images/hero_banners',
    'community': 'HROC_Website_New/generated_images/community_photos',
    'icons': 'HROC_Website_New/generated_images/service_icons',
    'infographics': 'HROC_Website_New/generated_images/informational_graphics',
    'backgrounds': 'HROC_Website_New/generated_images/background_patterns'
}

# ============================================================================
# PART 1: FLUX.2 IMAGE GENERATION PROMPTS
# ============================================================================

HERO_PROMPTS = {
    'hero_01_mobile_outreach_vehicle': 'Professional photo of a branded mobile outreach RV in Seattle streets, daytime, community members approaching with dignity, warm inclusive atmosphere, realistic details, 4K resolution, well-lit urban setting',
    'hero_02_community_engagement': 'Documentary-style photo of Indigenous community members engaged in conversation with peer counselors, authentic connection, urban park setting, genuine smiles, warm lighting, professional composition',
    'hero_03_peer_support': 'Close-up of two people in meaningful conversation, peer support in action, compassionate expressions, community environment, natural warm lighting, professional photography, authentic moment',
    'hero_04_naloxone_training': 'Real-looking training session with peer educator showing naloxone kit to small group, community center, diverse participants, educational materials visible, focused and engaged expressions',
    'hero_05_hands_holding': 'Artistic photo of diverse hands holding together in circle, symbolizing community solidarity, harm reduction mission, overhead shot, warm inclusive feeling, professional composition',
    'hero_06_pacific_northwest_landscape': 'Beautiful Pacific Northwest landscape with Seattle skyline, mountains in background, rainy climate beauty, hope and healing atmosphere, professional photography, inspiring scene',
    'hero_07_community_circle': 'Group of diverse community members sitting in healing circle, Indigenous-informed practice, outdoor setting, genuine connection, professional photography, warm lighting'
}

COMMUNITY_PROMPTS = {
    'community_01_diverse_group_smiling': 'Diverse group of community members smiling together authentically, inclusive representation, outdoor community space, warm genuine moment, professional photography, real connection',
    'community_02_peer_counselor_listening': 'Peer counselor actively listening with empathy and genuine care, one-on-one interaction, compassionate body language, community setting, professional photography',
    'community_03_elder_and_youth': 'Elder and youth in intergenerational connection, wisdom sharing, outdoor setting, genuine affection and respect, authentic Indigenous representation, professional photography',
    'community_04_volunteers_organizing': 'Diverse volunteer team organizing harm reduction supplies, collaborative energy, community warehouse, focused purposeful action, professional documentation',
    'community_05_person_receiving_naloxone': 'Respectful documentation of peer providing naloxone kit with dignity and care, street outreach setting, compassionate interaction, realistic details',
    'community_06_group_training_session': 'Community members in naloxone training session, engaged participation, educational materials visible, diverse participants, urban community center',
    'community_07_mobile_unit_service': 'Peer health worker providing service from mobile unit, compassionate care, street-involved individual receiving support, realistic urban setting',
    'community_08_safe_space_interior': 'Warm welcoming interior of safe space, cozy furnishings, community posters, inclusive environment, natural lighting, realistic space design',
    'community_09_person_hope_expression': 'Portrait of person with hopeful peaceful expression, healing process visualization, warm lighting, genuine emotion, professional portrait',
    'community_10_hands_distributing_supplies': 'Close-up of hands exchanging harm reduction supplies with dignity and respect, community care, realistic details, warm lighting',
    'community_11_team_photo_staff': 'Professional team photo of HROC staff and peer leaders, diverse group, community center setting, unified purposeful expressions',
    'community_12_people_walking_together': 'Diverse community members walking together with purpose, urban setting, connection and solidarity, movement and action, professional photography',
    'community_13_celebration_gathering': 'Community celebration gathering with joy and togetherness, outdoor space, authentic happiness, diverse participation, festive atmosphere',
    'community_14_person_receiving_care': 'Respectful image of person receiving health screening or care service, compassionate healthcare worker, dignity-centered interaction',
    'community_15_youth_empowerment': 'Youth in empowerment and educational setting, peer mentoring, hopeful expressions, community space, authentic representation'
}

SERVICE_ICON_PROMPTS = {
    'icon_01_naloxone_kit': 'Professional medical illustration icon of naloxone kit/Narcan box, clean design, modern medical icon style, vibrant colors, 3D realistic rendering',
    'icon_02_syringe_exchange': 'Professional medical icon showing sterile syringe exchange symbol, harm reduction focused, clinical style, recognizable imagery, modern design',
    'icon_03_peer_support': 'Icon symbolizing peer support with two connected figures, compassionate design, professional style, modern illustration, warm colors',
    'icon_04_healthcare_navigation': 'Healthcare navigation icon with medical cross and directional elements, professional medical icon style, modern design, clear symbolism',
    'icon_05_mobile_outreach': 'Mobile outreach RV icon, professional vehicle illustration, recognizable design, community-focused, modern icon style',
    'icon_06_education_training': 'Education icon with training elements, professional style, modern illustration, book/lightbulb combination, recognizable learning symbol',
    'icon_07_harm_reduction_supplies': 'Icon representing diverse harm reduction supplies, professional medical illustration, clean design, recognizable variety',
    'icon_08_crisis_support': 'Crisis support icon with helping hands and emergency elements, professional design, compassionate symbolism, modern illustration',
    'icon_09_cultural_competency': 'Cultural competency icon with diverse representation and healing symbols, professional design, Indigenous-informed imagery',
    'icon_10_community_resources': 'Community resources icon with network and connection elements, professional design, interconnected concept, modern style',
    'icon_11_safe_space': 'Safe space icon with protective welcoming elements, professional design, home/sanctuary symbolism, warm inviting appearance',
    'icon_12_wellness_check': 'Wellness and health check icon, professional medical style, modern design, positive health imagery, vibrant colors'
}

BACKGROUND_PROMPTS = {
    'bg_pattern_01_flowing_waves': 'Abstract flowing waves pattern, organic movement, healthcare brand colors (magenta and cyan), subtle texture, seamless design',
    'bg_pattern_02_geometric_shapes': 'Modern geometric shapes pattern, contemporary design, healthcare brand colors, professional aesthetic, subtle movement',
    'bg_pattern_03_gradient_mesh': 'Beautiful gradient mesh background, blending magenta and cyan smoothly, professional modern design, subtle texture',
    'bg_pattern_04_organic_curves': 'Organic curved lines pattern, flowing natural forms, healthcare colors, professional aesthetic, subtle texture',
    'bg_pattern_05_dot_matrix': 'Dot matrix pattern with professional design, healthcare colors, modern tech aesthetic, subtle texture',
    'bg_pattern_06_watercolor_wash': 'Watercolor wash pattern, artistic fluid design, magenta and cyan blending, professional aesthetic, natural texture',
    'bg_pattern_07_line_art': 'Line art pattern with flowing lines, contemporary design, healthcare colors, professional aesthetic, subtle texture',
    'bg_pattern_08_radial_burst': 'Radial burst pattern with energy and movement, healthcare colors, professional design, subtle texture',
    'bg_pattern_09_tribal_modern': 'Modern tribal-inspired pattern, Indigenous art influence, healthcare colors, professional aesthetic, meaningful symbolism',
    'bg_pattern_10_light_texture': 'Light subtle texture pattern, minimalist design, healthcare brand colors, professional background, ambient feeling'
}

# ============================================================================
# PART 2: NANO BANANA INFOGRAPHIC GENERATION PROMPTS
# ============================================================================

INFOGRAPHIC_PROMPTS = {
    'info_01_service_area_map': 'Professional infographic map showing King and Pierce Counties service area, highlighted regions, location markers, clean data visualization, professional design, map-style layout',
    'info_02_naloxone_saves_lives_stat': 'Infographic showing naloxone overdose prevention statistics with compelling numbers, visual impact, professional medical design, data-driven visualization, large impact numbers',
    'info_03_harm_reduction_principles': 'Infographic explaining harm reduction principles with icons and text, educational design, clear visual hierarchy, professional layout, 4-5 key principles illustrated',
    'info_04_services_flowchart': 'Flowchart infographic showing available services and pathways, organizational structure, professional design, clear navigation visualization, arrow-based flow',
    'info_05_impact_numbers': 'Impact metrics infographic with compelling statistics display, lives saved, people served, professional design, data visualization, inspiring numbers layout',
    'info_06_overdose_response_steps': 'Step-by-step infographic for overdose response procedure, educational format, numbered steps, professional medical design, practical clarity, 4-5 steps illustrated',
    'info_07_resource_directory': 'Infographic resource directory showing available community resources, organized layout, professional design, icons with descriptions, accessible information',
    'info_08_timeline_organization_history': 'Timeline infographic showing HROC organization history and milestones, chronological design, professional visualization, compelling narrative, year-by-year progression',
    'info_09_supplies_checklist': 'Visual checklist infographic of harm reduction supplies available, organized layout, clear iconography, professional design, practical utility, checkmark style',
    'info_10_volunteer_opportunities': 'Infographic showing volunteer opportunities and roles, recruitment focused, professional design, appealing presentation, role descriptions with icons',
    'info_11_donation_impact': 'Donation impact infographic showing how donations create change, compelling statistics, professional design, fundraising focused, visual connection between donation and impact',
    'info_12_monthly_outreach_calendar': 'Monthly outreach calendar infographic showing service locations and dates, organized layout, professional design, practical utility, calendar-style presentation'
}

# ============================================================================
# ASSET GENERATOR CLASS
# ============================================================================

class AssetGenerator:
    def __init__(self):
        self.fal_key = os.getenv('FAL_KEY')
        if not self.fal_key:
            raise ValueError('FAL_KEY environment variable not set')

        self.generated = []
        self.failed = []
        self.api_calls = 0

    def ensure_output_dirs(self):
        """Create output directories"""
        for dir_path in OUTPUT_DIRS.values():
            Path(dir_path).mkdir(parents=True, exist_ok=True)
        print("✅ Output directories ready")

    def log_update(self, update):
        """Log queue updates"""
        if isinstance(update, fal_client.InProgress):
            for log in update.logs:
                print(f"  → {log['message']}")

    def generate_flux_image(self, filename, prompt, category, image_size="landscape_4_3"):
        """Generate single FLUX.2 image"""
        try:
            print(f"📸 Generating: {filename}")

            result = fal_client.subscribe(
                "fal-ai/flux-2",
                arguments={
                    "prompt": prompt,
                    "guidance_scale": 3.0,
                    "num_inference_steps": 28,
                    "image_size": image_size,
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
                    print(f"   ✅ Saved to: {output_path}")
                    self.generated.append((filename, category, "FLUX.2"))
                    return output_path

            self.failed.append((filename, "No image returned"))
            return None

        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def generate_nano_banana_infographic(self, filename, prompt):
        """Generate infographic with Nano Banana"""
        try:
            print(f"📊 Generating infographic: {filename}")

            result = fal_client.subscribe(
                "fal-ai/nano-banana",
                arguments={
                    "prompt": f"Create a professional infographic: {prompt}",
                    "model": "flux-pro",
                    "image_size": "landscape_16_9",
                },
                with_logs=True,
                on_queue_update=self.log_update,
            )

            if result.get('images') and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                output_path = f"{OUTPUT_DIRS['infographics']}/{filename}.png"

                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"   ✅ Saved to: {output_path}")
                    self.generated.append((filename, "infographics", "Nano Banana"))
                    return output_path

            self.failed.append((filename, "No infographic returned"))
            return None

        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def generate_batch(self, prompts, category, image_generator, image_size="landscape_4_3"):
        """Generate batch of images"""
        print(f"\n🎨 Generating {category.upper()} ({len(prompts)} items)")
        print("=" * 70)

        for filename, prompt in prompts.items():
            image_generator(filename, prompt, category, image_size)
            time.sleep(1)  # Rate limiting

    def generate_all_flux_images(self):
        """Generate all FLUX.2 images"""
        print("\n" + "=" * 70)
        print("FLUX.2 IMAGE GENERATION")
        print("=" * 70)

        self.generate_batch(HERO_PROMPTS, 'hero', self.generate_flux_image)
        self.generate_batch(COMMUNITY_PROMPTS, 'community', self.generate_flux_image)
        self.generate_batch(SERVICE_ICON_PROMPTS, 'icons', self.generate_flux_image, image_size="square")
        self.generate_batch(BACKGROUND_PROMPTS, 'backgrounds', self.generate_flux_image)

    def generate_all_infographics(self):
        """Generate all Nano Banana infographics"""
        print("\n" + "=" * 70)
        print("NANO BANANA INFOGRAPHIC GENERATION")
        print("=" * 70 + "\n")

        for filename, prompt in INFOGRAPHIC_PROMPTS.items():
            self.generate_nano_banana_infographic(filename, prompt)
            time.sleep(1)

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)
        print(f"✅ Successfully generated: {len(self.generated)} assets")
        print(f"❌ Failed to generate: {len(self.failed)} assets")

        if self.generated:
            print("\n📦 Generated Assets by Type:")
            flux_count = len([x for x in self.generated if x[2] == "FLUX.2"])
            nano_count = len([x for x in self.generated if x[2] == "Nano Banana"])
            print(f"  - FLUX.2 Images: {flux_count}")
            print(f"  - Nano Banana Infographics: {nano_count}")

        if self.failed:
            print("\n⚠️ Failed generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

        print("\n✨ Next Steps:")
        print("  1. Review generated images in output directories")
        print("  2. Test all links on site")
        print("  3. Commit changes to git")
        print("  4. Deploy to hrocinc.org")

def main():
    try:
        print("HROC Complete Asset Generation")
        print("=" * 70)
        print("This will generate:")
        print("  - 56 FLUX.2 images (heroes, community, icons, backgrounds)")
        print("  - 12 Nano Banana infographics")
        print("=" * 70 + "\n")

        generator = AssetGenerator()
        print("[OK] FAL API key detected\n")

        generator.ensure_output_dirs()

        # Generate FLUX.2 images
        generator.generate_all_flux_images()

        # Generate Nano Banana infographics
        generator.generate_all_infographics()

        # Print summary
        generator.print_summary()

        return 0

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
