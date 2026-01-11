#!/usr/bin/env python3
"""
Add TrueNAS GUI route to Traefik
Access at: https://nas.isn.biz
"""
import yaml

# Read the current configuration
with open('/tmp/dynamic.yml.new', 'r') as f:
    config = yaml.safe_load(f)

# Add TrueNAS GUI router
config['http']['routers']['truenas-gui'] = {
    'rule': 'Host(`nas.isn.biz`)',
    'entryPoints': ['websecure'],
    'service': 'truenas-gui',
    'tls': {
        'certResolver': 'letsencrypt'
    }
}

# Add TrueNAS GUI service (port 80 is default TrueNAS web UI)
config['http']['services']['truenas-gui'] = {
    'loadBalancer': {
        'servers': [
            {'url': 'http://10.0.0.89:80'}
        ]
    }
}

# Write the updated configuration
with open('/tmp/dynamic.yml.new', 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("TrueNAS GUI route added!")
print("Access at: https://nas.isn.biz")
