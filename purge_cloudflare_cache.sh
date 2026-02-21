#!/bin/bash
# Purge Cloudflare cache for hrocinc.org
# Credentials loaded from 1Password

EMAIL=$(op item get "Cloudflare" --vault "TrueNAS Infrastructure" --fields username 2>/dev/null)
API_KEY=$(op item get "Cloudflare" --vault "TrueNAS Infrastructure" --fields credential 2>/dev/null)

if [ -z "$EMAIL" ] || [ -z "$API_KEY" ]; then
  echo "Failed to load Cloudflare credentials from 1Password."
  echo "Make sure OP_SERVICE_ACCOUNT_TOKEN is set or run: eval \$(op signin)"
  exit 1
fi

echo "Getting zone ID for hrocinc.org..."
ZONE_ID=$(curl -s -X GET "https://api.cloudflare.com/client/v4/zones?name=hrocinc.org" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" | jq -r '.result[0].id')

echo "Zone ID: $ZONE_ID"

if [ "$ZONE_ID" != "null" ] && [ -n "$ZONE_ID" ]; then
  echo "Purging cache..."
  curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/purge_cache" \
    -H "X-Auth-Email: $EMAIL" \
    -H "X-Auth-Key: $API_KEY" \
    -H "Content-Type: application/json" \
    --data '{"purge_everything":true}' | jq

  echo ""
  echo "Cloudflare cache purged successfully!"
else
  echo "Could not find zone ID for hrocinc.org"
  exit 1
fi
