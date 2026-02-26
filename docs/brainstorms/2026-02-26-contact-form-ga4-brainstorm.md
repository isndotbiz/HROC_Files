# Brainstorm: Contact Form Backend + GA4 Analytics
**Date:** 2026-02-26
**Status:** Draft

---

## What We're Building

Two related features to make hrocinc.org functional beyond display:

1. **Contact form backend** — The form at `#contact` currently fakes submission (logs to console, shows a green message). We need real delivery to `admin@hrocinc.org` with spam protection.

2. **GA4 analytics** — No analytics exist today. We need pageview tracking plus four meaningful conversion events across the site.

---

## Why This Approach

### Contact Form → Netlify Forms (AJAX mode)

Netlify Forms is the obvious fit for a Netlify-hosted static site:

- **Zero infrastructure** — No backend, no API keys, no serverless function to maintain
- **Free tier** — 100 submissions/month (sufficient for a small nonprofit)
- **Built-in spam** — Netlify honeypot field; reCAPTCHA upgrade available if needed
- **Email notifications** — Configure in Netlify dashboard, sends to `admin@hrocinc.org`
- **AJAX submission** — Use `fetch()` to POST to Netlify so the user stays on page; the existing green success message (`form-success` div) is preserved with no UX change

This avoids the alternatives: third-party services add an external dependency for no benefit; a serverless function would require Resend/SendGrid API keys and more code to maintain.

### GA4 → gtag.js snippet in `<head>`

Standard Google Analytics 4 implementation on a static site:

- Add the global site tag (`gtag.js`) to all five HTML pages
- Wire custom events in `script.js` for the four tracked actions
- No GTM (overkill for a 5-page static site)
- No cookie consent banner initially — GA4 can run in basic mode; revisit if GDPR/CCPA concerns arise later

---

## Key Decisions

| Decision | Choice | Rationale |
|---|---|---|
| Form backend | Netlify Forms | Zero-infra, native Netlify integration |
| Form submission style | AJAX (fetch + existing success UI) | Stays on page, preserves current UX |
| Spam protection | Netlify honeypot | Free, zero config |
| Analytics platform | GA4 | Standard, free, good nonprofit dashboards |
| GA4 implementation | gtag.js in `<head>` | Simplest for a static site |
| GTM | No | 5-page static site doesn't need tag manager overhead |
| Cookie consent | Deferred | Basic GA4 is acceptable for now |

### Events to Track

| Event | Trigger | GA4 Event Name |
|---|---|---|
| Contact form submit | Successful Netlify fetch response | `form_submit` (built-in) |
| PDF downloads | Click on `.pdf` link on documents page | `file_download` (built-in) |
| Donation button clicks | Click on donation CTA buttons | `donation_intent` (custom) |
| Outbound link clicks | Click on external links (social, etc.) | `click` + `outbound_link` (custom) |

---

## Implementation Scope

### index.html changes
- Add `netlify`, `name="contact"`, `data-netlify-honeypot="bot-field"` to form
- Remove `action="#"` (or leave it; fetch overrides it)
- Add hidden honeypot input: `<input name="bot-field" type="hidden">`
- Add GA4 `<script>` tag in `<head>` for all 5 pages (index, bri, lilly, jonathan, documents)

### script.js changes
- Upgrade contact form handler: wrap existing logic in `fetch('/', { method: 'POST', body: new FormData(form) })`, keep success message on `.then()`
- Add outbound link click tracking
- Add donation button click tracking
- Add file download tracking (documents page)

### netlify.toml changes
- No changes expected (no build command needed for Netlify Forms)
- Verify CSP headers allow `www.googletagmanager.com` and `www.google-analytics.com`

### Manual prerequisite (one-time)
- Create GA4 property at analytics.google.com → get Measurement ID (`G-XXXXXXXXXX`)
- In Netlify dashboard: Forms → enable notifications → set email to `admin@hrocinc.org`

---

## Open Questions

*None — all key decisions resolved through dialogue.*

---

## Resolved Questions

| Question | Answer |
|---|---|
| Form backend approach? | Netlify Forms |
| Form UX on submit? | Stay on page, show existing success message (AJAX) |
| GA4 property exists? | No — needs to be created first |
| Which events to track? | Form submit, PDF downloads, donation clicks, outbound links |

---

## Out of Scope

- **Founder photo consolidation** — Mentioned in context but separate task; defer
- **Donation payment processing** — Donation form is a separate integration (Stripe, PayPal, etc.)
- **reCAPTCHA** — Netlify honeypot sufficient for now; upgrade only if spam becomes a problem
- **Cookie consent banner** — Deferred; revisit if GDPR/CCPA compliance is required
- **Playwright test updates** — Will be needed after implementation; include in plan

---

## Risks & Notes

- **CSP headers in netlify.toml** — Current `Content-Security-Policy` may block GA4 or Netlify form POSTs. Must audit and update `script-src` and `connect-src` directives.
- **GA4 placeholder** — If a fake `G-XXXXXXXXXX` ID is committed while waiting for the real one, GA4 will silently fail. Use a clear comment placeholder instead.
- **Playwright tests** — The 16 existing tests check for console errors and no broken resources. GA4 errors (network or console) could break CI if the measurement ID isn't valid. Use a test-environment guard if needed.
- **Form duplicate submissions** — Disable the submit button after first click to prevent accidental double-send.
