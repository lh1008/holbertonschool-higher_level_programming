#!/usr/bin/python3
""" Module that sends a POST request to a passed URL """
import urllib.parse
import urllib.request
from sys import argv


url = argv[1]
values = {'email': argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html.decode())
