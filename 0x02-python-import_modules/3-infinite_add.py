#!/usr/bin/python3
import sys


def add():
    args = sys.argv[1:]
    length = len(args)
    sum = 0
    if length == 0:
        print("0")
    elif length == 1:
        print(f"{args[0]}")
    else:
        for i, arg in enumerate(args, start=1):
            sum += int(arg)
        print(f"{sum}")


if __name__ == "__main__":
    add()
