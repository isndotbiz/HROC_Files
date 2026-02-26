# CLAUDE.md - HROC Non-Profit Website

**Project:** Healing Roots Outreach Collective (HROC Inc)
**Location:** `D:/workspace/HROC_Files/` (Unix path: `/d/workspace/HROC_Files/`)
**Status:** Live on Netlify at hrocinc.org | Cloudflare CDN/DNS | S3 for images
**Last Updated:** 2026-02-25

---

## Quick Overview

HROC (Healing Roots Outreach Collective) is a 501(c)(3) nonprofit providing Indigenous-led mobile harm reduction services in King & Pierce Counties, WA. Live at https://hrocinc.org.

**Architecture:**
```
Browser → Cloudflare (DNS/CDN/SSL) → Netlify (HTML pages)
                                   → S3 (images, PDFs via direct URL)
```

**Technology:**
- Static HTML/CSS/JS site (no framework)
- Netlify hosting (Site ID: `f5c7828a-b18a-41c1-a8bc-c64e5beb13ba`, publish dir: `HROC_Website_New`)
- S3 bucket `hroc-website-20251230043930` (us-east-1) for images and PDFs
- Cloudflare zone `0da5d1116d7e40e8c77615ce8a757cd1`, SSL: Full mode
- GitHub Actions CI/CD (3-job pipeline: Netlify deploy + S3 sync + Playwright tests)

---

## Organization Details

- **EIN:** 39-3295288 | **UBI:** 605 944 010
- **Address:** 2122 S 272ND ST APT B111, Kent, WA 98032
- **Phone:** (253) 881-7377
- **GitHub:** https://github.com/isndotbiz/HROC_Files.git

**Founders:**
- **Bri** - Co-Founder & Executive Director
- **Lilly** - Co-Founder & Cultural Director
- **Jonathan** - Co-Founder & Operations Lead

**Mission:** Community support, lived experience first, Indigenous wisdom, collective power, authentic care.

---

## Directory Structure

```
HROC_Files/
├── CLAUDE.md                         # This file
├── .git/                             # Git repo (separate from workspace)
├── .github/workflows/deploy.yml      # CI/CD pipeline (3-job)
├── .serena/memories/                 # Serena AI context
├── netlify.toml                      # Netlify config (security headers, caching)
├── playwright.config.ts              # Playwright test config
├── package.json                      # npm: @playwright/test
├── tests/site-health.spec.ts         # 16 Playwright CI tests
│
├── HROC_Website_New/                 # PRIMARY WEBSITE (deployed to Netlify)
│   ├── index.html                    # Homepage (782 lines)
│   ├── styles.css                    # All styles (2945 lines)
│   ├── script.js                     # Vanilla JS (338 lines)
│   ├── bri.html / lilly.html / jonathan.html / documents.html
│   ├── images/founders/              # Founder portraits (NOT in git - S3 only)
│   ├── images/generated/             # AI service images
│   ├── generated_images/community_photos/
│   └── pdfs/                         # Public documents
│
├── HROC_Enhanced_Website/            # Older version (not deployed)
├── HROC_Public/                      # Older version (not deployed)
│
├── deploy.sh                         # Legacy NAS deployment (not primary)
├── purge_cloudflare_cache.sh         # Purge CF cache post-deploy
├── enable_cf_dev_mode.sh             # Toggle Cloudflare dev mode
├── sync_all_to_s3.py                 # Manual S3 sync utility
├── generate_founder_images.py        # AI image generation (fal.ai)
│
└── [80+ historical .md docs]         # Deployment history, status reports
```

---

## Current Status

- **Live Site:** https://hrocinc.org (Netlify primary)
- **DNS:** hrocinc.org A → 75.2.60.5 (Netlify LB), www CNAME → hrocinc.netlify.app
- **Git branch:** `main` is primary
- **TrueNAS (10.0.0.89):** No longer serving website - legacy infrastructure only

---

## Quick Start

```bash
cd /d/workspace/HROC_Files

# IMPORTANT: Unset stale Windows GITHUB_TOKEN before git operations
unset GITHUB_TOKEN

# Check status
git status
git log --oneline -10

# View website locally
cd HROC_Website_New
python3 -m http.server 8081
# Open http://localhost:8081
```

---

## Deployment

Deployment is **automatic** on push to `main` via GitHub Actions:

1. `deploy-netlify` - pushes HTML to Netlify
2. `sync-s3-assets` - syncs images/PDFs to S3
3. `site-health-check` - runs 16 Playwright tests after deploy

