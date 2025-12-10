# HROC Website Deployment Guide

## 🎯 Current Status

**Commit Ready to Deploy:**
```
Commit Hash: 7d6d4bfd1913e329494939e33ea3bc37d2e821cc
Message: Comprehensive website transformation: Founders showcase, 60+ images, enhanced design
Status: Created locally, ready to push
Website Size: 122 MB
```

---

## 📤 Step 1: Push to GitHub

Your commit is created and ready. Choose your preferred authentication method:

### **Option A: Using Personal Access Token (Recommended)**

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token" (classic)
3. Select scopes: `repo` (full control of private repositories)
4. Copy the token
5. Run these commands:

```bash
cd /Users/jonathanmallinger/Documents/HROC_Files

# Set Git to use the token
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Push with credentials
git push origin main
# When prompted for password, paste your Personal Access Token
```

### **Option B: Using GitHub CLI (If installed)**

```bash
brew install gh  # If not already installed
gh auth login    # Follow the prompts to authenticate
git push origin main
```

### **Option C: Using SSH with key registration**

1. Ensure your SSH key is registered on GitHub: https://github.com/settings/keys
2. Add the key to SSH agent:
```bash
ssh-add -K ~/.ssh/id_ed25519
```

3. Change remote to SSH:
```bash
git remote set-url origin git@github.com:isndotbiz/HROC_Files.git
git push origin main
```

### **Option D: Store credentials in git config (Simple)**

```bash
git config --global credential.helper store
git push origin main
# Enter your GitHub username and Personal Access Token (not password)
# This will be stored for future pushes
```

---

## 🚀 Step 2: Deploy to NAS Server (10.0.0.89)

### **Prerequisites:**
- SSH access to NAS server at 10.0.0.89
- SSH key registered on server, OR username/password for authentication
- Know the deployment path (typically `/var/www/hroc` or similar)

### **Deployment Method A: Using SCP (Secure Copy)**

```bash
# Navigate to the HROC_Files directory
cd /Users/jonathanmallinger/Documents/HROC_Files

# Copy the website files to the NAS server
# Replace 'user' with your actual username on the NAS server
scp -r HROC_Website_New/ user@10.0.0.89:/var/www/hroc/

# Or if using a specific port (e.g., 2222):
scp -P 2222 -r HROC_Website_New/ user@10.0.0.89:/var/www/hroc/
```

### **Deployment Method B: Using SSH & rsync (Faster for updates)**

```bash
# More efficient for syncing
rsync -avz --delete HROC_Website_New/ user@10.0.0.89:/var/www/hroc/

# With specific port:
rsync -avz -e "ssh -p 2222" --delete HROC_Website_New/ user@10.0.0.89:/var/www/hroc/
```

### **Deployment Method C: Direct SSH & tar (All-in-one)**

```bash
# Create tar archive and deploy in one command
cd /Users/jonathanmallinger/Documents/HROC_Files && \
tar czf - HROC_Website_New/ | ssh user@10.0.0.89 "cd /var/www && tar xzf -"
```

---

## 🔄 Step 3: Verify Deployment & Restart Services

Once files are deployed to the NAS server:

```bash
# SSH into the server
ssh user@10.0.0.89

# Verify files were deployed
ls -la /var/www/hroc/HROC_Website_New/

# Check file permissions (if needed)
sudo chown -R www-data:www-data /var/www/hroc/HROC_Website_New/
sudo chmod -R 755 /var/www/hroc/HROC_Website_New/

# Restart Nginx (if using Nginx)
sudo systemctl restart nginx

# Or restart Apache (if using Apache)
sudo systemctl restart apache2

# Verify the service is running
sudo systemctl status nginx
```

---

## 🌐 Step 4: Test the Live Website

### **Test Local Deployment:**
```bash
# Test on the NAS server directly
curl http://10.0.0.89:8081/HROC_Website_New/
```

### **Test via Cloudflare Tunnel:**
- Visit: https://hrocinc.org
- Check that all images are loading
- Test responsive design on mobile
- Verify founder section displays properly
- Test crisis buttons (call/text)

### **Quick Verification Checklist:**
- [ ] Founder portraits load correctly
- [ ] 60+ images display without 404 errors
- [ ] Navigation works smoothly
- [ ] Crisis banner visible at top
- [ ] Mobile menu works on phones
- [ ] Contact form loads
- [ ] Donation section accessible
- [ ] Page load time is acceptable

