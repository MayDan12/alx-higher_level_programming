#!/usr/bin/python3
"""This scripts same as 1-hbtn_header with requests module"""

if __name__ == '__main__':
    import requests
    import sys
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
