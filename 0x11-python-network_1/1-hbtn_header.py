#!/usr/bin/python3
"""Python script that fetches http headers and show value of X-Request-Id"""

import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        value = res.getheader('X-Request-Id')
        print(value)
