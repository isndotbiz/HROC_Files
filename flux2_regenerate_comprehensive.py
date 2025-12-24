#!/usr/bin/env python3
"""
HROC Image Regeneration Script using FAL AI FLUX.2 [dev]
Regenerates all hero banners, community photos, service icons, and infographics
with enhanced realism, crisper text, and better composition.

Install: pip install fal-client
Setup: Set FAL_KEY environment variable or create .env file
"""

import os
import fal_client
from pathlib import Path
from dotenv import load_dotenv
import time
import json
from typing import Optional

# Load environment variables
load_dotenv()

# Configuration
OUTPUT_DIRS = {
    'hero': 'HROC_Website_New/generated_images/hero_banners',
    'community': 'HROC_Website_New/generated_images/community_photos',
    'icons': 'HROC_Website_New/generated_images/service_icons',
    'infographics': 'HROC_Website_New/generated_images/informational_graphics',
    'backgrounds': 'HROC_Website_New/generated_images/background_patterns'
}

# Hero Banner Prompts (Enhanced for FLUX.2)
HERO_PROMPTS = {
    'hero_01_mobile_outreach_vehicle': 'Professional photo of a branded mobile outreach RV in Seattle streets, daytime, community members approaching with dignity, warm inclusive atmosphere, realistic details, 4K resolution, well-lit urban setting',
    'hero_02_community_engagement': 'Documentary-style photo of Indigenous community members engaged in conversation with peer counselors, authentic connection, urban park setting, genuine smiles, warm lighting, professional composition, no artificial look',
    'hero_03_peer_support': 'Close-up of two people in meaningful conversation, peer support in action, compassionate expressions, community environment, natural warm lighting, professional photography, authentic moment',
    'hero_04_naloxone_training': 'Real-looking training session with peer educator showing naloxone kit to small group, community center, diverse participants, educational materials visible, focused and engaged expressions, realistic details',
    'hero_05_hands_holding': 'Artistic photo of diverse hands holding together in circle, symbolizing community solidarity, harm reduction mission, overhead shot, warm inclusive feeling, professional composition, meaningful symbolism',
    'hero_06_pacific_northwest_landscape': 'Beautiful Pacific Northwest landscape with Seattle skyline, mountains in background, rainy climate beauty, hope and healing atmosphere, professional photography, inspiring scene',
    'hero_07_community_circle': 'Group of diverse community members sitting in healing circle, Indigenous-informed practice, outdoor setting, genuine connection, professional photography, warm lighting, authentic gathering'
}

# Community Photo Prompts (Enhanced for FLUX.2)
COMMUNITY_PROMPTS = {
    'community_01_diverse_group_smiling': 'Diverse group of community members smiling together authentically, inclusive representation, outdoor community space, warm genuine moment, professional photography, no posing, real connection',
    'community_02_peer_counselor_listening': 'Peer counselor actively listening with empathy and genuine care, one-on-one interaction, compassionate body language, community setting, professional photography, authentic moment',
    'community_03_elder_and_youth': 'Elder and youth in intergenerational connection, wisdom sharing, outdoor setting, genuine affection and respect, authentic Indigenous representation, professional photography',
    'community_04_volunteers_organizing': 'Diverse volunteer team organizing harm reduction supplies, collaborative energy, community warehouse, focused purposeful action, professional documentation, realistic details',
    'community_05_person_receiving_naloxone': 'Respectful documentation of peer providing naloxone kit with dignity and care, street outreach setting, compassionate interaction, realistic details, professional photography',
    'community_06_group_training_session': 'Community members in naloxone training session, engaged participation, educational materials visible, diverse participants, urban community center, professional documentation',
    'community_07_mobile_unit_service': 'Peer health worker providing service from mobile unit, compassionate care, street-involved individual receiving support, realistic urban setting, professional photography',
    'community_08_safe_space_interior': 'Warm welcoming interior of safe space, cozy furnishings, community posters, inclusive environment, natural lighting, realistic space design, healing atmosphere',
    'community_09_person_hope_expression': 'Portrait of person with hopeful peaceful expression, healing process visualization, warm lighting, genuine emotion, professional portrait, respectful representation',
    'community_10_hands_distributing_supplies': 'Close-up of hands exchanging harm reduction supplies with dignity and respect, community care, realistic details, warm lighting, meaningful interaction',
    'community_11_team_photo_staff': 'Professional team photo of HROC staff and peer leaders, diverse group, community center setting, unified purposeful expressions, professional documentation',
    'community_12_people_walking_together': 'Diverse community members walking together with purpose, urban setting, connection and solidarity, movement and action, professional photography, inspiring scene',
    'community_13_celebration_gathering': 'Community celebration gathering with joy and togetherness, outdoor space, authentic happiness, diverse participation, festive atmosphere, professional photography',
    'community_14_person_receiving_care': 'Respectful image of person receiving health screening or care service, compassionate healthcare worker, dignity-centered interaction, realistic details',
    'community_15_youth_empowerment': 'Youth in empowerment and educational setting, peer mentoring, hopeful expressions, community space, authentic representation, professional photography'
}

