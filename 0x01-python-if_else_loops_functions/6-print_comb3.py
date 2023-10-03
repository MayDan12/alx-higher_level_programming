#!/usr/bin/python3
for The_digit1 in range(0, 10):
    for The_digit2 in range(The_digit1 + 1, 10):
        if The_digit1 == 8 and The_digit2 == 9:
            print("{}{}".format(The_digit1, The_digit2))
        else:
            print("{}{}".format(The_digit1, The_digit2), end=", ")
