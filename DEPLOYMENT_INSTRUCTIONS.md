# HROC Website Deployment Instructions

## 🎯 Overview

The HROC website has an automated deployment system that:
- Stores all credentials securely in 1Password
- Hosts images and large files on S3 for fast loading
- Deploys website files to TrueNAS server
- Automatically deploys on git push via GitHub Actions

## 🔐 Infrastructure Details

### S3 Bucket
- **Bucket Name**: `hroc-website-20251230043930`
- **Region**: `us-east-1`
- **Purpose**: Hosting images and PDF files
- **Access**: Public read access enabled
- **CDN**: CloudFront (optional, for caching)

### TrueNAS Server
- **IP**: 10.0.0.89
- **User**: root
- **Path**: `/mnt/tank/websites/kusanagi/web/hrocinc.org/`
- **Backup Path**: `/mnt/tank/backups/`
- **Web Server**: Nginx (via Kusanagi container)
- **Reverse Proxy**: Traefik

### Credentials Storage
All credentials are stored in 1Password:
- **AWS Access Key**: Item "AWS Access Key" in 1Password
- **AWS Secret Key**: Item "Aws Secret Access" in 1Password
- **SSH Key**: Stored locally and in GitHub Secrets for CI/CD

## 🚀 Deployment Methods

### Method 1: Automatic Deployment (Recommended)

Every push to the `main` branch that affects `HROC_Website_New/` automatically triggers deployment.

**What happens automatically:**
1. Code is pushed to GitHub
2. GitHub Actions workflow runs
3. Images/PDFs sync to S3
4. Website files deploy to TrueNAS
5. Permissions are set correctly
6. Website is verified

**To use:**
```bash
# Make your changes
git add HROC_Website_New/
git commit -m "Update website content"
git push origin main

# Deployment happens automatically!
# Check status: https://github.com/isndotbiz/HROC_Files/actions
```

### Method 2: Manual Deployment with deploy.sh

Uses 1Password CLI for secure credential management.

**Prerequisites:**
```bash
# Install 1Password CLI (if not installed)
brew install 1password-cli

# Sign in to 1Password
eval $(op signin)

# Verify SSH access
ssh root@10.0.0.89 "echo 'Connection OK'"
```

**Deploy everything:**
```bash
./deploy.sh
```

**Dry run (test without deploying):**
```bash
DRY_RUN=true ./deploy.sh
```

**Deploy only to S3:**
```bash
DEPLOY_SERVER=false ./deploy.sh
```

**Deploy only to server:**
```bash
DEPLOY_S3=false ./deploy.sh
```

### Method 3: Manual rsync Deployment

For quick server-only deployments without S3 sync.

```bash
# Create backup first
ssh root@10.0.0.89 "tar -czf /mnt/tank/backups/hrocinc-backup-$(date +%Y%m%d-%H%M%S).tar.gz -C /mnt/tank/websites/kusanagi/web hrocinc.org"

# Deploy files
rsync -avz --progress --delete \
    --exclude '.git' \
    --exclude 'node_modules' \
    --exclude '.DS_Store' \
    HROC_Website_New/ \
    root@10.0.0.89:/mnt/tank/websites/kusanagi/web/hrocinc.org/

# Fix permissions
ssh root@10.0.0.89 "chown -R 33:33 /mnt/tank/websites/kusanagi/web/hrocinc.org && chmod -R 755 /mnt/tank/websites/kusanagi/web/hrocinc.org"
```

## ⚙️ GitHub Actions Setup

### Required Secrets

Add these secrets to your GitHub repository (Settings → Secrets and variables → Actions):

1. **AWS_ACCESS_KEY_ID**
   - Get from: `op item get "AWS Access Key" --fields credential`
   - Paste into GitHub secret

2. **AWS_SECRET_ACCESS_KEY**
   - Get from: `op item get "Aws Secret Access" --fields credential`
   - Paste into GitHub secret

3. **TRUENAS_SSH_KEY**
   - Get your SSH private key: `cat ~/.ssh/id_ed25519`
   - Paste into GitHub secret

### Setting up GitHub Secrets

```bash
# 1. Go to GitHub repository
open https://github.com/isndotbiz/HROC_Files/settings/secrets/actions

# 2. Click "New repository secret"

# 3. Add AWS_ACCESS_KEY_ID
op item get "AWS Access Key" --fields credential

# 4. Add AWS_SECRET_ACCESS_KEY
op item get "Aws Secret Access" --fields credential

# 5. Add TRUENAS_SSH_KEY
cat ~/.ssh/id_ed25519
```

## 🔧 Setting Up SSH Access

### For TrueNAS Server

```bash
# 1. Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "deploy@hrocinc.org"

# 2. Copy key to server
ssh-copy-id root@10.0.0.89

# 3. Test connection
ssh root@10.0.0.89 "echo 'SSH works!'"
```

### For GitHub Actions

The SSH key is already configured in the GitHub Actions workflow. Just ensure the `TRUENAS_SSH_KEY` secret is set.

## 📊 What Gets Deployed Where

### S3 Bucket Content
```
hroc-website-20251230043930/
├── images/               (2MB - Small images and logos)
├── generated_images/     (53MB - AI-generated founder photos)
└── pdfs/                 (13MB - Documents and resources)
```

