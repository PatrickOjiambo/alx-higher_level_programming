def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    printed_elements += 1
            except IndexError:
                raise  # Raise an IndexError if x is larger than the length of my_list
    except IndexError:
        pass  # Ignore index errors if x is larger than the length of my_list

    print()
    return printed_elements

