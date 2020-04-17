#!/usr/bin/python3
""" Module that takes my Github credentials and displays id """
import requests
from sys import argv


def main():
    req = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2]))
    k = req.json()
    print('{}'.format(k.get('id')))

if __name__ == '__main__':
    main()
