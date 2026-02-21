# HROC Files Project Overview

## Purpose
This project contains files and resources for **Healing Roots Outreach Collective (HROC)**, a 501(c)(3) nonprofit organization. The project includes:
- Website source code and assets
- Deployment scripts (AWS S3, NAS server, GitHub)
- LoRA training scripts for AI-generated images
- Documentation and compliance materials
- Notion import files for organizational operations

## Tech Stack
- **Website**: Static HTML/CSS/JavaScript (no framework)
- **Hosting**: 
  - Netlify (PRIMARY at hrocinc.org, Site ID: f5c7828a-b18a-41c1-a8bc-c64e5beb13ba)
  - AWS S3 bucket `hroc-website-20251230043930` (images, PDFs - assets only, 77 files, 12.8 MiB)
  - Cloudflare (CDN/DNS, zone ID: 0da5d1116d7e40e8c77615ce8a757cd1, SSL: Full mode)
- **Deployment**: Bash scripts, Python scripts (boto3 for S3)
- **Image Generation**: Python scripts using Flux LoRA models
- **Version Control**: Git/GitHub

## Key Directories
- `HROC_Website_New/` - Main website source files
- `HROC_Public/` - Public documents for transparency
- `Generated_Images/` - AI-generated images (not tracked in git)
- `Archive_*` - Historical/backup files

## Website URL
- Production: https://hrocinc.org\n- Backup (Netlify): https://hrocinc.netlify.app

## GitHub Repository
- https://github.com/isndotbiz/HROC_Files.git
