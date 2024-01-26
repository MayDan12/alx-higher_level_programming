#!/usr/bin/python3

"""This scripts POST request to http://0.0.0.0:5000/search_user"""

if __name__ == '__main__':
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        ars = sys.argv[1]
    except Exception:
        ars = ""
    q = {"q": ars}
    rq = requests.post(url, data=q)
    try:
        result = rq.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
