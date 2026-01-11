# Deploy to TrueNAS from Local Network

## 🎯 Quick Start

Run these commands on your computer that's on the same network as the TrueNAS server (10.0.0.89):

```bash
# 1. Navigate to wherever you want the code
cd ~/Projects  # or wherever you prefer

# 2. Clone the repository (first time only)
git clone https://github.com/isndotbiz/HROC_Files.git
cd HROC_Files

# OR if you already have it, just pull latest changes
cd HROC_Files
git pull origin main

# 3. Deploy to TrueNAS server (server only, S3 already updated)
DEPLOY_S3=false ./deploy.sh
```

That's it! The script will automatically deploy to the TrueNAS server at 10.0.0.89.

---

## 📋 Detailed Steps

### First Time Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/isndotbiz/HROC_Files.git
   cd HROC_Files
   ```

2. **Ensure 1Password CLI is installed:**
   ```bash
   # On macOS
   brew install 1password-cli

   # Sign in to 1Password
   eval $(op signin)
   ```

3. **Set up SSH access to TrueNAS (if not already done):**
   ```bash
   # Copy your SSH key to the server
   ssh-copy-id root@10.0.0.89

   # Test connection
   ssh root@10.0.0.89 "echo 'SSH works!'"
   ```

### Every Time You Deploy

1. **Pull latest changes from GitHub:**
   ```bash
   cd HROC_Files
   git pull origin main
   ```

2. **Deploy to TrueNAS:**
   ```bash
   # Option A: Server only (recommended - S3 already updated by GitHub Actions)
   DEPLOY_S3=false ./deploy.sh

   # Option B: Everything (S3 + Server)
   ./deploy.sh

   # Option C: Test first (dry run)
   DRY_RUN=true DEPLOY_S3=false ./deploy.sh
   ```

---

## ⚙️ Deployment Options

### Server Only (Recommended)
Since GitHub Actions already updates S3, just deploy to the server:
```bash
DEPLOY_S3=false ./deploy.sh
```

### Everything (S3 + Server)
If you want to deploy both:
```bash
./deploy.sh
```

### Dry Run (Test Without Deploying)
To see what would happen without actually deploying:
```bash
DRY_RUN=true DEPLOY_S3=false ./deploy.sh
```

---

## 🔍 What the Script Does

When you run `DEPLOY_S3=false ./deploy.sh`, it will:

1. ✅ Retrieve credentials from 1Password (automatically)
2. ✅ Create backup on TrueNAS server
3. ✅ Sync website files to `/mnt/tank/websites/kusanagi/web/hrocinc.org/`
4. ✅ Set correct permissions (33:33, 755)
5. ✅ Verify deployment

---

## 📁 What Gets Deployed to TrueNAS

```
/mnt/tank/websites/kusanagi/web/hrocinc.org/
├── index.html
├── bri.html
├── jonathan.html
├── lilly.html
├── documents.html
├── styles.css
├── script.js
├── images/
├── generated_images/
├── pdfs/
└── (other supporting files)
```

**NOTE:** Large files (lora_models, lora_training, image-generator) are excluded from deployment.

---

## 🆘 Troubleshooting

### SSH Connection Failed
```bash
# Test if server is reachable
ping 10.0.0.89

# Test SSH access
ssh root@10.0.0.89 "echo 'Connection OK'"

# If SSH fails, copy your key again
ssh-copy-id root@10.0.0.89
```

### 1Password Authentication Issues
```bash
# Check if signed in
op whoami

# Sign in if needed
eval $(op signin)

# Or if 1Password desktop app is running, it should auto-authenticate
```

### Website Not Updating After Deployment
```bash
# Clear Cloudflare cache
./purge_cloudflare_cache.sh

# Or reload Nginx on server
ssh root@10.0.0.89 "docker exec kusanagi-nginx nginx -s reload"
```

---

## 🔗 Useful Links

- **GitHub Repository**: https://github.com/isndotbiz/HROC_Files
- **GitHub Actions (S3 deploys)**: https://github.com/isndotbiz/HROC_Files/actions
- **Website**: https://hrocinc.org
- **Full Deployment Docs**: See DEPLOYMENT_INSTRUCTIONS.md

---

## 💡 Workflow Summary

**Development Process:**
1. Make changes to website locally
2. Commit and push to GitHub
3. GitHub Actions automatically deploys to S3 ✅
4. Pull changes on local network computer
5. Run `DEPLOY_S3=false ./deploy.sh` to deploy to TrueNAS ✅

**Result:** Website is updated on both S3 (for assets) and TrueNAS (for serving)!
