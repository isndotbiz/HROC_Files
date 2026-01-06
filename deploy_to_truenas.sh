#!/bin/bash
# HROC Website Deployment to TrueNAS
# This script deploys the website to TrueNAS at 10.0.0.89

set -e

echo "=========================================="
echo "🚀 HROC Website Deployment to TrueNAS"
echo "=========================================="
echo ""

# Configuration from .env.local
NAS_SERVER="10.0.0.89"
NAS_USER="jdmal"
NAS_PORT="22"
WEBSITE_DIR="/mnt/tank/encrypted/containers/hrocinc/web"

# Source directory
SOURCE_DIR="./HROC_Website_New"

echo "📁 Source: $SOURCE_DIR"
echo "🖥️  Target: $NAS_USER@$NAS_SERVER:$WEBSITE_DIR"
echo ""

# Step 1: Test SSH connection
echo "1️⃣  Testing SSH connection..."
if ssh -o ConnectTimeout=5 -p $NAS_PORT $NAS_USER@$NAS_SERVER "echo 'SSH OK'" 2>/dev/null; then
    echo "✅ SSH connection successful!"
else
    echo "❌ SSH connection failed!"
    echo ""
    echo "Please ensure:"
    echo "  1. SSH key is set up: ssh-copy-id -p $NAS_PORT $NAS_USER@$NAS_SERVER"
    echo "  2. TrueNAS is accessible at $NAS_SERVER"
    echo ""
    exit 1
fi
echo ""

# Step 2: Create directory if it doesn't exist
echo "2️⃣  Ensuring website directory exists..."
ssh -p $NAS_PORT $NAS_USER@$NAS_SERVER "mkdir -p $WEBSITE_DIR" 2>/dev/null || true
echo "✅ Directory ready"
echo ""

# Step 3: Sync website files
echo "3️⃣  Syncing website files..."
rsync -avz --delete \
    --exclude '.git' \
    --exclude 'node_modules' \
    --exclude '*.md' \
    --exclude 'lora_training' \
    --exclude 'image-generator' \
    -e "ssh -p $NAS_PORT" \
    $SOURCE_DIR/ \
    $NAS_USER@$NAS_SERVER:$WEBSITE_DIR/

echo "✅ Files synced!"
echo ""

# Step 4: Update Git repository on NAS (if it exists)
echo "4️⃣  Pulling latest changes from GitHub on TrueNAS..."
ssh -p $NAS_PORT $NAS_USER@$NAS_SERVER "cd /mnt/tank/encrypted/HROC_Files 2>/dev/null && git pull origin main" 2>/dev/null || {
    echo "⚠️  Git repository not found or couldn't pull. Files were synced via rsync."
}
echo ""

# Step 5: Display deployment info
echo "=========================================="
echo "✅ Deployment Complete!"
echo "=========================================="
echo ""
echo "📊 Deployment Summary:"
echo "  • New S3 Bucket: hroc-website-20251230043930"
echo "  • Region: us-east-1"
echo "  • Files synced: $(find $SOURCE_DIR -type f | wc -l | xargs)"
echo "  • Website: https://hrocinc.org"
echo ""
echo "🔍 Next Steps:"
echo "  1. Visit https://hrocinc.org to verify"
echo "  2. Check that all images load from new S3 bucket"
echo "  3. Test responsive design on mobile/tablet"
echo ""
