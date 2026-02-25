# Session 2026-02-21: Netlify Migration, S3 Curation, Credential Cleanup, Password Rotation, Playwright CI

## Summary
Complete migration of hrocinc.org from TrueNAS self-hosted to Netlify + S3 + Cloudflare, with full credential audit, password rotation, and Playwright CI tests.

---

## 1. Netlify Migration (from TrueNAS)

### What was done
- **Netlify** is now the primary host for the static HTML site
  - Site ID: `f5c7828a-b18a-41c1-a8bc-c64e5beb13ba`
  - Publish dir: `HROC_Website_New`
  - Created `netlify.toml` with security headers, caching, clean URLs
- **Cloudflare DNS** updated:
  - A record `hrocinc.org` → `75.2.60.5` (Netlify LB)
  - CNAME `www.hrocinc.org` → `hrocinc.netlify.app`
  - SSL mode: Full, Always Use HTTPS enabled
  - Zone ID: `0da5d1116d7e40e8c77615ce8a757cd1`
- **deploy.yml** rewritten with 3 parallel jobs:
  1. `deploy-netlify` - deploys HTML to Netlify
  2. `sync-s3-assets` - syncs images/PDFs to S3
  3. `site-health-check` - Playwright tests post-deploy (runs after jobs 1 & 2)

### Key files changed
- `.github/workflows/deploy.yml` - complete rewrite
- `netlify.toml` - new file
- `.gitignore` - added `.netlify`, `!.env.tpl`

---

## 2. S3 Curation

### Bucket: `hroc-website-20251230043930` (us-east-1)
- **Before:** 172 files (~50MB+), many unused
- **After curation:** reduced to ~77 referenced files (12.8 MiB)
- **Then re-expanded:** uploaded all 64 local founder images back after discovering HTML references them

### What was removed from S3
- HTML files from S3 root (served by Netlify now)
- Duplicate `founders/` and `generated/` top-level directories
- Unused community photos (04-15)
- Unused background patterns, hero banners, service icons
- Misc_Guides PDFs, markdown/JSON docs

### Critical lesson learned
- The `--delete` flag on `aws s3 sync` in CI **deleted founder images** because they aren't committed to git (too large, ~40MB)
- **Fix:** Removed `--delete` from the founder images sync step. Only `images/generated/`, `generated_images/community_photos/`, and `pdfs/` use `--delete`
- Founder images are managed via **direct S3 upload**, not git

### S3 bucket configuration
- ACLs disabled (bucket policy controls access)
- Public read via bucket policy (no `--acl public-read` needed on upload)
- Upload command: `aws s3 sync HROC_Website_New/images/founders/ s3://hroc-website-20251230043930/images/founders/ --content-type "image/webp"`

---

## 3. Credential Audit & Cleanup

### Files cleaned (commit `27e45ff`)
| File | What was hardcoded | Replaced with |
|------|-------------------|---------------|
| `fix_traefik_config.sh` | `sshpass -p 'uppercut%$##'` | 1Password SSH key lookup |
| `DEPLOY_TO_TRUENAS_COMPLETE.md` | 4x plaintext password references | 1Password CLI commands |
| `DEPLOYMENT_SUCCESSFUL.md` | 1x plaintext password reference | 1Password vault reference |
| `purge_cloudflare_cache.sh` | Hardcoded CF email + API key | `op item get "Cloudflare"` lookups |
| `enable_cf_dev_mode.sh` | Hardcoded CF email + API key + zone ID | `op item get` + dynamic API fetch |
| `upload_to_s3.py` | Hardcoded macOS path | `Path(__file__).resolve().parent` |

### Stale GITHUB_TOKEN env var
- Windows User env var `GITHUB_TOKEN` (stale PAT, now removed) was overriding `gh auth`
- Removed via PowerShell: `[System.Environment]::SetEnvironmentVariable('GITHUB_TOKEN', $null, 'User')`
- **Note:** This keeps coming back in shell sessions. Use `unset GITHUB_TOKEN && gh auth switch --user isndotbiz` before git push

---

## 4. TrueNAS Password Rotation

### Passwords rotated via TrueNAS REST API (`http://10.0.0.89:81/api/v2.0/`)
| Account | User ID | Old Password | New Password | Status |
|---------|---------|-------------|-------------|--------|
| `root` | 1 | `uppercut%$##` (exposed in git) | `VMZQlEe_%G4DcHRr1E2x#Zxq` | Changed (password_disabled=True for web) |
| `truenas_admin` | 70 | `Tigeruppercut1913!` | `!QBk*XBmi0h@tGRSbfhdn+It` | Changed & verified |

### 1Password items updated (manually by user)
- **"Truenas Password"** (vault: TrueNAS Infrastructure) → `credential` field updated
- **"TrueNAS API Key"** (vault: TrueNAS Infrastructure) → `password` field updated

