# DEPLOY TO TRUENAS - COMPLETE GUIDE

## 🎯 CRITICAL DEPLOYMENT INFO

Your HROC website is hosted on a **TrueNAS server at 10.0.0.89**

### Where Files Go:
```
/mnt/tank/encrypted/containers/hrocinc/web/
```

This folder is mounted as a Docker volume for the Nginx container that serves your website.

---

## 🔐 AUTHENTICATION CREDENTIALS

### SSH Access
```
Hostname: 10.0.0.89
Username: root
Port: 22
SSH Key: ~/.ssh/truenas_admin_10_0_0_89
Password Fallback: uppercut%$##
```

### Quick SSH Command:
```bash
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89
```

### If SSH Key Not Working:
```bash
# Use password authentication
ssh root@10.0.0.89
# When prompted for password, enter: uppercut%$##
```

---

## 📋 DEPLOYMENT STEPS (RECOMMENDED METHOD)

### Step 1: Deploy Files via SCP
```bash
# Copy entire HROC_Website_New folder to TrueNAS
scp -r -i ~/.ssh/truenas_admin_10_0_0_89 HROC_Website_New/* root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/

# Verify files transferred
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "ls -la /mnt/tank/encrypted/containers/hrocinc/web/"
```

### Step 2: Verify HTML Files
```bash
# Check if index.html is there
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "head -20 /mnt/tank/encrypted/containers/hrocinc/web/index.html"
```

### Step 3: Restart Docker Container
```bash
# Reload Nginx (no downtime)
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx nginx -s reload"

# Or restart container
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker restart hrocinc-nginx"
```

### Step 4: Verify Website Live
```bash
# Check Nginx is running
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker ps | grep hrocinc-nginx"

# Check for errors in logs
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker logs hrocinc-nginx"
```

---

## 🚀 QUICK ONE-LINER DEPLOYMENT

```bash
# Replace everything on TrueNAS and reload
scp -r -i ~/.ssh/truenas_admin_10_0_0_89 HROC_Website_New/* root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/ && \
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx nginx -s reload" && \
echo "✓ Deployment complete - Website updated!"
```

---

## 🐳 DOCKER CONTAINER INFO

### Container Details
```
Container Name: hrocinc-nginx
Image: nginx:latest
Port: 8081 (mapped to 443 on host via Nginx proxy)
Mount: /mnt/tank/encrypted/containers/hrocinc/web/ → /usr/share/nginx/html/
Status: Check with: docker ps | grep hrocinc-nginx
```

### Common Docker Commands
```bash
# SSH into TrueNAS first:
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89

# Then use these:

# View running containers
docker ps | grep hrocinc

# View container logs (real-time)
docker logs -f hrocinc-nginx

# Restart container
docker restart hrocinc-nginx

# Execute command in container
docker exec hrocinc-nginx ls /usr/share/nginx/html/

# Check container stats
docker stats hrocinc-nginx
```

---

## 📁 FILE STRUCTURE ON TRUENAS

After deployment, your files will be at:
```
/mnt/tank/encrypted/containers/hrocinc/web/
├── index.html          ← Main homepage
├── documents.html      ← Document library
├── bri.html           ← Bri's profile
├── lilly.html         ← Lilly's profile
├── jonathan.html      ← Jonathan's profile
├── styles.css         ← Main stylesheet
├── script.js          ← JavaScript
├── images/
│   └── generated/     ← Generated images
├── generated_images/  ← Additional generated images
│   ├── community_photos/
│   ├── hero_banners/
│   ├── service_icons/
│   ├── background_patterns/
│   └── informational_graphics/
└── pdfs/             ← PDF documents
    ├── Governance/
    ├── Policies/
    ├── IRS/
    ├── Financial_Plans/
    └── ...
```

---

## 🌐 PUBLIC WEBSITE ACCESS

After deployment, your site is accessible at:
- **Production:** https://hrocinc.org
- **Internal:** http://10.0.0.89:8081

### DNS & SSL
```
Domain: hrocinc.org
SSL: Handled by Cloudflare Tunnel
HTTPS: Yes (auto-renewed)
```

---

## ✅ POST-DEPLOYMENT CHECKLIST

After deploying, verify everything:

