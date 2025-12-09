# 🌐 HROC Enhanced Website - Deployment Guide

## 🎯 What This Is

A fully accessible (WCAG 2.2 Level AA compliant), visually engaging public transparency hub for Healing Roots Outreach Collective.

## ✨ Features

✅ **Accessibility First**
- WCAG 2.2 Level AA compliant
- Screen reader optimized with ARIA labels
- Full keyboard navigation
- Skip to main content link
- High contrast colors (4.5:1+ ratios)
- Visible focus indicators
- Responsive design
- Reduced motion support

✅ **Visual Design**
- Modern, professional aesthetic
- Emoji icons (used accessibly)
- Progress bars and visual metrics
- Interactive file library
- Smooth animations (with reduced motion fallback)

✅ **Content**
- Mission and values
- Document categories
- Searchable file library
- Compliance dashboard
- 30-60-90 day action plan
- Contact information

## 📁 Files Included

- `index.html` - Main website file
- `styles.css` - Accessible, responsive styles
- `script.js` - Interactive features with accessibility
- `README.md` - This file

## 🚀 Deployment Options

### Option 1: GitHub Pages (Free, Recommended)

**Steps:**
1. Create a GitHub account if you don't have one
2. Create a new repository named `hroc-website`
3. Upload these files to the repository
4. Go to Settings → Pages
5. Under "Source", select "main" branch
6. Click Save
7. Your site will be live at `https://[your-username].github.io/hroc-website/`

**To use custom domain (healingrootsoutreachcollective.org):**
1. In GitHub Pages settings, enter your custom domain
2. In your domain registrar (where you bought the domain):
   - Add a CNAME record pointing to `[your-username].github.io`
   - Or add A records pointing to GitHub's IPs

### Option 2: Netlify (Free, Easy)

**Steps:**
1. Create account at netlify.com
2. Drag and drop the entire `HROC_Enhanced_Website` folder
3. Site goes live immediately
4. Optional: Connect custom domain in site settings

### Option 3: Traditional Web Hosting

**Steps:**
1. Connect to your web host via FTP/SFTP
2. Upload all files to your public_html or www directory
3. Ensure file permissions are correct (644 for files, 755 for directories)
4. Access via your domain

## 🔧 Before Deployment - Update File Paths

**IMPORTANT:** The website references files from `../HROC_Public/`. You need to either:

**Option A: Upload HROC_Public folder alongside**
```
your-server/
├── HROC_Enhanced_Website/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── HROC_Public/
    ├── 00_Action_Plan/
    ├── 01_Governance/
    └── ...
```

**Option B: Update paths in index.html and script.js**

Replace all instances of:
- `../HROC_Public/` with `HROC_Public/`
- `../HROC_Public_Notion.zip` with `HROC_Public_Notion.zip`

## 🎨 Customization Tips

### Change Colors
Edit `styles.css` variables at the top:
```css
:root {
  --color-primary: #0066cc;  /* Your brand color */
  --color-secondary: #047857; /* Accent color */
}
```

### Add Your Logo
Replace the logo path in `index.html`:
```html
<img src="path/to/your/logo.png" alt="HROC logo">
```

### Update Contact Info
Edit the contact section in `index.html` with your actual information.

## ✅ Pre-Deployment Checklist

- [ ] Update file paths (if needed)
- [ ] Add your actual contact information
- [ ] Upload HROC_Public folder or update paths
- [ ] Test all download links work
- [ ] Verify logo displays correctly
- [ ] Run accessibility check (Lighthouse in Chrome DevTools)
- [ ] Test on mobile devices
- [ ] Test keyboard navigation (Tab through entire site)

## 🧪 Testing After Deployment

**Accessibility Tests:**
1. Run Lighthouse audit (Chrome DevTools → Lighthouse → Accessibility)
   - Target score: 95-100
2. Install axe DevTools extension and run scan
   - Target: 0 critical issues
3. Test with keyboard only (no mouse)
   - All features should be accessible
4. Test with screen reader (NVDA on Windows, VoiceOver on Mac)

**Functionality Tests:**
1. Search file library
2. Filter files by folder
3. Click download links
4. Navigate with keyboard (Tab key)
5. Test on mobile device
6. Test in different browsers (Chrome, Firefox, Safari, Edge)

## 📊 Monitoring & Maintenance

**Monthly:**
- Run accessibility audit
- Test all download links
- Update compliance progress bars
- Review and update action items

**Quarterly:**
- Update document library with new files
- Refresh compliance dashboard data
- Check for broken links

**Annually:**
- Review and update content
- Refresh colors/branding if needed
- Verify WCAG compliance with latest standards

## 🆘 Troubleshooting

**Problem: Files won't download**
- Check file paths are correct
- Verify HROC_Public folder is uploaded
- Check file permissions (should be 644)

**Problem: Site looks broken**
- Verify styles.css loaded (check browser console)
- Clear browser cache
- Check for JavaScript errors in console

**Problem: Low accessibility score**
- Run specific tool (axe, WAVE) to see issues
- Most common: missing alt text, low contrast
- Refer to Web Accessibility Checklist

## 📞 Support Resources

- **Web Accessibility:** https://webaim.org
- **GitHub Pages:** https://docs.github.com/pages
- **Netlify:** https://docs.netlify.com

## 📝 License & Attribution

This website was created for Healing Roots Outreach Collective.
Built with accessibility and compliance in mind.

**Tech Stack:**
- HTML5 (semantic, accessible)
- CSS3 (WCAG 2.2 compliant)
- Vanilla JavaScript (accessible, progressive enhancement)
- Google Fonts (Inter, Poppins)

---

**Questions?** Contact your board chair or technical lead.

**Last Updated:** December 2025
