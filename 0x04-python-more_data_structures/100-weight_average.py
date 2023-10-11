#!/usr/bin/python3
def weight_average(my_list=[]):
    """This function does weight average"""
    if not my_list:
        return 0

    nums = 0
    dens = 0

    for tup in my_list:
        nums += tup[0] * tup[1]
        dens += tup[1]

    return (nums / dens)
