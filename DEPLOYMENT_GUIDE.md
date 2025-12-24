# HROC Website Deployment Guide

## 🚀 Deployment to hrocinc.org

### Pre-Deployment Checklist
- [ ] All changes committed to git
- [ ] Test site locally
- [ ] Verify all founder pages load correctly
- [ ] Check all links (PDF, external, internal)
- [ ] Test on mobile devices
- [ ] Crisis hotline buttons work (tel: & sms:)
- [ ] All images load properly

### Current Status
- ✅ All code changes committed
- ✅ Founder pages created (bri.html, lilly.html, jonathan.html)
- ✅ Email addresses integrated
- ✅ Links fixed and verified
- ✅ Ready for deployment

## 📋 Deployment Steps

### Option 1: Manual FTP/SFTP Upload
```bash
# Using SFTP:
sftp user@hrocinc.org
cd public_html
put -r HROC_Website_New/*
quit
```

### Option 2: Git-based Deployment
```bash
git push origin main
# Then on server: git pull origin main
```

### Option 3: Hosting Control Panel
1. Log into cPanel/Plesk
2. Go to File Manager
3. Upload HROC_Website_New folder
4. Set proper permissions (644 for files, 755 directories)

## 🔗 Critical Files

Must deploy these files:
- index.html (updated with founder links)
- bri.html (NEW)
- lilly.html (NEW)
- jonathan.html (NEW)
- documents.html (updated links)
- styles.css
- script.js
- images/ folder
- pdfs/ folder

## ✅ Post-Deployment Verification

Test these URLs:
- [ ] https://hrocinc.org/ - Homepage
- [ ] https://hrocinc.org/bri.html - Bri's page
- [ ] https://hrocinc.org/lilly.html - Lilly's page
- [ ] https://hrocinc.org/jonathan.html - Jonathan's page
- [ ] https://hrocinc.org/documents.html - Documents page

Test functionality:
- [ ] Founder cards clickable and link to profiles
- [ ] Email links work (copy to clipboard)
- [ ] Crisis hotline buttons functional
- [ ] All images load from S3 CDN
- [ ] PDF links accessible
- [ ] Mobile responsive (test on phone)

## 🔒 Security for Production

1. Ensure HTTPS enabled
2. Redirect http → https
3. Validate all form inputs
4. Set proper file permissions (644/755)

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| 404 errors | Check file paths (case-sensitive) |
| Images not loading | Images on S3 CDN, check browser console |
| CSS/JS not loading | Verify in root directory, hard refresh |
| Slow loading | Cache enabled? Check GTmetrix |

## 📞 Support Contacts

- Hosting Provider: Contact for SSH/FTP access
- Domain Registrar: For DNS changes
- AWS S3: For CDN/image issues

---

Created: December 15, 2025 | Status: Ready for Deployment
