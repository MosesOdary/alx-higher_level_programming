#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for j in range(len(matrix[k])):
            if (j != 0):
                print(" ", end='')
            print("{:d}".format(matrix[k][j]), end='')

        print()
