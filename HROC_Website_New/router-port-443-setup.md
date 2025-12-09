# Router Port 443 Configuration Guide

## Quick Setup Summary

You need to add ONE port forwarding rule to your router:

```
Service Name: HTTPS / HROC-SSL
External Port: 443
Internal IP: 10.0.0.89
Internal Port: 8444
Protocol: TCP
```

---

## Network Information

**Your Setup:**
- Server IP: `10.0.0.89`
- Gateway/Router: `10.0.0.1`
- Public IP: `73.140.158.252`
- Current HTTP forwarding: External 80 → Internal 8081 ✅ (already working)
- Need HTTPS forwarding: External 443 → Internal 8444 ⏳ (needs configuration)

---

## Step-by-Step Instructions

### Step 1: Access Your Router

Try these router admin URLs:
- http://10.0.0.1
- http://192.168.1.1
- http://192.168.0.1

If none work, check your router's label or manual for the admin URL.

**Default login credentials** (common routers):
- Username: `admin` / Password: `admin`
- Username: `admin` / Password: `password`
- Username: `` (blank) / Password: `admin`

### Step 2: Find Port Forwarding Settings

Look for these menu names (varies by router):
- "Port Forwarding"
- "Virtual Server"
- "NAT / QoS"
- "Applications & Gaming"
- "Firewall" → "Port Forwarding"
- "Advanced" → "Port Forwarding"

### Step 3: Copy Existing HTTP Rule

Since port 80 is already forwarded, find that rule and duplicate it:

**Existing Rule (reference):**
```
Service: HTTP / Web Server
External Port: 80
Internal IP: 10.0.0.89
Internal Port: 8081
Protocol: TCP
Status: Enabled
```

### Step 4: Create New HTTPS Rule

Add a new rule with these exact values:

| Field | Value |
|-------|-------|
| Service Name | `HTTPS` or `HROC-SSL` |
| External Port Start | `443` |
| External Port End | `443` |
| Internal IP | `10.0.0.89` |
| Internal Port Start | `8444` |
| Internal Port End | `8444` |
| Protocol | `TCP` (not UDP, not Both - just TCP) |
| Status/Enable | `Enabled` or `On` |

**IMPORTANT:** Make sure it's port `8444` not `443` for internal port!

### Step 5: Save and Apply

- Click "Save" or "Apply"
- Some routers require a reboot - if prompted, click "Reboot Now"
- Wait 30-60 seconds for router to restart

### Step 6: Test HTTPS

After router restarts, test HTTPS access:

```bash
# From any computer (not the server):
curl -I https://hrocinc.org

# Should return:
# HTTP/2 200
# server: nginx
# ...
```

Or open in browser: https://hrocinc.org

**Expected result:** Padlock icon + website loads

---

## Router-Specific Instructions

### pfSense / OPNsense

1. Navigate to: **Firewall → NAT → Port Forward**
2. Click **"Add"** (arrow pointing down)
3. Configure:
   - Interface: `WAN`
   - Protocol: `TCP`
   - Destination: `WAN address`
   - Destination Port Range: `HTTPS (443)`
   - Redirect Target IP: `10.0.0.89`
   - Redirect Target Port: `8444`
   - Description: `HROC HTTPS`
4. Click **"Save"**
5. Click **"Apply Changes"**

### Ubiquiti UniFi

1. Navigate to: **Settings → Routing & Firewall → Port Forwarding**
2. Click **"Create New Port Forward Rule"**
3. Configure:
   - Name: `HROC HTTPS`
   - Forward IP: `10.0.0.89`
   - Forward Port: `8444`
   - Protocol: `TCP`
   - External Port: `443`
4. Click **"Apply Changes"**

### Netgear

1. Navigate to: **Advanced → Advanced Setup → Port Forwarding**
2. Click **"Add Custom Service"**
3. Configure:
   - Service Name: `HROC_HTTPS`
   - Protocol: `TCP`
   - External Port: `443`
   - Internal Port: `8444`
   - Internal IP: `10.0.0.89`
4. Click **"Apply"**

### TP-Link

1. Navigate to: **Forwarding → Virtual Servers**
2. Click **"Add New"**
3. Configure:
   - Service Port: `443`
   - IP Address: `10.0.0.89`
   - Internal Port: `8444`
   - Protocol: `TCP`
   - Status: `Enabled`
4. Click **"Save"**

### Linksys

1. Navigate to: **Applications & Gaming → Single Port Forwarding**
2. Find an empty row
3. Configure:
   - Application Name: `HROC_HTTPS`
   - External Port: `443`
   - Internal Port: `8444`
   - Protocol: `TCP`
   - To IP Address: `10.0.0.89`
   - Enabled: `✓`
4. Click **"Save Settings"**

### ASUS

