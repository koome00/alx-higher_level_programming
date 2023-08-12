#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = argv[1:]
    result = 0
    for i in range(0, len(num)):
        result += int(num[i])
    print("{:d}".format(result))
