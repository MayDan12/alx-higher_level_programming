#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """This finction removes all c character from a string"""
    dan = [f for f in my_string if f != 'c' and f != 'C']
    return ("".join(dan))
