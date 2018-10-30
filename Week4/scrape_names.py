#!/usr/bin/env python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL: ')
enter_count = int(input('Enter count: '))
enter_position = int(input('Enter position: ')) - 1
counter = 1
def scrape(url):
    global counter
    urls = []
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        urls.append(tag.get('href', None))

    print("Runtime: " + str(counter) + " Retrieveing: " + urls[enter_position])
    if counter == enter_count:
        exit(0)
    counter = counter + 1
    return scrape(urls[enter_position])

scrape(url)
