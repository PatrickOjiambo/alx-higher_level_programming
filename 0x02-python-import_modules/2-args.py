#!/usr/bin/python3
import sys


def print_this():
    args = sys.argv[1:]
    if len(args) == 0:
        print("{} arguments.".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
        for arg in args:
            print("1: {}".format(arg))


if __name__ == "__main__":
    print_this()
