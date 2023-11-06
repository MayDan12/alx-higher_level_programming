#!/usr/bin/python3
"""This defines a class checking function"""

def is_same_class(obj, a_class):
    """This function checks if an object is exactly an instance of a given class

    Args:
        obj (any): Object to check
        a_class (type): Class mto match the type of obj to.
    Returns:
        if obj is an instance of a_class - true
        else - false.
     """
     if type(obj) == a_class:
         return(True)
     return(False)
