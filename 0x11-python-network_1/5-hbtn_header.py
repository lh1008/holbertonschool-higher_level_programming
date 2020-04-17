#!/usr/bin/python3
"""
Module that takes in a URL, sends request
and displays a value variable
"""
import requests
from sys import argv


def main():
    """ Method that sends the request and displays value """
    req = requests.get(argv[1])
    print(req.headers['X-Request-Id'])

if __name__ == '__main__':
    main()
