#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    empty_list = []
    for number in my_list:
        if number % 2 == 0:
            empty_list.append(True)
        else:
            empty_list.append(False)
    return empty_list
