#!/usr/bin/python3
# 12-fizzbuzz.py
def fizzbuzz():
    for thenumber in range(1, 101):
        if thenumber % 3 == 0 and thenumber % 5 == 0:
            print("FizzBuzz ", end="")
        elif thenumber % 3 == 0:
            print("Fizz ", end="")
        elif thenumber % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(thenumber), end="")
