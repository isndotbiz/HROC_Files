# Push Images to TrueNAS - Instructions

## The Issue
The TrueNAS server (10.0.0.89) is not reachable from this network. You'll need to run the image push from a computer on the local network where TrueNAS is located.

## Script Ready
I've created `push_images_to_truenas.sh` which will sync all images to TrueNAS:
- **Founder photos**: `HROC_Website_New/images/founders/` (bri, lilly, jonathan headshots + all professional photos)
- **Community photos**: `HROC_Website_New/generated_images/` (15 community images)
- **All other images**: service icons, graphics, etc.

## How to Push Images

### Option 1: From Local Network Computer
1. Remote into the PC on the local network (where TrueNAS is accessible)
2. Pull this GitHub repo or sync these files:
   ```bash
   cd ~/Workspace/HROC_Files
   git pull origin main
   ```
3. Run the image push script:
   ```bash
   ./push_images_to_truenas.sh
   ```

### Option 2: Using Tailscale (Recommended for Future)
If you set up Tailscale on both this Mac and the TrueNAS server:
1. Install Tailscale on TrueNAS
2. Get the Tailscale IP of TrueNAS (something like 100.x.x.x)
3. Edit `push_images_to_truenas.sh` and change:
   ```bash
   SERVER_IP="10.0.0.89"  # Change to Tailscale IP
   ```
4. Run from anywhere: `./push_images_to_truenas.sh`

## What the Script Does
1. ✓ Tests SSH connection to TrueNAS
2. ✓ Syncs `images/` directory (all founder photos, graphics)
3. ✓ Syncs `generated_images/` directory (community photos)
4. ✓ Sets correct permissions (www-data:www-data)
5. ✓ Shows summary of files pushed

## After Pushing Images
The images will be at:
- `/mnt/tank/websites/kusanagi/web/hrocinc.org/images/`
- `/mnt/tank/websites/kusanagi/web/hrocinc.org/generated_images/`

Then you can deploy the full website with:
```bash
./deploy.sh
```

Or just deploy to S3 and skip TrueNAS:
```bash
DEPLOY_SERVER=false ./deploy.sh
```
