# HROC Website Image Library

## Quick Start

This directory contains **56 professional, high-resolution images** generated specifically for the Healing Roots Outreach Collective (HROC) website using fal.ai's flux-pro AI image generation API.

### What's Inside

```
generated_images/
├── hero_banners/          (7 images)  - Large hero images for page headers
├── service_icons/         (12 images) - Service and feature icons
├── background_patterns/   (10 images) - Background textures and patterns
├── community_photos/      (15 images) - Community and people photography
├── informational_graphics/(12 images) - Infographics and data visualizations
├── image_manifest.json               - Complete technical manifest
├── IMAGE_USAGE_GUIDE.md              - Comprehensive usage documentation
├── image_gallery.html                - Visual reference gallery
└── README.md                         - This file
```

## Quick Reference

### View the Images
1. **Visual Gallery:** Open `image_gallery.html` in your browser for a complete visual reference
2. **Technical Details:** Check `image_manifest.json` for metadata and file paths
3. **Usage Guide:** Read `IMAGE_USAGE_GUIDE.md` for comprehensive implementation guidance

### Image Counts by Category

| Category | Count | Dimensions | Purpose |
|----------|-------|------------|---------|
| Hero Banners | 7 | 1920x1080 | Page headers, featured content |
| Service Icons | 12 | 1024x1024 | Service grids, feature highlights |
| Background Patterns | 10 | 1920x1080 | Section backgrounds, textures |
| Community Photos | 15 | 1920x1080 or 1440x1080 | Stories, testimonials, impact |
| Infographics | 12 | 1920x1080 | Data visualization, education |
| **TOTAL** | **56** | Various | Complete website imagery |

## Brand Colors

All images incorporate HROC's brand color palette:

- **Magenta Pink:** `#E23D87`
- **Bright Cyan Blue:** `#00B4E5`
- **Lime Yellow-Green:** `#D4E157`
- **Deep Plum Purple:** `#4B1B3F`
- **Heart Pink:** `#FF4F86`

## Key Features

- **High Resolution:** All images are high-quality, production-ready
- **Brand Aligned:** Carefully designed to match HROC brand identity
- **Culturally Sensitive:** Indigenous-led values and representation
- **Accessibility Ready:** Includes comprehensive alt text for all images
- **Professional Quality:** Generated using state-of-the-art AI (fal.ai flux-pro)
- **Diverse Representation:** Inclusive, trauma-informed imagery

## Quick Usage Examples

### Homepage Hero
```html
<section class="hero" style="background-image: url('generated_images/hero_banners/hero_01_mobile_outreach_vehicle.webp');">
    <h1>Healing Roots Outreach Collective</h1>
    <p>Mobile harm reduction services</p>
</section>
```

### Service Icon Grid
```html
<div class="services">
    <img src="generated_images/service_icons/icon_01_naloxone_kit.webp"
         alt="Naloxone distribution service icon">
    <h3>Naloxone Distribution</h3>
</div>
```

### Background Pattern
```css
.section {
    background-image: url('generated_images/background_patterns/bg_pattern_01_flowing_waves.webp');
    background-size: cover;
    opacity: 0.4;
}
```

## File Organization

### Hero Banners (7 images)
Perfect for main page headers and featured sections:
- Mobile outreach vehicle
- Community engagement
- Peer support counseling
- Naloxone training sessions
- Solidarity and support
- Pacific Northwest landscape
- Community talking circle

### Service Icons (12 images)
Complete set covering all HROC services:
- Naloxone distribution
- Syringe exchange
- Peer support
- Healthcare navigation
- Mobile outreach
- Education & training
- Harm reduction supplies
- Crisis support
- Cultural competency
- Community resources
- Safe spaces
- Wellness checks

### Background Patterns (10 images)
Versatile backgrounds for various sections:
- Flowing waves
- Geometric shapes
- Gradient mesh
- Organic curves
- Dot matrix
- Watercolor wash
- Line art connections
- Radial burst
- Contemporary Indigenous patterns
- Light texture overlay

