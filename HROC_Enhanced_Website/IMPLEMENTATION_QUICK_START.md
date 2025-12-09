# HROC Website Redesign - Quick Start Guide

**Goal:** Transform transparency hub → Crisis-focused harm reduction service website
**Timeline:** 3-4 weeks (phased implementation)
**Focus:** Mobile-first, WCAG 2.1 AA compliant, <3s load time

---

## FILES CREATED

1. **UX_UI_OPTIMIZATION_PLAN.md** (29KB)
   - Complete strategy document
   - 10 sections covering all requirements
   - Performance targets and accessibility checklist
   - Implementation phases and priorities

2. **UX_UI_CODE_SNIPPETS.html** (36KB)
   - 6 ready-to-use code snippets
   - Copy-paste HTML/CSS/JavaScript
   - Crisis banner, mobile menu, forms, FABs
   - Performance and accessibility utilities

3. **This file** - Quick start reference

---

## CRITICAL CHANGES NEEDED

### Current State Issues
- ❌ Transparency hub focus (wrong audience)
- ❌ Governance documents prioritized over services
- ❌ No crisis contact above fold
- ❌ No mobile menu
- ❌ No service request form
- ❌ Render-blocking Google Fonts

### Target State (Crisis-Focused)
- ✅ Crisis banner sticky header (tel:/sms: links)
- ✅ Service delivery prioritized
- ✅ Mobile hamburger menu
- ✅ Minimal-friction service request form
- ✅ Floating action buttons (call/text/locate)
- ✅ Optimized performance (<3s load)

---

## PHASE 1: CRITICAL (WEEK 1) - DO THIS FIRST

### 1. Add Crisis Banner (15 min)
**File:** `index.html`
**Location:** Add immediately after `<body>` tag, before existing header

```html
<div class="crisis-banner" role="banner">
  <a href="tel:+12065551234" class="crisis-cta">
    📞 Crisis Line: (206) 555-1234
  </a>
  <a href="sms:+12065551234" class="crisis-cta">
    💬 Text Us
  </a>
</div>
```

**File:** `styles.css`
**Location:** Add to end of file

```css
.crisis-banner {
  background: #1e293b;
  color: white;
  padding: 1rem;
  text-align: center;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.crisis-cta {
  display: inline-flex;
  gap: 8px;
  background: #b91c1c;
  color: white;
  padding: 12px 24px;
  margin: 0 8px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 700;
  min-height: 48px;
}
```

### 2. Update Page Metadata (2 min)
**File:** `index.html`
**Replace:** Lines 7-8

```html
<meta name="description" content="Indigenous-led mobile harm reduction services. Free naloxone, syringe exchange, wound care, and peer support via RV. Serving King and Pierce Counties, WA.">
<title>Healing Roots Outreach Collective | Free Harm Reduction Services | King & Pierce Counties</title>
```

### 3. Add Service Request Link to Hero (5 min)
**File:** `index.html`
**Location:** Inside `.hero-actions` div (around line 57)

```html
<a class="btn btn-primary" href="/request-services">
  🏥 Request Services
</a>
```

### 4. Fix Google Fonts (Async Loading) (5 min)
**File:** `index.html`
**Replace:** Lines 9-11

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
      rel="stylesheet" media="print" onload="this.media='all'">
<noscript>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</noscript>
```

### 5. Add Mobile Touch Target Fixes (10 min)
**File:** `styles.css`
**Location:** Inside `@media (max-width: 768px)` block

```css
@media (max-width: 768px) {
  /* Existing styles... */

  /* NEW: Ensure touch targets are minimum 48px */
  .btn, a[href^="tel"], a[href^="sms"], button {
    min-height: 48px;
    min-width: 48px;
    padding: 14px 20px;
  }

  input, select, textarea {
    min-height: 48px;
    font-size: 16px; /* Prevents iOS zoom on focus */
  }
}
```

**Total Time:** ~37 minutes
**Impact:** Crisis accessibility, mobile usability, performance boost

---

## PHASE 2: HIGH PRIORITY (WEEK 2)

### 6. Create Service Request Page
**New File:** `request-services.html`
**Reference:** `UX_UI_CODE_SNIPPETS.html` → Snippet 3 (Service Request Form)
**Copy entire form HTML/CSS**

### 7. Implement Mobile Hamburger Menu
**Files:** `index.html`, `styles.css`, `script.js`
**Reference:** `UX_UI_CODE_SNIPPETS.html` → Snippet 2
**Replace:** Existing `.main-nav` section

### 8. Add Floating Action Buttons
**File:** `index.html` (before `</body>`)
**Reference:** `UX_UI_CODE_SNIPPETS.html` → Snippet 4

### 9. Optimize Images
**Action:** Convert logo and images to WebP format

```bash
# Install cwebp (on Mac with Homebrew)
brew install webp

# Convert images
cwebp -q 85 hrocinc.png -o hrocinc.webp
```

**Update HTML:**
```html
<picture>
  <source srcset="hrocinc.webp" type="image/webp">
  <img src="hrocinc.png" alt="HROC Logo" width="120" height="120">
