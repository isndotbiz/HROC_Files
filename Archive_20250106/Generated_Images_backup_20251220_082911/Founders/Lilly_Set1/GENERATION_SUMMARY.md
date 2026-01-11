# Lilly LoRA Training & Image Generation Summary

**Date**: December 10, 2025, 04:12 AM PST

## Training Details

### LoRA Model Information
- **Model URL**: https://v3b.fal.media/files/b/0a85bd29/Iqpj0FUdAYYG33YylWnig_pytorch_lora_weights.safetensors
- **Trigger Word**: `LILLYHROC`
- **Training Steps**: 1000
- **Training Images**: 15 high-quality photos
- **Model Size**: 89.7 MB
- **Platform**: fal.ai (flux-lora-fast-training)

### Training Images Selected
15 best quality images from `/Officers/L/` directory (sorted by file size):

1. 465168804_28361199616812436_5751942585475638287_n.jpg (0.37 MB)
2. 48254049_2977552725603808_5124881399949557760_n.jpg (0.21 MB)
3. 68464588_3594627087229699_863639879374864384_n.jpg (0.19 MB)
4. 476631329_29394838913448496_2307585454577419700_n.jpg (0.16 MB)
5. 37559149_2672470186112065_1827130730405167104_n.jpg (0.13 MB)
6. 471158746_10170369453580113_1599087482745391689_n.jpg (0.12 MB)
7. 300092520_8709944829031207_8982943806673575852_n.jpg (0.11 MB)
8. 69094541_3594626923896382_1976423913873211392_n.jpg (0.10 MB)
9. 466794925_28472749095657487_955909156098841755_n.jpg (0.10 MB)
10. 47684243_2963720526987028_2336958209027211264_n.jpg (0.09 MB)
11. 37609868_2672470272778723_4210998911541706752_n.jpg (0.09 MB)
12. 37585401_2672470036112080_895303280224108544_n.jpg (0.09 MB)
13. 466624071_28475145468751183_5845941264203776075_n.jpg (0.08 MB)
14. 101952115_4630429943649403_2558855581170002706_n.jpg (0.08 MB)
15. 51771423_3127101283982284_6519078348881133568_n.jpg (0.07 MB)

## Generated Professional Images

Successfully generated **10 professional images** of Lilly in various business settings.

### Image Details

1. **lilly_professional_01.jpg** (134 KB)
   - Prompt: Professional headshot of LILLYHROC, business attire, clean white background, corporate photography, high quality, 4k

2. **lilly_professional_02.jpg** (199 KB)
   - Prompt: LILLYHROC in professional business suit, standing confidently in modern office, natural lighting, professional photography

3. **lilly_professional_03.jpg** (204 KB)
   - Prompt: LILLYHROC sitting at executive desk, business casual attire, office environment, professional portrait

4. **lilly_professional_04.jpg** (175 KB)
   - Prompt: LILLYHROC giving presentation, business formal wear, conference room setting, professional photograph

5. **lilly_professional_05.jpg** (201 KB)
   - Prompt: LILLYHROC professional portrait, navy blazer, outdoor corporate campus background, natural light

6. **lilly_professional_06.jpg** (192 KB)
   - Prompt: LILLYHROC in business meeting, sitting at conference table, professional attire, corporate setting

7. **lilly_professional_07.jpg** (184 KB)
   - Prompt: LILLYHROC standing by office window, professional business wear, city view background, elegant portrait

8. **lilly_professional_08.jpg** (139 KB)
   - Prompt: LILLYHROC professional headshot, friendly smile, business casual, grey background, studio lighting

9. **lilly_professional_09.jpg** (200 KB)
   - Prompt: LILLYHROC walking in modern office corridor, business suit, professional photography, confident pose

10. **lilly_professional_10.jpg** (170 KB)
    - Prompt: LILLYHROC portrait in professional blazer, arms crossed, office background, corporate headshot style

## Generation Settings

- **Base Model**: fal-ai/flux-lora
- **Inference Steps**: 28
- **Guidance Scale**: 3.5
- **Output Format**: JPEG
- **Image Size**: 1024x1024
- **LoRA Scale**: 1.0
- **Safety Checker**: Enabled

## File Locations

- **Training Script**: `/Users/jonathanmallinger/Documents/HROC_Files/train_lilly_lora_v2.py`
- **Generated Images Directory**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Lilly_Set1/`
- **LoRA Model Info**: `/Users/jonathanmallinger/Documents/HROC_Files/Generated_Images/Founders/Lilly_Set1/lora_model_info.json`
- **Source Photos**: `/Users/jonathanmallinger/Documents/HROC_Files/Officers/L/`

## How to Use the LoRA Model

To generate more images using this trained LoRA model, use the following parameters:

```python
{
  "prompt": "Your prompt here with LILLYHROC",
  "loras": [
    {
      "path": "https://v3b.fal.media/files/b/0a85bd29/Iqpj0FUdAYYG33YylWnig_pytorch_lora_weights.safetensors",
      "scale": 1.0
    }
  ],
  "model_name": "fal-ai/flux-lora",
  "num_inference_steps": 28,
  "guidance_scale": 3.5,
  "image_size": {"width": 1024, "height": 1024}
}
```

## Notes

- All images feature consistent character representation using the trained LoRA
- Professional business settings and attire throughout
- Suitable for corporate use, marketing materials, and professional profiles
- Total generation time: ~6 minutes (including training)
- Training completed successfully with 1000 steps
