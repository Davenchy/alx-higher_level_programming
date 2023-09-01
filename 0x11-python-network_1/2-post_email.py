#!/usr/bin/python3
"""Script that sends a POST request with email and prints utf8 encoded response
"""

import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    data = {
        'email': sys.argv[2]
    }
    data = urllib.parse.urlencode(data).encode('ascii')

    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as res:
        message = res.read().decode('utf-8')
        print(message)
