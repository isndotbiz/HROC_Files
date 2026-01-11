#!/usr/bin/env python3
"""
Traefik configuration for isn.biz subdomains only
- nas.isn.biz → TrueNAS GUI
- Add more subdomains as needed

hrocinc.org stays on Kusanagi (not Traefik)
"""
import yaml

# Read the current configuration
with open('/tmp/dynamic.yml.new', 'r') as f:
    config = yaml.safe_load(f)

# Initialize if needed
if 'http' not in config:
    config['http'] = {}
if 'routers' not in config['http']:
    config['http']['routers'] = {}
if 'services' not in config['http']:
    config['http']['services'] = {}

# ===========================================
# TrueNAS GUI - nas.isn.biz
# ===========================================
config['http']['routers']['truenas-gui'] = {
    'rule': 'Host(`nas.isn.biz`)',
    'entryPoints': ['websecure'],
    'service': 'truenas-gui',
    'tls': {
        'certResolver': 'letsencrypt'
    }
}

config['http']['services']['truenas-gui'] = {
    'loadBalancer': {
        'servers': [
            {'url': 'http://10.0.0.89:80'}
        ]
    }
}

# ===========================================
# Remove hrocinc.org from Traefik (it uses Kusanagi)
# ===========================================
if 'hrocinc' in config['http']['routers']:
    del config['http']['routers']['hrocinc']
    print("✓ Removed hrocinc.org from Traefik (uses Kusanagi instead)")

if 'hrocinc' in config['http']['services']:
    del config['http']['services']['hrocinc']

# Write the updated configuration
with open('/tmp/dynamic.yml.new', 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("\n✅ Traefik config updated!")
print("\nisn.biz subdomains via Traefik:")
print("  • https://nas.isn.biz → TrueNAS GUI")
print("\nKusanagi (not Traefik):")
print("  • https://hrocinc.org → HROC WordPress site")
print("  • https://www.isn.biz → ISN WordPress site")
print("\nDNS record needed:")
print("  nas.isn.biz  A  73.140.158.252")
