#!/bin/bash
# Enable Cloudflare Development Mode for hrocinc.org
# Credentials loaded from 1Password

EMAIL=$(op item get "Cloudflare" --vault "TrueNAS Infrastructure" --fields username 2>/dev/null)
API_KEY=$(op item get "Cloudflare" --vault "TrueNAS Infrastructure" --fields credential 2>/dev/null)

if [ -z "$EMAIL" ] || [ -z "$API_KEY" ]; then
  echo "Failed to load Cloudflare credentials from 1Password."
  echo "Make sure OP_SERVICE_ACCOUNT_TOKEN is set or run: eval \$(op signin)"
  exit 1
fi

# Get zone ID dynamically
ZONE_ID=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=hrocinc.org" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" | jq -r '.result[0].id')

if [ -z "$ZONE_ID" ] || [ "$ZONE_ID" = "null" ]; then
  echo "Could not find zone ID for hrocinc.org"
  exit 1
fi

echo "Enabling Cloudflare Development Mode (bypasses all caching for 3 hours)..."
curl -s -X PATCH "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/development_mode" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  --data '{"value":"on"}' | jq

echo ""
echo "Development mode enabled! All caching bypassed for 3 hours."
echo "Test the site now: https://hrocinc.org"
