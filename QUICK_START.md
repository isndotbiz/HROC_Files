# Quick Start: Generate & Deploy HROC Images

## TL;DR - Run Everything in 15 Minutes

### 1. Get Your API Keys

**FAL.ai API Key:**
- Go to https://fal.ai
- Sign up (free account)
- Get your API key from account settings

**AWS Credentials:**
- You should already have AWS access for the S3 bucket
- Get your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

### 2. Install Requirements

```bash
pip install boto3 requests
```

### 3. Run the Pipeline

```bash
# Set your API keys
export FAL_API_KEY="sk-..."
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."

# Run everything in one command
bash run_image_pipeline.sh
```

That's it! The script will:
1. ✓ Generate 35 high-quality images with "nanao banana" aesthetic
2. ✓ Upload them to your S3 bucket
3. ✓ Update all HTML files to point to new images
4. ✓ Deploy to your TrueNAS web server

## What Gets Created

### Images (35 total)
- **27 Service Images** (3 per service × 9 services)
  - Primary service image
  - Infographic
  - Community scene

- **8 Impact/Gallery Images**
  - 3 impact story hero images
  - 5 service gallery images

### All images follow the "nanao banana" theme:
- Warm, inclusive aesthetic
- Diverse representation
- Community-focused visuals
- Professional quality
- Suitable for nonprofit website

## After Deployment

Visit your website and verify:
1. http://hrocinc.org
2. Check impact stories have new images
3. Click on each of 9 services to verify images load
4. Check gallery grids look symmetrical

## If Something Goes Wrong

### "FAL_API_KEY not set" error
```bash
export FAL_API_KEY="your-actual-api-key"
```

### "AWS credentials not set" error
```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
```

### "S3 upload failed" error
- Verify credentials work: `aws s3 ls s3://hroc-outreach-assets-1765630540/`
- Check bucket name is correct
- Ensure you have upload permissions

### "TrueNAS deployment failed" error
- Verify SSH access: `ssh root@10.0.0.89`
- Check the target path exists on server
- Verify network connectivity

## Detailed Guides

For more detailed information, see:
- **IMAGE_GENERATION_GUIDE.md** - Full walkthrough with all details
- **generate_images_fal.py** - Image generation script
- **upload_images_to_s3.py** - S3 upload script
- **update_html_images.py** - HTML update script

## What's Being Generated

Each service gets 3 tailored images:

**Service: Overdose Prevention**
- Image 1: Naloxone training educator with community members
- Image 2: Educational infographic on overdose prevention
- Image 3: Community outreach vehicle scene

**Service: Syringe Exchange**
- Image 1: Sterile equipment exchange program
- Image 2: Disease prevention infographic
- Image 3: Community health worker interaction

**Service: Wound Care**
- Image 1: Compassionate wound care assessment
- Image 2: Medical care technique infographic
- Image 3: Professional healthcare moment

**Service: Health Screening**
- Image 1: Mobile health clinic scene
- Image 2: Health screening indicators infographic
- Image 3: Community health fair

**Service: Peer Support**
- Image 1: Support circle illustration
- Image 2: Peer support journey infographic
- Image 3: Mentorship moment

**Service: Housing Support**
- Image 1: Housing navigation with support worker
- Image 2: Housing support process infographic
- Image 3: Success story (person with new housing)

**Service: Cultural Healing**
- Image 1: Indigenous healing circle
- Image 2: Cultural healing practices infographic
- Image 3: Traditional ceremony moment

**Service: Education Training**
- Image 1: Naloxone training workshop
- Image 2: Training curriculum infographic
- Image 3: Hands-on training session

**Service: Resource Navigation**
- Image 1: Navigator helping with benefits
- Image 2: Benefits and resources infographic
- Image 3: Healthcare advocacy moment

**Impact Stories**
- Hero 1: Powerful community portrait (transformation visible)
- Hero 2: Community gathering celebration
- Hero 3: Healing journey progress moment

## Performance Notes

- First run takes ~10 minutes (image generation time)
- Subsequent runs would be faster if you regenerate different prompts
- S3 upload typically takes 2-3 minutes for ~35 images
- HTML updates take ~30 seconds
- TrueNAS deployment takes 1-2 minutes

## File Sizes

- Each generated image: ~500KB-2MB
- Total generated: ~25-50MB
- All images optimized for web display

## Next Steps After Deployment

1. **Verify images load** on all pages
2. **Check S3 CDN performance** (images should load quickly)
3. **Optional: Set up CloudFront** for faster global delivery
4. **Optional: Generate WebP versions** for better compression
5. **Share with team** - website is now visually complete!

---

**Questions?** See IMAGE_GENERATION_GUIDE.md for detailed troubleshooting and additional information.
