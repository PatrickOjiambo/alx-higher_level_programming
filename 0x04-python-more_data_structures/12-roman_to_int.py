#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    for i in roman_string:
        if i == 'I':
            i = 1
        elif i == 'X':
            i = 10
        elif i == 'V':
            i = 5
        elif i == 'L':
            i = 50
        elif i == 'M':
            i = 1000
        elif i == 'C':
            i = 100
        elif isinstance(roman_string, str) is False:
            return None
        else:
            i = 500
        sum = sum + i
    return sum
