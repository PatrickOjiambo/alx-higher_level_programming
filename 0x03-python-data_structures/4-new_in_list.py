#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        new = my_list.copy()
        return new
    elif idx + 1 > len(my_list):
        new = my_list.copy()
        return new
    else:
        new = my_list.copy()
        new[idx] = element
        return new
