#!/bin/bash

# HROC Website Deployment Script
# Deploys updated website files to TrueNAS (10.0.0.89)

TARGET_HOST="root@10.0.0.89"
TARGET_PATH="/mnt/tank/encrypted/containers/hrocinc/web/"

echo "========================================================================"
echo "HROC WEBSITE DEPLOYMENT"
echo "========================================================================"
echo "Target: $TARGET_HOST:$TARGET_PATH"
echo ""

# Files to deploy
FILES=(
  "HROC_Website_New/index.html"
  "HROC_Website_New/bri.html"
  "HROC_Website_New/lilly.html"
  "HROC_Website_New/jonathan.html"
  "HROC_Website_New/documents.html"
  "HROC_Website_New/styles.css"
  "HROC_Website_New/script.js"
  "HROC_Website_New/service-overdose-prevention.html"
  "HROC_Website_New/service-syringe-exchange.html"
  "HROC_Website_New/service-wound-care.html"
  "HROC_Website_New/service-health-screening.html"
  "HROC_Website_New/service-peer-support.html"
  "HROC_Website_New/service-housing-support.html"
  "HROC_Website_New/service-cultural-healing.html"
  "HROC_Website_New/service-education-training.html"
  "HROC_Website_New/service-resource-navigation.html"
)

echo "Deploying files to TrueNAS..."
echo ""

for file in "${FILES[@]}"; do
  if [ -f "$file" ]; then
    echo "[DEPLOY] $file"
    scp -o StrictHostKeyChecking=no "$file" "$TARGET_HOST:$TARGET_PATH" 2>&1 | grep -E "Error|Denied|Connection" && echo "[ERROR] Failed to deploy $file" || echo "[OK]"
  else
    echo "[SKIP] $file (not found)"
  fi
done

echo ""
echo "========================================================================"
echo "DEPLOYMENT COMPLETE"
echo "========================================================================"
echo ""
echo "Website should now be live at:"
echo "- http://hrocinc.org"
echo "- https://hrocinc.org"
echo ""
echo "Images are served from S3 CDN:"
echo "- https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com"
echo ""
echo "Verify deployment by checking:"
echo "1. Homepage loads (index.html)"
echo "2. Founder pages load (bri.html, lilly.html, jonathan.html)"
echo "3. All images display from S3"
echo "4. Gallery grids are symmetrical (3x3)"