# Service Icon Prompts (Enhanced for FLUX.2)
SERVICE_ICON_PROMPTS = {
    'icon_01_naloxone_kit': 'Professional medical illustration icon of naloxone kit/Narcan box, clean design, modern medical icon style, clear recognizable, vibrant colors, 3D realistic rendering',
    'icon_02_syringe_exchange': 'Professional medical icon showing sterile syringe exchange symbol, harm reduction focused, clinical style, recognizable imagery, modern design, professional colors',
    'icon_03_peer_support': 'Icon symbolizing peer support with two connected figures, compassionate design, professional style, modern illustration, warm colors, recognizable concept',
    'icon_04_healthcare_navigation': 'Healthcare navigation icon with medical cross and directional elements, professional medical icon style, modern design, clear symbolism, recognizable',
    'icon_05_mobile_outreach': 'Mobile outreach RV icon, professional vehicle illustration, recognizable design, community-focused, modern icon style, vibrant presentation',
    'icon_06_education_training': 'Education icon with training elements, professional style, modern illustration, book/lightbulb combination, recognizable learning symbol, vibrant colors',
    'icon_07_harm_reduction_supplies': 'Icon representing diverse harm reduction supplies, professional medical illustration, clean design, recognizable variety, modern icon style',
    'icon_08_crisis_support': 'Crisis support icon with helping hands and emergency elements, professional design, compassionate symbolism, modern illustration style, recognizable',
    'icon_09_cultural_competency': 'Cultural competency icon with diverse representation and healing symbols, professional design, Indigenous-informed imagery, modern illustration, inclusive',
    'icon_10_community_resources': 'Community resources icon with network and connection elements, professional design, interconnected concept, modern style, recognizable symbols',
    'icon_11_safe_space': 'Safe space icon with protective welcoming elements, professional design, home/sanctuary symbolism, modern illustration, warm inviting appearance',
    'icon_12_wellness_check': 'Wellness and health check icon, professional medical style, modern design, positive health imagery, recognizable wellness symbol, vibrant colors'
}

# Background Pattern Prompts (Enhanced for FLUX.2)
BACKGROUND_PROMPTS = {
    'bg_pattern_01_flowing_waves': 'Abstract flowing waves pattern, organic movement, healthcare brand colors (magenta and cyan), subtle texture, professional background, seamless design',
    'bg_pattern_02_geometric_shapes': 'Modern geometric shapes pattern, contemporary design, healthcare brand colors, professional aesthetic, subtle movement, seamless pattern',
    'bg_pattern_03_gradient_mesh': 'Beautiful gradient mesh background, blending magenta and cyan smoothly, professional modern design, subtle texture, ambient lighting effect',
    'bg_pattern_04_organic_curves': 'Organic curved lines pattern, flowing natural forms, healthcare colors, professional aesthetic, subtle texture, healing energy feeling',
    'bg_pattern_05_dot_matrix': 'Dot matrix pattern with professional design, healthcare colors, modern tech aesthetic, subtle texture, professional background, recognizable pattern',
    'bg_pattern_06_watercolor_wash': 'Watercolor wash pattern, artistic fluid design, magenta and cyan blending, professional aesthetic, natural texture, healing feeling',
    'bg_pattern_07_line_art': 'Line art pattern with flowing lines, contemporary design, healthcare colors, professional aesthetic, subtle texture, modern look',
    'bg_pattern_08_radial_burst': 'Radial burst pattern with energy and movement, healthcare colors, professional design, subtle texture, dynamic feeling',
    'bg_pattern_09_tribal_modern': 'Modern tribal-inspired pattern, Indigenous art influence, healthcare colors, professional aesthetic, meaningful symbolism, contemporary design',
    'bg_pattern_10_light_texture': 'Light subtle texture pattern, minimalist design, healthcare brand colors, professional background, ambient feeling, versatile use'
}

