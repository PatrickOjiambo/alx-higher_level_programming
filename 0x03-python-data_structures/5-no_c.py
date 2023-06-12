#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for letter in my_string:
        if letter != 'c' or 'C':
            string += letter
    return string