### TrueNAS access notes
- **Web UI:** `http://10.0.0.89:81` (port 81, not 443/444)
- **API:** `http://10.0.0.89:81/api/v2.0/`
- **API key:** `1-MNpPD2UhWN6zHRuBwawPzKf6ijl4z4657E7mLT5MVC10ALjhvzBVEz6dkKVkrg1c` (still valid, not rotated)
- **SSH:** Port 22 open on LAN IP (10.0.0.89), no SSH key configured for this Windows machine
- **Tailscale IP:** `100.67.89.29` (NOT `100.83.75.4`), but TCP ports firewalled on Tailscale interface
- **TrueNAS version:** 25.10.1, hostname: `truenas`
- Password change API calls take ~60-90s (use long timeout)

---

## 5. Playwright CI Tests

### Test file: `tests/site-health.spec.ts`
16 tests across 6 describe blocks:
- **Per page (5 pages × 3 tests):** loads with HTTP 200, has no broken images (HTTP response codes), has no console errors
- **S3 Assets:** all S3 image URLs individually HEAD-checked for 200

### Configuration
- `playwright.config.ts` - chromium only, 60s timeout, 1 retry
- `package.json` - `@playwright/test ^1.50.0`
- CI job runs after both `deploy-netlify` and `sync-s3-assets` complete
- `SITE_URL=https://hrocinc.org` env var

### Key design decisions
- Broken images test uses HTTP response status codes only (not `naturalWidth`) to avoid false positives from lazy-loaded/off-screen images
- Console error filter excludes Cloudflare-injected `cdn-cgi`/`email-decode` script errors
- Page scroll triggers lazy loading before checking

---

## 6. 1Password Service Accounts

### Old service account (read-only)
- Integration ID: `LO5UEPHYMBGPNK7EJU7GM4GNVM`
- Token starts with: `ops_eyJzaWduSW5BZGRyZXNzIjoibXkuMXBhc3N3b3JkLmNvbSIs...` (salt: `XCbVodjnTW16GXsR18lZsc`)
- Permissions: Read-only on TrueNAS Infrastructure vault

### New service account (read TrueNAS, read+write Research)
- Integration ID: `SNY7B4L5OJDYZCK3O4RHY4HCMA`
- Token starts with: `ops_eyJzaWduSW5BZGRyZXNzIjoibXkuMXBhc3N3b3JkLmNvbSIs...` (salt: `ukEtO1gZcUyy-vg3YcfOPA`)
- Permissions: Read on TrueNAS Infrastructure, Read+Write on Research vault
- TrueNAS Infrastructure vault write access could not be enabled (1Password UI limitation)

---

## 7. Git Commits This Session

| Hash | Message |
|------|---------|
| `df471a2` | Switch hosting to Netlify primary with Cloudflare DNS and curate S3 |
| `27e45ff` | Remove all hardcoded credentials, use 1Password lookups |
| `9de618e` | Add Playwright CI tests and upload missing S3 founder images |
| `a703fbc` | Fix S3 sync: remove --delete from founder images |

---

## 8. Current Architecture

```
Browser → Cloudflare (DNS/CDN/SSL) → Netlify (HTML pages)
                                   → S3 (images, PDFs via direct URL)
```

- **HTML:** Netlify (atomic deploys from git)
- **Images:** S3 bucket `hroc-website-20251230043930` (us-east-1)
- **PDFs:** Same S3 bucket under `pdfs/` prefix
- **DNS/SSL:** Cloudflare (Full SSL mode)
- **CI:** GitHub Actions → Netlify deploy + S3 sync + Playwright health check
- **TrueNAS:** No longer serving the website (was the old host)

---

## 9. Known Issues / Gotchas

1. **GITHUB_TOKEN env var** keeps reappearing - always `unset GITHUB_TOKEN` before git operations
2. **Founder images not in git** - they're uploaded directly to S3 (~40MB total). CI must NOT use `--delete` for founder sync
3. **1Password service account** cannot write to TrueNAS Infrastructure vault - password updates must be done manually
4. **TrueNAS Tailscale** TCP ports are firewalled - use LAN IP `10.0.0.89` for API/SSH access
5. **TrueNAS web UI** is on port **81** (not standard 443/444)
6. **Cloudflare email-decode.min.js** returns 404 to curl but works in browsers (Cloudflare-injected, filtered in tests)

---

## 10. Pages & Image Counts

| Page | Images | Status |
|------|--------|--------|
| Homepage (`/`) | 16 | All 200 |
| Bri (`/bri`) | 6 | All 200 |
| Lilly (`/lilly`) | 6 | All 200 |
| Jonathan (`/jonathan`) | 5 | All 200 |
| Documents (`/documents`) | 0 | 200 |
| **Total unique images** | **33** | **All 200** |
