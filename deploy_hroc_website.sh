#!/bin/bash
# HROC Website Deployment Script
# Deploys the HROC website to TrueNAS server via SCP

# Configuration
SOURCE_DIR="/Users/jonathanmallinger/Workspace/HROC_Files/HROC_Website_New"
SERVER_USER="root"
SERVER_HOST="your-server"  # Replace with your actual server hostname/IP
DEST_PATH="/mnt/tank/websites/kusanagi/web-hrocinc"

# S3 Bucket URL for assets
S3_BASE_URL="https://hroc-website-20251230043930.s3.us-east-1.amazonaws.com"

echo "============================================"
echo "HROC Website Deployment Script"
echo "============================================"
echo ""
echo "Source: $SOURCE_DIR"
echo "Destination: $SERVER_USER@$SERVER_HOST:$DEST_PATH"
echo "S3 Bucket: $S3_BASE_URL"
echo ""

# Files and directories to exclude from deployment
EXCLUDES=(
    "node_modules"
    ".DS_Store"
    ".git"
    ".gitignore"
    "*.log"
    "*.txt"
    "lora_training"
    "lora_models"
    "image-generator/node_modules"
    ".env"
    "*.py"
    "*.sh"
    "*.md"
)

# Build rsync exclude arguments
EXCLUDE_ARGS=""
for EXCLUDE in "${EXCLUDES[@]}"; do
    EXCLUDE_ARGS="$EXCLUDE_ARGS --exclude='$EXCLUDE'"
done

echo "Files to deploy:"
echo "- index.html"
echo "- documents.html"
echo "- bri.html, lilly.html, jonathan.html (founder pages)"
echo "- styles.css"
echo "- script.js"
echo "- images/ (local fallback images)"
echo ""
echo "Note: Most images and all PDFs are served from S3:"
echo "  $S3_BASE_URL"
echo ""

# Check if server details are configured
if [ "$SERVER_HOST" == "your-server" ]; then
    echo "ERROR: Please edit this script and set SERVER_HOST to your actual server hostname/IP"
    echo ""
    echo "Manual deployment command:"
    echo ""
    echo "  scp -r $SOURCE_DIR/*.html $SOURCE_DIR/*.css $SOURCE_DIR/*.js $SERVER_USER@<YOUR-SERVER>:$DEST_PATH/"
    echo ""
    echo "Or use rsync for more control:"
    echo ""
    echo "  rsync -avz --progress \\"
    echo "    --exclude='node_modules' \\"
    echo "    --exclude='.DS_Store' \\"
    echo "    --exclude='lora_training' \\"
    echo "    --exclude='lora_models' \\"
    echo "    --exclude='image-generator' \\"
    echo "    --exclude='*.md' \\"
    echo "    --exclude='*.py' \\"
    echo "    --exclude='*.log' \\"
    echo "    $SOURCE_DIR/ $SERVER_USER@<YOUR-SERVER>:$DEST_PATH/"
    exit 1
fi

# Confirm deployment
read -p "Deploy to $SERVER_HOST? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 0
fi

# Deploy using rsync (more efficient than scp for updates)
echo "Deploying..."
eval rsync -avz --progress $EXCLUDE_ARGS "$SOURCE_DIR/" "$SERVER_USER@$SERVER_HOST:$DEST_PATH/"

if [ $? -eq 0 ]; then
    echo ""
    echo "============================================"
    echo "Deployment successful!"
    echo "============================================"
    echo ""
    echo "Website deployed to: https://hrocinc.org"
    echo ""
    echo "Assets are served from S3:"
    echo "  Images: $S3_BASE_URL/images/"
    echo "  PDFs:   $S3_BASE_URL/pdfs/"
    echo ""
else
    echo "Deployment failed. Check the error messages above."
    exit 1
fi
