#!/bin/bash
set -euo pipefail

# Push all images to TrueNAS server
# This script syncs ONLY image directories

# Color output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Pushing Images to TrueNAS Server${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WEBSITE_DIR="${SCRIPT_DIR}/HROC_Website_New"
SERVER_USER="root"
SERVER_IP="10.0.0.89"
SERVER_PATH="/mnt/tank/websites/kusanagi/web/hrocinc.org/"

# Test SSH connection
echo -e "${BLUE}[1/3] Testing SSH connection to ${SERVER_USER}@${SERVER_IP}...${NC}"
if ! ssh -o ConnectTimeout=5 "${SERVER_USER}@${SERVER_IP}" "echo 'SSH connection successful'" &> /dev/null; then
    echo -e "${RED}✗ SSH connection failed${NC}"
    echo "Please ensure:"
    echo "  1. SSH key is set up: ssh-copy-id ${SERVER_USER}@${SERVER_IP}"
    echo "  2. Server is reachable: ping ${SERVER_IP}"
    exit 1
fi
echo -e "${GREEN}✓ SSH connection verified${NC}"

# Push founder images
echo ""
echo -e "${BLUE}[2/3] Syncing images/founders/ to TrueNAS...${NC}"
if [ -d "${WEBSITE_DIR}/images" ]; then
    rsync -avz --progress \
        "${WEBSITE_DIR}/images/" \
        "${SERVER_USER}@${SERVER_IP}:${SERVER_PATH}images/"
    echo -e "${GREEN}✓ Founder images synced${NC}"
else
    echo -e "${YELLOW}⚠ images/ directory not found${NC}"
fi

# Push generated/community images
echo ""
echo -e "${BLUE}[3/3] Syncing generated_images/ to TrueNAS...${NC}"
if [ -d "${WEBSITE_DIR}/generated_images" ]; then
    rsync -avz --progress \
        "${WEBSITE_DIR}/generated_images/" \
        "${SERVER_USER}@${SERVER_IP}:${SERVER_PATH}generated_images/"
    echo -e "${GREEN}✓ Generated images synced${NC}"
else
    echo -e "${YELLOW}⚠ generated_images/ directory not found${NC}"
fi

# Set correct permissions
echo ""
echo "Setting correct permissions on server..."
ssh "${SERVER_USER}@${SERVER_IP}" \
    "chown -R 33:33 ${SERVER_PATH}images ${SERVER_PATH}generated_images && \
     chmod -R 755 ${SERVER_PATH}images ${SERVER_PATH}generated_images" \
    && echo -e "${GREEN}✓ Permissions set (www-data:www-data)${NC}"

# Show summary
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  All Images Pushed to TrueNAS!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

IMAGE_COUNT=$(ssh "${SERVER_USER}@${SERVER_IP}" "find ${SERVER_PATH}images -type f | wc -l")
GEN_COUNT=$(ssh "${SERVER_USER}@${SERVER_IP}" "find ${SERVER_PATH}generated_images -type f 2>/dev/null | wc -l || echo 0")
TOTAL_SIZE=$(ssh "${SERVER_USER}@${SERVER_IP}" "du -sh ${SERVER_PATH}images ${SERVER_PATH}generated_images 2>/dev/null | awk '{s+=\$1} END {print s}'" || echo "unknown")

echo "Summary:"
echo "  Founder images: ${IMAGE_COUNT} files"
echo "  Generated images: ${GEN_COUNT} files"
echo "  Server: ${SERVER_USER}@${SERVER_IP}"
echo "  Path: ${SERVER_PATH}"
echo ""
