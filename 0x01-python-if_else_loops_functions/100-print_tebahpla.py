#!/usr/bin/python3
# 100-print_tebahpla.py
"""This print alphabet in reverse order"""
da = 0
for y in range(ord('z'), ord('a') -1, -1):
    print("{}".format(chr(y - da)), end="")
    da = 32 if da == 0 else 0
