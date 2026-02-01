# CLAUDE.md - HROC Non-Profit Website

**Project:** Healing Roots Outreach Collective (HROC Inc)
**Location:** `/mnt/d/workspace/projects/HROC_Files/`
**Status:** Live on Wix (hroc.org) | Local development copies available
**Last Updated:** 2026-02-01

---

## Quick Overview

HROC (Healing Roots Outreach Collective) is a non-profit organization with a live website at hroc.org. This directory contains local development copies, deployment scripts, and comprehensive documentation for the HROC website and infrastructure.

**Website:** https://hroc.org (currently on Wix)
**Purpose:** Community support and non-profit services
**Technology:** WordPress/Kusanagi backend, S3 + CDN for images

---

## Project Information

### Organization Details

**Legal Information:**
- **EIN:** 39-3295288
- **UBI:** 605 944 010
- **Address:** 2122 S 272ND ST APT B111, Kent, WA 98032
- **Phone:** (253) 881-7377
- **Website:** hroc.org

**Founders:**
- **Bri** - Co-Founder & Executive Director
- **Lilly** - Co-Founder & Cultural Director
- **Jonathan** - Co-Founder & Operations Lead

**Mission:**
Community support, lived experience first, indigenous wisdom, collective power, authentic care.

---

## Directory Structure

```
HROC_Files/
├── CLAUDE.md                           # This file
├── 00_START_HERE.md                   # Quick start guide
├── .git/                              # Separate git repository
├── .serena/                           # Serena AI context
│   └── memories/
│       ├── project_overview.md
│       ├── code_style_and_conventions.md
│       ├── suggested_commands.md
│       └── task_completion_checklist.md
│
├── HROC_Website_New/                  # Main website files
│   ├── index.html                     # Enhanced website
│   ├── styles.css                     # 400+ lines of styling
│   ├── images/                        # 60+ integrated images
│   └── pdfs/                          # Document resources
│
├── HROC_Enhanced_Website/             # Alternative version
├── HROC_Public/                       # Public-facing version
│
├── deploy.sh                          # Automated deployment
│
└── [Documentation Files]              # 80+ markdown docs
    ├── DEPLOYMENT_GUIDE.md
    ├── DEPLOYMENT_INSTRUCTIONS.md
    ├── FINAL_DEPLOYMENT_INSTRUCTIONS.md
    ├── CODEX_*.md                     # Codex system docs
    ├── ARCHIVAL_PLAN_*.md             # Archival strategies
    └── NOTION_*.md                    # Notion integration
```

---

## Current Status

### Website
- **Live Site:** hroc.org (hosted on Wix)
- **Local Copies:** 3 versions available
  - `HROC_Website_New/` - Primary development copy (enhanced)
  - `HROC_Enhanced_Website/` - Alternative version
  - `HROC_Public/` - Public-facing version

### Known Issues
- **Alicia's photos need consistency fixes** - Multiple photo versions, needs standardization
- **S3 image delivery optimization** - Can be improved
- **Multiple local copies** - Consider consolidating

### Infrastructure
- **Backend:** Kusanagi (WordPress optimized)
- **Images:** S3 + CDN delivery
- **Backup:** 701MB WordPress backup (March 2024)
- **Server:** Potentially 10.0.0.89 (TrueNAS)

---

## How to Use

### Quick Start

```bash
# Navigate to project
cd /mnt/d/workspace/projects/HROC_Files/

# Read the comprehensive start guide
cat 00_START_HERE.md

# Check git status
git status

# View recent changes
git log --oneline -10
```

### Viewing the Website Locally

```bash
cd /mnt/d/workspace/projects/HROC_Files/HROC_Website_New/

# Open in browser
open index.html
# Or on WSL:
explorer.exe index.html
```

### Making Updates

```bash
# 1. Navigate to website directory
cd /mnt/d/workspace/projects/HROC_Files/HROC_Website_New/

# 2. Edit files
code index.html
code styles.css

# 3. Test changes locally (open in browser)

# 4. Commit changes
cd /mnt/d/workspace/projects/HROC_Files/
git add HROC_Website_New/
git commit -m "Description of changes"
git push
```

---

## Deployment

### Current Deployment: Wix
The live site (hroc.org) is currently hosted on Wix. Any changes need to be manually updated in the Wix editor.

### Alternative: Self-Hosted Deployment

