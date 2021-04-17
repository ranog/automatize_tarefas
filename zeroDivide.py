#!/usr/bin/env python3


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")


for i in range(0, 13):
    print(spam(i))
