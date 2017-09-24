#!/usr/bin/env python3

from math import factorial


def digit_sum(num):
    return sum(int(i) for i in str(num))


def euler020():
    return digit_sum(factorial(100))


if __name__ == "__main__":
    print(euler020())