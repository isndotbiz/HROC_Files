# Face-Consistent Image Generation - Model Comparison Guide

## Overview

This guide compares three state-of-the-art image generation models for creating founder portrait variations with 100% face consistency:

1. **Flux Kontext** - Advanced image-to-image with context awareness
2. **Qwen Image** - Purpose-built for face consistency (Qwen-Edit-2509)
3. **Z-Image Turbo** - Ultra-fast generation with LoRA consistency

---

## Detailed Model Analysis

### 1. FLUX.1 Kontext [Pro]

**Model ID**: `fal-ai/flux-pro/kontext`

#### Strengths
- ✅ **12B Parameters**: Most powerful model for detail and consistency
- ✅ **Context Awareness**: Understands spatial relationships and composition
- ✅ **Precise Control**: Fine-grained control over edits and variations
- ✅ **Professional Quality**: Excellent for high-end portrait work
- ✅ **Well-Documented**: Extensive API documentation available

#### Weaknesses
- ⚠️ **Slower**: ~30-40 seconds per image generation
- ⚠️ **Higher Cost**: ~$0.08 per image (1024×1024)
- ⚠️ **Not Face-Specialized**: Generic image-to-image, not specifically for faces

#### Performance
- **Speed**: Medium (30-40 seconds)
- **Cost**: $0.08/image
- **Quality**: Excellent
- **Face Consistency**: Good (context-based)
- **Best For**: High-quality professional portraits, detailed variations

#### API Example
```javascript
await fal.subscribe('fal-ai/flux-pro/kontext', {
  input: {
    image_url: referenceImage,
    prompt: "Description of desired variation",
    strength: 0.7, // 70% image guidance
    num_inference_steps: 30
  }
});
```

