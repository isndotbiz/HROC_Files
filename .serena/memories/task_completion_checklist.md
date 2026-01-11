# Task Completion Checklist

After completing any task on this project, follow this checklist:

## Code Changes
1. **Test locally** - Open HTML files in browser, verify changes
2. **Check accessibility** - Run Lighthouse audit if UI changed
3. **Verify mobile responsiveness** - Check on different screen sizes

## Before Committing
1. **Review changes** - `git status` and `git diff`
2. **Check .gitignore** - Ensure no sensitive files or generated content is staged
3. **Stage relevant files** - `git add <files>`
4. **Commit with descriptive message** - `git commit -m "Description"`

## Deployment (if website changed)
1. **Push to GitHub** - `git push origin main`
2. **Run deployment script** - `./deploy.sh` or `python3 sync_to_new_s3.py`
3. **Purge Cloudflare cache** - `./purge_cloudflare_cache.sh`
4. **Verify live site** - Visit https://hrocinc.org

## Documentation Updates
- Update relevant `.md` files if functionality changed
- Update `START_HERE.md` if setup process changed

## No Automated Testing
This project does not have automated tests. Manual verification is required.
