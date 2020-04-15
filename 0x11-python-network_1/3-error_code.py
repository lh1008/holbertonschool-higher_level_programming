#!/usr/bin/python3
""" Module that sends a request to a passed URL and displays body """
import urllib.parse
import urllib.request
from sys import argv


url = argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode())
except urllib.error.HTTPError as er:
    print('Error code: {}'.format(er.code))
