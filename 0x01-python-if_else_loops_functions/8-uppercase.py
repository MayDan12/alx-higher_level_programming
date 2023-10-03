#!/usr/bin/python3
# 8-uppercase.py
def uppercase(upper):
    for z in upper:
        if ord(z) >= 97 and ord(z) <= 122:
            z = chr(ord(z) - 32)
        print("{}".format(z), end="")
    print("")
