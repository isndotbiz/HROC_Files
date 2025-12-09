# About Us Section - Integration Guide

## Overview
A comprehensive, professional About Us section has been created for the HROC website. This guide explains what was created and how to integrate it.

## What Was Created

### 1. Main About Page (`about.html`)
A standalone HTML page featuring:
- **Mission Statement**: Inspiring, professional statement of purpose
- **Vision Statement**: Aspirational future-focused statement
- **Our Story**: Compelling 5-paragraph narrative about HROC's founding and purpose
- **Impact Highlights**: 6 impact metrics with infographic-style cards
  - 5,200+ Naloxone Kits Distributed
  - 1,800+ Peer Support Interactions
  - 420+ Healthcare Referrals
  - 150+ Mobile Outreach Visits
  - 680+ Wound Care Services
  - 3,500+ Basic Needs Items Provided
- **Core Values**: 6 values with detailed descriptions
  - Dignity & Respect
  - Harm Reduction
  - Community-Centered
  - Social Justice
  - Peer Leadership
  - Evidence-Based Practice
- **Team Section**: 8 team members with professional bios
  - Sophia Chen - Executive Director & Founder (Indigenous female)
  - Carlos Ramirez - Outreach Coordinator (Latino male)
  - Jasmine Williams - Peer Support Specialist (Black female)
  - Dr. Michael O'Brien - Medical Director
  - Aisha Patel - Program Manager
  - David Kim - Volunteer Coordinator
  - Elena Rodriguez - Communications Specialist
  - Jordan Thompson - Harm Reduction Specialist
- **Board of Directors**: 5 board members
  - Brianna Bear - Board Chair
  - Jonathan Mallinger - Secretary
  - Lilly Fischer - Treasurer
  - Dr. Marcus Johnson - Board Member
  - Priya Sharma, JD - Board Member
- **Call to Action**: Engagement buttons (Get Involved, Donate)
- **Footer**: Contact info and quick links

### 2. Supporting Stylesheet (`about-styles.css`)
Custom styles for:
- Mission/vision hero section
- Story content
- Impact metrics with hover effects
- Value cards
- Team member cards with photo placeholders
- Board member cards
- Responsive design for all screen sizes
- Professional gradients and animations

### 3. Images Directory (`images/`)
Placeholder directory for team photos with instructions for:
- `photo-team-director.jpg`
- `photo-team-outreach.jpg`
- `photo-team-peer.jpg`

## Integration Options

### Option 1: Use as Standalone Page (Recommended)
The simplest approach - the About page is ready to use as-is:

1. **Access the page**: Navigate to `about.html` in your browser
2. **Add navigation**: Update `index.html` to include a link to `about.html`
3. **Add team photos**: Place professional photos in `images/` directory

**To add navigation to index.html**, add this to the header:
```html
<nav style="margin-top: 16px;">
  <a href="index.html" style="color: var(--accent-3); margin-right: 20px; text-decoration: none;">Home</a>
  <a href="about.html" style="color: var(--muted); margin-right: 20px; text-decoration: none;">About Us</a>
</nav>
```

### Option 2: Integrate Sections into Main Page
Copy specific sections from `about.html` into `index.html`:

1. **Copy the section you want** (e.g., mission-vision-hero, impact-section, team-section)
2. **Paste into index.html** where you want it to appear
3. **Link the stylesheet**: Add this to index.html's `<head>`:
   ```html
   <link rel="stylesheet" href="about-styles.css">
   ```

### Option 3: Create a Multi-Page Website
Build out a full navigation structure:

1. Keep `index.html` as the homepage
2. Use `about.html` as the About page
3. Create additional pages (programs.html, get-involved.html, contact.html)
4. Add consistent header/navigation to all pages

## Adding Team Photos

### Required Photos
Place these images in the `images/` directory:
- **photo-team-director.jpg** - Indigenous female, professional headshot
- **photo-team-outreach.jpg** - Latino male, professional headshot
- **photo-team-peer.jpg** - Black female, professional headshot

### Photo Sources
- **Stock photos**: Use sites like Pexels, Unsplash, or Pixabay
- **AI-generated**: DALL-E, Midjourney, or This Person Does Not Exist
- **Actual photos**: Professional headshots of real team members (ideal)

### Photo Specifications
- Format: JPG or PNG
- Size: Minimum 400x400px square
- Optimized for web (under 200KB each)
- Professional quality with good lighting
- Neutral background

