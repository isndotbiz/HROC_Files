# AWS S3 Sync Plan for HROC Generated Images

## Directory Inventory Summary

**Total Images Found:** 44 images
**Total Directory Size:** 19 MB
**Last Updated:** 2025-12-18

## Images Per Service Breakdown

| Service Directory | Image Count | Status |
|------------------|-------------|--------|
| service-cultural-healing | 3 | Original images (1,2,3) |
| service-education-training | 3 | Original images (1,2,3) |
| service-gallery | 5 | Mixed (1-5) |
| service-health-screening | 3 | Original images (1,2,3) |
| service-housing-support | 3 | Original images (1,2,3) |
| service-overdose-prevention | 6 | **Complete (1-6)** |
| service-peer-support | 3 | Original images (1,2,3) |
| service-resource-navigation | 3 | Original images (1,2,3) |
| service-syringe-exchange | 6 | **Complete (1-6)** |
| service-wound-care | 4 | **Partial (1-4, missing 5,6)** |
| Root level (impact stories) | 3 | Impact story hero images |

## Missing Images Alert

**INCOMPLETE SERVICES - DO NOT SYNC YET:**

1. **service-cultural-healing**: Missing images 4, 5, 6
2. **service-education-training**: Missing images 4, 5, 6
3. **service-health-screening**: Missing images 4, 5, 6
4. **service-housing-support**: Missing images 4, 5, 6
5. **service-peer-support**: Missing images 4, 5, 6
6. **service-resource-navigation**: Missing images 4, 5, 6
7. **service-wound-care**: Missing images 5, 6

**COMPLETE SERVICES:**
- service-overdose-prevention (6 images)
- service-syringe-exchange (6 images)

**Expected Total When Complete:** 57 images (9 services × 6 images + 3 gallery + 3 impact + 3 placeholder)

## File Size Analysis

### Large Files (> 1MB):
- service-overdose-prevention/4.png: 1.5 MB
- service-overdose-prevention/5.png: 1.7 MB
- service-overdose-prevention/6.png: 1.9 MB
- service-syringe-exchange/4.png: 1.5 MB
- service-syringe-exchange/5.png: 1.5 MB
- service-syringe-exchange/6.png: 2.0 MB
- service-wound-care/4.png: 1.4 MB

Total large files: ~11.5 MB (60% of total size)

### Small Files (< 500KB):
All original images (1,2,3) and gallery images: ~7.5 MB

## AWS S3 Sync Command

### Primary Sync Command
```bash
aws s3 sync D:/workspace/HROC_Files/HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read --delete
```

### Conservative Sync (No Delete)
```bash
aws s3 sync D:/workspace/HROC_Files/HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read
```

### Dry Run (Test First)
```bash
aws s3 sync D:/workspace/HROC_Files/HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read --dryrun
```

## Sync Strategy

### Current Recommendation: DO NOT SYNC YET

**Reason:** Only 2 out of 9 services have complete image sets (6 images each)

### Pre-Sync Checklist

- [ ] Verify all 9 service directories have images 1-6 (54 images total)
- [ ] Confirm impact story hero images are present (3 images)
- [ ] Check service-gallery images are complete (currently 5 images)
- [ ] Run dry-run to preview changes
- [ ] Backup existing S3 bucket state (if any)
- [ ] Verify AWS credentials are configured
- [ ] Test public-read ACL permissions

### Sync Execution Steps

1. **Verify AWS CLI Configuration**
   ```bash
   aws configure get region
   aws configure get aws_access_key_id
   aws s3 ls s3://hroc-outreach-assets-1765630540/ --region us-west-2
   ```

2. **Run Dry-Run First**
   ```bash
   aws s3 sync D:/workspace/HROC_Files/HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read --dryrun
   ```

3. **Execute Actual Sync**
   ```bash
   aws s3 sync D:/workspace/HROC_Files/HROC_Website_New/generated_images s3://hroc-outreach-assets-1765630540/images/generated_images --region us-west-2 --acl public-read
   ```

4. **Verify Upload**
   ```bash
   aws s3 ls s3://hroc-outreach-assets-1765630540/images/generated_images/ --recursive --region us-west-2 --human-readable
   ```

## Expected Sync Time Estimation

**Current State (44 images, 19 MB):**
- Estimated upload time: 1-3 minutes (depending on connection speed)
- Average speed assumption: 10 Mbps = ~1.5 MB/s
- Calculation: 19 MB ÷ 1.5 MB/s ≈ 12-13 seconds + AWS processing overhead

**When Complete (57 images, estimated ~24-25 MB):**
- Estimated upload time: 2-4 minutes
- With typical AWS overhead: 3-5 minutes total

## S3 Bucket Structure After Sync

```
s3://hroc-outreach-assets-1765630540/images/generated_images/
├── impact-story-hero-1.png
├── impact-story-hero-2.png
├── impact-story-hero-3.png
├── service-cultural-healing/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-education-training/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-gallery/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   └── 5.png
├── service-health-screening/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-housing-support/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-overdose-prevention/
│   ├── 1.png ✓
│   ├── 2.png ✓
│   ├── 3.png ✓
│   ├── 4.png ✓
│   ├── 5.png ✓
│   └── 6.png ✓
├── service-peer-support/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-resource-navigation/
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png (MISSING)
│   ├── 5.png (MISSING)
│   └── 6.png (MISSING)
├── service-syringe-exchange/
│   ├── 1.png ✓
│   ├── 2.png ✓
│   ├── 3.png ✓
│   ├── 4.png ✓
│   ├── 5.png ✓
│   └── 6.png ✓
└── service-wound-care/
    ├── 1.png
    ├── 2.png
    ├── 3.png
    ├── 4.png
    ├── 5.png (MISSING)
    └── 6.png (MISSING)
```

## CDN/CloudFront Access URLs

After sync, images will be accessible at:
```
https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/{path}
```

Or via CloudFront (if configured):
```
https://d[distribution-id].cloudfront.net/images/generated_images/{path}
```

Example:
```
https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/service-overdose-prevention/4.png
```

## Post-Sync Verification

1. **Test random sample URLs** - Verify public accessibility
2. **Check file count** - Should match local count (currently 44, target 57)
3. **Verify ACL permissions** - Ensure public-read is applied
4. **Test website integration** - Confirm images load correctly on site

## Notes

- **--delete flag**: Use cautiously; will remove S3 files not present locally
- **--acl public-read**: Makes all images publicly accessible (required for website)
- **--dryrun**: Always test first to preview changes
- Regional bucket in us-west-2, ensure region flag is included

## Generation Status

**Images Generated:** 44/57 (77% complete)
**Services Complete:** 2/9 (22% complete)
**Ready to Sync:** NO - Wait for all services to reach 6 images each

---

**Last Updated:** 2025-12-18 20:53 UTC
**Generated By:** Claude Code AWS S3 Sync Preparation
