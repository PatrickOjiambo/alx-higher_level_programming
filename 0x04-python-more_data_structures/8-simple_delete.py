#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    response = a_dictionary.get(key, 1)
    if response == 1:
        return a_dictionary
    else:
        del a_dictionary[key]
    return a_dictionary
