#!/bin/bash
EMAIL="jdmallin25x40@gmail.com"
API_KEY="b90eb8d819ae0c4ab1c14a481db66b99b2d38"
ZONE_ID="0da5d1116d7e40e8c77615ce8a757cd1"

echo "Checking DNS records for hrocinc.org..."
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?name=hrocinc.org" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" | jq -r '.result[] | "Type: \(.type), Name: \(.name), Content: \(.content), Proxied: \(.proxied)"'

echo ""
echo "Checking www.hrocinc.org..."
curl -s -X GET "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?name=www.hrocinc.org" \
  -H "X-Auth-Email: $EMAIL" \
  -H "X-Auth-Key: $API_KEY" \
  -H "Content-Type: application/json" | jq -r '.result[] | "Type: \(.type), Name: \(.name), Content: \(.content), Proxied: \(.proxied)"'
