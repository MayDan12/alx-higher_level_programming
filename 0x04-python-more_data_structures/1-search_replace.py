#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """This function search and replace a list"""
    newest_list = list(map(lambda x: replace if x == search else x, my_list))
    return (newest_list)
