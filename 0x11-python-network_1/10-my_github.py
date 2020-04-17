#!/usr/bin/python3
""" Module that takes my Github credentials and displays id """
import requests
from sys import argv


req = requests.get('https://api.github.com/users/lh1008')
print(req.url)
print(req.text)