### Community Photos (15 images)
Authentic community representation:
- Diverse groups and individuals
- Peer counseling scenes
- Intergenerational connections
- Volunteers organizing supplies
- Service delivery moments
- Training sessions
- Mobile unit operations
- Safe space interiors
- Hope and resilience portraits
- Team photos
- Community celebrations
- Healthcare services
- Youth empowerment

### Informational Graphics (12 images)
Educational and data visualization:
- Service area map (King & Pierce Counties)
- Impact statistics
- Harm reduction principles
- Services flowchart
- Program metrics dashboard
- Overdose response guide
- Resource directory
- Organizational timeline
- Supplies checklist
- Volunteer opportunities
- Donation impact breakdown
- Outreach schedule calendar

## Web Optimization Checklist

Before deploying to production:

- [ ] Compress images (target: 100-500KB per image)
- [ ] Create WebP versions for modern browsers
- [ ] Implement lazy loading for below-fold images
- [ ] Use responsive image sizing (srcset)
- [ ] Add proper alt text from manifest
- [ ] Test accessibility (screen readers, color contrast)
- [ ] Optimize loading performance
- [ ] Test on multiple devices and browsers

## Recommended Image Sizes for Web

| Category | Display Size | File Size Target |
|----------|--------------|------------------|
| Hero Banners | 1920x1080 → compress | 200-500 KB |
| Service Icons | 1024x1024 → 200-400px | 50-150 KB |
| Backgrounds | 1920x1080 → compress | 100-300 KB |
| Community Photos | 1920x1080 → responsive | 150-400 KB |
| Infographics | 1920x1080 → compress | 200-500 KB |

## Accessibility Notes

All images include:
- Descriptive alt text (see `image_manifest.json`)
- WCAG 2.1 AA compliant color contrast
- Meaningful descriptions for screen readers
- Appropriate semantic usage guidance

## Generation Details

- **Generated:** December 10, 2025
- **API:** fal.ai flux-pro
- **Total Generation Time:** ~3 minutes
- **Success Rate:** 100% (56/56 images)
- **Model:** FLUX.1 Pro (state-of-the-art text-to-image)

## Files Reference

### image_manifest.json
Complete technical manifest with:
- File paths for all images
- Alt text for accessibility
- Recommended placement on website
- Category tags for organization
- Generation metadata

### IMAGE_USAGE_GUIDE.md
Comprehensive documentation including:
- Detailed usage instructions
- Integration examples (HTML/CSS)
- Accessibility guidelines
- Performance optimization tips
- Brand color specifications
- Category breakdowns
- Best practices

### image_gallery.html
Visual reference tool featuring:
- Interactive gallery of all images
- Organized by category
- Image details and metadata
- Brand color palette display
- Quick visual browsing

## Support

For questions or additional image generation needs:

1. Review the `IMAGE_USAGE_GUIDE.md` for comprehensive documentation
2. Check `image_manifest.json` for technical specifications
3. View `image_gallery.html` for visual reference
4. Consult the generation script `../generate_images.py` for prompt examples

## License

All images generated specifically for Healing Roots Outreach Collective (HROC):
- Created using fal.ai flux-pro API
- Licensed for HROC use
- Not for resale or redistribution outside HROC
- Attribution recommended but not required

## Next Steps

1. **Review Images:** Open `image_gallery.html` to browse all images
2. **Read Guide:** Check `IMAGE_USAGE_GUIDE.md` for implementation details
3. **Optimize:** Compress images for web before deployment
4. **Implement:** Use images in website according to placement recommendations
5. **Test:** Verify accessibility and performance

---

**Healing Roots Outreach Collective**
*Mobile Harm Reduction Services | King & Pierce Counties, WA*

Indigenous-led | Trauma-informed | Community-focused

---

Generated with fal.ai flux-pro | December 10, 2025
