#!/usr/bin/python3
def number_keys(a_dictionary):
    nums = 0
    lists_keys = list(a_dictionary.keys())

    for j in lists_keys:
        nums += 1

    return (nums)
