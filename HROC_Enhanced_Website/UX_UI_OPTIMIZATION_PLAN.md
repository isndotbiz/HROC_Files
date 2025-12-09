# HROC Website UX/UI Optimization Plan
**Mobile-First Harm Reduction Services | WCAG 2.1 AA Compliant**

---

## CRITICAL CONTEXT

**Current State:** Transparency hub focused on governance documents
**Target State:** Crisis-response harm reduction service website
**Primary Users:** People in crisis needing immediate harm reduction services
**Access Method:** 90%+ mobile, potentially under stress/intoxication
**Success Metrics:** Service requests, naloxone access, crisis intervention engagement

---

## 1. HOMEPAGE REDESIGN (CRISIS-FIRST)

### Hero Section (Above-the-Fold)
```
┌─────────────────────────────────────────┐
│ [LOGO] HEALING ROOTS OUTREACH COLLECTIVE│
│                                         │
│ ⚠️ IN CRISIS? NEED HELP NOW?           │
│                                         │
│ ┌─────────────────────────────────────┐│
│ │  📞 CALL NOW: (206) XXX-XXXX       ││
│ │     (24/7 Crisis Line)              ││
│ └─────────────────────────────────────┘│
│                                         │
│ ┌─────────────────────────────────────┐│
│ │  💬 TEXT FOR HELP                   ││
│ └─────────────────────────────────────┘│
│                                         │
│ 🏥 Get Free Naloxone  |  🚐 Mobile RV  │
└─────────────────────────────────────────┘
```

**Key Changes:**
- **Crisis banner:** Large, high-contrast emergency contact (min 44x44px touch target)
- **Direct action CTAs:** tel: and sms: links for one-tap contact
- **Remove:** Transparency hub language (move to /about page)
- **Visual hierarchy:** Crisis → Services → About (not governance-first)

### Critical Needs Banner (Sticky on Scroll)
```html
<div class="crisis-banner" role="alert" aria-live="polite">
  <a href="tel:+12065551234" class="crisis-cta">
    <span class="icon">📞</span>
    <span>Crisis Line: (206) 555-1234</span>
  </a>
  <a href="sms:+12065551234" class="crisis-cta">
    <span class="icon">💬</span>
    <span>Text Us</span>
  </a>
</div>
```

