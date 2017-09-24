#!/usr/bin/env python3

from pyprimes import primes_below


def euler010():
    """
    --- Summation of primes ---
    Find the sum of all the primes below two million
    """
    result = 0
    for prime in primes_below(2_000_000):
        result += prime

    return result


if __name__ == "__main__":
    print(euler010())