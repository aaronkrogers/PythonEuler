#!/usr/bin/env python3

from Euler002 import fibonacci_generator


def euler025():
    count = 1
    for fib in fibonacci_generator():
        count += 1
        if len(str(fib)) == 1000:
            return count, fib


if __name__ == "__main__":
    print(euler025())