# Lilly Image Upload Instructions

## Images to Upload to S3

The following 6 images need to be uploaded to complete Lilly's page transformation:

### Source Directory
```
/Users/jonathanmallinger/Workspace/HROC_Files/group/l/
```

### Images to Upload
1. `qwen_lilly_01_professional_office_laptop.webp`
2. `qwen_lilly_02_business_casual_outdoor.webp`
3. `qwen_lilly_03_conference_room.webp`
4. `qwen_lilly_06_outdoor_professional.webp`
5. `qwen_lilly_07_modern_office_desk.webp`
6. `qwen_lilly_10_community_engagement.webp`

### S3 Destination
- **Bucket:** `hroc-outreach-assets-1765630540`
- **Region:** `us-west-2`
- **Prefix:** `images/founders/l/`
- **ACL:** `public-read`
- **Content-Type:** `image/webp`

### Upload URLs (after upload)
Each image will be accessible at:
```
https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/[filename]
```

## Upload Methods

### Option 1: AWS CLI
```bash
cd /Users/jonathanmallinger/Workspace/HROC_Files/group/l/

aws s3 cp qwen_lilly_01_professional_office_laptop.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read

aws s3 cp qwen_lilly_02_business_casual_outdoor.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read

aws s3 cp qwen_lilly_03_conference_room.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read

aws s3 cp qwen_lilly_06_outdoor_professional.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read

aws s3 cp qwen_lilly_07_modern_office_desk.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read

aws s3 cp qwen_lilly_10_community_engagement.webp \
  s3://hroc-outreach-assets-1765630540/images/founders/l/ \
  --content-type image/webp --acl public-read
```

### Option 2: AWS Console
1. Navigate to: https://s3.console.aws.amazon.com/s3/buckets/hroc-outreach-assets-1765630540
2. Navigate to folder: `images/founders/l/`
3. Click "Upload"
4. Add the 6 files listed above
5. Set permissions: Public read access
6. Set metadata: Content-Type = `image/webp`
7. Upload

### Option 3: Updated Python Script (with valid credentials)
Update the Python script at `/Users/jonathanmallinger/Workspace/HROC_Files/group/upload_lilly_images.py` with valid AWS credentials, then run:
```bash
cd /Users/jonathanmallinger/Workspace/HROC_Files/group/
python3 upload_lilly_images.py
```

## Verification

After upload, verify each image is accessible by visiting:
1. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_01_professional_office_laptop.webp
2. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_02_business_casual_outdoor.webp
3. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_03_conference_room.webp
4. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_06_outdoor_professional.webp
5. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_07_modern_office_desk.webp
6. https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/founders/l/qwen_lilly_10_community_engagement.webp

## Status

- ✅ HTML transformation complete: `/Users/jonathanmallinger/Workspace/HROC_Files/HROC_Website_New/lilly.html`
- ⏳ Images pending upload (AWS credentials issue)
- 🔧 Waiting for valid AWS credentials to complete upload

## Notes

The provided AWS credentials were invalid. The HTML has been updated with the correct S3 URLs, but the images need to be uploaded using valid credentials or the AWS console.
