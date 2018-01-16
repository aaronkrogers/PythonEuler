#!/usr/bin/env python3

from pyprimes import factors  # work smarter, not harder ;)


def euler003() -> int:
    """Largest prime factor

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    
    Return solution to project euler #3
    """
    return max(factors(600851475143))


if __name__ == "__main__":
    print(euler003())