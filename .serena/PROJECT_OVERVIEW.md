# HROC Files - Project Overview

**Project:** HROC Inc (Healing Roots Outreach Center) Website & Systems
**Status:** Live on Wix (hroc.org)
**Type:** Non-profit organization website and documentation
**Location:** `/mnt/d/workspace/HROC_Files/`
**Last Updated:** 2026-02-01

---

## Purpose

HROC Inc is a 501(c)(3) non-profit organization providing addiction recovery and outreach services. This repository contains:
- Website content and assets
- Organizational documentation
- Legal and compliance documents
- Strategic planning materials
- Complete organizational history

---

## Quick Facts

**Organization Details:**
- **EIN:** 39-3295288
- **UBI:** 605 944 010
- **Address:** 2122 S 272ND ST APT B111, Kent, WA 98032
- **Phone:** (253) 881-7377
- **Website:** https://hroc.org (live on Wix)
- **Status:** Active 501(c)(3) non-profit

**Repository Stats:**
- **Size:** 736 MB
- **Git:** Separate repository with full history
- **Context:** `.serena/` for AI assistance
- **Documentation:** Extensive (100+ documents)

---

## Directory Structure

```
HROC_Files/
├── .serena/                    # Serena AI context
├── .git/                       # Git repository
├── .github/                    # GitHub workflows
├── CLAUDE.md                   # Claude quick reference
├── 00_START_HERE.md           # Main entry point
│
├── HROC_Enhanced_Website/     # Latest website version
├── HROC_Public/               # Public-facing content
├── HROC_Website_New/          # Redesign files
│
├── docs/                      # Documentation hub
│   ├── Codex/                # Codex AI agent system
│   ├── Strategic_Planning/   # Strategic plans
│   ├── Consolidation/        # System consolidation
│   └── [other categories]
│
└── pdfs/                      # Legal & compliance
    ├── Formation/            # Corporate documents
    ├── IRS/                  # Tax exemption
    ├── Policies/             # Organizational policies
    └── SPV/                  # SPV LLC documents
```

---

## Current Deployment

### Live Website (Wix)
- **URL:** https://hroc.org
- **Platform:** Wix (paid subscription)
- **Status:** Live and operational
- **Admin:** Access via Wix dashboard

### Known Issues
1. **Photo Consistency** - Alicia's photos need standardization
2. **Mobile Optimization** - Some pages need responsive fixes
3. **Content Updates** - Strategic plan updates pending

---

## Key Documents

### Strategic Planning
- `ARCHIVAL_PLAN_2025.md` - Long-term preservation strategy
- `CODEX_PHASE_3_HROC_HANDOFF.md` - System transition plan
- `COMPLETE_PACKAGE_SUMMARY.md` - Full organizational overview

### Legal & Compliance
- `pdfs/Formation/` - Articles of incorporation, bylaws
- `pdfs/IRS/` - 501(c)(3) determination letter
- `pdfs/Policies/` - All organizational policies
- `pdfs/SPV/` - SPV LLC (mobile outreach vehicle)

### Deployment
- `DEPLOYMENT_INSTRUCTIONS.md` - Wix deployment guide
- `DEPLOY_TO_TRUENAS_COMPLETE.md` - Infrastructure setup
- `DEPLOYMENT_STATUS_REPORT.md` - Current status

### Codex System
- `CODEX_SYSTEM_OVERVIEW.md` - AI agent architecture
- `CODEX_QUICK_START.md` - Getting started
- `CODEX_INVOCATION_EXAMPLES.md` - Usage examples

---

## Credentials & Access

**All credentials stored in 1Password:**
- Vault: `HROC Inc` or `TrueNAS Infrastructure`
- Wix admin credentials
- Domain registrar access
- SSH keys for infrastructure
- Database credentials (when applicable)

**Access via 1Password CLI:**
```bash
eval $(op signin)
op item list --vault "HROC Inc"
op item get "Wix Admin" --vault "HROC Inc"
```

**NEVER hardcode credentials** - Always use 1Password CLI retrieval.

---

## Development Workflow

### Making Changes to Website

1. **Edit on Wix:**
   - Log into Wix dashboard
   - Make changes in editor
   - Preview thoroughly
   - Publish when ready

2. **Update Repository:**
   - Export changes from Wix (if applicable)
   - Update local files
   - Commit to git:
   ```bash
   cd /mnt/d/workspace/HROC_Files
   git add .
   git commit -m "Description of changes"
   git push
   ```

