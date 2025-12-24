@echo off
REM AWS S3 Sync Script for HROC Generated Images (Windows)
REM DO NOT RUN UNTIL ALL IMAGES ARE GENERATED (57 total expected)

echo ==========================================
echo HROC Generated Images S3 Sync Script
echo ==========================================
echo.

REM Configuration
set "LOCAL_DIR=D:\workspace\HROC_Files\HROC_Website_New\generated_images"
set "S3_BUCKET=s3://hroc-outreach-assets-1765630540/images/generated_images"
set "AWS_REGION=us-west-2"

echo Configuration:
echo   Local Dir: %LOCAL_DIR%
echo   S3 Bucket: %S3_BUCKET%
echo   Region: %AWS_REGION%
echo.

REM Check AWS CLI
where aws >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] AWS CLI not found. Please install AWS CLI.
    pause
    exit /b 1
)
echo [OK] AWS CLI installed

REM Check AWS credentials
aws sts get-caller-identity >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] AWS credentials not configured
    echo Run: aws configure
    pause
    exit /b 1
)
echo [OK] AWS credentials configured
echo.

REM Warning about incomplete images
echo ==========================================
echo WARNING: Image generation incomplete!
echo ==========================================
echo Current: 44 images (estimated)
echo Expected: 57 images
echo Missing: ~13 images
echo.
echo Services status:
echo   [COMPLETE] service-overdose-prevention (6/6)
echo   [COMPLETE] service-syringe-exchange (6/6)
echo   [PARTIAL] service-wound-care (4/6)
echo   [INCOMPLETE] service-cultural-healing (3/6)
echo   [INCOMPLETE] service-education-training (3/6)
echo   [INCOMPLETE] service-health-screening (3/6)
echo   [INCOMPLETE] service-housing-support (3/6)
echo   [INCOMPLETE] service-peer-support (3/6)
echo   [INCOMPLETE] service-resource-navigation (3/6)
echo ==========================================
echo.

set /p CONTINUE="Continue with sync anyway? (y/N): "
if /i not "%CONTINUE%"=="y" (
    echo Sync cancelled.
    pause
    exit /b 0
)

echo.
echo ==========================================
echo Step 1: DRY-RUN
echo ==========================================
echo Running dry-run to preview changes...
echo.

aws s3 sync "%LOCAL_DIR%" "%S3_BUCKET%" --region "%AWS_REGION%" --acl public-read --dryrun

echo.
set /p PROCEED="Proceed with actual sync? (y/N): "
if /i not "%PROCEED%"=="y" (
    echo Sync cancelled.
    pause
    exit /b 0
)

echo.
echo ==========================================
echo Step 2: ACTUAL SYNC
echo ==========================================
echo Uploading to S3...
echo.

aws s3 sync "%LOCAL_DIR%" "%S3_BUCKET%" --region "%AWS_REGION%" --acl public-read

if %errorlevel% equ 0 (
    echo.
    echo ==========================================
    echo [SUCCESS] Sync completed!
    echo ==========================================
    echo.
    echo Images now accessible at:
    echo https://hroc-outreach-assets-1765630540.s3.us-west-2.amazonaws.com/images/generated_images/
    echo.
    echo Verifying upload...
    aws s3 ls "%S3_BUCKET%" --recursive --region "%AWS_REGION%" --human-readable
) else (
    echo.
    echo [ERROR] Sync failed. Check error messages above.
)

echo.
pause
