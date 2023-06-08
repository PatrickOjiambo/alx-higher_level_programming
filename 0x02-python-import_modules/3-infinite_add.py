#!/usr/bin/python3
import sys


def sum():
    add = 0
    args = sys.argv[1:]
    for arg in args:
        num = int(arg)
        add = add + num
    print("{}".format(add))


if __name__ == "__main__":
    sum()
