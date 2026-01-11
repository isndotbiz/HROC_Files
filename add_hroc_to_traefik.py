#!/usr/bin/env python3
import yaml

# Read the current configuration
with open('/tmp/dynamic.yml.new', 'r') as f:
    config = yaml.safe_load(f)

# Add HROC router
config['http']['routers']['hrocinc'] = {
    'rule': 'Host(`hrocinc.org`) || Host(`www.hrocinc.org`)',
    'entryPoints': ['websecure'],
    'service': 'hrocinc',
    'tls': {
        'certResolver': 'letsencrypt'
    },
    'middlewares': ['securityHeaders@file']
}

# Add HROC service
config['http']['services']['hrocinc'] = {
    'loadBalancer': {
        'servers': [
            {'url': 'http://10.0.0.89:8081'}
        ],
        'healthCheck': {
            'path': '/',
            'interval': '30s',
            'timeout': '5s'
        }
    }
}

# Write the updated configuration
with open('/tmp/dynamic.yml.new', 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False)

print("Configuration updated!")
