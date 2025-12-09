# Quick Setup Guide

## 1. Add Your API Key

```bash
cd image-generator
cp .env.example .env
nano .env  # or use any text editor
```

Add your fal.ai API key to `.env`:
```
FAL_KEY=your_actual_api_key_here
```

Get your API key from: https://fal.ai/dashboard/keys

## 2. Test the Tool

```bash
node generate.js --test
```

This will show you all available images without generating anything.

## 3. Generate Your First Image

Try generating a test image:

```bash
node generate.js --id abstract-hope
```

This will generate a small abstract background image to test the setup.

## 4. Generate Category

Once you're comfortable, generate a full category:

```bash
node generate.js --category hero
```

This will generate all 3 hero images for your website.

---

## Available Commands

### See all options:
```bash
node generate.js --help
```

### Test mode (no API calls):
```bash
npm run test
```

### Generate specific image:
```bash
node generate.js --id hero-main
```

### Generate category:
```bash
node generate.js --category services
```

---

## Output Location

Images are saved to:
```
../images/generated/
```

Review them there, then copy the ones you like to:
```
../images/
```

---

## Cost Estimate

Using fal.ai Flux Dev model:
- **Single image:** ~$0.025
- **Hero category (3 images):** ~$0.075
- **Services category (4 images):** ~$0.10
- **All images (12 total):** ~$0.30

Always use `--test` first to see what will be generated!

---

## Troubleshooting

### Module not found
```bash
npm install
```

### Permission denied
```bash
chmod +x generate.js
```

### API key error
Make sure `.env` file exists and contains:
```
FAL_KEY=your_key_here
```

---

**Ready to generate beautiful images for HROC!** 🎨