The project includes deployment scripts for self-hosting:

```bash
cd /mnt/d/workspace/projects/HROC_Files/

# Automated deployment
./deploy.sh

# Follow prompts to:
# 1. Push to GitHub
# 2. Deploy to NAS server (10.0.0.89)
# 3. Restart web services
# 4. Verify deployment
```

**Manual Deployment:**
See `FINAL_DEPLOYMENT_INSTRUCTIONS.md` for step-by-step guide.

---

## Key Features

### Website Features (HROC_Website_New/)

**Founder Profiles:**
- 3 professional AI-generated founder portraits
- Compelling bios with personal mission quotes
- Responsive card layout

**Leadership Principles:**
- 🔥 Lived Experience First
- 🌍 Indigenous Wisdom
- 👥 Collective Power
- 💚 Authentic Care

**Gallery:**
- 60+ integrated images
- Organized collections
- Responsive image loading

**Technical:**
- WCAG 2.2 AA accessibility
- 100% mobile responsive
- 400+ lines of CSS styling
- 432 lines of HTML modifications

---

## Infrastructure Details

### Backend: Kusanagi
- WordPress-optimized server stack
- High-performance PHP/MySQL
- Nginx reverse proxy
- Redis caching

### Image Delivery: S3 + CDN
- Amazon S3 bucket for storage
- CloudFront CDN distribution
- Optimized delivery globally
- Reduced server load

### Backup Strategy
- WordPress backup: 701MB (March 2024)
- Git version control for code
- Multiple local copies for redundancy
- Archival plan for Baby NAS transfer

---

## Serena AI Context

The project includes comprehensive Serena AI context in `.serena/memories/`:

### project_overview.md
Complete project overview including:
- Organization details
- Website structure
- Deployment information
- Infrastructure topology

### code_style_and_conventions.md
Coding standards for:
- HTML/CSS formatting
- File organization
- Naming conventions
- Best practices

### suggested_commands.md
Common commands for:
- Git operations
- Deployment tasks
- Testing procedures
- Maintenance tasks

### task_completion_checklist.md
Task tracking for:
- Website updates
- Deployment steps
- Quality assurance
- Documentation updates

---

## Documentation Overview

### Start Here Docs
- `00_START_HERE.md` - Main quick start guide
- `CODEX_QUICK_START.md` - Codex system quick reference
- `CODEX_SYSTEM_OVERVIEW.md` - Complete Codex documentation

### Deployment Docs
- `DEPLOYMENT_GUIDE.md` - Comprehensive deployment guide
- `DEPLOYMENT_INSTRUCTIONS.md` - Step-by-step instructions
- `FINAL_DEPLOYMENT_INSTRUCTIONS.md` - Pre-launch checklist
- `DEPLOY_TO_TRUENAS_COMPLETE.md` - TrueNAS deployment
- `DEPLOY_FROM_LOCAL_NETWORK.md` - Local network deployment

### Status & Completion Docs
- `DEPLOYMENT_COMPLETE.md` - Deployment completion status
- `DEPLOYMENT_SUCCESSFUL.md` - Success confirmation
- `DEPLOYMENT_STATUS_REPORT.md` - Detailed status report
- `DOCUMENT_CLEANUP_COMPLETE.md` - Documentation cleanup

### Codex System Docs
- `CODEX_AGENTS_README.md` - Agent system documentation
- `CODEX_INVOCATION_EXAMPLES.md` - Usage examples
- `CODEX_PHASE_3_HROC_HANDOFF.md` - Handoff documentation
- `CODEX_PHASE_3_LAUNCH_INSTRUCTIONS.md` - Launch guide
- `CODEX_SYSTEM_QUICK_REFERENCE.txt` - Quick reference

### Archival Planning
- `ARCHIVAL_PLAN_2025.md` - 2025 archival strategy
- `ARCHIVAL_PLAN_QUICK_REFERENCE.md` - Quick archival guide

### Integration Docs
- `NOTION_IMPORT_COMPLETE.md` - Notion import status
- `NOTION_IMPORT_README.md` - Notion integration guide
- `1PASSWORD_SETUP_COMPLETE.md` - 1Password integration

### Package & Summary Docs
- `COMPLETE_PACKAGE_SUMMARY.md` - Complete package overview
- `PACKAGE_PREPARATION_COMPLETE.md` - Package prep status