**Implementation:**
- `position: sticky; top: 0; z-index: 1000`
- High contrast: Dark background (#1e293b), white text (14.7:1 ratio)
- Min height: 64px (comfortable touch targets)

### Impact Metrics Placement
**Move to:** Secondary position (after services, before footer)
**Redesign:** Real-time service impact, not governance compliance

```
┌──────────────────────────────────────────────────┐
│ OUR IMPACT THIS MONTH                            │
│                                                  │
│ 🩹 247 Naloxone Kits  |  🚐 89 Mobile Visits    │
│ 🤝 156 Peer Sessions  |  ⚕️ 43 Wound Care       │
└──────────────────────────────────────────────────┘
```

### Donation CTA with Disclosure
**Location:** Footer (not hero)
**Language:** Required tax-exempt disclosure + transparency link

```html
<section class="donate-section">
  <h2>Support Our Work</h2>
  <p>Your donation helps us provide free harm reduction services.</p>

  <a href="/donate" class="btn-donate">Donate Now</a>

  <p class="legal-disclosure">
    Healing Roots Outreach Collective is a 501(c)(3) tax-exempt organization.
    EIN: 39-3295288. Contributions are tax-deductible to the extent permitted by law.
    <a href="/transparency">View our financial transparency reports</a>
  </p>
</section>
```

---

## 2. NAVIGATION STRUCTURE

### Main Navigation (Mobile-First)
**Hamburger Menu for Mobile (< 768px):**
```
☰  HROC                              📞 CALL
```

**Expanded Menu:**
```
┌─────────────────────────────────────┐
│ ✖ Close                             │
│                                     │
│ 🏠 Home                             │
│ 🏥 Services ▼                       │
│   → Naloxone Distribution           │
│   → Syringe Services                │
│   → Wound Care                      │
│   → Peer Support                    │
│   → Mobile RV Locations             │
│ 📍 Find Us                          │
│ ℹ️ About                            │
│ 💰 Donate                           │
│ 📄 Transparency                     │
│                                     │
│ ⚠️ CRISIS CONTACTS                 │
│ 📞 Call: (206) XXX-XXXX            │
│ 💬 Text: (206) XXX-XXXX            │
└─────────────────────────────────────┘
```

**Desktop Navigation (> 768px):**
```
[LOGO] Home | Services ▼ | Find Us | About | Donate    [📞 CRISIS LINE]
```

### Service Dropdown Organization
```html
<nav aria-label="Main navigation">
  <button aria-expanded="false" aria-controls="services-menu">
    Services
  </button>
  <ul id="services-menu" role="menu">
    <li role="menuitem"><a href="/services/naloxone">Naloxone (Narcan)</a></li>
    <li role="menuitem"><a href="/services/syringe">Syringe Exchange</a></li>
    <li role="menuitem"><a href="/services/wound-care">Wound Care</a></li>
    <li role="menuitem"><a href="/services/peer-support">Peer Support</a></li>
    <li role="menuitem"><a href="/services/cultural-wellness">Cultural Wellness</a></li>
  </ul>
</nav>
```

### Quick Action Buttons (Floating)
```css
.quick-actions {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 999;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.quick-action-btn {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font-size: 28px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
```

**Buttons:**
- 📞 Call (tel: link)
- 💬 Text (sms: link)
- 📍 Find RV location (geolocation-enabled)

---

## 3. MOBILE-FIRST DESIGN FEATURES

### One-Tap Calling/Texting
```html
<!-- Crisis line -->
<a href="tel:+12065551234" class="tel-link" aria-label="Call crisis line at 206-555-1234">
  <span class="icon" aria-hidden="true">📞</span>
  <span class="text">(206) 555-1234</span>
</a>

<!-- Text support -->
<a href="sms:+12065551234?&body=I%20need%20help" class="sms-link" aria-label="Text crisis line">
  <span class="icon" aria-hidden="true">💬</span>
  <span class="text">Text for Help</span>
</a>
```

**CSS for Touch Targets (WCAG 2.5.5):**
```css
.tel-link, .sms-link {
  min-width: 48px;   /* WCAG minimum */
  min-height: 48px;  /* iOS recommends 44px, Android 48px */
  padding: 16px 24px;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 18px;
  font-weight: 700;
}
```

### Location-Based Service Finder
```html
<section class="location-finder">
  <h2>Find Our Mobile RV</h2>
  <p>We serve King and Pierce Counties, Washington</p>

  <button id="find-nearest" class="btn-primary">
    📍 Find Nearest Location
  </button>

  <div id="location-results" role="region" aria-live="polite">
    <!-- Populated via geolocation API -->
  </div>

  <div id="schedule">
    <h3>This Week's Schedule</h3>
    <ul>
      <li><strong>Mon 2-6pm:</strong> Seattle - Pike & 3rd</li>
      <li><strong>Tue 10am-2pm:</strong> Tacoma - MLK Jr. Way</li>
      <li><strong>Wed 3-7pm:</strong> Kent - James St</li>
    </ul>
  </div>
</section>
```

**JavaScript Implementation:**
```javascript
document.getElementById('find-nearest').addEventListener('click', () => {
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      position => {
        const { latitude, longitude } = position.coords;
        findNearestLocation(latitude, longitude);
      },
      error => {
        // Fallback: show all locations with search
        showAllLocations();
      }
    );
  } else {
    showAllLocations();
  }
});
```

### Quick Naloxone Access
```html
<div class="naloxone-quickstart">
  <h2>🏥 Need Naloxone (Narcan)?</h2>
  <p>Free, no questions asked. Available immediately.</p>

  <div class="quick-access">
    <a href="tel:+12065551234" class="btn-emergency">
      📞 Call to Get Narcan Now
    </a>
    <a href="/locations" class="btn-secondary">
      📍 Pick Up Locations
    </a>
  </div>

  <details>
    <summary>What is Naloxone?</summary>
    <p>Naloxone (Narcan) reverses opioid overdoses. It's safe, easy to use, and saves lives.</p>
    <a href="/naloxone-training">Watch 2-min training video</a>
  </details>
</div>
```

### Form Simplification Strategies
**Service Request Form (Minimal Fields):**
```html
<form action="/request-service" method="post" class="service-form">
  <h2>Request Services</h2>

  <!-- Only essential fields -->
  <label for="name">Name (optional, or use initials)</label>
  <input type="text" id="name" name="name" autocomplete="name">

  <label for="contact">How to reach you</label>
  <input type="tel" id="contact" name="contact"
         placeholder="Phone or email"
         autocomplete="tel">

  <fieldset>
    <legend>What do you need? (check all)</legend>
    <label><input type="checkbox" name="service" value="naloxone"> Naloxone</label>
    <label><input type="checkbox" name="service" value="syringes"> Clean syringes</label>
    <label><input type="checkbox" name="service" value="wound-care"> Wound care</label>
    <label><input type="checkbox" name="service" value="peer-support"> Someone to talk to</label>
    <label><input type="checkbox" name="service" value="other"> Other</label>
  </fieldset>

  <label for="urgency">Urgency</label>
  <select id="urgency" name="urgency" required>
    <option value="emergency">Emergency - need help now</option>
    <option value="today">Today if possible</option>
    <option value="this-week">This week</option>
  </select>

  <button type="submit" class="btn-primary">Submit Request</button>
  <p class="privacy-note">Your information is confidential and never shared.</p>
</form>
```

**Key Principles:**
- Max 5-7 fields
- No required fields except urgency
- Clear privacy assurance
- Autofill attributes for faster completion
- Large form controls (min 16px font, 48px height)

---

## 4. PERFORMANCE OPTIMIZATION

### Target: <3 Second Load Time

#### Image Optimization
**Specific Techniques:**
```bash
# Convert to WebP format (60-80% smaller)
cwebp -q 85 hrocinc.png -o hrocinc.webp

# Generate responsive images
convert hrocinc.png -resize 320x hrocinc-320.webp
convert hrocinc.png -resize 768x hrocinc-768.webp
convert hrocinc.png -resize 1200x hrocinc-1200.webp
```

**HTML Implementation:**
```html
<picture>
  <source
    srcset="hrocinc-320.webp 320w,
            hrocinc-768.webp 768w,
            hrocinc-1200.webp 1200w"
    sizes="(max-width: 768px) 100vw, 50vw"
    type="image/webp">
  <img src="hrocinc.png" alt="HROC Logo" loading="lazy" width="120" height="120">
</picture>
```

**Current Issues:**
- Remove large PDF links from homepage
- Logo is 120px max - likely fine, but confirm <20KB
- Replace emoji with SVG icons for better performance

#### Code Optimization
**CSS Critical Path:**
```html
<!-- Inline critical CSS in <head> -->
<style>
  /* Critical above-the-fold styles */
  :root{--primary:#0066cc;--text:#1e293b;--bg:#fff}
  body{font:18px/1.6 Inter,sans-serif;margin:0}
  .crisis-banner{background:#1e293b;color:#fff;padding:1rem;position:sticky;top:0}
  .crisis-cta{display:inline-flex;gap:8px;color:#fff;padding:12px 24px;
              background:#b91c1c;border-radius:8px;min-height:48px}
  /* ... more critical styles ... */
</style>

<!-- Load full CSS asynchronously -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

**JavaScript Optimization:**
```html
<!-- Defer non-critical JavaScript -->
<script src="script.js" defer></script>

<!-- Remove Google Fonts render-blocking (current issue) -->
<!-- BEFORE: -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">

<!-- AFTER: -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
      rel="stylesheet" media="print" onload="this.media='all'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet"></noscript>
```

**Minification:**
```bash
# CSS minification
npx cssnano styles.css styles.min.css

# JavaScript minification
npx terser script.js -o script.min.js -c -m

# HTML minification
npx html-minifier --collapse-whitespace --remove-comments index.html -o index.min.html
```

#### Hosting Recommendations
- **CDN:** Cloudflare (free tier) for static assets
- **Compression:** Enable Brotli/gzip on server
- **Caching:** Set long cache headers for static assets
```apache
# .htaccess example
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

---

## 5. ACCESSIBILITY FEATURES (WCAG 2.1 AA)

### Compliance Checklist

#### ✅ Already Implemented (Keep)
- [x] Skip to main content link
- [x] Semantic HTML5 (header, nav, main, footer)
- [x] ARIA labels and roles
- [x] Focus indicators (3px outline, 2px offset)
- [x] Color contrast ratios (7.5:1 minimum)
- [x] Keyboard navigation support
- [x] Screen reader announcements (aria-live)
- [x] Reduced motion support

#### ⚠️ Needs Improvement

**1. Form Labels (WCAG 1.3.1, 3.3.2)**
```html
<!-- CURRENT (missing visible label): -->
<input type="search" placeholder="Search files..." aria-label="Search">

<!-- IMPROVED: -->
<label for="search">Search files:</label>
<input type="search" id="search" placeholder="e.g., bylaws, budget">
```

**2. Link Purpose (WCAG 2.4.4)**
```html
<!-- AVOID: -->
<a href="/services">Click here</a>

<!-- BETTER: -->
<a href="/services">View our harm reduction services</a>
```

**3. Error Identification (WCAG 3.3.1)**
```html
<form>
  <label for="phone">Phone number *</label>
  <input type="tel" id="phone" required aria-describedby="phone-error">
  <span id="phone-error" class="error" role="alert" hidden>
    Please enter a valid phone number
  </span>
</form>
```

**4. Touch Target Size (WCAG 2.5.5)**
```css
/* Current buttons are 48px+ ✓ */
/* Ensure all interactive elements meet minimum */
a, button, input[type="submit"], input[type="checkbox"], input[type="radio"] {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 16px; /* Adds to touch area */
}

/* Exception: inline text links can be smaller IF
   surrounded by whitespace/padding */
```

**5. Language Declaration (WCAG 3.1.1)**
```html
<!-- CURRENT: ✓ -->
<html lang="en">

<!-- ADD for multilingual content: -->
<p lang="es">Servicios disponibles en español</p>
```

### Screen Reader Optimization

**Announce Dynamic Content:**
```html
<!-- Location results -->
<div id="location-results" aria-live="polite" aria-atomic="true">
  <!-- Populated by JS - screen reader will announce changes -->
</div>

<!-- Form submission status -->
<div role="status" aria-live="polite" class="sr-only">
  Form submitted successfully. We'll contact you within 2 hours.
</div>
```

**Image Alt Text Best Practices:**
```html
<!-- Decorative images -->
<img src="divider.png" alt="" role="presentation">

<!-- Functional images -->
<a href="/naloxone">
  <img src="naloxone-icon.png" alt="Learn about naloxone distribution">
</a>

<!-- Complex images (charts) -->
<img src="impact-chart.png" alt="Bar chart showing 247 naloxone kits distributed, 89 mobile visits, 156 peer sessions">
<a href="impact-data.csv">Download chart data (CSV)</a>
```

**Heading Hierarchy:**
```html
<!-- CORRECT structure: -->
<h1>Healing Roots Outreach Collective</h1>
  <h2>Services</h2>
    <h3>Naloxone Distribution</h3>
    <h3>Syringe Services</h3>
  <h2>Locations</h2>

<!-- AVOID: -->
<h1>Healing Roots</h1>
<h3>Services</h3>  <!-- Skipped h2 -->
```

### Keyboard Navigation Enhancements

**Focus Management for Modals:**
```javascript
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  // Trap focus within modal
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstElement) {
        e.preventDefault();
        lastElement.focus();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        e.preventDefault();
        firstElement.focus();
      }
    }

    // Close on Escape
    if (e.key === 'Escape') {
      closeModal(modalId);
    }
  });

  modal.removeAttribute('hidden');
  firstElement.focus();
}
```

**Skip Navigation Links:**
```html
<!-- Add multiple skip links for complex pages -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<a href="#services" class="skip-link">Skip to services</a>
<a href="#contact" class="skip-link">Skip to contact</a>
```

---

## 6. CONVERSION OPTIMIZATION

### Service Request Flow Design

**Step 1: Entry Points (Multiple Pathways)**
```
┌─ Homepage Hero → "Get Services" CTA
├─ Crisis Banner → "I need help now"
├─ Services Page → Individual service CTAs
├─ Floating Action Button → Quick request
└─ Footer → "Request Services" link
```

**Step 2: Triage (Urgency-Based Routing)**
```html
<div class="urgency-triage">
  <h2>How soon do you need help?</h2>

  <a href="tel:+12065551234" class="urgency-btn emergency">
    <span class="icon">🚨</span>
    <strong>RIGHT NOW</strong>
    <span>Call our crisis line</span>
  </a>

  <a href="/request?urgency=today" class="urgency-btn urgent">
    <span class="icon">⚡</span>
    <strong>TODAY</strong>
    <span>Submit quick request</span>
  </a>

  <a href="/schedule" class="urgency-btn scheduled">
    <span class="icon">📅</span>
    <strong>THIS WEEK</strong>
    <span>Schedule a visit</span>
  </a>
</div>
```

**Step 3: Minimal Friction Form**
- Pre-filled urgency (based on step 2 selection)
- Optional name/contact (encourage but don't require)
- Checkbox services (visual, easy to scan)
- Large submit button
- Confirmation message with next steps

**Step 4: Confirmation & Next Steps**
```html
<div class="confirmation" role="alert">
  <h2>✅ Request Received</h2>
  <p><strong>We'll contact you within 2 hours</strong> at the number/email you provided.</p>

  <div class="next-steps">
    <h3>While you wait:</h3>
    <ul>
      <li>📍 <a href="/locations">Find our nearest location</a></li>
      <li>🏥 <a href="/naloxone">Learn about naloxone</a></li>
      <li>📞 Crisis? Call now: (206) 555-1234</li>
    </ul>
  </div>

  <p class="privacy">Your information is confidential. We never share your data.</p>
</div>
```

### Donation Flow Design

**Step 1: Context-Aware Donation Ask**
```html
<!-- After reading about services -->
<div class="donation-cta inline">
  <p>💙 Like what we do? <a href="/donate">Your donation helps us provide free services</a></p>
</div>

<!-- On transparency page -->
<div class="donation-cta impact">
  <h3>See Our Impact. Support Our Work.</h3>
  <p>100% of donations go directly to harm reduction services.</p>
  <a href="/donate" class="btn-primary">Donate Now</a>
</div>
```

**Step 2: Donation Page Design**
```html
<section class="donate-page">
  <h1>Support Life-Saving Harm Reduction</h1>

  <!-- Impact framing -->
  <div class="impact-grid">
    <div class="impact-item">
      <h3>$25</h3>
      <p>Provides 10 naloxone kits</p>
    </div>
    <div class="impact-item">
      <h3>$50</h3>
      <p>Supplies one mobile RV visit</p>
    </div>
    <div class="impact-item">
      <h3>$100</h3>
      <p>Funds peer support sessions for 5 people</p>
    </div>
  </div>

  <!-- Simple donation form -->
  <form action="/process-donation" method="post">
    <fieldset>
      <legend>Select amount:</legend>
      <label><input type="radio" name="amount" value="25"> $25</label>
      <label><input type="radio" name="amount" value="50"> $50</label>
      <label><input type="radio" name="amount" value="100"> $100</label>
      <label><input type="radio" name="amount" value="custom"> Custom amount</label>
    </fieldset>

    <label for="custom-amount">Custom amount ($)</label>
    <input type="number" id="custom-amount" name="custom-amount" min="1" disabled>

    <button type="submit" class="btn-primary">Donate Securely</button>
  </form>

  <!-- Legal disclosure -->
  <p class="legal-disclosure">
    Healing Roots Outreach Collective is a 501(c)(3) tax-exempt organization (EIN: 39-3295288).
    Your donation is tax-deductible to the extent permitted by law. You will receive a receipt via email.
  </p>

  <p><a href="/transparency">View our financial transparency reports</a></p>
</section>
```

**Step 3: Payment Processing**
- Use Stripe or PayPal (trusted, accessible)
- Mobile-optimized checkout
- Email receipt automatically
- Thank you page with social share options

### Crisis Intervention Pathways

**Pathway 1: Phone (Immediate)**
```
User clicks "📞 CALL NOW"
  ↓
tel: link triggers native dialer
  ↓
One tap to call
  ↓
Trained peer responder answers
```

**Pathway 2: Text (Asynchronous)**
```
User clicks "💬 TEXT"
  ↓
sms: link opens messaging app with pre-filled text
  ↓
User sends message
  ↓
Automated reply: "Thanks for reaching out. A peer responder will reply within 30 min."
  ↓
Human response with next steps
```

**Pathway 3: Web Form (Non-Critical)**
```
User navigates to /request-services
  ↓
Urgency triage (emergency → phone redirect)
  ↓
Fill minimal form
  ↓
Confirmation with estimated response time
  ↓
Email/text notification to staff
```

### Urgency Indicators

**Visual Design:**
```css
/* Emergency (red) */
.urgency-emergency {
  background: #b91c1c;
  color: white;
  border: 3px solid #7f1d1d;
  animation: pulse 2s infinite;
}

/* Urgent (orange) */
.urgency-urgent {
  background: #ea580c;
  color: white;
}

/* Scheduled (blue) */
.urgency-scheduled {
  background: #0066cc;
  color: white;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}
```

**Implementation:**
```html
<div class="service-card urgency-emergency">
  <span class="urgency-badge" role="status">🚨 Emergency</span>
  <h3>Overdose Response</h3>
  <p>If someone is overdosing, call 911 first, then us for naloxone support.</p>
  <a href="tel:911" class="btn-emergency">📞 Call 911</a>
  <a href="tel:+12065551234" class="btn-secondary">Then call us</a>
</div>
```

---

## 7. IMPLEMENTATION PRIORITY

### Phase 1: Critical (Week 1)
1. ✅ Add crisis banner with tel:/sms: links
2. ✅ Implement mobile hamburger menu
3. ✅ Create service request form (minimal)
4. ✅ Optimize images (WebP conversion)
5. ✅ Fix touch target sizes (<44px issues)

### Phase 2: High Priority (Week 2)
1. ✅ Build location finder with schedule
2. ✅ Add naloxone quick-access section
3. ✅ Implement floating action buttons
4. ✅ Create donation page with disclosure
5. ✅ Add urgency triage flow

### Phase 3: Enhancement (Week 3-4)
1. ✅ Integrate geolocation API
2. ✅ Build impact metrics dashboard
3. ✅ Add multilingual content (ES, Indigenous languages)
4. ✅ Implement analytics (privacy-respecting)
5. ✅ A/B test CTA placement

---

## 8. PERFORMANCE BUDGET

| Metric | Target | Current | Action |
|--------|--------|---------|--------|
| **Page Load** | <3s | Unknown | Measure with Lighthouse |
| **First Contentful Paint** | <1.5s | Unknown | Inline critical CSS |
| **Largest Contentful Paint** | <2.5s | Unknown | Optimize images, lazy load |
| **Total Page Size** | <500KB | ~50KB (good) | Maintain, add image optimization |
| **JavaScript** | <100KB | ~13KB (excellent) | Keep minimal |
| **CSS** | <50KB | ~19KB (excellent) | Keep minimal |
| **Images** | <200KB | Unknown | WebP, responsive images |

**Measurement:**
```bash
# Run Lighthouse audit
npx lighthouse https://hroc.com --output=html --output-path=./audit.html

# Check Core Web Vitals
npx web-vitals-cli https://hroc.com
```

---

## 9. ACCESSIBILITY TESTING CHECKLIST

### Automated Testing
```bash
# axe-core CLI
npx @axe-core/cli https://hroc.com --save audit.json

# Pa11y
npx pa11y https://hroc.com --runner axe --standard WCAG2AA

# WAVE API (requires key)
curl "https://wave.webaim.org/api/request?key=YOUR_KEY&url=https://hroc.com"
```

### Manual Testing

**Keyboard Navigation:**
- [ ] Tab through all interactive elements (logical order)
- [ ] Shift+Tab reverses tab order
- [ ] Enter/Space activates buttons/links
- [ ] Escape closes modals/menus
- [ ] Arrow keys navigate menus/radio groups

**Screen Reader Testing:**
- [ ] Test with NVDA (Windows, free)
- [ ] Test with VoiceOver (Mac/iOS, built-in)
- [ ] Test with TalkBack (Android, built-in)
- [ ] Verify all images have alt text
- [ ] Verify form labels are read correctly
- [ ] Verify landmarks are announced (header, nav, main, footer)

**Visual Testing:**
- [ ] Zoom to 200% (text remains readable, no overflow)
- [ ] Test with Windows High Contrast Mode
- [ ] Test with browser dark mode
- [ ] Verify color isn't only indicator (icons + text)
- [ ] Verify focus indicators are visible

**Mobile Testing:**
- [ ] Test on actual iOS device (not just simulator)
- [ ] Test on actual Android device
- [ ] Test tel: and sms: links work
- [ ] Test touch targets are 44x44px minimum
- [ ] Test with screen rotated (landscape mode)

---

## 10. QUICK WINS (Implement Today)

### 1. Add Crisis Banner (15 min)
```html
<!-- Add to top of <body>, before <header> -->
<div class="crisis-banner" role="banner">
  <a href="tel:+12065551234" class="crisis-cta">
    <span aria-hidden="true">📞</span> Crisis Line: (206) 555-1234
  </a>
  <a href="sms:+12065551234" class="crisis-cta">
    <span aria-hidden="true">💬</span> Text Us
  </a>
</div>
```

```css
/* Add to styles.css */
.crisis-banner {
  background: #1e293b;
  color: white;
  padding: 1rem;
  text-align: center;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.crisis-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #b91c1c;
  color: white;
  padding: 12px 24px;
  margin: 0 8px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 700;
  min-height: 48px;
  transition: background 0.2s;
}

.crisis-cta:hover, .crisis-cta:focus {
  background: #991b1b;
  outline: 3px solid white;
  outline-offset: 2px;
}
```

### 2. Fix Touch Targets (10 min)
```css
/* Add to styles.css */
@media (max-width: 768px) {
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

### 3. Optimize Fonts (5 min)
```html
<!-- Replace current font loading with async method -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap"
      rel="stylesheet" media="print" onload="this.media='all'">
<noscript>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</noscript>
```

### 4. Add Service Request Link to Hero (5 min)
```html
<!-- Add to hero-actions div -->
<a class="btn btn-primary" href="/request-services">
  <span role="img" aria-hidden="true">🏥</span>
  Request Services
</a>
```

### 5. Update Page Title/Description (2 min)
```html
<!-- Replace current meta -->
<title>Healing Roots Outreach Collective | Free Harm Reduction Services | King & Pierce Counties</title>
<meta name="description" content="Indigenous-led mobile harm reduction services. Free naloxone, syringe exchange, wound care, and peer support via RV. Serving King and Pierce Counties, WA.">
```

---

## NEXT STEPS

1. **Measure current performance:** Run Lighthouse audit to establish baseline
2. **Prioritize Phase 1 changes:** Crisis banner, mobile nav, service request form
3. **User testing:** Show prototype to 3-5 people from target audience
4. **Iterate based on feedback:** Adjust language, CTAs, flow
5. **Implement Phase 2:** Location finder, naloxone section, donation page
6. **Launch and monitor:** Track conversion rates, bounce rates, service requests

---

## APPENDIX: CODE SNIPPETS FILE REFERENCE

See `UX_UI_CODE_SNIPPETS.html` for complete HTML/CSS/JS implementations of:
- Mobile hamburger menu
- Service request form
- Location finder with geolocation
- Donation page
- Crisis intervention pathways
- Accessibility utilities

---

**Document Version:** 1.0
**Last Updated:** 2025-12-08
**Next Review:** After Phase 1 implementation (Week 2)
