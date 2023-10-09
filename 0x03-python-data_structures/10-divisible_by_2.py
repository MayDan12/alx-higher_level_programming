#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    more_than = []
    for v in range(len(my_list)):
        if my_list[v] % 2 == 0:
            more_than.append(True)
        else:
            more_than.append(False)

    return (more_than)
