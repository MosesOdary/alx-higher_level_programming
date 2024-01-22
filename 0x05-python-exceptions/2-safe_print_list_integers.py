#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    numberOfPrintedElements = 0

    for i in range(x): # for (int i = 0; i < x; i++)
        try:
            print("{:d}".format(my_list[i]), end="")
            numberOfPrintedElements += 1
        except (ValueError, TypeError):
            pass
    print()
    return numberOfPrintedElements