### TrueNAS Server Content
```
/mnt/tank/websites/kusanagi/web/hrocinc.org/
├── index.html
├── bri.html
├── jonathan.html
├── lilly.html
├── documents.html
├── styles.css
├── script.js
├── cloudflare-tunnel-setup.sh
├── ssl-renewal-setup.sh
├── nginx.conf
├── nginx-ssl.conf
├── generate_images.py
├── images/               (Synced from local)
├── generated_images/     (Synced from local)
├── pdfs/                 (Synced from local)
└── lora_models/          (Excluded from deployment)
```

## 🌐 Verification Steps

After deployment, verify:

1. **Website loads**: https://hrocinc.org
2. **Images load from S3**: Check browser Network tab
3. **PDFs load**: Test document downloads
4. **Mobile responsive**: Test on phone/tablet
5. **No console errors**: Check browser console
6. **SSL certificate**: Verify HTTPS is working

### Quick verification commands:

```bash
# Test website response
curl -I https://hrocinc.org

# Count deployed files on server
ssh root@10.0.0.89 "find /mnt/tank/websites/kusanagi/web/hrocinc.org -type f | wc -l"

# Check deployed file size
ssh root@10.0.0.89 "du -sh /mnt/tank/websites/kusanagi/web/hrocinc.org"

# Verify S3 bucket contents
aws s3 ls s3://hroc-website-20251230043930/ --recursive --human-readable --summarize
```

## 🔄 Rollback Procedure

If something goes wrong, you can rollback using server backups:

```bash
# 1. List available backups
ssh root@10.0.0.89 "ls -lh /mnt/tank/backups/hrocinc-backup-*"

# 2. Restore from backup (replace TIMESTAMP)
ssh root@10.0.0.89 "tar -xzf /mnt/tank/backups/hrocinc-backup-TIMESTAMP.tar.gz -C /mnt/tank/websites/kusanagi/web/"

# 3. Fix permissions
ssh root@10.0.0.89 "chown -R 33:33 /mnt/tank/websites/kusanagi/web/hrocinc.org && chmod -R 755 /mnt/tank/websites/kusanagi/web/hrocinc.org"
```

## 🐛 Troubleshooting

### SSH Connection Issues

```bash
# Test basic connectivity
ping 10.0.0.89

# Verbose SSH debug
ssh -v root@10.0.0.89

# Check SSH key permissions
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Re-add SSH key
ssh-copy-id root@10.0.0.89
```

### AWS/S3 Issues

```bash
# Test AWS credentials
aws sts get-caller-identity

# List S3 buckets
aws s3 ls

# Sync manually
aws s3 sync HROC_Website_New/images s3://hroc-website-20251230043930/images --dryrun
```

### Website Not Updating

```bash
# Clear Cloudflare cache
./purge_cloudflare_cache.sh

# Reload Nginx on server
ssh root@10.0.0.89 "docker exec kusanagi-nginx nginx -s reload"

# Restart Nginx container
ssh root@10.0.0.89 "docker restart kusanagi-nginx"
```

### GitHub Actions Failing

1. Check workflow run: https://github.com/isndotbiz/HROC_Files/actions
2. Verify secrets are set correctly
3. Check SSH key has correct permissions on server
4. Ensure server is accessible from GitHub's IP ranges

## 📁 File Structure

```
HROC_Files/
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions deployment
├── HROC_Website_New/               # Website source files
│   ├── *.html                      # Website pages
│   ├── styles.css                  # Styling
│   ├── script.js                   # JavaScript
│   ├── images/                     # Image assets
│   ├── generated_images/           # AI-generated photos
│   └── pdfs/                       # PDF documents
├── deploy.sh                       # Manual deployment script
├── create_s3_bucket.py            # S3 bucket creation
├── sync_to_new_s3.py              # S3 sync utility
├── check_cloudflare_dns.sh        # DNS verification
├── purge_cloudflare_cache.sh      # Cache management
└── DEPLOYMENT_INSTRUCTIONS.md     # This file
```

## 🔗 Quick Links

- **Website**: https://hrocinc.org
- **GitHub Repo**: https://github.com/isndotbiz/HROC_Files
- **GitHub Actions**: https://github.com/isndotbiz/HROC_Files/actions
- **S3 Bucket**: hroc-website-20251230043930
- **TrueNAS**: http://10.0.0.89
- **Cloudflare Dashboard**: https://dash.cloudflare.com

## 📝 Recent Changes

### 2026-01-10: Automated Deployment System
- Integrated 1Password CLI for secure credential management
- Created comprehensive deploy.sh script
- Set up GitHub Actions for automatic deployment
- Updated documentation with new procedures

### 2025-12-30: S3 Migration
- Created new S3 bucket: hroc-website-20251230043930
- Migrated 68MB of images and PDFs to S3
- Updated all HTML files with S3 URLs
- Decommissioned old S3 bucket

## ⚠️ Important Notes

- **Always test with DRY_RUN=true first** before deploying to production
- Backups are created automatically before each deployment
- S3 files are cached for 1 year (max-age=31536000)
- Server permissions must be 33:33 (www-data user)
- Never commit credentials to git - use 1Password only
- GitHub Actions secrets should be rotated periodically
