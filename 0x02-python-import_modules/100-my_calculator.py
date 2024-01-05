#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    array = len(sys.argv) - 1
    if array != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = sys.argv[2]
        c = int(sys.argv[3])

        if b not in ('+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            if b == '+':
                print("{} + {} = {}".format(a, c, add(a, c)))
            elif b == '-':
                print("{} - {} = {}".format(a, c, sub(a, c)))
            elif b == '*':
                print("{} * {} = {}".format(a, c, mul(a, c)))
            else:
                print("{} / {} = {}".format(a, c, div(a, c)))
