# HROC Image Generator (fal.ai)

AI-powered image generation tool for creating website graphics using fal.ai's Flux model.

---

## Quick Start

### 1. Install Dependencies

```bash
cd image-generator
npm install
```

### 2. Configure API Key

Create a `.env` file with your fal.ai API key:

```bash
cp .env.example .env
# Edit .env and add your API key
```

Get your API key from: https://fal.ai/dashboard/keys

### 3. Test Configuration

```bash
npm run test
```

This will show all available image categories and IDs.

---

## Usage

### Generate Specific Image

```bash
node generate.js --id hero-main
```

### Generate Category

```bash
node generate.js --category hero
```

### Generate All Images (Use Carefully!)

```bash
node generate.js --all
```

---

## Available Categories

### 1. **Hero/Banner Images** (`hero`)
Large header images for main page and sections:
- `hero-main` - Main hero banner
- `hero-community` - Community outreach banner
- `hero-services` - Services overview banner

### 2. **Service Illustrations** (`services`)
Visual representations of harm reduction services:
- `service-naloxone` - Naloxone distribution
- `service-supplies` - Harm reduction supplies
- `service-outreach` - Mobile outreach
- `service-education` - Community education

### 3. **Community Photos** (`community`)
Representative images of community and outreach:
- `community-diverse` - Diverse community members
- `community-volunteer` - Community volunteers
- `community-support` - Peer support

### 4. **Abstract/Background** (`abstract`)
Abstract background images with brand colors:
- `abstract-hope` - Hope and healing abstract
- `abstract-community` - Community connection abstract

---

## Command-Line Options

```
-c, --category <name>    Generate all images in a category
-i, --id <id>           Generate a specific image by ID
-a, --all               Generate all images
-t, --test              Show available categories and IDs
-h, --help              Show help message
```

---

## Examples

### Generate All Hero Images

```bash
node generate.js --category hero
```

### Generate Single Image

```bash
node generate.js --id service-naloxone
```

### See What's Available

```bash
node generate.js --test
```

---

## Output

Generated images are saved to:
```
HROC_Website_New/images/generated/
```

Image specifications:
- **Size:** 1920x1080px (configurable in .env)
- **Format:** JPG
- **Quality:** High (50 inference steps)
- **Model:** fal-ai/flux/dev

---

## Customization

### Add New Images

Edit `prompts.json` to add new image prompts:

```json
{
  "id": "your-image-id",
  "description": "Description of image",
  "prompt": "Detailed prompt for AI generation",
  "negative_prompt": "Things to avoid",
  "filename": "output-filename.jpg"
}
```

### Adjust Image Settings

Edit `.env` file:

```env
IMAGE_WIDTH=1920
IMAGE_HEIGHT=1080
IMAGE_QUALITY=high    # high (50 steps) or normal (28 steps)
NUM_IMAGES=1
```

---

## Brand Colors

All prompts are configured to use HROC brand colors:
- **Magenta:** #E91E8C
- **Cyan:** #00D4E8
- **Lime:** #C8E800
- **Yellow:** #FFE600

---

## Cost Considerations

Each image generation uses fal.ai API credits. Costs vary by model:
- **Flux Dev:** ~$0.025 per image (high quality)
- **Flux Schnell:** ~$0.003 per image (fast)

**Tip:** Use `--test` to preview what will be generated before running `--all`

---

## Troubleshooting

### Error: FAL_KEY not found

Make sure you've created a `.env` file with your API key:

```bash
echo "FAL_KEY=your_api_key_here" > .env
```

### Images Not Generating

1. Check API key is valid
2. Verify you have API credits
3. Check internet connection
4. Review error messages in console

### Poor Quality Images

1. Increase `NUM_INFERENCE_STEPS` in generate.js
2. Try different prompts
3. Add more specific details to prompts

---

## Integration with Website

### 1. Review Generated Images

```bash
open images/generated/
```

### 2. Move to Website Directory

```bash
# Move selected images to main images folder
mv images/generated/hero-main.jpg images/
```

### 3. Update HTML

```html
<!-- In index.html -->
<div class="hero" style="background-image: url('images/hero-main.jpg')">
  <!-- Hero content -->
</div>
```

### 4. Deploy to Server

```bash
# Upload to TrueNAS server
scp -i ~/.ssh/truenas_admin_10_0_0_89 images/*.jpg \
  root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/images/
```

---

## Safety and Ethics

All prompts are configured with safety guidelines:
- **Negative prompts** exclude harmful content
- **Safety checker** enabled in API calls
- **Positive focus** on healing, community, and support
- **Diverse representation** in community images

---

## Files Structure

```
image-generator/
├── package.json          # Dependencies
├── generate.js           # Main generator script
├── prompts.json          # Image prompts configuration
├── .env.example          # Environment template
├── .env                  # Your API key (git-ignored)
├── README.md            # This file
└── images/
    └── generated/        # Output directory
```

---

## Support

**fal.ai Documentation:** https://fal.ai/models/fal-ai/flux/dev
**HROC Repository:** https://github.com/isndotbiz/HROC_Files

---

**Created for:** Healing Roots Outreach Collective
**Model:** fal.ai Flux Dev
**Version:** 1.0.0
