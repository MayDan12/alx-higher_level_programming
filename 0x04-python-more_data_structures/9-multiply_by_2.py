#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dirs = a_dictionary.copy()
    lists_keys = list(new_dir.keys())

    for i in lists_keys:
        new_dirs[i] *= 2

    return (new_dirs)
