#!/usr/bin/python3
"""
A module that opens a file for writing
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    (UTF8) and returns the number
    of characters written:
    Args:
        filename(str): name of the file
        text(str):String to be written to the file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
    return content
