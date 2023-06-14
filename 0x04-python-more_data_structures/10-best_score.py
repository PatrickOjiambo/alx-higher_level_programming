#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = 0
    if a_dictionary == None:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                return key
