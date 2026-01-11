# Founder Positioning Dataset

## Overview

This dataset contains **30 professional founder portrait variations** (10 per founder) with **subtle positioning differences**. This dataset is designed for both website display variations and as high-quality training data.

### Founders Included
- **Jonathan Mallinger** (President/Co-Founder)
- **Bri** (Secretary/Co-Founder)
- **Lilly** (Co-Founder)

## Dataset Structure

```
Positioning_Dataset/
├── Jonathan/
│   ├── jonathan_positioning_01_direct_facing_neutral.png
│   ├── jonathan_positioning_02_slight_head_tilt_left.png
│   ├── jonathan_positioning_03_slight_head_tilt_right.png
│   ├── jonathan_positioning_04_over_shoulder_look.png
│   ├── jonathan_positioning_05_seated_close_up.png
│   ├── jonathan_positioning_06_standing_full_body.png
│   ├── jonathan_positioning_07_leaning_casual_professional.png
│   ├── jonathan_positioning_08_three_quarter_profile.png
│   ├── jonathan_positioning_09_hands_visible_active_pose.png
│   └── jonathan_positioning_10_natural_candid_moment.png
├── Bri/
│   ├── bri_positioning_01_direct_facing_neutral.png
│   ├── ... (8 more variations)
│   └── bri_positioning_10_natural_candid_moment.png
└── Lilly/
    ├── lilly_positioning_01_direct_facing_neutral.png
    ├── ... (8 more variations)
    └── lilly_positioning_10_natural_candid_moment.png
```

## Positioning Variations

Each founder has 10 subtle variations organized by positioning technique:

### Variation Reference

| ID | Name | Focus | Description |
|----|------|-------|-------------|
| 1 | Direct Facing - Neutral | Head angle, Distance | Head straight, directly facing camera, neutral professional expression |
| 2 | Slight Head Tilt Left | Head angle | Head tilted slightly to the left, friendly approachable |
| 3 | Slight Head Tilt Right | Head angle | Head tilted slightly to the right, thoughtful pose |
| 4 | Over Shoulder Look | Body posture, Head angle | Body angled away, looking over shoulder at camera |
| 5 | Seated - Close Up | Body posture, Distance | Seated position, closer to camera, more intimate framing |
| 6 | Standing Full Body | Body posture, Distance | Full body standing position, further from camera |
| 7 | Leaning Casual Professional | Body posture | Leaning against desk/wall, relaxed but professional |
| 8 | Three Quarter Profile | Body posture, Head angle | Head/body at three-quarter angle, slightly away from camera |
| 9 | Hands Visible - Active Pose | Body posture, Hand positioning | Hands prominently visible, active engaged gesture |
| 10 | Natural Candid Moment | All - natural variation | More candid, natural expression, slight genuine smile |

## Setting Variations

The dataset uses a **mix of consistent and varied settings**:

### Consistent Setting (Variations 1-5, 9)
- Modern professional office environment
- Consistent lighting setup
- Focus on body posture and head positioning changes
- Ideal for direct visual comparison

### Varied Settings (Variations 6-8, 10)
- Modern office
- Casual professional spaces
- Outdoor professional settings
- Natural and varied lighting
- More diverse context

## Technical Specifications

### Generation Method
- **API**: fal.ai FLUX LoRA Fast Training
- **Models Used**: Pre-trained LoRA models for each founder
  - Jonathan: `JDMHROC`
  - Bri: `BRIHROC`
  - Lilly: `LILLYHROC`

### Image Quality
- **Resolution**: 1024x1024 pixels
- **Aspect Ratio**: 1:1 (square)
- **Format**: PNG
- **Color Profile**: sRGB

### Generation Settings
- **Inference Steps**: 30
- **Guidance Scale**: 7.5
- **Seed**: 42 (consistent for reproducibility)

## Use Cases

### Website Display
- **Hero Section**: Use variation 1, 2, or 10 for primary founder images
- **About Page**: Rotate through variations for visual interest
- **Team Page**: Use contrasting variations (e.g., 4 & 6) for layout variety
- **Social Media**: Mix professional (1, 2, 3) with casual (7, 10) for tone variety

### Training & Evaluation
- **LoRA Model Refinement**: Use full dataset to retrain models with improved pose diversity
- **A/B Testing**: Compare variations 1 vs. 2 vs. 10 for audience preference
- **Brand Consistency**: Ensure consistent visual identity across founder portraits
- **Accessibility**: Provide varied visual representations for diverse audiences

### Marketing Materials
- **Print Materials**: Variations 1, 5, 6 work well for professional printing
- **Digital Ads**: Variations 2, 4, 9 provide dynamic engagement
- **Presentations**: Use variation 6 (full body) for leadership context

## Metadata

Each variation includes:
- **Variation ID** (1-10)
- **Variation Name** (descriptive)
- **Focus Area** (what positioning changed)
- **Setting Type** (consistent vs. varied)
- **Suggested Use Cases**

### Access Metadata
```json
{
  "founder": "Jonathan",
  "variation_id": 1,
  "name": "Direct Facing - Neutral",
  "focus": ["Head angle", "Distance"],
  "setting": "consistent",
  "suggested_uses": ["primary headshot", "professional context"],
  "generation_date": "2024-12-17",
  "model_used": "JDMHROC",
  "quality_score": "professional"
}
```

## Quality Assessment

All images in this dataset meet professional standards:
- ✓ Professional lighting and composition
- ✓ Clear facial features and expressions
- ✓ Consistent brand representation
- ✓ High resolution suitable for print (300 DPI @ 3.4"×3.4")
- ✓ Web-optimized (72 DPI @ 1024×1024px)

## Next Steps

### Recommended Actions
1. **Review Dataset**: Assess variations across all founders
2. **Gather Feedback**: Get stakeholder input on favorite variations
3. **Select Primary Portraits**: Choose 2-3 variations per founder for main website use
4. **Archive Full Set**: Keep complete dataset for future training/refinement
5. **Update Website**: Implement chosen variations in website design

### Future Enhancements
- Generate additional style variations (casual, outdoor, event-based)
- Create animated transitions between selected variations
- Develop seasonal/contextual image rotations
- Build AI-powered portrait selector for dynamic website

## Generation Script

To regenerate or modify this dataset:

```bash
python3 generate_founder_positioning_dataset.py
```

Configuration file: `founder_positioning_prompts.json`

## File Manifest

- **Total Images**: 30 (10 per founder)
- **Total File Size**: ~15-20 MB (PNG format, 1024x1024)
- **Generation Time**: ~15-20 minutes (including API calls and downloads)
- **Last Generated**: [See GENERATION_SUMMARY.json]

## Questions & Support

For questions about this dataset or modifications needed, refer to:
- Generation script: `generate_founder_positioning_dataset.py`
- Prompt configuration: `founder_positioning_prompts.json`
- Generation summary: `GENERATION_SUMMARY.json`
