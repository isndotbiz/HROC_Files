#!/bin/bash

# HROC Website Image Generation and Deployment Pipeline
# This script runs all steps: generate, upload, update HTML, and deploy

set -e  # Exit on error

echo ""
echo "========================================================================"
echo "HROC Website Image Generation & Deployment Pipeline"
echo "========================================================================"
echo ""

# Check environment variables
if [ -z "$FAL_API_KEY" ]; then
    echo "ERROR: FAL_API_KEY environment variable not set"
    echo "Usage: export FAL_API_KEY='your-fal-api-key' && bash run_image_pipeline.sh"
    exit 1
fi

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "ERROR: AWS_ACCESS_KEY_ID environment variable not set"
    echo "Usage: export AWS_ACCESS_KEY_ID='your-access-key' && bash run_image_pipeline.sh"
    exit 1
fi

if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    echo "ERROR: AWS_SECRET_ACCESS_KEY environment variable not set"
    echo "Usage: export AWS_SECRET_ACCESS_KEY='your-secret-key' && bash run_image_pipeline.sh"
    exit 1
fi

echo "✓ Environment variables verified"
echo ""

# Step 1: Generate images
echo "========================================================================"
echo "STEP 1: Generate Images with FAL.ai (5-10 minutes)"
echo "========================================================================"
echo ""

python3 generate_images_fal.py
if [ $? -eq 0 ]; then
    echo "✓ Image generation completed successfully"
else
    echo "✗ Image generation failed"
    exit 1
fi

echo ""

# Step 2: Upload to S3
echo "========================================================================"
echo "STEP 2: Upload Images to S3 (2-3 minutes)"
echo "========================================================================"
echo ""

python3 upload_images_to_s3.py
if [ $? -eq 0 ]; then
    echo "✓ S3 upload completed successfully"
else
    echo "✗ S3 upload failed"
    exit 1
fi

echo ""

# Step 3: Update HTML
echo "========================================================================"
echo "STEP 3: Update HTML Image References (30 seconds)"
echo "========================================================================"
echo ""

python3 update_html_images.py
if [ $? -eq 0 ]; then
    echo "✓ HTML update completed successfully"
else
    echo "✗ HTML update failed"
    exit 1
fi

echo ""

# Step 4: Deploy to TrueNAS
echo "========================================================================"
echo "STEP 4: Deploy to TrueNAS (1-2 minutes)"
echo "========================================================================"
echo ""

bash deploy_to_truenas.sh
if [ $? -eq 0 ]; then
    echo "✓ TrueNAS deployment completed successfully"
else
    echo "✗ TrueNAS deployment failed"
    exit 1
fi

echo ""
echo "========================================================================"
echo "PIPELINE COMPLETE!"
echo "========================================================================"
echo ""
echo "Website should now be live with new images at:"
echo "  - http://hrocinc.org"
echo "  - https://hrocinc.org"
echo "  - http://10.0.0.89 (Direct TrueNAS access)"
echo ""
echo "Images are hosted on S3 CDN:"
echo "  - https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com"
echo ""
echo "Next: Verify deployment by checking:"
echo "  1. Homepage loads correctly"
echo "  2. Impact stories display with new hero images"
echo "  3. All 9 service pages load images"
echo "  4. Gallery grids are symmetrical (3x3)"
echo ""