```bash
# To trigger deployment:
unset GITHUB_TOKEN
git add HROC_Website_New/
git commit -m "Description of changes"
git push origin main

# Post-deploy: purge Cloudflare cache
./purge_cloudflare_cache.sh
```

### S3 Sync - CRITICAL RULES

```bash
# Founder images: NO --delete (images are NOT in git, ~40MB total)
aws s3 sync HROC_Website_New/images/founders s3://hroc-website-20251230043930/images/founders \
  --content-type "image/webp" --cache-control "max-age=31536000"

# Other asset directories: OK to use --delete
aws s3 sync HROC_Website_New/images/generated s3://hroc-website-20251230043930/images/generated \
  --cache-control "max-age=31536000" --delete
aws s3 sync HROC_Website_New/pdfs s3://hroc-website-20251230043930/pdfs \
  --cache-control "max-age=31536000" --delete
```

---

## Testing

```bash
# Install dependencies (first time)
npm install
npx playwright install chromium

# Run Playwright tests
npm test

# Test against local server
SITE_URL=http://localhost:8081 npm test
```

16 tests across 6 describe blocks:
- Per page (5 pages): HTTP 200, no broken images, no console errors
- S3 Assets: HEAD-check all S3 image URLs for 200

---

## Key Technical Details

### Website Files
- **HTML:** Semantic HTML5, WCAG 2.2 AA accessibility
- **CSS:** Single `styles.css`, mobile-first, no framework
- **JS:** Vanilla JS in `script.js`
- **Images:** `.webp` format preferred, served from S3

### Netlify Config (`netlify.toml`)
- Publish dir: `HROC_Website_New`
- Security headers: X-Frame-Options DENY, XSS protection, CSP
- Cache headers: HTML 1h, CSS/JS 1d, webp/PDF 1yr immutable
- Clean URL redirect: `/index.html` → `/`

### GitHub Actions Secrets Required
- `NETLIFY_AUTH_TOKEN` - Netlify deploy token
- `NETLIFY_SITE_ID` - `f5c7828a-b18a-41c1-a8bc-c64e5beb13ba`
- `AWS_ACCESS_KEY_ID` - AWS credentials for S3 sync
- `AWS_SECRET_ACCESS_KEY` - AWS credentials for S3 sync

---

## Credentials (1Password)

All credentials stored in 1Password vaults ("True" vault and "Research" vault).
Service account token and FAL API key also in `D:/workspace/.env.local`.

```bash
# Sign in and access credentials
eval $(op signin)
op item list | grep -i hroc
op item get "Cloudflare" --vault "True"
```

**Common vault items:** AWS S3, Cloudflare, Netlify, FAL API Key, TrueNAS API Key

---

## Known Gotchas

1. **`GITHUB_TOKEN` Windows env var** - Stale PAT in Windows User env vars overrides `gh auth`. Always `unset GITHUB_TOKEN` before git/gh operations.
2. **Founder images not in git** - ~40MB total, stored directly in S3. Never add `--delete` to founder image sync in CI.
3. **TrueNAS web UI port** - Uses port **81** (not 80/443): `http://10.0.0.89:81`
4. **TrueNAS Tailscale** - TCP ports firewalled on Tailscale interface; use LAN IP `10.0.0.89`
5. **1Password service account** - Cannot write to "True" vault; credential updates must be done manually
6. **Cloudflare email-decode.min.js** - Returns 404 to curl but works in browsers (Cloudflare-injected, filtered in Playwright tests)

---

## Git Workflow

This is a **separate git repository** from the main workspace.

```bash
cd /d/workspace/HROC_Files

# Check remote
git remote -v  # origin = https://github.com/isndotbiz/HROC_Files.git

# Feature branch workflow
git checkout -b feature/description
# make changes...
git add HROC_Website_New/
git commit -m "feat: description"
unset GITHUB_TOKEN && git push origin feature/description
# Create PR on GitHub
```

---

## Serena AI Context

See `.serena/memories/` for:
- `project_overview.md` - Architecture, tech stack, key IDs
- `suggested_commands.md` - All common commands
- `task_checklist.md` - Open TODOs and deployment checklist
- `code_style_and_conventions.md` - Coding standards
- `credentials_and_tokens.md` - Credential reference (tokens/IDs, not plaintext secrets)
- `session_2026_02_21_netlify_migration.md` - Full session notes for Netlify migration

---

**Last Updated:** 2026-02-25
**Maintained By:** HROC Team + Jonathan Mallinger + Claude AI
**Status:** Active, live on Netlify
**Canonical Location:** `D:/workspace/HROC_Files/`
