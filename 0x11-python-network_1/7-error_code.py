#!/usr/bin/python3
"""This scripts with requests model"""

if __name__ == '__main__':
    import requests
    import sys
    re = requests.get(sys.argv[1])
    if re.status_code >= 400:
        print("Error code: {}".format(re.status_code))
    else:
        print(re.text)
