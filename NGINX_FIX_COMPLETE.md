# Nginx Routing Issue - FIXED! ✅

**Date:** December 9, 2025
**Status:** 🟢 RESOLVED

---

## Problem Summary

External requests to **hrocinc.org** were serving WordPress (isn.biz) content instead of the HROC harm reduction website.

---

## Root Cause

**Router Port Forwarding Misconfiguration:**
- Comcast router was forwarding external port 80 → server port 8080 (WordPress container)
- This bypassed the host nginx reverse proxy on port 80
- Traffic went directly to WordPress container, which served content for all hostnames

---

## Solution Implemented

### Server-Side Workaround Using iptables

Since direct router access wasn't available, I implemented a server-side redirect:

```bash
iptables -t nat -I PREROUTING -i enp9s0 -p tcp --dport 8080 -j REDIRECT --to-port 80
```

**How It Works:**
1. External traffic arrives on port 8080 (from router)
2. iptables intercepts it at PREROUTING stage
3. Redirects to port 80 (host nginx reverse proxy)
4. Nginx routes correctly based on Host header:
   - `hrocinc.org` → port 8081 (HROC Docker container)
   - `isn.biz` → port 8080 (WordPress Docker container)

---

## Verification Results

### ✅ Both Sites Working Correctly:

**HROC Site:**
```bash
$ curl -s http://hrocinc.org | grep title
<title>Healing Roots Outreach Collective | Mobile Harm Reduction Services</title>
```

**WordPress Site:**
```bash
$ curl -s http://isn.biz | grep title
<title>iSN.BiZ</title>
```

### Routing Confirmed:
- External IP (73.140.158.252) with Host: hrocinc.org → HROC site ✓
- Domain hrocinc.org → HROC site ✓
- Domain isn.biz → WordPress site ✓

---

## Persistence Configuration

The iptables rule has been made persistent across reboots:

**Rule Location:**
```
/etc/iptables/rules.v4
```

**Auto-restore Script:**
```
/etc/rc.local
```

The rule will be automatically restored when the server reboots.

---

## Technical Details

### Server Configuration:

**Host Nginx** (Port 80/443):
- Version: nginx/1.22.1
- Config: `/etc/nginx/sites-enabled/`
- Proxy rules:
  - `hrocinc.org` → `127.0.0.1:8081`
  - `isn.biz` → `127.0.0.1:8080`

**Docker Containers:**
- `hrocinc-nginx`: Port 8081 → HROC static site
- `kusanagi-nginx`: Port 8080 → WordPress site

**iptables NAT Chain:**
```
1. REDIRECT tcp dpt:8080 → port 80 (NEW RULE)
2. DOCKER chain processing
```

---

## DNS Configuration

Current DNS setup:
- `hrocinc.org` → `73.140.158.252` (direct, no CDN)
- `isn.biz` → Cloudflare IPs (proxied)
- TTL: 300 seconds (5 minutes)

---

## Optional Future Improvements

### 1. Fix Router Port Forwarding (Recommended)

The proper fix is to change the router configuration:

**Current (Workaround):**
```
Router: Port 80 → Server Port 8080 → iptables redirect → Port 80
```

**Ideal:**
```
Router: Port 80 → Server Port 80 → nginx routing
```

**To Fix:**
1. Access router at http://10.0.0.1
2. Navigate to Port Forwarding settings
3. Change: External Port 80 → Internal Port 8080
4. To: External Port 80 → Internal Port 80

### 2. Enable HTTPS for hrocinc.org

Currently hrocinc.org only works on HTTP (port 80). To enable HTTPS:

```bash
# Install certbot for Let's Encrypt
apt install certbot python3-certbot-nginx

# Get SSL certificate
certbot --nginx -d hrocinc.org -d www.hrocinc.org

# Auto-renew setup
systemctl enable certbot.timer
```

### 3. Enable Cloudflare Proxy

Currently hrocinc.org DNS points directly to your IP (grey cloud). To add Cloudflare protection:
1. Login to Cloudflare
2. Enable proxy for hrocinc.org (orange cloud)
3. Benefits: DDoS protection, caching, SSL

---

## Server Access

**SSH Command:**
```bash
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89
```

**View iptables rules:**
```bash
iptables -t nat -L PREROUTING -n -v --line-numbers
```

**Reload nginx:**
```bash
systemctl reload nginx
```

---

## Troubleshooting

### If hrocinc.org Stops Working After Reboot:

1. **Check if iptables rule is active:**
```bash
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "iptables -t nat -L PREROUTING -n -v | grep 8080"
```

2. **Manually restore if needed:**
```bash
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "iptables-restore < /etc/iptables/rules.v4"
```

3. **Verify rc.local is executable:**
```bash
ssh -i ~/.ssh/truenas_admin_10_0_0_89 root@10.0.0.89 "ls -la /etc/rc.local"
```

### If WordPress (isn.biz) Stops Working:

The iptables rule only affects external traffic. Internal container communication on port 8080 should still work. If isn.biz fails:

1. Check container is running:
```bash
docker ps | grep kusanagi-nginx
```

2. Check nginx proxy config:
```bash
cat /etc/nginx/sites-enabled/isn.biz.conf
```

---

## Summary

**Problem:** Router misconfiguration causing wrong site to load
**Solution:** iptables redirect at server level
**Result:** Both sites working correctly ✅
**Status:** Production ready 🚀

---

**Fixed by:** Claude Code
**Date:** December 9, 2025 01:30 AM PST
**Method:** iptables NAT PREROUTING redirect
