# HROC Website - Troubleshooting Commands for Codex

## Quick Test - Does S3 Work?

```bash
# Test if S3 bucket is accessible
curl -I "https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated/service-overdose-prevention.png"
# Should return: HTTP/1.1 200 OK
```

## Check Current HTML on Server

```bash
# SSH into TrueNAS
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89

# Check what's in the HTML file
grep "service-overdose-prevention" /mnt/tank/encrypted/containers/hrocinc/web/index.html | head -1

# Count total S3 references
grep -c "hroc-outreach-assets-1765630540.s3" /mnt/tank/encrypted/containers/hrocinc/web/index.html
# Should be: 60

# View a few sample paths
grep -o 'hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/[^"]*' /mnt/tank/encrypted/containers/hrocinc/web/index.html | head -5
```

## Check Docker Container

```bash
# SSH into TrueNAS
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89

# Check if Docker is running
docker ps | grep hrocinc-nginx

# Check what Docker is serving
docker exec hrocinc-nginx grep "service-overdose-prevention" /usr/share/nginx/html/index.html | head -1

# Check Docker logs for errors
docker logs hrocinc-nginx | tail -50

# Restart Docker
docker restart hrocinc-nginx
```

## Check S3 Bucket

```bash
# List all S3 objects
aws s3 ls s3://hroc-outreach-assets-1765630540/ --recursive --region us-west-2 | wc -l
# Should be 155+

# Check specific folder
aws s3 ls s3://hroc-outreach-assets-1765630540/images/generated/ --region us-west-2

# Check bucket policy
aws s3api get-bucket-policy --bucket hroc-outreach-assets-1765630540 --region us-west-2
```

## Browser DevTools Steps

1. Go to https://hrocinc.org
2. Press F12 to open DevTools
3. Click "Network" tab
4. Press Ctrl+F5 to hard refresh
5. Look for image requests (.png files)
6. Check status codes:
   - 200 = Success
   - 403 = Permission denied
   - 404 = Not found
   - Missing = Not requested

## Clear Cache Completely

```bash
# Windows/Linux
Ctrl+Shift+Delete → Select "All time" → Clear data

# Mac
Cmd+Shift+Delete → Select "All time" → Clear data

# Then hard refresh
Ctrl+F5 (Windows/Linux) or Cmd+Shift+R (Mac)
```

## Verify Paths

```bash
# Check paths in HTML
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "
grep -o 'images/generated/[^\"]*' /mnt/tank/encrypted/containers/hrocinc/web/index.html | sort -u | head -5
grep -o 'generated_images/[^\"]*' /mnt/tank/encrypted/containers/hrocinc/web/index.html | sort -u | head -5
"

# Check paths in S3
aws s3 ls s3://hroc-outreach-assets-1765630540/images/generated/ --region us-west-2 | head -5
aws s3 ls s3://hroc-outreach-assets-1765630540/generated_images/community_photos/ --region us-west-2 | head -3
```

## Check for CORS Issues

```bash
# If you see CORS errors in browser console, run:
aws s3api put-bucket-cors --bucket hroc-outreach-assets-1765630540 --region us-west-2 --cors-configuration '{
  "CORSRules": [
    {
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET"],
      "AllowedOrigins": ["*"]
    }
  ]
}'
```

## Full Diagnostic

```bash
echo "1. Testing S3"
curl -s -I "https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated/service-overdose-prevention.png" | head -1

echo ""
echo "2. HTML S3 references"
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "grep -c 'hroc-outreach-assets-1765630540.s3' /mnt/tank/encrypted/containers/hrocinc/web/index.html"

echo ""
echo "3. Docker status"
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "docker ps | grep hrocinc-nginx"

echo ""
echo "4. S3 file count"
aws s3 ls s3://hroc-outreach-assets-1765630540/ --recursive --region us-west-2 | wc -l
```

## Common Issues & Fixes

### Images return 404
- Path doesn't match S3
- Check: `grep "service-overdose" /mnt/tank/encrypted/containers/hrocinc/web/index.html`
- Should show full S3 URL with correct path

### Images return 403
- S3 permission issue
- Fix: Re-apply bucket policy
- ```bash
  aws s3api put-bucket-policy --bucket hroc-outreach-assets-1765630540 --region us-west-2 --policy '{
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::hroc-outreach-assets-1765630540/*"
    }]
  }'
  ```

### Images don't load after clearing cache
- Docker may be serving stale HTML
- Restart: `docker restart hrocinc-nginx`
- Wait 5 seconds
- Hard refresh browser

### CORS errors in console
- Apply CORS policy (see "Check for CORS Issues" section above)

## Key IPs/Ports

```
TrueNAS: 10.0.0.89
  SSH Port: 22
  HTTP Port: 80 → Docker:8081
  HTTPS Port: 443 → Docker:8444

S3:
  Region: us-west-2
  Bucket: hroc-outreach-assets-1765630540
  Base URL: https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/

Website:
  HTTP: http://hrocinc.org
  HTTPS: https://hrocinc.org
```

---

**Run these commands and share output if images still not showing.**
