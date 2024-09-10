#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
try:
    if number < 0:
        print(f"{number} is negative")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is positive")
except TypeError as e:
    print("TypeError")
