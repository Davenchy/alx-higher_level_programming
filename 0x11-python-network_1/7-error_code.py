#!/usr/bin/python3
"""Script that sends a request and handles errors"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
        exit()
    value = res.text
    print(value)
