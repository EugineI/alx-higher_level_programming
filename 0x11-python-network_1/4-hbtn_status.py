#!/usr/bin/python3
"""
fetch a given url
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as status:
    content = status.read()
    print('Body response:')
    print('\t- type: {}'.format(type(content.decode('utf-8'))))
    print('\t- content: {}'.format(content.decode('utf-8')))
