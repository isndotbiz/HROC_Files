# Suggested Commands for HROC Files

## Deployment Commands

### Deploy to NAS Server
```bash
./deploy.sh
```
Interactive script that pushes to GitHub and deploys to NAS server via rsync.

### Sync to S3
```bash
python3 sync_to_new_s3.py
```
Uploads website assets to AWS S3 bucket.

### Purge Cloudflare Cache
```bash
./purge_cloudflare_cache.sh
```

### Enable Cloudflare Dev Mode
```bash
./enable_cf_dev_mode.sh
```

### Check Cloudflare DNS
```bash
./check_cloudflare_dns.sh
```

## Git Commands
```bash
# Check status
git status

# Stage and commit
git add -A
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

## File Operations (macOS/Darwin)
```bash
# List files
ls -la

# Find files
find . -name "*.html"

# Search in files
grep -r "pattern" .

# Copy with rsync
rsync -avz source/ destination/
```

## Python Environment
The project uses Python 3 with boto3 for AWS operations. No virtual environment is strictly required for deployment scripts.

```bash
# Run Python scripts
python3 script_name.py
```

## Website Testing
After deployment, verify at:
- https://hrocinc.org
- Check all pages: index.html, documents.html, bri.html, jonathan.html, lilly.html
