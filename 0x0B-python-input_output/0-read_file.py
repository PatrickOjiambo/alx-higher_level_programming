#!/usr/bin/python3
"""
A module that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """
    function that reads a text file
    (UTF8) and prints it to stdout:
    Args:
        Filename(str): Contains the file name as string
    """
    with open(filename, 'r') as file:
        content = file.read().decode("utf-8")
        print(content)
