# Portrait Dataset Generated with FAL AI Qwen Models

## Overview
Successfully generated **120 professional portrait images** from 3 source images using FAL AI's Qwen image editing models.

## Dataset Composition

### By Source Image:
- **j1.webp**: 40 variations
  - 5 Close-ups (facial expressions & features)
  - 5 Upper body shots (posture & styling)
  - 5 Multiple angles (left profile → right profile)
  - 5 Full-body images (silhouette & style)
  - Plus secondary set of 20 with refined prompts

- **l1.webp**: 40 variations (same categories)
- **b1.webp**: 40 variations (same categories)

### File Organization:
- `{source}_close_ups_1-5.webp` - Close-up facial expressions
- `{source}_upper_body_1-5.webp` - Upper body shots
- `{source}_multiple_angles_1-5.webp` - Different angles (profiles)
- `{source}_full_body_1-5.webp` - Full-body portraits

Plus alternate naming convention:
- `{source}_close_1-5.webp`
- `{source}_upper_1-5.webp`
- `{source}_angle_1-5.webp`
- `{source}_full_1-5.webp`

## AI Models Used
1. **fal-ai/qwen-image-edit-2509-lora-gallery/face-to-full-portrait**
   - Used for: Close-ups, Upper body, Full-body shots
   - Specializes in portrait variations

2. **fal-ai/qwen-image-edit-2509-lora-gallery/multiple-angles**
   - Used for: Multi-angle shots
   - Generates different perspectives of the same subject

## Generation Details
- **Total Images**: 120 WebP files
- **Total Size**: 88 MB
- **Format**: WebP (optimized)
- **Generation Time**: ~2 hours
- **API**: FAL AI with Qwen image models

## Prompts Categories

### Close-ups (5 variations per source)
- Natural smile and eyes
- Serious expression with piercing eyes
- Contemplative look with facial details
- Genuine warmth and smile
- Dramatic expression

### Upper Body (5 variations per source)
- Confident standing pose with professional attire
- Relaxed posture with casual styling
- Dynamic pose showing movement
- Elegant pose with sophisticated styling
- Approachable pose with friendly demeanor

### Multiple Angles (5 variations per source)
- Left profile view
- Three-quarter front-left angle
- Straight front view
- Three-quarter front-right angle
- Right profile view

### Full-Body (5 variations per source)
- Standing straight, neutral expression, formal outfit
- Dynamic standing pose, casual styling
- Seated pose, relaxed, contemporary outfit
- Standing with slight lean, business casual
- Standing professional stance, elegant styling

## Usage
These images can be used for:
- Training computer vision models
- Character design references
- Portfolio demonstrations
- AI model benchmarking
- Dataset augmentation
