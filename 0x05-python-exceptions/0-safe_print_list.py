#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    numberOfPrintedElements = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            numberOfPrintedElements += 1
        print()
        return numberOfPrintedElements
    except IndexError:
        print()
        return numberOfPrintedElements
