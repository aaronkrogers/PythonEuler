#!/usr/bin/env python3

from itertools import count
from pyprimes import primes_below


def euler005(upper_bound=20):
    """
    ---Smallest multiple---
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    :return: int
    """
    result = 1
    primes = primes_below(upper_bound)
    for prime in primes:
        for num in count(start=1):
            if prime ** num > upper_bound:
                result *= prime ** (num-1)
                break
    return result


if __name__ == "__main__":
    print(euler005())