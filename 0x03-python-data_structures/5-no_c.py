#!/usr/bin/python3

def no_c(my_string):
    newString = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c') and (my_string[i] != 'C'):
            newString += my_string[i]

    return newString
