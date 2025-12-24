#!/bin/bash
# AWS S3 Sync Script for HROC Generated Images
# DO NOT RUN UNTIL ALL IMAGES ARE GENERATED (57 total expected)

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=========================================="
echo "HROC Generated Images S3 Sync Script"
echo "=========================================="
echo ""

# Configuration
LOCAL_DIR="D:/workspace/HROC_Files/HROC_Website_New/generated_images"
S3_BUCKET="s3://hroc-outreach-assets-1765630540/images/generated_images"
AWS_REGION="us-west-2"

# Count local images
IMAGE_COUNT=$(find "$LOCAL_DIR" -type f \( -name "*.png" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.webp" \) 2>/dev/null | wc -l)
echo "Current local image count: $IMAGE_COUNT"
echo "Expected image count: 57 (when all services complete)"
echo ""

# Pre-flight checks
echo "Pre-flight checks:"
echo "==================="

# Check AWS CLI
if ! command -v aws &> /dev/null; then
    echo -e "${RED}✗ AWS CLI not found. Please install AWS CLI.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ AWS CLI installed${NC}"

# Check AWS credentials
if ! aws sts get-caller-identity &> /dev/null; then
    echo -e "${RED}✗ AWS credentials not configured${NC}"
    echo "Run: aws configure"
    exit 1
fi
echo -e "${GREEN}✓ AWS credentials configured${NC}"

# Check bucket access
if ! aws s3 ls "$S3_BUCKET" --region "$AWS_REGION" &> /dev/null; then
    echo -e "${YELLOW}⚠ Warning: Cannot access S3 bucket (may not exist yet)${NC}"
else
    echo -e "${GREEN}✓ S3 bucket accessible${NC}"
fi

echo ""

# Warn if image count is low
if [ "$IMAGE_COUNT" -lt 57 ]; then
    echo -e "${YELLOW}=========================================="
    echo "WARNING: Image generation incomplete!"
    echo "=========================================="
    echo "Current: $IMAGE_COUNT images"
    echo "Expected: 57 images"
    echo "Missing: $((57 - IMAGE_COUNT)) images"
    echo ""
    echo "Services status:"
    echo "  ✓ service-overdose-prevention (6/6)"
    echo "  ✓ service-syringe-exchange (6/6)"
    echo "  ⚠ service-wound-care (4/6)"
    echo "  ✗ service-cultural-healing (3/6)"
    echo "  ✗ service-education-training (3/6)"
    echo "  ✗ service-health-screening (3/6)"
    echo "  ✗ service-housing-support (3/6)"
    echo "  ✗ service-peer-support (3/6)"
    echo "  ✗ service-resource-navigation (3/6)"
    echo -e "==========================================${NC}"
    echo ""

    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Sync cancelled. Generate remaining images first."
        exit 1
    fi
fi

# Ask for confirmation
echo ""
echo "Ready to sync:"
echo "  From: $LOCAL_DIR"
echo "  To:   $S3_BUCKET"
echo "  Region: $AWS_REGION"
echo "  ACL: public-read"
echo ""
read -p "Run DRY-RUN first? (recommended) (Y/n): " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Nn]$ ]]; then
    echo ""
    echo "Running DRY-RUN..."
    echo "==================="
    aws s3 sync "$LOCAL_DIR" "$S3_BUCKET" \
        --region "$AWS_REGION" \
        --acl public-read \
        --dryrun

    echo ""
    read -p "Proceed with actual sync? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Sync cancelled."
        exit 0
    fi
fi

# Perform actual sync
echo ""
echo "Syncing to S3..."
echo "================="
aws s3 sync "$LOCAL_DIR" "$S3_BUCKET" \
    --region "$AWS_REGION" \
    --acl public-read

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}=========================================="
    echo "✓ Sync completed successfully!"
    echo -e "==========================================${NC}"
    echo ""
    echo "Verifying upload..."
    REMOTE_COUNT=$(aws s3 ls "$S3_BUCKET" --recursive --region "$AWS_REGION" | wc -l)
    echo "Remote file count: $REMOTE_COUNT"
    echo "Local file count: $IMAGE_COUNT"

    if [ "$REMOTE_COUNT" -eq "$IMAGE_COUNT" ]; then
        echo -e "${GREEN}✓ File counts match!${NC}"
    else
        echo -e "${YELLOW}⚠ File count mismatch - verify manually${NC}"
    fi

    echo ""
    echo "Images now accessible at:"
    echo "https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/"
else
    echo -e "${RED}✗ Sync failed. Check error messages above.${NC}"
    exit 1
fi
