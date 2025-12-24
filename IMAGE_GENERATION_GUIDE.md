# HROC Website Image Generation Guide

## Overview

This guide walks you through generating, uploading, and deploying new images for the HROC website using FAL.ai for image generation and AWS S3 for hosting.

## Prerequisites

### 1. FAL.ai Account and API Key

1. Create a free account at [FAL.ai](https://fal.ai)
2. Navigate to your account settings and copy your API key
3. You'll use this in the generation step below

### 2. AWS Credentials

You need AWS credentials for uploading images to the S3 bucket. Set these environment variables:

```bash
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
```

### 3. Python Dependencies

Install required Python packages:

```bash
pip install boto3 requests
```

## Workflow

### Step 1: Generate Images with FAL.ai

This script generates all service images, impact story images, and infographics using FAL.ai with the "nanao banana" aesthetic theme.

```bash
export FAL_API_KEY="your-fal-api-key"
python3 generate_images_fal.py
```

**What this does:**
- Generates 3 images for each of 9 service pages (27 total)
- Generates 3 impact story hero images
- Generates 5 gallery images
- Total: ~35 high-quality images

**Output:**
- Images saved to: `HROC_Website_New/generated_images/`
- Directory structure:
  ```
  generated_images/
  ├── service-overdose-prevention/
  │   ├── 1.png (primary)
  │   ├── 2.png (infographic)
  │   └── 3.png (community scene)
  ├── service-syringe-exchange/
  ├── service-wound-care/
  ├── service-health-screening/
  ├── service-peer-support/
  ├── service-housing-support/
  ├── service-cultural-healing/
  ├── service-education-training/
  ├── service-resource-navigation/
  ├── impact-story-hero-1.png
  ├── impact-story-hero-2.png
  ├── impact-story-hero-3.png
  └── service-gallery-image/
      ├── 1.png
      ├── 2.png
      ├── 3.png
      ├── 4.png
      └── 5.png
  ```

**Notes:**
- First-time generation may take 5-10 minutes
- Each image request to FAL.ai takes ~30-60 seconds
- Images are generated sequentially with 2-second delays to respect API rate limits
- All images use "nanao banana" aesthetic theme for consistent visual style

### Step 2: Upload Images to S3

This script uploads all generated images to your S3 bucket with public read access.

```bash
python3 upload_images_to_s3.py
```

**What this does:**
- Uploads all generated images to S3 bucket
- Sets proper content types (PNG/JPEG)
- Enables public read access (ACL: public-read)
- Sets cache headers (1-year expiration)

**Output:**
- Images uploaded to: `https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/`
- Example: `https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-overdose-prevention/1.png`

**What to do if upload fails:**
- Check AWS credentials: `echo $AWS_ACCESS_KEY_ID`
- Verify S3 bucket exists and you have access
- Check S3 bucket policy allows uploads
- Verify bucket name: `hroc-outreach-assets-1765630540`

### Step 3: Update HTML Image References

This script updates all HTML files to point to the newly generated images on S3.

```bash
python3 update_html_images.py
```

**What this does:**
- Updates service page primary images
- Updates service page gallery images
- Updates impact story images on index.html
- Updates service thumbnail images on index.html

**Files modified:**
- `index.html`
- `service-overdose-prevention.html`
- `service-syringe-exchange.html`
- `service-wound-care.html`
- `service-health-screening.html`
- `service-peer-support.html`
- `service-housing-support.html`
- `service-cultural-healing.html`
- `service-education-training.html`
- `service-resource-navigation.html`

### Step 4: Deploy to TrueNAS

After updating HTML files, deploy to the web server:

```bash
bash deploy_to_truenas.sh
```

**What this does:**
- SCP transfers all updated HTML files to TrueNAS web server
- Target: `root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/`

**Deployment checklist:**
- ✓ index.html with new impact story images
- ✓ All 9 service pages with new service-specific images
- ✓ styles.css (no changes needed)
- ✓ script.js (no changes needed)

### Step 5: Verify Deployment

1. Check website homepage: `http://hrocinc.org` or `http://10.0.0.89`
2. Verify impact stories display correctly
3. Check each service page loads images properly:
   - http://hrocinc.org/service-overdose-prevention.html
   - http://hrocinc.org/service-syringe-exchange.html
   - (etc. for all 9 services)
4. Verify image gallery grids are symmetrical (3x3)
5. Check S3 CDN performance

## Image Specifications

### Image Format & Size
- **Format:** PNG (lossless quality)
- **Dimensions:** 1920x1080 (landscape 16:9)
- **File size:** ~500KB-2MB per image

### Image Style & Theme
- **Theme:** "nanao banana" aesthetic (warm, inclusive, community-focused)
- **Style:** Professional illustrations with diverse representation
- **Colors:** Warm earth tones, accessible color palettes
- **Content:** Community-focused, healing-focused, inclusive healthcare scenes

### Image Categories

**Service Primary Images (1 per service):**
- Main visual for service detail page
- Professional illustration showing service in action
- Diverse, respectful representation

**Service Infographics (1 per service):**
- Educational information graphic
- Icons and clear messaging
- Benefits and program components

**Community Scene Images (1 per service):**
- HROC team member with community member
- Trust-building moment
- Warm, welcoming atmosphere

**Impact Story Heroes (3 total):**
- Powerful community portraits
- Transformation visible through image
- Hope and stability represented

**Service Gallery Images (5 total):**
- Diverse healthcare and community moments
- Multiple perspectives on HROC services
- Varied community interactions

## Troubleshooting

### Issue: FAL.ai API returns 401 error
**Solution:** Check your API key is correctly set:
```bash
echo $FAL_API_KEY
```

### Issue: S3 upload fails with "Access Denied"
**Solution:** Verify AWS credentials and S3 bucket permissions:
```bash
aws s3 ls s3://hroc-outreach-assets-1765630540/
```

### Issue: Images still showing on website after deployment
**Solution:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Or hard refresh (Ctrl+Shift+R)
3. Check CloudFront cache if applicable
4. Verify TrueNAS deployment succeeded: `bash deploy_to_truenas.sh`

### Issue: Deployment to TrueNAS fails
**Solution:**
- Verify SSH access: `ssh root@10.0.0.89`
- Check TrueNAS is running and accessible
- Verify TrueNAS target path exists: `/mnt/tank/encrypted/containers/hrocinc/web/`

## Complete Workflow Command Sequence

Run all steps in order:

```bash
# Step 1: Generate images (5-10 minutes)
export FAL_API_KEY="your-fal-api-key"
python3 generate_images_fal.py

# Step 2: Upload to S3 (2-3 minutes)
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
python3 upload_images_to_s3.py

# Step 3: Update HTML references (30 seconds)
python3 update_html_images.py

# Step 4: Deploy to TrueNAS (1-2 minutes)
bash deploy_to_truenas.sh

# Step 5: Verify in browser (manual)
# Visit: http://hrocinc.org
# Check all images load and display correctly
```

## Image URL Format

All generated images are hosted on S3 CDN with this URL pattern:

```
https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/{category}/{subcategory}/{image_name}
```

**Examples:**
- `https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-overdose-prevention/1.png`
- `https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/impact-story-hero-1.png`

## Next Steps (Optional Enhancements)

1. **CloudFront CDN:** Set up AWS CloudFront distribution for faster global image delivery
2. **Image Optimization:** Add WebP format generation for better compression
3. **Responsive Images:** Add picture element with multiple sizes for mobile optimization
4. **Image Lazy Loading:** Add native lazy-loading attributes to all images
5. **Alt Text:** Ensure all images have descriptive alt text for accessibility

## Support

If you encounter issues:
1. Check that all prerequisites are installed
2. Verify environment variables are set correctly
3. Review the troubleshooting section above
4. Check S3 bucket permissions and AWS credentials
5. Verify TrueNAS server is accessible
