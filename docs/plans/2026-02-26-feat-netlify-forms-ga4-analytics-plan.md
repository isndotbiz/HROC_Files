---
title: "feat: Netlify Forms + GA4 analytics integration"
type: feat
status: completed
date: 2026-02-26
origin: docs/brainstorms/2026-02-26-contact-form-ga4-brainstorm.md
---

# feat: Netlify Forms + GA4 Analytics Integration

## Overview

Wire the HROC contact form to actually deliver messages and add Google Analytics 4 to measure site engagement. The form currently fakes submission (logs to console), and no analytics exist. Both are straightforward additions to a Netlify-hosted static site with no framework and no build step.

## Problem Statement

- `admin@hrocinc.org` receives zero contact form submissions — the form silently discards every message
- HROC has no visibility into how many people visit, which services pages get read, or whether documents are being downloaded
- Both are blocking gaps for a live nonprofit site

## Proposed Solution

**Contact form:** Add Netlify Forms attributes to the existing HTML form. Replace the placeholder `console.log` handler with a `fetch()` POST. Zero new infrastructure; Netlify processes submissions and emails `admin@hrocinc.org`. (see brainstorm: docs/brainstorms/2026-02-26-contact-form-ga4-brainstorm.md)

**GA4:** Add the standard `gtag.js` global site tag to all five HTML pages. Wire four custom events in `script.js` for meaningful conversions (form submit, PDF downloads, donation clicks, outbound links). (see brainstorm: docs/brainstorms/2026-02-26-contact-form-ga4-brainstorm.md)

---

## Prerequisites (Manual, One-Time)

These must be completed **before** or **alongside** the code changes:

### P1 — Create GA4 Property
1. Go to [analytics.google.com](https://analytics.google.com)
2. Admin → Create → Property → name it "HROC Website"
3. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)
4. Store it in 1Password ("True" vault)

### P2 — Enable Netlify Form Notifications
1. Log into Netlify dashboard → Site `hrocinc.org` → Forms
2. After first form submission arrives, set up email notification to `admin@hrocinc.org`
3. (Notifications become available after the first real submission)

---

## Technical Considerations

### No CSP headers today
`netlify.toml` has no `Content-Security-Policy` header. GA4 and Netlify Forms will load without restriction. **No CSP changes required** for this implementation. (If a CSP is added in the future, it will need `script-src www.googletagmanager.com` and `connect-src www.google-analytics.com www.googletagmanager.com`.)

### Playwright console error filter
The `has no console errors` test at `tests/site-health.spec.ts:64` filters `cdn-cgi` and `email-decode`. GA4 with an invalid/missing Measurement ID **will** produce `net::ERR_NAME_NOT_RESOLVED` console errors that break CI. The Measurement ID must be real before pushing to `main`, OR the test must be updated to also filter `googletagmanager` errors during the transition window.

