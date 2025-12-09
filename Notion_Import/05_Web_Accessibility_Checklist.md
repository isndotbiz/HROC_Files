# ♿ Web Accessibility Checklist

> **Ensuring our website is accessible to all users, including people with disabilities.**

---

## 🎯 Why Accessibility Matters

- **1 in 4 adults** has a disability
- **Legal requirement:** ADA Title II/III compliance
- **Better for everyone:** Improved usability benefits all users
- **SEO boost:** Semantic HTML helps search engines
- **Mission alignment:** Reflects our values of inclusion and equity

**Standard:** WCAG 2.2 Level AA (current legal standard for 2025)

---

## ✅ Quick Accessibility Audit

**Use this checklist monthly to assess your website:**

### Visual Accessibility

- [ ] Text contrast: 4.5:1 for normal text, 3:1 for large text
- [ ] UI component contrast: 3:1 (buttons, form borders, icons)
- [ ] Don't use color alone to convey information
- [ ] Page supports 200% browser zoom without content loss
- [ ] Text is resizable without assistive technology
- [ ] Images have appropriate alt text (or alt="" if decorative)

**Test with:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

### Keyboard Navigation

- [ ] All interactive elements accessible via keyboard
- [ ] Tab order follows logical visual flow
- [ ] Visible focus indicators on all focusable elements (3:1 contrast, 2px thick)
- [ ] No keyboard traps (can always navigate away)
- [ ] "Skip to main content" link present and functional
- [ ] Modal dialogs can be closed with Esc key

**Test with:** Unplug your mouse, navigate entire site with Tab, Enter, Esc

---

### Content Structure

- [ ] Proper heading hierarchy (h1 → h2 → h3, no skipped levels)
- [ ] One main landmark per page (`<main>` element)
- [ ] Semantic HTML elements (`<nav>`, `<article>`, `<aside>`, etc.)
- [ ] Descriptive link text (not "click here" or "read more")
- [ ] Form labels associated with inputs
- [ ] Error messages clear and associated with fields
- [ ] Lists use `<ul>`, `<ol>`, or `<dl>` elements

**Test with:** Review HTML structure in browser dev tools

---

### Media Accessibility

- [ ] All meaningful images have alt text
- [ ] Decorative images have alt="" or are CSS backgrounds
- [ ] Complex images (charts, infographics) have long descriptions
- [ ] Videos have captions
- [ ] Audio content has transcripts
- [ ] No content flashes more than 3 times per second

**Test with:** Screen reader (NVDA, VoiceOver)

---

### Interaction & Forms

- [ ] Touch targets minimum 44x44 pixels
- [ ] Forms have clear labels for all inputs
- [ ] Required fields indicated (not just by color)
- [ ] Error prevention and clear error messages
- [ ] Success messages announced to screen readers
- [ ] Time limits have warnings and extensions
- [ ] No unexpected changes on focus or input

**Test with:** Mobile device, keyboard-only navigation

---

## 🔧 Common Issues & Fixes

### Issue 1: Low Color Contrast

**Problem:** Text is hard to read (fails 4.5:1 ratio)

**Fix:**
```css
/* Bad: Low contrast */
color: #999999; /* 2.8:1 on white */

/* Good: High contrast */
color: #4a5568; /* 9.7:1 on white */
```

**Colors that work well on white:**
- Navy: #001f3f (16.5:1)
- Dark gray: #2c3e50 (12.6:1)
- Teal: #008080 (4.6:1)

---

### Issue 2: Missing Alt Text

**Problem:** Images without alt text leave screen reader users confused

**Fix:**
```html
<!-- Bad: No alt text -->
<img src="logo.png">

<!-- Good: Descriptive alt text -->
<img src="logo.png" alt="Healing Roots Outreach Collective">

<!-- Good: Decorative image -->
<img src="divider.png" alt="" role="presentation">
```

**Guidelines:**
- Informative images: Describe what's in the image
- Functional images (links, buttons): Describe the function
- Decorative images: Use alt="" or CSS background
- Complex images: Provide long description

---

### Issue 3: Unclear Link Text

**Problem:** Links that say "click here" don't describe destination

