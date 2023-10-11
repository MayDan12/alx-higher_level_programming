#!/usr/bin/python3
def uniq_add(my_list=[]):
    """This is a function that adds uniq"""
    uniqs_list = set(my_list)
    nums = 0

    for h in uniqs_list:
        nums += h

    return (nums)
