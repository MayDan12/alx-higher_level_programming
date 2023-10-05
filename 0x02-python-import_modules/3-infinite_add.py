#!/usr/bin/python3

if __name__ == "__main__":
    """This functrion does infinite addition of multiple numbers."""
    import sys

    count = 0

    for d in range(len(sys.argv) - 1):
        count += int(sys.argv[d + 1])
    print("{}".format(count))