**Fix:**
```html
<!-- Bad: Non-descriptive -->
<a href="/report.pdf">Click here</a> for our annual report.

<!-- Good: Descriptive -->
<a href="/report.pdf">Read our 2024 Annual Report</a>

<!-- Bad: Generic -->
<a href="/programs">Learn more</a>

<!-- Good: Specific -->
<a href="/programs">Explore our Healthcare Programs</a>
```

---

### Issue 4: No Visible Focus Indicator

**Problem:** Keyboard users can't see where they are on page

**Fix:**
```css
/* Bad: Focus outline removed */
:focus {
  outline: none; /* Never do this without replacement! */
}

/* Good: Clear focus indicator */
:focus-visible {
  outline: 3px solid #0066ff;
  outline-offset: 2px;
  border-radius: 2px;
}

/* Better: Consistent with brand */
a:focus-visible,
button:focus-visible {
  outline: 3px solid #0066cc; /* Your brand blue */
  outline-offset: 2px;
}
```

---

### Issue 5: Form Fields Without Labels

**Problem:** Screen readers can't identify what each field is for

**Fix:**
```html
<!-- Bad: No label association -->
<label>Name</label>
<input type="text" name="name">

<!-- Good: Proper label association -->
<label for="name">Name</label>
<input type="text" id="name" name="name" required aria-required="true">

<!-- Good: Includes hint -->
<label for="email">Email Address <span aria-label="required">*</span></label>
<input type="email" id="email" name="email"
       aria-describedby="email-hint" required>
<span id="email-hint">We'll never share your email</span>
```

---

## 📱 Testing Tools

### Automated Testing (Find ~40-60% of issues)

**Browser Extensions:**
1. **axe DevTools** - Most comprehensive, provides fix guidance
2. **WAVE** - Visual feedback overlay on page
3. **Lighthouse** - Built into Chrome DevTools

**Run monthly:**
- [ ] Run axe DevTools on homepage
- [ ] Run axe DevTools on key pages (about, donate, programs, contact)
- [ ] Run Lighthouse accessibility audit
- [ ] Review and fix all critical issues

---

### Manual Testing (Essential - catches remaining 40-60%)

**Keyboard Navigation (Weekly):**
- [ ] Unplug mouse
- [ ] Tab through entire homepage
- [ ] Tab through donation form
- [ ] Tab through contact form
- [ ] Verify all functionality works
- [ ] Check focus indicators visible

**Screen Reader (Monthly):**
- [ ] Test homepage with NVDA (Windows) or VoiceOver (Mac)
- [ ] Verify page title announced
- [ ] Navigate by headings
- [ ] Navigate by landmarks
- [ ] Fill out forms
- [ ] Listen to image descriptions

**Zoom Testing (Monthly):**
- [ ] Set browser zoom to 200%
- [ ] Verify no content cut off
- [ ] Verify all functionality works
- [ ] Check mobile responsiveness

**Color Contrast (Before publishing changes):**
- [ ] Test all new text colors with WebAIM Contrast Checker
- [ ] Ensure 4.5:1 for normal text, 3:1 for large text
- [ ] Test button and link colors

---

## 🎨 Accessible Design Guidelines

### Typography

**Font Size:**
- Minimum 16px (1rem) for body text
- Allow user to zoom to 200%

**Font Selection:**
- Sans-serif for body (Inter, Helvetica, Arial)
- Avoid script fonts for body text
- Use decorative fonts sparingly for headings only

**Spacing:**
- Line height: 1.5× font size
- Paragraph spacing: 2× font size
- Adequate letter and word spacing

**Example:**
```css
body {
  font-family: 'Inter', 'Helvetica', Arial, sans-serif;
  font-size: 1rem; /* 16px */
  line-height: 1.5;
  color: #2c3e50; /* Dark gray, 12.6:1 contrast */
}

h1, h2, h3 {
  line-height: 1.2;
  margin-bottom: 0.5em;
}

p {
  margin-bottom: 1.5em;
}
```

---

### Color Usage

**Do:**
- Use high-contrast color combinations
- Provide multiple visual cues (color + icon + text)
- Test for colorblindness (8% of men, 0.5% of women)

**Don't:**
- Rely on color alone to convey information
- Use red/green as only distinction
- Use low-contrast colors for text

