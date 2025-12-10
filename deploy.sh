#!/bin/bash

# HROC Website Deployment Script
# This script automates GitHub push and NAS server deployment

set -e  # Exit on error

echo "=========================================="
echo "🚀 HROC Website Deployment Script"
echo "=========================================="
echo ""

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
REPO_DIR="/Users/jonathanmallinger/Documents/HROC_Files"
GITHUB_REPO="https://github.com/isndotbiz/HROC_Files.git"
NAS_SERVER="${NAS_SERVER:-10.0.0.89}"
NAS_USER="${NAS_USER:-root}"
NAS_PATH="${NAS_PATH:-/var/www/hroc}"
NAS_PORT="${NAS_PORT:-22}"

# Step 1: Verify we're in the right directory
echo -e "${BLUE}Step 1: Verifying repository directory...${NC}"
if [ ! -d "$REPO_DIR" ]; then
    echo -e "${RED}Error: Repository directory not found at $REPO_DIR${NC}"
    exit 1
fi

cd "$REPO_DIR"
echo -e "${GREEN}✓ Found repository at $REPO_DIR${NC}"
echo ""

# Step 2: Check git status
echo -e "${BLUE}Step 2: Checking git status...${NC}"
git_status=$(git status --porcelain HROC_Website_New/index.html HROC_Website_New/styles.css 2>/dev/null || echo "")
if [ -z "$git_status" ]; then
    echo -e "${GREEN}✓ Website files are committed${NC}"
else
    echo -e "${YELLOW}⚠ Uncommitted changes detected. Please commit first.${NC}"
    exit 1
fi

# Get commit info
COMMIT_HASH=$(git rev-parse --short HEAD)
COMMIT_MSG=$(git log -1 --format=%B | head -1)
echo -e "${GREEN}✓ Latest commit: $COMMIT_HASH - $COMMIT_MSG${NC}"
echo ""

# Step 3: Push to GitHub
echo -e "${BLUE}Step 3: Pushing to GitHub...${NC}"
echo "Repository: $GITHUB_REPO"
echo "Branch: main"
echo ""

read -p "Proceed with GitHub push? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    # Try to push
    if git push origin main 2>/dev/null; then
        echo -e "${GREEN}✓ Successfully pushed to GitHub!${NC}"
    else
        echo -e "${YELLOW}⚠ GitHub push requires authentication${NC}"
        echo "Please authenticate with:"
        echo "  1. Personal Access Token (recommended)"
        echo "  2. GitHub CLI (gh auth login)"
        echo "  3. SSH key (ssh-add ~/.ssh/id_ed25519)"
        echo ""
        echo "Then try: git push origin main"
        echo "Continuing with NAS deployment..."
    fi
else
    echo "Skipping GitHub push"
fi
echo ""

# Step 4: Deploy to NAS Server
echo -e "${BLUE}Step 4: Deploying to NAS Server...${NC}"
echo "Server: $NAS_USER@$NAS_SERVER:$NAS_PATH"
echo "Port: $NAS_PORT"
echo ""

read -p "Proceed with NAS server deployment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Testing SSH connection to NAS server..."

    if timeout 5 ssh -p $NAS_PORT -o ConnectTimeout=5 -o StrictHostKeyChecking=no $NAS_USER@$NAS_SERVER "whoami" &>/dev/null; then
        echo -e "${GREEN}✓ SSH connection successful!${NC}"
        echo ""

        echo "Deploying files using rsync..."
        rsync -avz -e "ssh -p $NAS_PORT" --delete \
            HROC_Website_New/ \
            $NAS_USER@$NAS_SERVER:$NAS_PATH/ 2>/dev/null || \
        echo -e "${YELLOW}Note: Some files may not have synced. Check permissions.${NC}"

        echo -e "${GREEN}✓ Files deployed to NAS server!${NC}"
        echo ""

        # Step 5: Restart services on NAS server
        echo -e "${BLUE}Step 5: Restarting web services on NAS server...${NC}"

        read -p "Restart Nginx on the server? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ssh -p $NAS_PORT $NAS_USER@$NAS_SERVER \
                "sudo systemctl restart nginx && echo 'Nginx restarted successfully'" \
                2>/dev/null || \
            ssh -p $NAS_PORT $NAS_USER@$NAS_SERVER \
                "sudo systemctl restart apache2 && echo 'Apache restarted successfully'" \
                2>/dev/null || \
            echo -e "${YELLOW}⚠ Could not restart web server. Check permissions.${NC}"

            echo -e "${GREEN}✓ Web server restarted!${NC}"
        fi
        echo ""

    else
        echo -e "${RED}✗ Cannot connect to NAS server${NC}"
        echo "Troubleshooting:"
        echo "  1. Verify SSH access: ssh -p $NAS_PORT $NAS_USER@$NAS_SERVER"
        echo "  2. Register SSH key: ssh-copy-id -p $NAS_PORT $NAS_USER@$NAS_SERVER"
        echo "  3. Check firewall: Is port $NAS_PORT open?"
        exit 1
    fi
else
    echo "Skipping NAS deployment"
fi
echo ""

# Step 6: Deployment Summary
echo "=========================================="
echo -e "${GREEN}✓ Deployment Complete!${NC}"
echo "=========================================="
echo ""
echo "🎉 Your HROC website has been deployed!"
echo ""
echo "Next steps:"
echo "  1. Visit https://hrocinc.org to verify deployment"
echo "  2. Test founder section, gallery images, and responsive design"
echo "  3. Check all images are loading correctly"
echo "  4. Verify crisis buttons are functional"
echo ""
echo "Commit Hash: $COMMIT_HASH"
echo "GitHub: https://github.com/isndotbiz/HROC_Files/commits/main"
echo "Website: https://hrocinc.org"
echo "NAS Server: http://$NAS_SERVER:8081"
echo ""
