#!/usr/bin/python3
"""This fetch alx intranet status page"""

if __name__ == '__main__':
    import urllib.request
    reqs = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(reqs) as response:
        html = response.read()

    print("Body response:")
    print("\t- type: {}".format(html.__class__))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('ascii')))
