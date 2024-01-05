#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    array = len(sys.argv)
    if (array == 1):
        print("0 arguments.")
    elif (array == 2):
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{array - 1} arguments:")
        for i in range(1, array):
            print(f"{i}: {sys.argv[i]}")
