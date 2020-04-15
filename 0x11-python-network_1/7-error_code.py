#!/usr/bin/python3
""" Module that takes in a URL sends a
requestand displays the body response
"""
import requests
from sys import argv


req = requests.get(argv[1])
code = req.status_code
if code >= 400:
    print('Error code: {}'.format(code))
else:
    print(req.content.decode())
