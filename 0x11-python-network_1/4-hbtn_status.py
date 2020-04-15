#!/usr/bin/python3
""" Module that fetches a URL """
import requests


req = requests.get('https://intranet.hbtn.io/status')
print('\t- type: {}'.format(type(req.text)))
print('\t- content: {}'.format(req.content.decode()))
