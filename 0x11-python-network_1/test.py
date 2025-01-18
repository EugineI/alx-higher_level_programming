#!/usr/bin/env python3
import urllib.request

with urllib.request.urlopen('https://member.theroom.com/alx') as f:
    html = f.read()
print(html.decode('utf_8'))
