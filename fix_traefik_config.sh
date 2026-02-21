#!/bin/bash
# Fix Traefik configuration to add HROC routing
# Credentials loaded from 1Password - no hardcoded secrets

SSH_KEY=$(op item get "TrueNAS SSH Key - jdmal" --vault "TrueNAS Infrastructure" --fields "private key" 2>/dev/null)
TRUENAS_HOST="10.0.0.89"

if [ -z "$SSH_KEY" ]; then
  echo "Failed to load SSH key from 1Password."
  echo "Make sure OP_SERVICE_ACCOUNT_TOKEN is set or run: eval \$(op signin)"
  exit 1
fi

# Write temp key file
TMPKEY=$(mktemp)
echo "$SSH_KEY" > "$TMPKEY"
chmod 600 "$TMPKEY"
trap "rm -f $TMPKEY" EXIT

ssh -i "$TMPKEY" -o StrictHostKeyChecking=no root@${TRUENAS_HOST} "cat > /tmp/hroc_router.yml << 'EOF'
    # HROC Website
    hrocinc:
      rule: \"Host(\`hrocinc.org\`) || Host(\`www.hrocinc.org\`)\"
      entryPoints:
        - websecure
      service: hrocinc
      tls:
        certResolver: letsencrypt
      middlewares:
        - securityHeaders@file
EOF

cat > /tmp/hroc_service.yml << 'EOF'
    hrocinc:
      loadBalancer:
        servers:
          - url: \"http://hrocinc-nginx:80\"
        healthChecks:
          - path: \"/\"
            interval: \"30s\"
            timeout: \"5s\"
EOF

# Backup original
cp /mnt/tank/infrastructure/traefik/config/dynamic.yml /mnt/tank/infrastructure/traefik/config/dynamic.yml.backup

# Remove the incorrectly added lines
sed -i '/# HROC Website/,\$d' /mnt/tank/infrastructure/traefik/config/dynamic.yml

# Now properly insert the router in the routers section
sed -i '/openwebui:/r /tmp/hroc_router.yml' /mnt/tank/infrastructure/traefik/config/dynamic.yml

# And the service in the services section
sed -i '/url: \"http:\/\/open-webui:8080\"/a\\' /mnt/tank/infrastructure/traefik/config/dynamic.yml
sed -i '/url: \"http:\/\/open-webui:8080\"/r /tmp/hroc_service.yml' /mnt/tank/infrastructure/traefik/config/dynamic.yml

echo 'Configuration updated!'
"
