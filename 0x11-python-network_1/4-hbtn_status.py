#!/usr/bin/python3
"""
fetch a given url
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as status:
        content = status.read()
        print('Body response:')
        print('\t- type: {}'.format(type(content.decode('utf-8'))))
        print('\t- content: {}'.format(content.decode('utf-8')))
