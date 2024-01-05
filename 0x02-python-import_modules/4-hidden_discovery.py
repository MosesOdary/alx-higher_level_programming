#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for __name__ in dir(hidden_4):
        if not __name__.startswith("__"):
            print(__name__)
