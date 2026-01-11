#!/bin/bash
EMAIL="jdmallin25x40@gmail.com"
API_KEY="b90eb8d819ae0c4ab1c14a481db66b99b2d38"
ZONE_ID="0da5d1116d7e40e8c77615ce8a757cd1"

echo "Enabling Cloudflare Development Mode (bypasses all caching for 3 hours)..."
curl -s -X PATCH "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/settings/development_mode" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  --data '{"value":"on"}' | jq

echo ""
echo "Development mode enabled! All caching bypassed for 3 hours."
echo "Test the site now: https://hrocinc.org"
