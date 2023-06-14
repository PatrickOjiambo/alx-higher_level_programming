#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    elif len(roman_string) == 0:
        return 0
    elif roman_string is None:
        return 0
    else:
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
            elif i == 'D':
                i = 500
            else:
                return 0
            sum = sum + i
        return sum
