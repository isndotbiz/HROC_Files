#!/bin/bash
# Purge Cloudflare cache for hrocinc.org

EMAIL="jdmallin25x40@gmail.com"
API_KEY="b90eb8d819ae0c4ab1c14a481db66b99b2d38"

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
  echo "✅ Cloudflare cache purged successfully!"
else
  echo "❌ Could not find zone ID for hrocinc.org"
fi
