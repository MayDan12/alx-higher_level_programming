#!/usr/bin/python3
#0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """This project is a good one"""
    count = 0

    try:
        for i in my_list:
            if count < x:
                print(i, end=' ')
                count += 1
            else:
                break
    except TypeError:
        print("Error: Invalid input list")

    print()


    return count
