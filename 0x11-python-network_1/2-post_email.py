#!/usr/bin/python3
"""This pythonn script sends a POST request"""

if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    reqs = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqs) as response:
        info = response.read()
    print(info.decode("ascii"))
