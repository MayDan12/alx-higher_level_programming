#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(strs, d):
    if d < 0:
        return (strs)
    return (strs[:d] + strs[d + 1:])
