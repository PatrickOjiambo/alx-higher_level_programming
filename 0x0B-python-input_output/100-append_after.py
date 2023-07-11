#!/usr/bin/python3
"""
This module contains a function that
inserts a line of text to a file, after
each line containing a specific string
(see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific
    string (see example):
    """

    my_arr = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for item in file:
            my_arr = my_arr + item
            if search_string in item:
                my_arr = my_arr + new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(my_arr)
