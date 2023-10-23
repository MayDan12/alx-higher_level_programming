#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """ This function divides two elements"""
    newlist = []
    for z in range (0, list_length):
        try:
            div = my_list_1[z] / my_list_2[z]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            newlist.append(div)
    return (newlist)
