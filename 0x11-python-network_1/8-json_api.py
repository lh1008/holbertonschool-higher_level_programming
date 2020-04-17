#!/usr/bin/python3
""" Module that sends a POST request with a letter as parameter """
import requests
from sys import argv


def main():
    """ Method that sends a POST with a parameter """
    if len(argv) == 1 or argv[1].isdigit():
        print('No result')
    else:
        req = requests.post('http://0.0.0.0:5000/search_user',
                            data={'q': argv[1]})
        k = req.json()
        print('[{}] {}'.format(k.get('id'), k.get('name')))

if __name__ == '__main__':
    main()
