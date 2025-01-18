#!/usr/bin/python3
#post email
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    my_email = sys.argv[2]

    data = urllib.parse.urlencode({'email': my_email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method = 'POST')

    with urllib.request.urlopen(req) as response:
        result = response.read()
    print('Your email is: {}'.format(result.decode('utf-8')))