- [ ] SSH connection to 10.0.0.89 works
- [ ] Files copied to /mnt/tank/encrypted/containers/hrocinc/web/
- [ ] Docker container is running (docker ps shows hrocinc-nginx)
- [ ] https://hrocinc.org loads in browser
- [ ] Founder pages work (bri.html, lilly.html, jonathan.html)
- [ ] Images load from S3 CDN
- [ ] PDFs accessible from documents.html
- [ ] Email links functional
- [ ] Crisis hotline buttons work
- [ ] Mobile responsive
- [ ] No console errors (F12 → Console)

---

## 🔧 TROUBLESHOOTING

### Files Not Updating on Website
```bash
# Clear Docker cache and reload
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx rm -rf /var/cache/nginx/*"
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx nginx -s reload"

# Hard refresh in browser (Ctrl+Shift+R or Cmd+Shift+R)
```

### 404 Errors on Specific Pages
```bash
# Check file exists on TrueNAS
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "ls -la /mnt/tank/encrypted/containers/hrocinc/web/bri.html"

# Check Nginx error logs
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker logs hrocinc-nginx | grep error"
```

### Images Not Loading
```bash
# Verify S3 bucket is accessible
# Images should be at: https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/

# Check HTML references S3 URLs
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "grep -c 's3.us-west-2.amazonaws.com' /mnt/tank/encrypted/containers/hrocinc/web/index.html"

# Should return a number > 0
```

### Can't Connect via SSH
```bash
# Try password authentication instead
ssh root@10.0.0.89
# When prompted, enter: uppercut%$##

# Or copy your SSH key to TrueNAS
ssh-copy-id -i ~/.ssh/truenas_admin_10_0_0_89.pub root@10.0.0.89
```

---

## 📊 WEBSITE INFRASTRUCTURE

```
Browser Request
    ↓
Cloudflare Tunnel (DNS: hrocinc.org)
    ↓
TrueNAS Host (10.0.0.89) - Main Nginx on Port 443
    ↓
Proxy to http://127.0.0.1:8081
    ↓
Docker Container (hrocinc-nginx)
    ↓
Serves files from /mnt/tank/encrypted/containers/hrocinc/web/
    ↓
HTML references S3 CDN for images
    ↓
AWS S3 Bucket (hroc-outreach-assets-1765630540) serves images
```

---

## 🔐 SECURITY NOTES

- SSH key should be protected (chmod 600)
- Password should only be used as fallback
- Always use HTTPS (https://hrocinc.org)
- Never share credentials in version control
- TrueNAS is behind Cloudflare Tunnel for DDoS protection

---

## 💾 WHERE TO STORE THIS INFO

**Create a file in your local machine at:**
```
~/.hroc_deployment.conf
```

**With content:**
```
TRUENAS_HOST=10.0.0.89
TRUENAS_USER=root
TRUENAS_SSH_KEY=~/.ssh/truenas_admin_10_0_0_89
TRUENAS_PASSWORD=uppercut%$##
WEB_ROOT=/mnt/tank/encrypted/containers/hrocinc/web/
DOCKER_CONTAINER=hrocinc-nginx
```

Then reference it:
```bash
source ~/.hroc_deployment.conf
ssh -i $TRUENAS_SSH_KEY $TRUENAS_USER@$TRUENAS_HOST
```

---

## 🎯 NEXT STEPS

1. **Verify SSH Key Exists:**
   ```bash
   ls -la ~/.ssh/truenas_admin_10_0_0_89
   ```

2. **Deploy Files:**
   ```bash
   scp -r -i ~/.ssh/truenas_admin_10_0_0_89 HROC_Website_New/* root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/
   ```

3. **Reload Website:**
   ```bash
   ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx nginx -s reload"
   ```

4. **Test:**
   - Open https://hrocinc.org in browser
   - Verify all pages load
   - Check founder profiles work
   - Test mobile responsiveness

---

## 📞 QUICK REFERENCE

| Task | Command |
|------|---------|
| **SSH into TrueNAS** | `ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89` |
| **Copy files** | `scp -r -i ~/.ssh/truenas_admin_10_0_0_89 HROC_Website_New/* root@10.0.0.89:/mnt/tank/encrypted/containers/hrocinc/web/` |
| **Reload website** | `ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker exec hrocinc-nginx nginx -s reload"` |
| **Check docker** | `ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker ps \| grep hrocinc"` |
| **View logs** | `ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker logs hrocinc-nginx"` |
| **List files** | `ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "ls /mnt/tank/encrypted/containers/hrocinc/web/"` |

---

**Created:** December 15, 2025
**For:** HROC Website Deployment
**Status:** Ready to Deploy
