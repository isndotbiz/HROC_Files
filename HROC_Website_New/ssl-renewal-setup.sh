#!/bin/bash

# SSL Certificate Auto-Renewal Script for HROC Website
# This script sets up automatic renewal of Let's Encrypt certificates

echo "=== HROC SSL Certificate Auto-Renewal Setup ==="
echo ""

# Configuration
CERT_DOMAIN="hrocinc.org"
CONTAINER_NAME="hrocinc-nginx"
LETSENCRYPT_DIR="/mnt/tank/encrypted/containers/hrocinc/letsencrypt"

echo "1. Testing certificate renewal (dry run)..."
docker run --rm \
  -v $LETSENCRYPT_DIR:/etc/letsencrypt \
  -v /mnt/tank/encrypted/containers/hrocinc/web:/var/www/html \
  certbot/certbot renew --dry-run

if [ $? -eq 0 ]; then
    echo "✅ Renewal test successful!"
else
    echo "❌ Renewal test failed. Please check configuration."
    exit 1
fi

echo ""
echo "2. Creating renewal cron job..."

# Create renewal script
cat > /root/renew-ssl.sh << 'EOF'
#!/bin/bash
# Auto-renewal script for Let's Encrypt certificates
# Runs daily, renews if within 30 days of expiration

LETSENCRYPT_DIR="/mnt/tank/encrypted/containers/hrocinc/letsencrypt"
CONTAINER_NAME="hrocinc-nginx"
LOG_FILE="/var/log/letsencrypt-renewal.log"

echo "[$(date)] Starting certificate renewal check..." >> $LOG_FILE

# Run certbot renewal
docker run --rm \
  -v $LETSENCRYPT_DIR:/etc/letsencrypt \
  -v /mnt/tank/encrypted/containers/hrocinc/web:/var/www/html \
  certbot/certbot renew >> $LOG_FILE 2>&1

if [ $? -eq 0 ]; then
    echo "[$(date)] Certificate renewal check completed successfully" >> $LOG_FILE

    # Reload nginx if certificates were renewed
    docker exec $CONTAINER_NAME nginx -s reload
    echo "[$(date)] Nginx reloaded" >> $LOG_FILE
else
    echo "[$(date)] Certificate renewal check failed" >> $LOG_FILE
fi

echo "" >> $LOG_FILE
EOF

chmod +x /root/renew-ssl.sh

echo "✅ Renewal script created at /root/renew-ssl.sh"

echo ""
echo "3. Setting up cron job to run daily at 3 AM..."

# Add cron job if it doesn't exist
(crontab -l 2>/dev/null | grep -v renew-ssl.sh; echo "0 3 * * * /root/renew-ssl.sh") | crontab -

echo "✅ Cron job installed"

echo ""
echo "4. Creating certificate monitoring script..."

cat > /root/check-ssl-expiry.sh << 'EOF'
#!/bin/bash
# Check SSL certificate expiration

DOMAIN="hrocinc.org"
EXPIRY_DATE=$(echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null | openssl x509 -noout -enddate 2>/dev/null | cut -d= -f2)

if [ -z "$EXPIRY_DATE" ]; then
    echo "❌ Unable to check certificate expiration"
    exit 1
fi

EXPIRY_EPOCH=$(date -d "$EXPIRY_DATE" +%s 2>/dev/null || date -j -f "%b %d %T %Y %Z" "$EXPIRY_DATE" +%s)
CURRENT_EPOCH=$(date +%s)
DAYS_LEFT=$(( ($EXPIRY_EPOCH - $CURRENT_EPOCH) / 86400 ))

echo "Certificate for $DOMAIN:"
echo "  Expires: $EXPIRY_DATE"
echo "  Days remaining: $DAYS_LEFT"

if [ $DAYS_LEFT -lt 30 ]; then
    echo "  ⚠️  WARNING: Certificate expires in less than 30 days!"
elif [ $DAYS_LEFT -lt 7 ]; then
    echo "  ❌ CRITICAL: Certificate expires in less than 7 days!"
else
    echo "  ✅ Certificate is valid"
fi
EOF

chmod +x /root/check-ssl-expiry.sh

echo "✅ Monitoring script created at /root/check-ssl-expiry.sh"

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "📋 What was configured:"
echo "  1. Automatic renewal runs daily at 3 AM"
echo "  2. Certificates will auto-renew 30 days before expiration"
echo "  3. Nginx will automatically reload after renewal"
echo "  4. Logs saved to /var/log/letsencrypt-renewal.log"
echo ""
echo "🔍 Useful commands:"
echo "  Check certificate expiration:  /root/check-ssl-expiry.sh"
echo "  Manual renewal:                /root/renew-ssl.sh"
echo "  View renewal logs:             tail -f /var/log/letsencrypt-renewal.log"
echo "  Test renewal:                  docker run --rm -v $LETSENCRYPT_DIR:/etc/letsencrypt certbot/certbot renew --dry-run"
echo ""
echo "📅 Current certificate info:"
docker run --rm -v $LETSENCRYPT_DIR:/etc/letsencrypt certbot/certbot certificates
