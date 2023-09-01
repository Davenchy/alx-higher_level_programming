#!/usr/bin/python3
"""Script that fetches the latest 10 commits from a specified repository
by a given user"""

import requests
import sys


if __name__ == '__main__':
    url = "https://api.github.com/repos/{owner}/{repo}/commits"
    repo = sys.argv[1]
    owner = sys.argv[2]

    res = requests.get(url.format(owner=owner, repo=repo),
                       headers={
                           'Accept': 'application/vnd.github+json',
                           "X-GitHub-Api-Version": "2022-11-28"
    },)

    if res.status_code == 200:
        counter = 0
        data = res.json()
        for commit in data:
            if counter >= 10:
                break

            sha = commit.get('sha')
            if sha is None:
                continue

            commit_data = commit.get('commit')
            if commit_data is None:
                continue

            author = commit_data.get('author')
            if author is None:
                continue

            name = author.get('name')
            if name is None:
                continue

            print("{}: {}".format(sha, name))
            counter += 1
