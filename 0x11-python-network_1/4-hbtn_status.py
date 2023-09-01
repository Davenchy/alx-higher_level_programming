#!/usr/bin/python3
"""Script that uses requests module to fetch
https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"

    res = requests.get(url)
    data = res.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
