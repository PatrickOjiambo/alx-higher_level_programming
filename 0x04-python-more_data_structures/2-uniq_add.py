#!/usr/bin/python3
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
def uniq_add(my_list=[]):

    new_list = set(my_list)
    final_value = reduce(lambda x, y: x + y, new_list)
    return final_value