#### Sources
- [FLUX.1 Kontext Documentation](https://fal.ai/models/fal-ai/flux-pro/kontext)
- [FLUX API Overview](https://fal.ai/flux)

---

### 2. Qwen-Image-Edit-2509 (Qwen Image)

**Model ID**: `fal-ai/qwen-image`

#### Strengths
- ✅ **100% Face Consistency**: Specifically designed for portrait variations
- ✅ **Advanced Editing**: Multi-image combinations (person + scene)
- ✅ **Lightning LoRAs**: Compatible with custom style LoRAs
- ✅ **September 2025 Latest**: Newest, most advanced version
- ✅ **Identity Preservation**: Maintains facial features across variations
- ✅ **Excellent Documentation**: Face consistency workflow guide available

#### Weaknesses
- ⚠️ **Medium Speed**: ~25-35 seconds per image
- ⚠️ **Medium Cost**: ~$0.06 per image (1024×1024)
- ⚠️ **Learning Curve**: More parameters to tune for optimal results

#### Performance
- **Speed**: Medium (25-35 seconds)
- **Cost**: $0.06/image
- **Quality**: Excellent (specialized for faces)
- **Face Consistency**: **Excellent (100%)**
- **Best For**: Portrait series, founder variations, identity preservation

#### Key Features
- `face_consistency_strength`: 0.0-1.0 (controls face preservation)
- Compatible with FaceDetailer for refinement
- Works with SeedVR2 for upscaling
- Supports Person + Scene combinations

#### API Example
```javascript
await fal.subscribe('fal-ai/qwen-image', {
  input: {
    image_url: referenceImage,
    prompt: "Description with face consistency requirement",
    face_consistency_strength: 1.0, // Maximum face preservation
    num_inference_steps: 30
  }
});
```

#### Sources
- [Qwen-Image Model](https://fal.ai/models/fal-ai/qwen-image)
- [Face Consistency Guide](https://myaiforce.com/face-consistency-qwen-edit-2509/)
- [Qwen Blog Introduction](https://blog.fal.ai/introducing-qwen-image/)
- [Latest Updates (2509)](https://qwen-image.net/blog/qwen-image-edit-2509-revolutionary-breakthrough)

---

### 3. Z-Image Turbo

**Model ID**: `fal-ai/z-image/turbo/image-to-image`

#### Strengths
- ✅ **Ultra-Fast**: Sub-second to 3-second generation
- ✅ **Affordable**: $0.0065/megapixel (cheapest option)
- ✅ **6B Parameters**: Extremely efficient model
- ✅ **LoRA Support**: 3 custom LoRA weights at inference time
- ✅ **Real-Time Ready**: Perfect for interactive applications
- ✅ **Commercial Use**: Licensed for production use

#### Weaknesses
- ⚠️ **Lower Detail**: 6B parameters = fewer details than larger models
- ⚠️ **Not Face-Specialized**: No dedicated face consistency features
- ⚠️ **Less Control**: Fewer inference steps (4-8 vs 20-50)
- ⚠️ **Consistency via LoRA**: Must train LoRA for consistent style

#### Performance
- **Speed**: **Very Fast (3-5 seconds)**
- **Cost**: **$0.0065/image (50% cheaper)**
- **Quality**: Good (acceptable for web/social)
- **Face Consistency**: Good (via LoRA training)
- **Best For**: Rapid prototyping, A/B testing, cost-sensitive workflows

#### Key Features
- 8-step inference pipeline (vs 20-50 for others)
- LoRA Trainer included for custom consistency
- ControlNet support for structural guidance
- 3 training modes: content, style, balanced

#### API Example
```javascript
await fal.subscribe('fal-ai/z-image/turbo/image-to-image', {
  input: {
    image_url: referenceImage,
    prompt: "Description of variation",
    strength: 0.65,
    num_inference_steps: 8 // Fast!
  }
});
```

#### Consistency Workflow
For 100% face consistency with Z-Turbo, you must:
1. Train a custom LoRA on founder photos
2. Use `content` mode to prioritize subject preservation
3. Apply LoRA at inference time

#### Sources
- [Z-Image Turbo Documentation](https://fal.ai/models/fal-ai/z-image/turbo/api)
- [Developer Guide](https://fal.ai/learn/devs/z-image-turbo-developer-guide)
- [Z-Image Turbo vs Z-Image Comparison](https://fal.ai/learn/devs/z-image-turbo-vs-z-image-comparison)

---

## Comparison Matrix

| Feature | Flux Kontext | Qwen Image | Z-Turbo |
|---------|--------------|-----------|---------|
| **Face Consistency** | Good | **Excellent (100%)** | Good (via LoRA) |
| **Speed** | Medium (30-40s) | Medium (25-35s) | **Very Fast (3-5s)** |
| **Cost per Image** | $0.08 | $0.06 | **$0.0065** |
| **Parameters** | **12B** | Unknown | 6B |
| **Best Quality** | ✅ Excellent | **✅ Excellent** | ✅ Good |
| **Ease of Use** | Medium | Medium | Easy |
| **Learning Curve** | Low | Medium | Low |
| **Production Ready** | Yes | Yes | Yes |
| **Face Specialized** | No | **Yes** | No |
| **LoRA Support** | No (built-in) | Yes (optional) | **Yes (required for consistency)** |

---

## Recommendation by Use Case

### For Maximum Quality + Face Consistency
**→ Choose Qwen Image**
- Best-in-class face consistency (100%)
- Excellent quality portraits
- Purpose-built for identity preservation
- Worth the extra cost for professional use

### For Speed + Cost (Accept Lower Quality)
**→ Choose Z-Image Turbo**
- 50% cheaper than competitors
- 6-10x faster generation
- Good enough for social media / website previews
- Perfect for A/B testing and rapid iterations

### For High-End Professional Work
**→ Choose Flux Kontext**
- Most powerful model (12B params)
- Excellent detail and composition control
- Better for complex lighting/backgrounds
- Best for print materials and marketing

---

## Cost Analysis (for 30-image dataset)

### Flux Kontext
- 30 images × $0.08 = **$2.40**
- Time: 30 × 35s ≈ 18 minutes

### Qwen Image
- 30 images × $0.06 = **$1.80** ✅ Best value
- Time: 30 × 30s ≈ 15 minutes
- Quality: Excellent for portraits

### Z-Image Turbo
- 30 images × $0.0065 = **$0.20** ✅ Cheapest
- Time: 30 × 4s ≈ 2 minutes ✅ Fastest
- Quality: Good, acceptable for web

---

## Testing Strategy

### Test 1: Single Founder (Lilly)
- 3 positioning variations per model
- Total: 9 test images
- Evaluate: Face consistency, quality, speed
- Cost: ~$0.50 total

### Test 2: All Three Founders
- 10 positioning variations per model (if test 1 passes)
- Total: 90 images
- Full dataset evaluation
- Cost: ~$5-10 depending on model choice

### Test 3: Model Blending
- Generate some variations with Qwen (face consistency)
- Generate some with Z-Turbo (speed/cost)
- Hybrid workflow for production

---

## Next Steps

1. **Run Test 1** (this script)
   - Generate 3 variations of Lilly with each model
   - Compare visual results
   - Check face consistency
   - Note generation times

2. **Review Results**
   - Download images from `/Generated_Images/Founders/Model_Comparison/`
   - Compare side-by-side
   - Evaluate face consistency
   - Check for artifacts or issues

3. **Choose Winner**
   - Select model(s) that best meet your needs
   - Consider quality vs. speed vs. cost tradeoffs
   - Plan production workflow

4. **Full Production**
   - Run full dataset generation with chosen model(s)
   - 10 variations per founder (30 total images)
   - Store in primary Positioning_Dataset folder

---

## API Pricing Reference

### Per Megapixel Pricing
- **Flux Kontext**: ~$0.08/image (1024×1024)
- **Qwen Image**: ~$0.06/image (1024×1024)
- **Z-Turbo**: $0.0065/image (1024×1024)

### Annual Costs (1000 images/month)
- **Flux Kontext**: ~$960/year
- **Qwen Image**: ~$720/year
- **Z-Turbo**: ~$78/year

---

## Troubleshooting

### If face consistency is poor
1. **Flux Kontext**: Increase `strength` parameter (0.8-0.9)
2. **Qwen Image**: Increase `face_consistency_strength` to 1.0
3. **Z-Turbo**: Train a custom LoRA for your founder

### If generation is slow
1. **Reduce inference steps** (Flux: 20, Qwen: 20, Z-Turbo: 4)
2. **Reduce resolution** (512×512 instead of 1024×1024)
3. **Use Z-Turbo** for speed

### If quality is poor
1. **Use Qwen Image** (purpose-built for faces)
2. **Improve reference image** (clear, well-lit photo)
3. **Refine prompt** (more specific description)

---

## Resources

**fal.ai Documentation**
- [FLUX Models](https://fal.ai/flux)
- [Qwen Image](https://fal.ai/models/fal-ai/qwen-image)
- [Z-Image Turbo](https://fal.ai/models/fal-ai/z-image/turbo)

**Face Consistency Guides**
- [Qwen Face Consistency (100%)](https://myaiforce.com/face-consistency-qwen-edit/)
- [Qwen Latest Features (2509)](https://qwen-image.net/)

**Prompt Engineering**
- [Z-Turbo Prompt Guide](https://fal.ai/learn/devs/z-image-turbo-prompt-guide)
- [FLUX Best Practices](https://docs.fal.ai/)

---

**Test Generated**: December 20, 2025
**Recommendation**: Start with Qwen Image for best face consistency results
