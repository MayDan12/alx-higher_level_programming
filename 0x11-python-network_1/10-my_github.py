#!/usr/bin/python3
"""This scripts takes GitHub credentials (username and password)"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    usernames = sys.argv[1]
    passwords = sys.argv[2]
    infos = (usernames, passwords)
    rq = requests.get(url, auth=infos)
    try:
        print(rq.json()['id'])
    except Exception:
        print('None')