---

## Common Tasks

### Fixing Alicia's Photos

```bash
cd /mnt/d/workspace/projects/HROC_Files/HROC_Website_New/images/

# 1. Identify all Alicia photos
find . -name "*alicia*" -o -name "*Alicia*"

# 2. Standardize naming
# 3. Choose best photo version
# 4. Update references in index.html
# 5. Remove duplicates

# 6. Commit changes
cd /mnt/d/workspace/projects/HROC_Files/
git add HROC_Website_New/images/
git commit -m "Standardize Alicia photos"
```

### Optimizing S3 Image Delivery

```bash
# Get S3 credentials from 1Password
eval $(op signin)
AWS_KEY=$(op item get "AWS S3" --vault "TrueNAS Infrastructure" --fields access_key)
AWS_SECRET=$(op item get "AWS S3" --vault "TrueNAS Infrastructure" --fields secret_key)

# Configure AWS CLI
aws configure set aws_access_key_id "$AWS_KEY"
aws configure set aws_secret_access_key "$AWS_SECRET"

# List buckets
aws s3 ls

# Sync images to S3
aws s3 sync HROC_Website_New/images/ s3://hroc-images/

# Set caching headers
aws s3 cp s3://hroc-images/ s3://hroc-images/ \
  --recursive \
  --metadata-directive REPLACE \
  --cache-control "max-age=31536000"
```

### Consolidating Website Versions

```bash
cd /mnt/d/workspace/projects/HROC_Files/

# Compare versions
diff -r HROC_Website_New/ HROC_Enhanced_Website/
diff -r HROC_Website_New/ HROC_Public/

# Determine canonical version (likely HROC_Website_New/)

# Archive others
mkdir -p archive/
mv HROC_Enhanced_Website/ archive/
mv HROC_Public/ archive/

# Document decision
git commit -m "Consolidate to single website version (HROC_Website_New)"
```

### Updating from Wix to Self-Hosted

```bash
# 1. Export from Wix (if possible)
# 2. Compare with local HROC_Website_New/
# 3. Merge any missing content
# 4. Test thoroughly
# 5. Deploy to TrueNAS
./deploy.sh
# 6. Update DNS to point to new server
# 7. Cancel Wix subscription
```

---

## Git Workflow

### This is a Separate Git Repository

HROC_Files has its own `.git/` directory, separate from the main workspace repository.

```bash
cd /mnt/d/workspace/projects/HROC_Files/

# Check status
git status

# View history
git log --oneline -20

# Check branches
git branch -a

# Remote repository
git remote -v
```

### Making Changes

```bash
# 1. Create feature branch
git checkout -b feature/photo-fixes

# 2. Make changes
# Edit files...

# 3. Stage changes
git add HROC_Website_New/

# 4. Commit with descriptive message
git commit -m "Fix: Standardize Alicia photos for consistency"

# 5. Push to remote
git push origin feature/photo-fixes

# 6. Create pull request (if using GitHub)
# 7. Merge to main after review
```

---

## Credentials (1Password)

All HROC credentials stored in 1Password vaults.

### Accessing Credentials

```bash
# Sign in
eval $(op signin)

# List HROC-related items
op item list | grep -i hroc

# Get specific credential
op item get "HROC AWS S3" --vault "TrueNAS Infrastructure"
op item get "HROC WordPress" --vault "TrueNAS Infrastructure"

# Get specific fields
WP_USER=$(op item get "HROC WordPress" --vault "TrueNAS Infrastructure" --fields username)
WP_PASS=$(op item get "HROC WordPress" --vault "TrueNAS Infrastructure" --fields password)
```

### Common Credentials
- WordPress admin login
- AWS S3 access keys
- Kusanagi server SSH key
- Database passwords
- CDN credentials

---

## Troubleshooting

### "Can't find website files"
```bash
# Verify you're in the right directory
pwd
# Should be: /mnt/d/workspace/projects/HROC_Files/

# Check for website directories
ls -la | grep HROC_Website
```

### "Git repository not found"
```bash
# Ensure you're in HROC_Files, not workspace root
cd /mnt/d/workspace/projects/HROC_Files/
git status
```

### "Deployment script fails"
```bash
# Check deployment script permissions
ls -la deploy.sh
# Should be executable: -rwxr-xr-x

# Make executable if needed
chmod +x deploy.sh

# Check script contents
cat deploy.sh
```

