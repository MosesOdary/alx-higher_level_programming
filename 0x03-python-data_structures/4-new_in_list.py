#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list

    newList = [j for j in my_list]
    newList[idx] = element
    return newList
