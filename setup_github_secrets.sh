#!/bin/bash
set -euo pipefail

# GitHub Secrets Setup Script
# This script helps you set up the required secrets for GitHub Actions deployment

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  GitHub Secrets Setup for HROC Deployment${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check if 1Password CLI is installed
if ! command -v op &> /dev/null; then
    echo -e "${YELLOW}⚠ 1Password CLI not found${NC}"
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
echo ""

# Retrieve credentials from 1Password
echo "Retrieving credentials from 1Password..."
AWS_ACCESS_KEY=$(op item get "AWS Access Key" --fields credential 2>/dev/null)
AWS_SECRET_KEY=$(op item get "Aws Secret Access" --fields credential 2>/dev/null)

if [ -z "$AWS_ACCESS_KEY" ] || [ -z "$AWS_SECRET_KEY" ]; then
    echo -e "${YELLOW}✗ Failed to retrieve AWS credentials from 1Password${NC}"
    exit 1
fi

echo -e "${GREEN}✓ AWS credentials retrieved${NC}"
echo ""

# Display instructions
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Setup Instructions${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "You need to add the following secrets to your GitHub repository:"
echo ""
echo "1. Go to: https://github.com/isndotbiz/HROC_Files/settings/secrets/actions"
echo "2. Click 'New repository secret' for each of the following:"
echo ""

echo -e "${GREEN}Secret 1: AWS_ACCESS_KEY_ID${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "$AWS_ACCESS_KEY"
echo ""

echo -e "${GREEN}Secret 2: AWS_SECRET_ACCESS_KEY${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "$AWS_SECRET_KEY"
echo ""

echo -e "${GREEN}Secret 3: TRUENAS_SSH_KEY${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ -f ~/.ssh/id_ed25519 ]; then
    cat ~/.ssh/id_ed25519
    echo ""
elif [ -f ~/.ssh/id_rsa ]; then
    cat ~/.ssh/id_rsa
    echo ""
else
    echo -e "${YELLOW}No SSH key found at ~/.ssh/id_ed25519 or ~/.ssh/id_rsa${NC}"
    echo "Please generate one:"
    echo "  ssh-keygen -t ed25519 -C \"deploy@hrocinc.org\""
    echo "  ssh-copy-id root@10.0.0.89"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  Quick Copy Commands${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo "# Copy AWS Access Key to clipboard:"
echo "echo '$AWS_ACCESS_KEY' | pbcopy"
echo ""
echo "# Copy AWS Secret Key to clipboard:"
echo "echo '$AWS_SECRET_KEY' | pbcopy"
echo ""
echo "# Copy SSH key to clipboard:"
echo "cat ~/.ssh/id_ed25519 | pbcopy"
echo ""
echo -e "${GREEN}After adding all secrets, your GitHub Actions workflow will be ready!${NC}"
echo ""
