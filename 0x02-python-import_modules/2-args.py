#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print(f"1: {args[0]}")
    else:
        print(f"{num_args} arguments:")
        for i, args in enumerate(args, start=1):
            print(f"{i}: {args}")


if __name__ == "__main__":
    main()
