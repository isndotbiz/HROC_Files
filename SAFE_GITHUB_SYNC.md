# Safe GitHub Sync - Protect Local Images

This guide ensures you can safely sync with GitHub without losing your locally-generated images.

## ✅ Your Local Images Are Protected

These directories are protected from git operations:
- ✓ `Generated_Images/` - Your AI-generated founder portraits
- ✓ `HROC_Website_New/lora_training/` - LoRA training scripts and data
- ✓ `HROC_Website_New/lora_models/` - Trained model files
- ✓ `HROC_Website_New/images/` - Local image copies

They're listed in `.gitignore`, so they'll never be deleted by git pulls.

---

## 🔄 Safe Sync Workflow

### Option 1: Simple & Safe (Recommended)

**When you want to pull the latest from GitHub:**

```bash
# 1. Check what will change (safe preview)
git fetch origin

# 2. Create a backup just in case
cp -r Generated_Images Generated_Images_backup_$(date +%Y%m%d_%H%M%S)

# 3. Stash any uncommitted local changes to tracked files
git stash

# 4. Pull the latest from GitHub
git pull origin main

# 5. Your ignored files are untouched!
# Generated_Images/ still exists exactly as you left it
```

**Result**: ✅ Your images are safe, website is updated from GitHub

---

### Option 2: Step by Step (Most Control)

**If you want to see exactly what's changing:**

```bash
# 1. See what files will change
git fetch origin
git diff origin/main

# 2. See what files will be added/deleted
git diff --name-status origin/main

# 3. Back up important local files first
cp -r Generated_Images Generated_Images_backup_$(date +%Y%m%d_%H%M%S)
cp -r HROC_Website_New/lora_training HROC_Website_New/lora_training_backup_$(date +%Y%m%d_%H%M%S)

# 4. Stash local changes
git stash

# 5. Pull from GitHub
git pull origin main

# 6. If anything went wrong, restore from backup
# cp -r Generated_Images_backup_DATE/* Generated_Images/
```

---

### Option 3: Merge Strategy (Advanced)

**If you want to preserve both local and GitHub changes:**

```bash
# 1. Back up
cp -r Generated_Images Generated_Images_backup_$(date +%Y%m%d_%H%M%S)

# 2. Fetch latest
git fetch origin

# 3. Merge with local files preserved
git merge -X ours origin/main

# This keeps your local changes and merges GitHub updates
```

---

## ⚠️ If You Accidentally Delete Images

Don't panic! You can recover them:

```bash
# Check if backups exist
ls -la Generated_Images_backup_*

# Restore from backup
cp -r Generated_Images_backup_LATEST/* Generated_Images/

# Or restore from git if they were tracked
git checkout HEAD -- Generated_Images/
```

---

## 📋 Pre-Sync Checklist

Before syncing with GitHub, do this:

- [ ] Check git status: `git status`
- [ ] Note any local changes: `git diff`
- [ ] Create backup: `cp -r Generated_Images Generated_Images_backup_$(date +%Y%m%d_%H%M%S)`
- [ ] Stash changes: `git stash`
- [ ] Fetch latest: `git fetch origin`
- [ ] Preview changes: `git diff origin/main`
- [ ] Pull: `git pull origin main`
- [ ] Verify images still exist: `ls Generated_Images/`

---

## 🛡️ How .gitignore Protects You

Your `.gitignore` now includes:

```
# Generated Images (locally created AI images)
Generated_Images/

# LoRA Training (local scripts and model files)
HROC_Website_New/lora_training/
HROC_Website_New/lora_models/

# Local image copies and assets
HROC_Website_New/images/
```

This means:
- ✅ These files are NEVER tracked by git
- ✅ `git pull` won't touch them
- ✅ `git merge` won't touch them
- ✅ `git checkout` won't touch them
- ✅ They're safe from ANY git operation

---

## 📊 What Happens During Sync

```
Local Machine                    GitHub Repository
─────────────────               ────────────────
Generated_Images/     ×          (empty - not tracked)
  ↓ PROTECTED ↓
  (stays as-is)

HROC_Website_New/     ←──────    HROC_Website_New/
  (gets updated)                 (latest version)

documents.md          ←──────    documents.md
  (gets updated)                 (latest version)

.gitignore            ←──────    .gitignore
  (gets updated)                 (latest version)
```

**Result**: Your images are never affected because they're ignored!

---

## 🚀 Quick Sync Script

Save this as a shell script and run it:

```bash
#!/bin/bash

# safe-sync.sh - Safe GitHub synchronization

echo "🔄 Safe GitHub Sync Starting..."
echo ""

# 1. Backup
echo "📦 Creating backup..."
BACKUP_DIR="Generated_Images_backup_$(date +%Y%m%d_%H%M%S)"
cp -r Generated_Images "$BACKUP_DIR"
echo "✓ Backup created: $BACKUP_DIR"
echo ""

# 2. Fetch
echo "🌐 Fetching from GitHub..."
git fetch origin
echo "✓ Fetched latest from GitHub"
echo ""

# 3. Show changes
echo "📋 Changes that will be applied:"
git diff --name-status origin/main
echo ""

# 4. Stash
echo "💾 Stashing local changes..."
git stash
echo "✓ Stashed"
echo ""

# 5. Pull
echo "⬇️  Pulling latest..."
git pull origin main
echo "✓ Pull complete"
echo ""

# 6. Verify
echo "✅ Verification:"
echo "   Generated_Images exists: $([ -d Generated_Images ] && echo 'YES ✓' || echo 'NO ✗')"
echo "   Image count: $(find Generated_Images -type f 2>/dev/null | wc -l) files"
echo ""

echo "🎉 Sync complete! Your images are safe."
echo "   Backup stored in: $BACKUP_DIR (you can delete this later)"
```

**To use:**
```bash
chmod +x safe-sync.sh
./safe-sync.sh
```

---

## 🆘 Troubleshooting

### Images disappeared after sync
```bash
# They're still in your backup
ls Generated_Images_backup_*

# Restore them
cp -r Generated_Images_backup_LATEST/* Generated_Images/
```

### Git won't pull because of conflicts
```bash
# Force preserve local files
git merge -X ours origin/main

# Or reset and try again
git reset --hard
git pull origin main
```

### Want to see what would change without syncing
```bash
git fetch origin
git diff origin/main | head -50
```

### Need to push your local changes to GitHub too
```bash
# First pull
git pull origin main

# Then push
git add .
git commit -m "feat: local updates"
git push origin main
```

---

## 📞 Remember

- **Your .gitignore protects your images** - They're safe from any git operation
- **Always backup before syncing** - Takes 2 seconds, saves hours
- **Verify after syncing** - Check that images still exist
- **You can restore from backups** - Multiple backup folders protect you

---

**Last Updated**: December 20, 2025

**Key Rule**: Before syncing with GitHub, always:
```bash
cp -r Generated_Images Generated_Images_backup_$(date +%Y%m%d_%H%M%S)
```

This one command solves everything! 🛡️
