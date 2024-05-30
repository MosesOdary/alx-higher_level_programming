#!/usr/bin/python3

import sys
if __name__ == "__main__":
    arg = [int(arg) for arg in sys.argv[1:]]
    result = sum(arg)
    print(result)
