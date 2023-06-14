#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    response = a_dictionary.get(key, 1)
    if response == 1:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
