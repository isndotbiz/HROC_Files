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
  - AWS S3 (for assets/CDN)
  - NAS server with Nginx (self-hosted)
  - GitHub Pages (backup)
  - Cloudflare (CDN/DNS)
- **Deployment**: Bash scripts, Python scripts (boto3 for S3)
- **Image Generation**: Python scripts using Flux LoRA models
- **Version Control**: Git/GitHub

## Key Directories
- `HROC_Website_New/` - Main website source files
- `HROC_Public/` - Public documents for transparency
- `Generated_Images/` - AI-generated images (not tracked in git)
- `Archive_*` - Historical/backup files

## Website URL
- Production: https://hrocinc.org

## GitHub Repository
- https://github.com/isndotbiz/HROC_Files.git
