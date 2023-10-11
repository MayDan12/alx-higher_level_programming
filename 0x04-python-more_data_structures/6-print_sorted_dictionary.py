#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ords = list(a_dictionary.keys())
    list_ords.sort()
    for i in list_ords:
        print("{}: {}".format(i, a_dictionary.get(i)))