### "Images not loading"
```bash
# Check image paths in HTML
grep -r "src=" HROC_Website_New/index.html

# Verify images exist
ls -la HROC_Website_New/images/

# Check for broken links
# Use browser dev tools Network tab
```

### "Wix sync issues"
```
# Wix doesn't support git sync
# Must manually update in Wix editor
# Or migrate to self-hosted solution
```

---

## Integration with Workspace

### Relationship to Main Workspace

HROC is one of three main projects in the workspace:

1. **Opportunity Research Bot** - AI opportunity discovery
2. **ISN.BIZ Website** - Company website
3. **HROC Website** - This project (non-profit site)

### Shared Infrastructure

- **1Password:** Shared credential management
- **Baby NAS:** Shared archival storage
- **Network:** Same 10.0.0.0/24 LAN
- **Git Practices:** Similar workflow standards

### Independent Elements

- **Git Repository:** Separate from main workspace
- **Deployment:** Independent deployment pipeline
- **Documentation:** Self-contained in project directory
- **Domain:** Separate domain (hroc.org)

---

## Key Decisions Made

### Why Separate Git Repository?
- **Independent versioning** - HROC has separate release cycle
- **Different contributors** - May have different access levels
- **Cleaner history** - Focused on HROC changes only
- **Deployment isolation** - HROC deploys independently

### Why Multiple Website Versions?
- **Development iterations** - Different enhancement phases
- **Backup copies** - Safety during major changes
- **A/B testing** - Compare different approaches
- **Migration safety** - Keep old version during transitions

### Why Kusanagi Backend?
- **WordPress optimization** - Best performance for WP
- **Security hardened** - Built-in security features
- **Easy management** - Command-line tools
- **Proven reliability** - Industry-standard stack

### Why S3 + CDN for Images?
- **Performance** - Faster global delivery
- **Cost-effective** - Pay only for usage
- **Scalable** - Handles traffic spikes
- **Reduced server load** - Offload image serving

---

## Future Enhancements

### Planned Improvements
1. **Photo Standardization** - Fix Alicia photo consistency
2. **S3 Optimization** - Improve image delivery
3. **Version Consolidation** - Single canonical website version
4. **Wix Migration** - Self-host on TrueNAS
5. **CI/CD Pipeline** - Automated testing and deployment

### Nice-to-Have Features
- **CMS Integration** - Easier content management
- **Analytics Dashboard** - Visitor tracking and insights
- **Donation Portal** - Integrated donation processing
- **Member Portal** - Community member login area
- **Event Calendar** - Automated event management

---

## Related Documentation

**Workspace Context:**
- `/mnt/d/workspace/WORKSPACE_CLAUDE.md` - Complete workspace organization
- `/mnt/d/workspace/CLAUDE.md` - Quick workspace reference
- `/mnt/d/workspace/.serena/WEBSITES.md` - Website deployment strategies

**Project Documentation:**
- `00_START_HERE.md` - Main quick start guide
- `.serena/memories/` - Serena AI context
- `DEPLOYMENT_GUIDE.md` - Deployment documentation
- `CODEX_SYSTEM_OVERVIEW.md` - Codex integration

---

## Support

### Getting Help

1. **Read `00_START_HERE.md`** - Comprehensive overview
2. **Check `.serena/memories/`** - AI context documentation
3. **Review deployment docs** - Step-by-step guides
4. **Check git history** - See what changed and why
5. **Consult workspace docs** - `.serena/` in workspace root

### Reporting Issues

- Document the issue clearly
- Include error messages
- Note what you were trying to do
- Specify which website version
- Check git status for uncommitted changes

---

## Summary

HROC is a non-profit website project with:
- Live site on Wix (hroc.org)
- Local development copies
- Comprehensive documentation
- Separate git repository
- Self-hosted deployment option
- Professional features and design

**Quick Start:** Read `00_START_HERE.md` then explore the `HROC_Website_New/` directory.

---

**Last Updated:** 2026-02-01
**Maintained By:** HROC Team + jdmal + Claude AI
**Status:** Active development, live on Wix
**Canonical Location:** `/mnt/d/workspace/projects/HROC_Files/`

**Note:** This is the authoritative HROC location. Old copy archived to `/mnt/d/workspace/Archive/2026-02-01/HROC_Files_old/`