---

## 🔧 Troubleshooting

### **GitHub Push Issues**

**Problem:** "Device not configured"
- **Solution:** Use Personal Access Token instead of password

**Problem:** SSH key not recognized
- **Solution:** Run `ssh-add ~/.ssh/id_ed25519` before pushing

### **NAS Server Deployment Issues**

**Problem:** "Permission denied (publickey)"
- **Solution:**
  1. Verify SSH key is on NAS server: `ssh-copy-id user@10.0.0.89`
  2. Or use password authentication: `scp -r HROC_Website_New/ user@10.0.0.89:/var/www/hroc/`

**Problem:** "Cannot find /var/www/hroc"
- **Solution:**
  1. SSH into server and check web root: `ssh user@10.0.0.89`
  2. Find the correct path: `find / -name "www" -type d 2>/dev/null`
  3. Deploy to the correct path

**Problem:** Images not loading (404 errors)
- **Solution:**
  1. Verify files copied correctly: `ls /var/www/hroc/HROC_Website_New/generated_images/`
  2. Check file permissions: `sudo chmod -R 755 /var/www/hroc/`
  3. Check web server logs: `sudo tail -f /var/log/nginx/error.log`

### **Website Not Accessible at https://hrocinc.org**

- **Check Cloudflare Tunnel:** Is it running? `cloudflared tunnel status`
- **Check Nginx configuration:** `sudo nginx -t`
- **Verify DNS:** `nslookup hrocinc.org`
- **Check firewall:** Is port 8081 open? `sudo ufw status`

---

## 📋 Complete Deployment Checklist

### **GitHub Push**
- [ ] Commit created locally (✅ Done: 7d6d4bfd)
- [ ] GitHub credentials set up (Personal Access Token or SSH)
- [ ] Pushed to main branch: `git push origin main`
- [ ] Verified on GitHub: https://github.com/isndotbiz/HROC_Files/commits/main

### **NAS Server Deployment**
- [ ] SSH access to 10.0.0.89 configured
- [ ] Files copied to `/var/www/hroc/HROC_Website_New/`
- [ ] File permissions set correctly (755)
- [ ] Nginx/Apache restarted
- [ ] Service verification: `systemctl status nginx`

### **Live Website Verification**
- [ ] Tested locally: http://10.0.0.89:8081
- [ ] Tested live: https://hrocinc.org
- [ ] All images loading
- [ ] Founder section displays
- [ ] Mobile responsive working
- [ ] Crisis buttons functional
- [ ] Forms accessible

### **Post-Deployment**
- [ ] Monitor website traffic
- [ ] Check error logs: `sudo tail -f /var/log/nginx/error.log`
- [ ] Verify SSL certificate valid: `curl -vI https://hrocinc.org`
- [ ] Test on multiple browsers
- [ ] Test on mobile devices

---

## 📞 Quick Reference

**Repository:** https://github.com/isndotbiz/HROC_Files
**Website URL:** https://hrocinc.org
**NAS Server:** 10.0.0.89:8081
**Local Path:** /Users/jonathanmallinger/Documents/HROC_Files/HROC_Website_New/

**Commit Details:**
- Hash: 7d6d4bfd1913e329494939e33ea3bc37d2e821cc
- Message: Comprehensive website transformation: Founders showcase, 60+ images, enhanced design
- Files Changed: 2 (index.html, styles.css)
- Insertions: 681
- Deletions: 61

---

## ✅ Success Indicators

Your deployment is successful when:
1. ✅ Commit appears on GitHub main branch
2. ✅ Files deployed to NAS server
3. ✅ Website loads at https://hrocinc.org
4. ✅ All 60+ images visible without errors
5. ✅ Founder section displays properly
6. ✅ Mobile responsive design works
7. ✅ Crisis buttons functional
8. ✅ Page load time is fast (<3 seconds)

---

## 🎉 You're Ready!

All the hard work is done! The website transformation is complete. Now just follow the steps above to:
1. Push to GitHub
2. Deploy to NAS server
3. Go live at https://hrocinc.org

Your HROC website will be the most beautiful nonprofit site on the web! 🚀
