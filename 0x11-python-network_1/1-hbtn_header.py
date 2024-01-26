#!/usr/bin/python3
""" This fetch X-request id from header response"""

if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        contents = response.getheader('X-Request-Id')

    print(contents)