**Example:**
```html
<!-- Bad: Color only -->
<p style="color: red;">Required field</p>

<!-- Good: Color + icon + text -->
<p style="color: #b91c1c;">
  <svg aria-hidden="true" role="img"><!-- error icon --></svg>
  <span class="sr-only">Error:</span> Required field
</p>
```

---

### Emojis & Icons

**Emojis:**
```html
<!-- Decorative emoji: hide from screen readers -->
<h2>
  <span role="img" aria-hidden="true">🏥</span>
  Healthcare Programs
</h2>

<!-- Meaningful emoji: provide label -->
<p>
  We've reached our goal!
  <span role="img" aria-label="celebration">🎉</span>
</p>
```

**Best practices:**
- Maximum 3 emojis per section
- Place at end of text when possible
- Always pair with descriptive text
- Don't replace words with emojis

**Icons:**
```html
<!-- Icon-only button needs aria-label -->
<button aria-label="Close menu">
  <svg aria-hidden="true"><!-- X icon --></svg>
</button>

<!-- Icon + text: hide icon -->
<button>
  <svg aria-hidden="true"><!-- Menu icon --></svg>
  <span>Menu</span>
</button>
```

---

## 📋 Monthly Maintenance Checklist

**Run these tests monthly:**

### Automated Tests (30 minutes)
- [ ] Run axe DevTools on all main pages
- [ ] Run WAVE on donation page
- [ ] Run Lighthouse on homepage
- [ ] Document any new issues
- [ ] Prioritize fixes (critical first)

### Manual Tests (1 hour)
- [ ] Keyboard navigation test (all pages)
- [ ] Focus indicator check
- [ ] Screen reader test (homepage + 1 other page)
- [ ] Zoom to 200% test
- [ ] Mobile responsive test

### Content Review (30 minutes)
- [ ] Check all new images have alt text
- [ ] Review new link text for clarity
- [ ] Verify headings in logical order
- [ ] Check form labels complete
- [ ] Test any new interactive elements

**Total time: ~2 hours/month**

**Log results in:** `/HROC_Public/Accessibility_Audits/[YYYY-MM]_Audit_Report.md`

---

## 🎯 Accessibility Score Goals

**Lighthouse Accessibility Score:**
- **Target:** 95-100
- **Minimum Acceptable:** 90
- **Current Score:** _____ (test monthly)

**axe DevTools:**
- **Target:** 0 critical issues, <3 moderate issues
- **Current:** _____ critical, _____ moderate

---

## 📚 Resources

### Testing Tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [WAVE](https://wave.webaim.org/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) (built into Chrome)

### Screen Readers
- [NVDA](https://www.nvaccess.org/) (Windows, free)
- VoiceOver (Mac/iOS, built-in - Cmd+F5 to activate)
- [JAWS](https://www.freedomscientific.com/products/software/jaws/) (Windows, paid)

### Learning
- [WebAIM](https://webaim.org/) - Comprehensive guides
- [A11Y Project](https://www.a11yproject.com/) - Accessibility checklist
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)

---

## 🚨 Red Flags

**If you see these, fix immediately:**

- 🔴 Color contrast failures on main text
- 🔴 No keyboard access to key functionality (donate button, forms)
- 🔴 Images without alt text in main content
- 🔴 Forms without labels
- 🔴 No focus indicators visible
- 🔴 Automatic playing video/audio
- 🔴 Content flashing rapidly

**These are critical accessibility barriers and may violate ADA.**

---

## ✅ Quick Wins

**Easy improvements you can make today:**

1. ✅ Add alt text to all images (15 minutes)
2. ✅ Increase font size to 16px minimum (5 minutes)
3. ✅ Add "skip to main content" link (10 minutes)
4. ✅ Check color contrast, darken low-contrast text (15 minutes)
5. ✅ Review link text, make descriptive (10 minutes)
6. ✅ Test keyboard navigation, add focus styles (20 minutes)

**Total time: ~75 minutes for significant accessibility improvement!**

---

## 📞 Get Help

**Questions about accessibility?**
- Review [WCAG 2.2 Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- Post in [A11Y Slack Community](https://web-a11y.slack.com/)
- Consult with web accessibility specialist

**Legal compliance questions?**
- Consult with attorney familiar with ADA web requirements

---

**Last Updated:** December 2025
**Next Review:** Monthly

**Make accessibility a habit, not an afterthought!**

