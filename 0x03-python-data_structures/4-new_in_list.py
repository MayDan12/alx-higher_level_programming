#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """This replace an element in a copy lit at a direct position"""
    if idx < 0 and idx > (len(my_list) - 1):
        return (my_list)

    good = [d for d in my_list]
    good[idx] = element
    return (good)
