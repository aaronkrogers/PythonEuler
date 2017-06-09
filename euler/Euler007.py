#!/usr/bin/env python3

from pyprimes import nth_prime  # work smarter ;)


def euler007():
    """
    ---10001st prime---
    
    By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    
    Return solution to projecteuler #7
    :return: int
    """
    return nth_prime(10001)


if __name__ == "__main__":
    print(euler007())