# Infographic Prompts (NEW - Enhanced for FLUX.2)
INFOGRAPHIC_PROMPTS = {
    'info_01_service_area_map': 'Professional infographic map showing King and Pierce Counties service area, highlighted regions, location markers, clean data visualization, professional design',
    'info_02_naloxone_saves_lives_stat': 'Infographic showing naloxone overdose prevention statistics, compelling numbers, visual impact, professional medical design, data-driven visualization',
    'info_03_harm_reduction_principles': 'Infographic explaining harm reduction principles with icons and text, educational design, clear visual hierarchy, professional layout, compelling imagery',
    'info_04_services_flowchart': 'Flowchart infographic showing available services and pathways, organizational structure, professional design, clear navigation visualization',
    'info_05_impact_numbers': 'Impact metrics infographic with compelling statistics, lives saved, people served, professional design, data visualization, inspiring numbers display',
    'info_06_overdose_response_steps': 'Step-by-step infographic for overdose response procedure, educational format, clear instructions, professional medical design, practical clarity',
    'info_07_resource_directory': 'Infographic resource directory showing available community resources, organized layout, professional design, accessible information',
    'info_08_timeline_organization_history': 'Timeline infographic showing HROC organization history and milestones, chronological design, professional visualization, compelling narrative',
    'info_09_supplies_checklist': 'Visual checklist infographic of harm reduction supplies available, organized layout, clear iconography, professional design, practical utility',
    'info_10_volunteer_opportunities': 'Infographic showing volunteer opportunities and roles, recruitment focused, professional design, appealing presentation',
    'info_11_donation_impact': 'Donation impact infographic showing how donations create change, compelling statistics, professional design, fundraising focused',
    'info_12_monthly_outreach_calendar': 'Monthly outreach calendar infographic showing service locations and dates, organized layout, professional design, practical utility'
}

class FluxImageGenerator:
    def __init__(self):
        self.fal_key = os.getenv('FAL_KEY')
        if not self.fal_key:
            raise ValueError('FAL_KEY environment variable not set. Please set it in .env file or environment.')

        self.generated = []
        self.failed = []

    def ensure_output_dirs(self):
        """Create output directories if they don't exist"""
        for dir_path in OUTPUT_DIRS.values():
            Path(dir_path).mkdir(parents=True, exist_ok=True)

    def log_update(self, update):
        """Log queue update messages"""
        if isinstance(update, fal_client.InProgress):
            for log in update.logs:
                print(f"  → {log['message']}")

    def generate_image(self, filename: str, prompt: str, category: str, image_size: str = "landscape_4_3") -> Optional[str]:
        """Generate a single image using FAL FLUX.2"""
        try:
            print(f"📸 Generating: {filename}")
            print(f"   Prompt: {prompt[:60]}...")

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

            if result['images'] and len(result['images']) > 0:
                image_url = result['images'][0]['url']
                output_path = f"{OUTPUT_DIRS[category]}/{filename}.png"

                # Download image
                import requests
                response = requests.get(image_url)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"   ✅ Saved to: {output_path}")
                    self.generated.append((filename, category))
                    return output_path
                else:
                    print(f"   ❌ Failed to download image")
                    self.failed.append((filename, "Download failed"))
                    return None
            else:
                print(f"   ❌ No image in result")
                self.failed.append((filename, "No image returned"))
                return None

        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            self.failed.append((filename, str(e)))
            return None

    def generate_batch(self, prompts: dict, category: str, image_size: str = "landscape_4_3"):
        """Generate a batch of images"""
        print(f"\n🎨 Generating {category.upper()} ({len(prompts)} images)")
        print("=" * 70)

        for filename, prompt in prompts.items():
            self.generate_image(filename, prompt, category, image_size)
            time.sleep(0.5)  # Rate limiting

    def generate_all(self):
        """Generate all images"""
        self.ensure_output_dirs()

        print("\n" + "=" * 70)
        print("HROC IMAGE GENERATION - FLUX.2 [dev]")
        print("=" * 70)

        # Generate hero banners
        self.generate_batch(HERO_PROMPTS, 'hero')

        # Generate community photos
        self.generate_batch(COMMUNITY_PROMPTS, 'community')

        # Generate service icons (square format)
        self.generate_batch(SERVICE_ICON_PROMPTS, 'icons', image_size="square")

        # Generate background patterns
        self.generate_batch(BACKGROUND_PROMPTS, 'backgrounds')

        # Generate infographics (landscape format for data viz)
        self.generate_batch(INFOGRAPHIC_PROMPTS, 'infographics', image_size="landscape_16_9")

        # Print summary
        self.print_summary()

    def print_summary(self):
        """Print generation summary"""
        print("\n" + "=" * 70)
        print("GENERATION COMPLETE")
        print("=" * 70)
        print(f"✅ Successfully generated: {len(self.generated)} images")
        print(f"❌ Failed to generate: {len(self.failed)} images")

        if self.failed:
            print("\nFailed generations:")
            for filename, error in self.failed:
                print(f"  - {filename}: {error}")

        print("\n📁 Output directories:")
        for category, path in OUTPUT_DIRS.items():
            print(f"  - {category}: {path}")

        print("\n💡 Next steps:")
        print("  1. Review generated images in output directories")
        print("  2. Update HTML references if filenames changed")
        print("  3. Commit changes to git")
        print("  4. Deploy to production")

def main():
    try:
        generator = FluxImageGenerator()
        print("✅ FAL API key detected")
        print("Starting comprehensive image regeneration...\n")
        generator.generate_all()

    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\n📝 Setup instructions:")
        print("  1. Create a .env file in the project root")
        print("  2. Add your FAL API key:")
        print("     FAL_KEY=your_api_key_here")
        print("  3. Get your key from: https://fal.ai")
        return 1
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit(main())
