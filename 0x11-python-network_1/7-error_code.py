#!/usr/bin/python3
""" Module that takes in a URL sends a
request and displays the body response
"""
import requests
from sys import argv


def main():
    """ Method thats sends request and displays body """
    req = requests.get(argv[1])
    code = req.status_code
    if code >= 400:
        print('Error code: {}'.format(code))
    else:
        print(req.content.decode())

if __name__ == '__main__':
    main()
