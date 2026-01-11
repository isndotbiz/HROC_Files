# Bri LoRA Models - Training Comparison

## Overview
Two separate FLUX LoRA models were trained for Bri using different photo selections and scenarios.

## Model 1 (BRIHROC - First Training)
- **Status**: Check first set directory for details
- **Trigger Word**: BRIHROC
- **Focus**: Initial professional portraits

## Model 2 (BRIHROC2 - Second Training) ✓ COMPLETED

### Training Details
- **Trigger Word**: BRIHROC2
- **Training Date**: December 10, 2025, 04:39 AM
- **Training Steps**: 1000
- **Training Images**: 15 high-quality photos
- **Training Time**: ~2.5 minutes (148 seconds)
- **Model URL**: https://v3b.fal.media/files/b/0a85bdb8/vEnaMpDJVqlhDLwy9ByVT_pytorch_lora_weights.safetensors

### Training Data
- 15 photos from `/Users/jonathanmallinger/Documents/HROC_Files/Officers/B/`
- All images compressed and resized to 1024px max dimension
- Total training data size: 1.94MB (zip file)
- Format: High-quality JPG (quality 85)

### Generated Images - Set 2
**Output Directory**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Bri_Set2/`

**10 Professional Images Generated**:
1. Casual business setting at modern cafe
2. Outdoor portrait in urban park
3. Team leadership presenting to group
4. Community engagement event
5. Conference room meeting
6. Creative workspace with plants
7. Walking in urban business district
8. Standing desk in modern office
9. Team collaboration brainstorming
10. Community garden/green space

**Image Specifications**:
- Size: portrait_4_3 (832x1216 pixels)
- Inference Steps: 28
- Guidance Scale: 3.5
- LoRA Scale: 1.0
- Total Size: ~1.9MB for all 10 images

### Scenario Focus - Set 2
This second set emphasized:
- Casual and creative professional environments
- Outdoor professional contexts
- Team collaboration and leadership
- Community engagement
- Sustainable/eco themes
- Dynamic and candid compositions

### Key Differences from Set 1
- More diverse environmental settings
- Greater emphasis on outdoor and casual contexts
- Team interaction scenarios included
- Community-focused themes
- Varied lighting conditions and backgrounds

## Files and Locations

### Model 2 Output
- **Generated Images**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Bri_Set2/bri_set2_professional_[1-10].png`
- **Summary**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Bri_Set2/generation_summary.txt`
- **Detailed Results**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Bri_Set2/RESULTS.md`

## Usage

To generate new images with Model 2, use:
- **Trigger word**: BRIHROC2
- **Model URL**: https://v3b.fal.media/files/b/0a85bdb8/vEnaMpDJVqlhDLwy9ByVT_pytorch_lora_weights.safetensors
- **Recommended settings**: 28 inference steps, 3.5 guidance scale

## Status Summary

✓ Model 2 Training: COMPLETED
✓ Image Generation Set 2: COMPLETED (10/10 images)
✓ Documentation: COMPLETED