3. **Document Changes:**
   - Update relevant markdown files
   - Add to CHANGELOG if significant
   - Update CLAUDE.md if structure changes

### Working with Documentation

1. **Adding New Documents:**
   - Place in appropriate `docs/` subdirectory
   - Add entry to `00_START_HERE.md` index
   - Commit to git with clear message

2. **Archiving Old Content:**
   - Move to appropriate archive location
   - Update indexes
   - Document reason for archival

---

## Git Workflow

### This is a Separate Git Repository
HROC_Files has its own git repository, separate from the main workspace.

```bash
# Status check
cd /mnt/d/workspace/HROC_Files
git status

# Commit changes
git add .
git commit -m "Update strategic planning docs"
git push

# View history
git log --oneline -10
```

### Branch Strategy
- **main** - Production-ready content
- Feature branches for major changes
- Tag releases for significant milestones

---

## Next Steps & Priorities

### High Priority
1. **Fix photo consistency** - Standardize Alicia's photos across site
2. **Update strategic plan** - Reflect 2026 priorities
3. **Mobile optimization** - Fix responsive design issues
4. **Content refresh** - Update outdated program information

### Medium Priority
1. **SEO optimization** - Improve search visibility
2. **Accessibility audit** - WCAG 2.1 AA compliance
3. **Performance optimization** - Page load times
4. **Analytics setup** - Track visitor engagement

### Future Considerations
1. **Platform migration?** - Evaluate Wix vs. custom site
2. **Donation integration** - Online giving platform
3. **Member portal** - Secure login for participants
4. **Newsletter system** - Email marketing integration

---

## Integration with Main Workspace

### How HROC Fits into D:\workspace

**HROC_Files is one of 3 major projects at workspace root:**
```
/mnt/d/workspace/
├── HROC_Files/              ← This project (non-profit website)
├── ISNBIZ_Files/            ← Company website
└── opportunity-research-bot/ ← AI opportunity system
```

**Shared Resources:**
- **Infrastructure:** Uses Xeon Gold server when needed
- **Credentials:** All in 1Password with other projects
- **Documentation:** Cross-referenced in `/docs/consolidation/`
- **Serena Context:** Workspace `.serena/` has cross-project info

**Independent Aspects:**
- Separate git repository
- Own domain and hosting
- Distinct organization (non-profit vs. for-profit)
- Different compliance requirements

---

## Compliance & Legal Notes

### 501(c)(3) Requirements
- **Annual Filing:** Form 990-N (e-Postcard) required
- **Public Disclosure:** Maintain transparency
- **Political Activity:** Prohibited
- **Lobbying:** Limited permitted activity

### Document Retention
- **Permanent:** Articles, bylaws, 501(c)(3) determination
- **7 Years:** Financial records, donor records
- **3 Years:** General correspondence

See `pdfs/Policies/Document_Retention_and_Destruction_Policy.pdf`

---

## Support & References

### Key Contacts
- **Founder/Director:** [Contact via 1Password]
- **Technical Support:** jdmal (repository maintainer)
- **Wix Support:** Via Wix dashboard

### External Resources
- **IRS Non-Profit:** https://www.irs.gov/charities-non-profits
- **WA Secretary of State:** https://www.sos.wa.gov/corps
- **Wix Support:** https://support.wix.com

### Internal Documentation
- `00_START_HERE.md` - Main navigation
- `CLAUDE.md` - Quick reference for AI assistance
- `.serena/` - This directory (Serena AI context)

---

## Performance Notes

### Running from Windows Filesystem (Current)
**Location:** `/mnt/d/workspace/HROC_Files/` (WSL mounting Windows drive)
**Performance:** Slower due to cross-filesystem operations
**Best for:** Documentation, light editing

### Running from Linux Filesystem (Recommended for Heavy Work)
**Location:** `/home/jdmal/workspace/HROC_Files/` (native ext4)
**Performance:** Much faster I/O
**Best for:** Large git operations, bulk file processing

**Migration Command:**
```bash
# Copy to Linux filesystem for better performance
rsync -av /mnt/d/workspace/HROC_Files/ /home/jdmal/workspace/HROC_Files/

# Work there for heavy operations
cd /home/jdmal/workspace/HROC_Files
```

---

**Maintained by:** jdmal + Serena AI
**Review schedule:** Update when significant changes occur
**Purpose:** Enable Serena to provide context-aware assistance for HROC project
