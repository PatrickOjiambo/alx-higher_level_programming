#!/usr/bin/python3
import sys


def print_this():
    args = sys.argv[1:]
    if len(args) == 0:
        print("{} arguments.".format(len(args)))
    elif len(args) == 1:
        print("{} argument:".format(len(args)))
    else:
        print("{} arguments:".format(len(args)))
        for count, arg in enumerate(args, start=1):
            print("{}: {}".format(count, arg))


if __name__ == "__main__":
    print_this()