</picture>
```

---

## PHASE 3: ENHANCEMENT (WEEK 3-4)

### 10. Create Services Landing Page
**New File:** `services.html`
**Content:**
- Hero: "Free, confidential harm reduction services"
- Service cards: Naloxone, Syringes, Wound Care, Peer Support
- Each card links to detail page
- CTA: "Request Services" prominent

### 11. Build Location Finder
**New File:** `locations.html`
**Features:**
- Weekly RV schedule (static for now)
- Interactive map (Google Maps embed or Mapbox)
- "Find Nearest Location" button (geolocation API)

### 12. Create Donation Page
**New File:** `donate.html`
**Reference:** `UX_UI_OPTIMIZATION_PLAN.md` → Section 6 (Donation Flow)
**Must include:** 501(c)(3) disclosure, EIN, tax-deductible language

### 13. Move Transparency Content
**Action:** Create separate section/page for governance docs
**New Structure:**
- `/` → Service delivery focus
- `/transparency` → Current governance hub content
- `/about` → Mission, values, team

---

## PERFORMANCE CHECKLIST

Run these after Phase 1 complete:

```bash
# Install Lighthouse CLI
npm install -g lighthouse

# Run audit
lighthouse http://localhost:8000 --view

# Target scores:
# Performance: 90+
# Accessibility: 95+
# Best Practices: 90+
# SEO: 90+
```

**Key Metrics:**
- First Contentful Paint: <1.5s
- Largest Contentful Paint: <2.5s
- Total Blocking Time: <300ms
- Cumulative Layout Shift: <0.1

---

## ACCESSIBILITY TESTING

### Automated
```bash
# Install axe CLI
npm install -g @axe-core/cli

# Run audit
axe http://localhost:8000 --save audit.json
```

### Manual Testing
1. **Keyboard Navigation**
   - Tab through all interactive elements
   - Verify logical focus order
   - Test Escape closes modals/menus

2. **Screen Reader**
   - Windows: Download NVDA (free)
   - Mac: Use built-in VoiceOver (Cmd+F5)
   - Test all pages, verify alt text and labels

3. **Mobile Device**
   - Test on actual iPhone and Android device
   - Verify tel: and sms: links work
   - Confirm touch targets are comfortable

4. **Visual**
   - Zoom to 200% (text should remain readable)
   - Test with browser dark mode
   - Verify focus indicators are visible

---

## MOBILE TESTING CHECKLIST

### iOS (Safari)
- [ ] Tel links trigger phone dialer
- [ ] SMS links open Messages app
- [ ] Touch targets are comfortable (not cramped)
- [ ] No horizontal scroll at any zoom level
- [ ] Forms don't trigger unwanted zoom (16px+ font size)
- [ ] Sticky crisis banner stays visible on scroll

### Android (Chrome)
- [ ] Tel links trigger phone dialer
- [ ] SMS links open messaging app
- [ ] Touch targets meet 48x48dp minimum
- [ ] Navigation menu slides smoothly
- [ ] No performance lag on mid-range devices

---

## TROUBLESHOOTING

### Issue: Crisis banner not sticky
**Fix:** Check z-index conflicts, ensure `position: sticky` is supported

### Issue: Mobile menu not appearing
**Fix:** Verify JavaScript loaded (`script.js`), check for errors in console

### Issue: Fonts loading slowly
**Fix:** Use system fonts temporarily, or implement font-display: swap

### Issue: Images too large
**Fix:** Run through WebP conversion, implement lazy loading

### Issue: Poor Lighthouse score
**Fix:**
1. Inline critical CSS
2. Defer non-critical JavaScript
3. Optimize images (WebP, proper sizing)
4. Remove render-blocking resources

---

## RESOURCES

### Documentation
- **Main Plan:** `UX_UI_OPTIMIZATION_PLAN.md`
- **Code Examples:** `UX_UI_CODE_SNIPPETS.html`
- **WCAG Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/

### Tools
- **Lighthouse:** https://developers.google.com/web/tools/lighthouse
- **axe DevTools:** https://www.deque.com/axe/devtools/
- **WebP Converter:** https://developers.google.com/speed/webp
- **NVDA Screen Reader:** https://www.nvaccess.org/download/

### Testing
- **Mobile Simulator:** Chrome DevTools (F12 → Toggle device toolbar)
- **Contrast Checker:** https://webaim.org/resources/contrastchecker/
- **Screen Reader Testing:** WebAIM Screen Reader Guide

---

## NEXT STEPS

1. ✅ **Complete Phase 1** (Week 1: Crisis banner, metadata, touch targets)
2. ✅ **Run initial Lighthouse audit** (Establish baseline)
3. ✅ **User test with 3-5 people** (Target audience: people who need services)
4. ✅ **Iterate based on feedback** (Adjust language, CTAs, flow)
5. ✅ **Complete Phase 2** (Week 2: Service form, mobile menu, FABs)
6. ✅ **Launch and monitor** (Track conversion rates, service requests)

---

## QUESTIONS?

Refer to the detailed plan for context:
- **Strategy & rationale:** `UX_UI_OPTIMIZATION_PLAN.md`
- **Implementation code:** `UX_UI_CODE_SNIPPETS.html`
- **Quick reference:** This file

---

**Version:** 1.0
**Last Updated:** 2025-12-08
**Next Review:** After Phase 1 completion (Week 2)
