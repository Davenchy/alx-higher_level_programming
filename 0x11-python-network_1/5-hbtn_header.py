#!/usr/bin/python3
"""Script that uses requests module to fetch url and shows value of
X-Request-Id header"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    res = requests.get(url)
    value = res.headers.get('X-Request-Id')
    print(value)
