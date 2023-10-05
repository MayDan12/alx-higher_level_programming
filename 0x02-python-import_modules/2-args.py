#!/usr/bin/python3

if __name__ == "__main__":
    """This function gives the number of lists and arguments"""
    import sys

    exact = len(sys.argv) - 1
    if exact == 0:
        print("0 arguments.")
    elif exact == 1:
        print("1 arguments.")
    else:
        print("{} arguments:".format(exact))
    for d in range(exact):
        print("{}: {}".format(d + 1, sys.argv[d + 1]))