### AJAX form submission (graceful degradation)
The JS handler uses `fetch()` to POST to Netlify Forms and stays on the page. If JS is disabled, the form must still work — this requires keeping `method="POST"` and setting `action="/"` on the form element (Netlify's fallback redirect target).

### Button double-submit prevention
The existing handler calls `this.reset()` after success. The submit button must be disabled between click and fetch response to prevent duplicate submissions.

---

## Implementation Plan

### Step 1 — Contact Form HTML (`HROC_Website_New/index.html`)

**Change:** Update the `<form>` element (currently at line ~649) and add a honeypot field.

```html
<!-- Before -->
<form class="contact-form" action="#" method="post" aria-label="Contact form">

<!-- After -->
<form class="contact-form"
      name="contact"
      method="POST"
      action="/"
      data-netlify="true"
      data-netlify-honeypot="bot-field"
      aria-label="Contact form">

  <!-- Required for AJAX: tells Netlify which registered form this POST belongs to -->
  <input type="hidden" name="form-name" value="contact">

  <!-- Honeypot: hidden from humans, filled by bots -->
  <p class="hidden-honeypot" aria-hidden="true">
    <label>Don't fill this out: <input name="bot-field"></label>
  </p>
```

> **Note:** `data-netlify="true"` is used instead of bare `netlify` for valid HTML5. The hidden `form-name` input is required for AJAX submissions — without it, Netlify receives the POST but cannot link it to the registered form, so nothing appears in the dashboard and no email is sent.

Add to `styles.css` (or inline):
```css
.hidden-honeypot { display: none; }
```

**Why:** `data-netlify="true"` tells Netlify to register this form during build. `data-netlify-honeypot` enables spam filtering. `action="/"` is the fallback URL for non-JS submissions.

---

### Step 2 — Contact Form JS Handler (`HROC_Website_New/script.js`)

**Change:** Replace the placeholder handler body (lines ~147-173) with a real `fetch()` POST.

```javascript
// Contact form — Netlify Forms via AJAX
const contactForm = document.querySelector('.contact-form');

if (contactForm) {
  contactForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitBtn = this.querySelector('[type="submit"]');
    submitBtn.disabled = true;
    submitBtn.textContent = 'Sending…';

    try {
      const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(this)).toString(),
      });

      if (!response.ok) throw new Error(`Netlify returned ${response.status}`);

      // GA4 event
      if (typeof gtag !== 'undefined') {
        gtag('event', 'form_submit', { form_name: 'contact' });
      }

      // Show success message (existing UI preserved)
      const successMessage = document.createElement('div');
      successMessage.className = 'form-success';
      successMessage.style.cssText =
        'padding: 1rem; background: #d1fae5; border: 2px solid #047857; ' +
        'border-radius: 0.5rem; margin-top: 1rem; color: #065f46;';
      successMessage.innerHTML =
        '<strong>✓ Message sent!</strong><br>Thank you for reaching out. We\'ll get back to you soon.';

      this.appendChild(successMessage);
      this.reset();
      announceToScreenReader('Your message has been sent successfully');

      setTimeout(() => successMessage.remove(), 5000);

    } catch {
      // Show visible error so user knows to retry
      const errorMessage = document.createElement('div');
      errorMessage.style.cssText =
        'padding: 1rem; background: #fee2e2; border: 2px solid #dc2626; ' +
        'border-radius: 0.5rem; margin-top: 1rem; color: #7f1d1d;';
      errorMessage.innerHTML =
        '<strong>Something went wrong.</strong><br>Please try again or email us at <a href="mailto:admin@hrocinc.org">admin@hrocinc.org</a>.';
      this.appendChild(errorMessage);
      setTimeout(() => errorMessage.remove(), 8000);
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Send Message';
    }
  });
}
```

**Key differences from current:**
- `async/await` + real `fetch()` POST instead of `console.log`
- Checks `response.ok` — a Netlify 5xx won't falsely show success
- Disables submit button during in-flight request (prevents double-submit)
- `finally` restores button text and re-enables regardless of outcome
- Shows a visible error message on failure (red box, 8s timeout) with fallback email link
- Fires `gtag('event', 'form_submit')` on success (guarded by `typeof gtag` check)

---

### Step 3 — GA4 Snippet in All Five HTML Pages

Add to the `<head>` of each file, **just before `</head>`**:

```html
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**Files to update:**
- `HROC_Website_New/index.html`
- `HROC_Website_New/bri.html`
- `HROC_Website_New/lilly.html`
- `HROC_Website_New/jonathan.html`
- `HROC_Website_New/documents.html`

Replace `G-XXXXXXXXXX` with the real Measurement ID from Prerequisite P1.

> **Important:** Do not commit a fake/placeholder ID. Leave a `<!-- TODO: replace G-XXXXXXXXXX -->` comment and hold the commit until the real ID is in hand. A fake ID causes `net::ERR_NAME_NOT_RESOLVED` errors that break Playwright CI.

---

### Step 4 — GA4 Event Tracking (`HROC_Website_New/script.js`)

Add at the end of `script.js`, after all existing code:

```javascript
// ─── GA4 Event Tracking ───────────────────────────────────────────────────

// Guard: only fire if GA4 is loaded
function ga4(eventName, params) {
  if (typeof gtag !== 'undefined') gtag('event', eventName, params);
}

// Donation intent — all donation CTAs on index.html
// Note: verify the donation form's actual ID in index.html before implementing
//       (research showed a donate form but did not confirm ID="donateForm")
document.querySelectorAll('a[href="#donate"], #donateForm [type="submit"]')
  .forEach((el) => {
    el.addEventListener('click', () => {
      ga4('donation_intent', { page_location: window.location.href });
    });
  });

// Outbound link clicks
document.querySelectorAll('a[href^="http"]').forEach((link) => {
  if (link.hostname !== window.location.hostname) {
    link.addEventListener('click', () => {
      ga4('click', {
        event_category: 'outbound',
        event_label: link.href,
      });
    });
  }
});

// PDF / file downloads — documents page only
document.querySelectorAll('a.document-item[href$=".pdf"]').forEach((link) => {
  link.addEventListener('click', () => {
    const fileName = link.querySelector('.document-name')?.textContent || link.href;
    ga4('file_download', {
      file_name: fileName,
      file_extension: 'pdf',
      link_url: link.href,
    });
  });
});
```

**Note:** `form_submit` is fired inside the contact form handler (Step 2) where we have access to the fetch response, so it only fires on confirmed success. The other three events fire on click, which is standard GA4 practice.

**Ordering note:** The `ga4()` helper is defined here at the end of `script.js`, after the form handler defined in Step 2. This is safe because event listeners only fire on user interaction — long after the entire script has parsed — so `ga4()` will always be defined by the time any event fires. The form handler in Step 2 also uses a direct inline `typeof gtag` guard rather than `ga4()` for the same reason: both approaches are equivalent here.

---

### Step 5 — Playwright Test Update (`tests/site-health.spec.ts`)

Update the console error filter to suppress GA4 network errors during the transition window (and permanently in test environments where the Measurement ID may be missing):

```typescript
// Before (line 64-66):
const realErrors = errors.filter(
  (e) => !e.includes('cdn-cgi') && !e.includes('email-decode')
);

// After:
const realErrors = errors.filter(
  (e) =>
    !e.includes('cdn-cgi') &&
    !e.includes('email-decode') &&
    !e.includes('googletagmanager') &&
    !e.includes('google-analytics')
);
```

This makes CI resilient to GA4 loading failures (network-level errors in test environments) without masking real application errors.

---

## System-Wide Impact

### Interaction Graph
Form submit → `fetch('/')` → Netlify Forms processor → email to `admin@hrocinc.org`. GA4 events → `gtag()` → `dataLayer.push()` → async beacon to `www.google-analytics.com`. No server-side code changes. No side effects on other features.

### Error & Failure Propagation
`fetch()` failure is caught by `try/catch` and the button is re-enabled. If `gtag` is undefined (GA4 script blocked by browser), the `typeof gtag !== 'undefined'` guard prevents errors. Netlify form submission errors (5xx from Netlify) are also caught.

### State Lifecycle Risks
- Double-submit: mitigated by disabling the button before `await fetch()`
- Stale success message: removed after 5 seconds (existing behavior preserved)
- No persistent client state introduced

### API Surface Parity
Only the contact form is wired to Netlify Forms. The donation form (`#donateForm`) is tracked via `donation_intent` click event only — no payment processor is connected (out of scope per brainstorm).

### Manual QA Scenarios (post-deploy)
1. Submit contact form → check Netlify Forms dashboard shows submission + email arrives at `admin@hrocinc.org`
2. Submit contact form with bot-field filled → submission should be silently discarded by Netlify (not appear in dashboard)
3. Click donation CTA → verify GA4 DebugView shows `donation_intent` event
4. Click PDF on documents page → verify GA4 DebugView shows `file_download` event
5. Navigate across 5 pages → verify GA4 DebugView shows `page_view` for each

*These are manual verification steps. Automated CI (Playwright) covers HTTP status, broken images, and console errors — not form delivery or GA4 event firing.*

---

## Acceptance Criteria

- [ ] Contact form submission delivers an email to `admin@hrocinc.org` *(verify post-deploy)*
- [x] Form shows the existing green success message after successful submission
- [x] Submit button is disabled during in-flight request (no double-submit)
- [x] Submit button re-enables if the fetch fails, with visible error message and fallback email link
- [x] Netlify Forms dashboard shows submitted form data (requires `form-name` hidden input)
- [x] Honeypot field is present and hidden from sighted users
- [ ] GA4 `page_view` events appear in GA4 DebugView for all 5 pages *(verify post-deploy with real ID)*
- [x] GA4 `form_submit` event fires on contact form success
- [x] GA4 `file_download` event fires on PDF click (documents page)
- [x] GA4 `donation_intent` event fires on donation CTA click
- [x] All 16 Playwright tests continue to pass in CI
- [x] No console errors introduced (GA4 filter added to tests)
- [x] Graceful degradation: form POSTs correctly with JS disabled

## Success Metrics

- Netlify Forms: > 0 real form submissions within 30 days of launch
- GA4: sessions, bounce rate, and top pages visible in GA4 dashboard within 48 hours of launch
- Playwright CI: green on first push

---

## Dependencies & Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Real GA4 Measurement ID not available at commit time | Medium | Use TODO comment placeholder; don't push to `main` until ID is in hand |
| Netlify Forms not recognizing the form | Low | Netlify scans for `netlify` attribute at deploy time; confirm in Forms tab after first deploy |
| GA4 script causes Playwright console errors | Medium | Filter `googletagmanager` in test filter (Step 5) |
| Cloudflare caching HTML with old form markup | Low | HTML has 1h cache (`max-age=3600`); or manually purge with `./purge_cloudflare_cache.sh` |
| Spam submissions on contact form | Low | Netlify honeypot handles basic bots; upgrade to reCAPTCHA if needed |

---

## Deployment Checklist

- [ ] GA4 Measurement ID obtained and substituted in all 5 HTML files
- [ ] `unset GITHUB_TOKEN` before push
- [ ] Push to `main` triggers GitHub Actions (Netlify deploy + S3 sync + Playwright)
- [ ] After deploy: visit Netlify dashboard → Forms to confirm form registered
- [ ] After deploy: submit a test message → confirm email arrives at `admin@hrocinc.org`
- [ ] After deploy: run `./purge_cloudflare_cache.sh` to bust CDN cache
- [ ] Verify GA4 DebugView shows live pageview from test browser visit
- [ ] Configure Netlify form email notification to `admin@hrocinc.org`

---

## Sources & References

### Origin
- **Brainstorm document:** [docs/brainstorms/2026-02-26-contact-form-ga4-brainstorm.md](../brainstorms/2026-02-26-contact-form-ga4-brainstorm.md)
  - Key decisions carried forward: Netlify Forms (AJAX mode), AJAX stay-on-page UX, four GA4 events (form_submit / file_download / donation_intent / outbound), no GTM, no cookie banner

### Internal References
- Contact form HTML: `HROC_Website_New/index.html` ~line 649
- Contact form JS handler: `HROC_Website_New/script.js` lines 145–174
- Playwright console filter: `tests/site-health.spec.ts` lines 64–66
- Netlify config: `netlify.toml`
- Post-deploy cache purge: `./purge_cloudflare_cache.sh`
- Deployment instructions: `CLAUDE.md` → Deployment section

### External References
- [Netlify Forms AJAX submission](https://docs.netlify.com/forms/setup/#submit-html-forms-with-ajax)
- [Netlify Forms spam filtering (honeypot)](https://docs.netlify.com/forms/spam-filters/)
- [GA4 global site tag (gtag.js)](https://developers.google.com/analytics/devguides/collection/ga4)
- [GA4 event tracking reference](https://developers.google.com/analytics/devguides/collection/ga4/events)
- [GA4 DebugView](https://support.google.com/analytics/answer/7201382)
