#!/usr/bin/python3
"""Script that fetches url and handles errors"""

import urllib.request
import urllib.parse
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            message = res.read().decode('utf-8')
            print(message)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
