#!/usr/bin/python3
"""Script that fetches my GitHub user id by using credentials"""

import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/users/{}"
    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get(url.format(username),
                       headers={
                           'Accept': 'application/vnd.github+json',
                           'Authorization': 'Bearer {}'.format(password),
                           "X-GitHub-Api-Version": "2022-11-28"
    },)

    if res.status_code == 200:
        print(res.json().get('id'))
    else:
        print("None")
