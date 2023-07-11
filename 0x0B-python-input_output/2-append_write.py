#!/usr/bin/python3
"""
A module that opens a file for writing
"""


def append_write(filename="", text=""):

    """
    appends a string at the end of a
    text file (UTF8) and returns the
    number of characters added:
    Args:
        filename(str): name of the file
        text(str):String to be written to the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write(text)
    return content
