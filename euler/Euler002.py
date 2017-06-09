#!/usr/bin/env python3


def fibonacci_generator(start=1, end=None):
    """
    :param start: int 
    :param end: int or None
    :return: int
    """
    current = start
    last = current
    while True:
        last, current = current, current+last
        if end and last > end:
            break
        yield last


def euler002():
    """
    ---Even Fibonacci numbers---
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed
    four million, find the sum of the even-valued terms.
    
    Return solution to projecteuler #2
    :return: int
    """
    result = 0
    # Filter out only even fibonacci numbers and
    # add them to result
    for fib in fibonacci_generator(end=4_000_000):
        if fib % 2 == 0:
            result += fib
    return result

if __name__ == "__main__":
    print(euler002())