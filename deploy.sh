#!/bin/bash
set -euo pipefail

# HROC Website Deployment Script
# Uses 1Password CLI for secure credential management

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  HROC Website Deployment Script${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if 1Password CLI is installed
if ! command -v op &> /dev/null; then
    echo -e "${RED}✗ 1Password CLI not found${NC}"
    echo "Please install it: brew install 1password-cli"
    exit 1
fi

# Check if signed into 1Password
if ! op account list &> /dev/null; then
    echo -e "${YELLOW}⚠ Not signed into 1Password CLI${NC}"
    echo "Please run: eval \$(op signin)"
    exit 1
fi

echo -e "${GREEN}✓ 1Password CLI ready${NC}"

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="${SCRIPT_DIR}/HROC_Website_New"
SERVER_USER="jdmal"  # Using jdmal user from 1Password SSH key
SERVER_IP="10.0.0.89"  # Using host from 1Password SSH key
SERVER_PATH="/mnt/tank/websites/kusanagi/web/hrocinc.org/"
BACKUP_DIR="/mnt/tank/backups"
BUCKET_NAME="hroc-website-20251230043930"
AWS_REGION="us-east-1"

# Deployment options
DEPLOY_TO_S3="${DEPLOY_S3:-true}"
DEPLOY_TO_SERVER="${DEPLOY_SERVER:-true}"
DRY_RUN="${DRY_RUN:-false}"

# Get credentials from 1Password
echo ""
echo -e "${BLUE}[1/4] Retrieving credentials from 1Password...${NC}"

# Get AWS credentials
AWS_ACCESS_KEY=$(op read "op://TrueNAS Infrastructure/AWS Access Key/username" 2>/dev/null)
AWS_SECRET_KEY=$(op read "op://TrueNAS Infrastructure/AWS Access Key/credential" 2>/dev/null)

if [ -z "$AWS_ACCESS_KEY" ] || [ -z "$AWS_SECRET_KEY" ]; then
    echo -e "${RED}✗ Failed to retrieve AWS credentials from 1Password${NC}"
    exit 1
fi

echo -e "${GREEN}✓ AWS credentials retrieved${NC}"

# Get SSH key for TrueNAS server
SSH_KEY_FILE="/tmp/truenas_deploy_key_$$"
trap "rm -f ${SSH_KEY_FILE}" EXIT

# Extract base64-encoded private key from secure note and decode it
SSH_KEY_BASE64=$(op item get "TrueNAS SSH Key - jdmal" --vault "TrueNAS Infrastructure" --format json 2>/dev/null | jq -r '.fields[] | select(.id=="notesPlain") | .value' | grep -A 1 "Private Key (base64):" | tail -1)

if [ -n "$SSH_KEY_BASE64" ]; then
    echo "$SSH_KEY_BASE64" | base64 -d > "${SSH_KEY_FILE}"
    chmod 600 "${SSH_KEY_FILE}"
    echo -e "${GREEN}✓ SSH key retrieved and decoded${NC}"
else
    echo -e "${YELLOW}⚠ SSH key not found in 1Password, will use default SSH key${NC}"
    SSH_KEY_FILE=""
fi

# Export AWS credentials for boto3 and aws CLI
export AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY"
export AWS_SECRET_ACCESS_KEY="$AWS_SECRET_KEY"
export AWS_REGION="$AWS_REGION"

# Step 1: Deploy to S3
if [ "$DEPLOY_TO_S3" = "true" ]; then
    echo ""
    echo -e "${BLUE}[2/4] Syncing assets to S3 bucket: ${BUCKET_NAME}...${NC}"

    if [ "$DRY_RUN" = "true" ]; then
        echo -e "${YELLOW}  (DRY RUN MODE)${NC}"
    fi

    # Check if aws CLI is installed
    if ! command -v aws &> /dev/null; then
        echo -e "${YELLOW}⚠ AWS CLI not found, installing...${NC}"
        brew install awscli
    fi

    # Sync images to S3
    if [ -d "${WEBSITE_DIR}/images" ]; then
        if [ "$DRY_RUN" = "true" ]; then
            aws s3 sync "${WEBSITE_DIR}/images" "s3://${BUCKET_NAME}/images" --dryrun
        else
            aws s3 sync "${WEBSITE_DIR}/images" "s3://${BUCKET_NAME}/images" \
                --content-type "image/webp" \
                --cache-control "max-age=31536000" \
                --delete
        fi
        echo -e "${GREEN}  ✓ Images synced${NC}"
    fi

    # Sync generated images to S3
    if [ -d "${WEBSITE_DIR}/generated_images" ]; then
        if [ "$DRY_RUN" = "true" ]; then
            aws s3 sync "${WEBSITE_DIR}/generated_images" "s3://${BUCKET_NAME}/generated_images" --dryrun
        else
            aws s3 sync "${WEBSITE_DIR}/generated_images" "s3://${BUCKET_NAME}/generated_images" \
                --content-type "image/webp" \
                --cache-control "max-age=31536000" \
                --delete
        fi
        echo -e "${GREEN}  ✓ Generated images synced${NC}"
    fi

    # Sync PDFs to S3
    if [ -d "${WEBSITE_DIR}/pdfs" ]; then
        if [ "$DRY_RUN" = "true" ]; then
            aws s3 sync "${WEBSITE_DIR}/pdfs" "s3://${BUCKET_NAME}/pdfs" --dryrun
        else
            aws s3 sync "${WEBSITE_DIR}/pdfs" "s3://${BUCKET_NAME}/pdfs" \
                --content-type "application/pdf" \
                --cache-control "max-age=31536000" \
                --delete
        fi
        echo -e "${GREEN}  ✓ PDFs synced${NC}"
    fi

    echo -e "${GREEN}✓ S3 sync complete${NC}"
else
    echo -e "${YELLOW}[2/4] Skipping S3 deployment (DEPLOY_S3=false)${NC}"
fi

# Step 2: Deploy to TrueNAS server
if [ "$DEPLOY_TO_SERVER" = "true" ]; then
    echo ""
    echo -e "${BLUE}[3/4] Deploying to TrueNAS server...${NC}"

    # Build SSH command options
    SSH_OPTS="-o ConnectTimeout=5 -o StrictHostKeyChecking=no"
    if [ -n "${SSH_KEY_FILE}" ]; then
        SSH_OPTS="${SSH_OPTS} -i ${SSH_KEY_FILE}"
    fi

    # Test SSH connection
    echo "  Testing SSH connection to ${SERVER_USER}@${SERVER_IP}..."
    if ! ssh ${SSH_OPTS} "${SERVER_USER}@${SERVER_IP}" "echo 'SSH connection successful'" &> /dev/null; then
        echo -e "${RED}✗ SSH connection failed${NC}"
        echo "Please ensure:"
        echo "  1. SSH key is configured in 1Password or locally"
        echo "  2. Server is reachable: ping ${SERVER_IP}"
        exit 1
    fi
    echo -e "${GREEN}  ✓ SSH connection verified${NC}"

    # Create backup on server
    if [ "$DRY_RUN" = "false" ]; then
        BACKUP_TIMESTAMP=$(date +%Y%m%d-%H%M%S)
        echo "  Creating backup on server..."
        ssh ${SSH_OPTS} "${SERVER_USER}@${SERVER_IP}" \
            "tar -czf ${BACKUP_DIR}/hrocinc-backup-${BACKUP_TIMESTAMP}.tar.gz -C /mnt/tank/websites/kusanagi/web hrocinc.org" \
            && echo -e "${GREEN}  ✓ Backup created: ${BACKUP_DIR}/hrocinc-backup-${BACKUP_TIMESTAMP}.tar.gz${NC}"
    fi

    # Build rsync SSH options
    RSYNC_SSH_OPTS="ssh ${SSH_OPTS}"

    # Sync files to server
    echo "  Syncing website files..."
    if [ "$DRY_RUN" = "true" ]; then
        echo -e "${YELLOW}  (DRY RUN MODE)${NC}"
        rsync -avzn --progress --delete \
            -e "${RSYNC_SSH_OPTS}" \
            --exclude '.git' \
            --exclude 'node_modules' \
            --exclude '.DS_Store' \
            --exclude 'lora_training' \
            --exclude 'image-generator' \
            --exclude 'lora_models' \
            "${WEBSITE_DIR}/" \
            "${SERVER_USER}@${SERVER_IP}:${SERVER_PATH}"
    else
        rsync -avz --progress --delete \
            -e "${RSYNC_SSH_OPTS}" \
            --exclude '.git' \
            --exclude 'node_modules' \
            --exclude '.DS_Store' \
            --exclude 'lora_training' \
            --exclude 'image-generator' \
            --exclude 'lora_models' \
            "${WEBSITE_DIR}/" \
            "${SERVER_USER}@${SERVER_IP}:${SERVER_PATH}"
    fi
    echo -e "${GREEN}  ✓ Files synced${NC}"

    # Fix permissions
    if [ "$DRY_RUN" = "false" ]; then
        echo "  Setting correct permissions..."
        ssh ${SSH_OPTS} "${SERVER_USER}@${SERVER_IP}" \
            "chown -R 33:33 ${SERVER_PATH} && chmod -R 755 ${SERVER_PATH}" \
            && echo -e "${GREEN}  ✓ Permissions set${NC}"
    fi

    echo -e "${GREEN}✓ Server deployment complete${NC}"
else
    echo -e "${YELLOW}[3/4] Skipping server deployment (DEPLOY_SERVER=false)${NC}"
fi

# Step 3: Verification
echo ""
echo -e "${BLUE}[4/4] Verifying deployment...${NC}"

# Verify server deployment
if [ "$DEPLOY_TO_SERVER" = "true" ] && [ "$DRY_RUN" = "false" ]; then
    FILE_COUNT=$(ssh ${SSH_OPTS} "${SERVER_USER}@${SERVER_IP}" "find ${SERVER_PATH} -type f | wc -l")
    TOTAL_SIZE=$(ssh ${SSH_OPTS} "${SERVER_USER}@${SERVER_IP}" "du -sh ${SERVER_PATH}" | cut -f1)
    echo -e "${GREEN}  ✓ Server files: ${FILE_COUNT} files, ${TOTAL_SIZE}${NC}"
fi

# Test website
echo "  Testing website..."
if curl -s -I https://hrocinc.org | grep -q "200 OK"; then
    echo -e "${GREEN}  ✓ Website is responding${NC}"
else
    echo -e "${YELLOW}  ⚠ Website check inconclusive${NC}"
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  Deployment Complete!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "Next steps:"
echo "  1. Visit https://hrocinc.org to verify"
echo "  2. Check browser console for any errors"
echo "  3. Test on mobile devices"
echo ""
echo "Usage examples:"
echo "  ${YELLOW}# Dry run (test without deploying)${NC}"
echo "  DRY_RUN=true ./deploy.sh"
echo ""
echo "  ${YELLOW}# Deploy only to S3${NC}"
echo "  DEPLOY_SERVER=false ./deploy.sh"
echo ""
echo "  ${YELLOW}# Deploy only to server${NC}"
echo "  DEPLOY_S3=false ./deploy.sh"
echo ""
