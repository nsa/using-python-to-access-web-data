#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter URL: ')
    if len(address) < 1: break

    print('Retrieving', address)
    uh = urllib.request.urlopen(address, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    print("Count: "+ str(len(js['comments'])))
    total = 0
    for item in js['comments']:
        total += int(item['count'])
    print('Total: ' + str(total))
