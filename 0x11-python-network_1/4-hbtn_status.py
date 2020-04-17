#!/usr/bin/python3
""" Module that fetches a URL """
import requests


def main():
    """ Method that fetches the URL """
    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.content.decode()))

if __name__ == '__main__':
    main()
