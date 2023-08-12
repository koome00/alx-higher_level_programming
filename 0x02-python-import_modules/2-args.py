#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    b = argv[1:]
    a = len(b)
    if a == 0:
        print(f"0 arguments.")
    elif a == 1:
        c = argv[1]
        print(f"{a:d} argument:")
        print(f"1: {c:}")
    else:
        print(f"{a: d} arguments:")
        for a, arg in enumerate(b):
            print(f"{a + 1} : {arg}")