1. Navigate to: **WAN → Virtual Server / Port Forwarding**
2. Enable "Virtual Server" if not enabled
3. In the Port Forwarding List, add:
   - Service Name: `HROC_HTTPS`
   - Port Range: `443`
   - Local IP: `10.0.0.89`
   - Local Port: `8444`
   - Protocol: `TCP`
4. Click **"Add"** then **"Apply"**

### D-Link

1. Navigate to: **Advanced → Port Forwarding**
2. Click **"Add"**
3. Configure:
   - Name: `HROC_HTTPS`
   - Public Port: `443`
   - Private Port: `8444`
   - Traffic Type: `TCP`
   - Private IP: `10.0.0.89`
   - Schedule: `Always`
4. Click **"Save Settings"**

---

## Verification & Testing

### Test 1: External HTTPS Access

```bash
# From outside your network:
curl -I https://hrocinc.org

# Expected output:
HTTP/2 200
server: nginx
date: ...
```

### Test 2: SSL Certificate Check

```bash
echo | openssl s_client -connect hrocinc.org:443 -servername hrocinc.org 2>&1 | grep -A 5 "subject=\|issuer="

# Expected output should show:
# subject=CN=hrocinc.org
# issuer=C=US, O=Let's Encrypt, CN=R...
```

### Test 3: Browser Test

1. Open https://hrocinc.org in browser
2. Look for padlock icon 🔒 in address bar
3. Click padlock → "Connection is secure"
4. Certificate should show:
   - Issued to: hrocinc.org
   - Issued by: Let's Encrypt
   - Valid until: March 9, 2026

### Test 4: SSL Labs Test

Visit: https://www.ssllabs.com/ssltest/analyze.html?d=hrocinc.org

**Expected Rating:** A or A+

---

## Troubleshooting

### Problem: "Connection refused" or "Unable to connect"

**Cause:** Port 443 forwarding not configured or router not restarted

**Solution:**
1. Double-check port forwarding rule exists
2. Verify all values are correct (especially internal port 8444)
3. Reboot router
4. Wait 2 minutes and test again

### Problem: "Certificate not trusted" or SSL error

**Cause:** Wrong certificate files or nginx misconfigured

**Solution:**
```bash
# On server, reload nginx:
ssh root@10.0.0.89 'docker exec hrocinc-nginx nginx -s reload'

# Check certificate files exist:
ssh root@10.0.0.89 'ls -la /mnt/tank/encrypted/containers/hrocinc/letsencrypt/live/hrocinc.org/'
```

### Problem: HTTP works but HTTPS doesn't

**Cause:** Port 443 forwarding not working

**Solution:**
1. Check if ISP blocks port 443 (some residential ISPs do)
2. Try testing from different network (mobile data)
3. Check router firewall isn't blocking outbound 443
4. Verify internal port is 8444 not 443

### Problem: "Wrong host" or "Certificate mismatch"

**Cause:** Accessing via www subdomain but certificate doesn't include it

**Solution:**
The certificate covers: hrocinc.org, www.hrocinc.org
Both should work. If not, regenerate certificate with all domains.

---

## Alternative: Using Different External Port

If your ISP blocks port 443, you can use an alternative:

**Option: Use port 8443 externally**

1. Configure router forwarding:
   - External: `8443` → Internal: `10.0.0.89:8444`
2. Access site via: `https://hrocinc.org:8443`
3. Note: Users will need to include `:8443` in URL

---

## Security Notes

- ✅ Port forwarding is safe when properly configured
- ✅ Only forwards port 443 traffic, nothing else
- ✅ Nginx handles all requests and has security headers
- ✅ SSL/TLS encrypts all traffic
- ✅ No additional firewall rules needed
- ⚠️ Never forward port 22 (SSH) to internet without VPN
- ⚠️ Never forward TrueNAS management ports

---

## After Configuration Checklist

- [ ] Port 443 forwarding rule added to router
- [ ] Rule shows: External 443 → 10.0.0.89:8444 TCP
- [ ] Router rebooted (if required)
- [ ] Waited 2 minutes for router to stabilize
- [ ] Tested: `curl -I https://hrocinc.org` returns HTTP/2 200
- [ ] Browser shows padlock icon when visiting site
- [ ] SSL Labs test shows A or A+ rating
- [ ] HTTP automatically redirects to HTTPS

---

## Need Help?

If you're unable to access your router or configure port forwarding:

1. **Find router model:** Check the label on your router
2. **Search for manual:** Google "[router model] port forwarding guide"
3. **Contact ISP:** Some ISPs provide routers - they can configure remotely
4. **Alternative:** Consider using Cloudflare Tunnel (no port forwarding needed)

---

**Once configured, your site will be accessible at:** https://hrocinc.org ✅

**Certificate will auto-renew every 60 days** (expires March 9, 2026)

**No further configuration needed!**