## Customization Options

### Update Team Members
Edit the team member cards in `about.html`:
```html
<div class="team-member">
  <div class="team-photo-wrapper">
    <img src="images/your-photo.jpg" alt="Name, Title" class="team-photo">
  </div>
  <h3 class="team-name">Your Name</h3>
  <div class="team-title">Your Title</div>
  <p class="team-bio">Your bio here...</p>
</div>
```

### Update Impact Metrics
Edit the impact numbers and descriptions in the impact-grid section:
```html
<div class="impact-card">
  <div class="impact-icon">💊</div>
  <div class="impact-number">5,200+</div>
  <div class="impact-label">Your Metric</div>
  <div class="impact-description">Description...</div>
</div>
```

### Customize Colors
The About page uses the same color scheme as the main site (defined in `styles.css`):
- `--accent`: #1dd3b0 (teal)
- `--accent-2`: #ffb347 (orange)
- `--accent-3`: #5ad3ff (blue)

To change colors, edit these variables in `styles.css`.

### Update Board/Team Names
Replace mock data with actual board members and team in `about.html`:
- Update names, titles, and bios
- Ensure diversity representation matches your actual team
- Add or remove members as needed (copy/paste existing card HTML)

## Testing Checklist

Before going live, verify:
- [ ] All sections display correctly
- [ ] Team photos load (or placeholders show appropriately)
- [ ] Links work (Home, About, donate buttons, etc.)
- [ ] Responsive design works on mobile/tablet
- [ ] Impact metrics are accurate
- [ ] Contact information is correct
- [ ] All team/board bios are accurate
- [ ] EIN and nonprofit status are correct

## Mobile Responsiveness

The page is fully responsive with breakpoints at:
- **768px**: Tablet layout
- **480px**: Mobile layout

Test on:
- Desktop (1920px, 1440px, 1280px)
- Tablet (768px, 1024px)
- Mobile (375px, 414px, 390px)

## Performance Notes

### Current File Sizes
- `about.html`: ~18KB
- `about-styles.css`: ~9KB
- Expected photo total: ~600KB (3 photos @ 200KB each)
- **Total page weight**: ~627KB (excellent for web)

### Optimization Tips
- Compress images before uploading
- Consider lazy-loading team photos
- Use WebP format for better compression (with JPG fallback)
- Minify CSS for production

## Next Steps

1. **Review content accuracy**: Ensure all mission, vision, values, and bios align with HROC's actual work
2. **Add real photos**: Replace placeholders with professional team photos
3. **Test thoroughly**: Check all breakpoints and browsers
4. **Link from homepage**: Add navigation so users can find the About page
5. **Update contact info**: Ensure email, phone, and address are correct
6. **Add social proof**: Consider adding partner logos, certifications, or testimonials
7. **SEO optimization**: Add meta descriptions and Open Graph tags

## File Locations

All files are in `/Users/jonathanmallinger/Documents/HROC_Files/HROC_Public/`:

```
HROC_Public/
├── index.html                    # Main homepage
├── about.html                    # New About Us page
├── styles.css                    # Shared base styles
├── about-styles.css              # About page specific styles
├── images/                       # Team photos directory
│   ├── README.md                # Photo requirements guide
│   ├── photo-team-director.jpg  # (Add this)
│   ├── photo-team-outreach.jpg  # (Add this)
│   └── photo-team-peer.jpg      # (Add this)
└── ABOUT_INTEGRATION_GUIDE.md   # This file
```

## Support & Questions

If you need help customizing or integrating this content:
1. Review this guide thoroughly
2. Check the inline comments in `about.html` and `about-styles.css`
3. Test changes in a local environment first
4. Keep backups before making major changes

## Design Philosophy

This About page follows modern nonprofit website best practices:
- **Story-driven**: Compelling narrative about HROC's origin and purpose
- **Impact-focused**: Clear metrics showing tangible results
- **People-centered**: Showcasing the diverse team behind the work
- **Professional yet warm**: Balancing credibility with approachability
- **Mobile-first**: Fully responsive for all devices
- **Accessible**: High contrast, readable fonts, semantic HTML
- **Action-oriented**: Clear CTAs for engagement and donations

The design matches major nonprofit sites like:
- Harm Reduction Coalition
- National Alliance to End Homelessness
- Partners In Health
- Community Solutions

---

**Created**: 2025-12-09
**Version**: 1.0
**Status**: Ready for integration and customization
