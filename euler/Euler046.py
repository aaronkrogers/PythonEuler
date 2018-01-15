#!/usr/bin/env python3

from itertools import count, takewhile
from pyprimes import isprime
from math import sqrt


def euler046() -> int:
    """Goldbach's other conjecture
    It was proposed by Christian Goldbach that every odd composite number
    can be written as the sum of a prime and twice a square.

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum
    of a prime and twice a square?
    """
    # generator of non-even composite numbers
    composites = (i for i in count(3, step=2) if not isprime(i))
    for C in composites:
        for x in range(1, int(sqrt(C/2))+1):
            p = C - (2 * x**2)
            x += 1
            if isprime(p):
                break
        else:
            return C


if __name__ == "__main__":
    print(euler046())
