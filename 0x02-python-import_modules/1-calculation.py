#!/usr/bin/python3

if __name__ == "__main__":
    """This function gives the sum, diff, multiple, and Qou of a and b."""
    from calculator_1 import add, sub, mul, div

    b = 5
    a = 10

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
