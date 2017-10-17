#!/usr/bin/env python3

from math import gcd
from pyprimes import factors


def product(lst):
    """Return the product of all of the numbers in lst
    """
    output = 1
    for a in lst:
        output *= a
    return output


def totient(n):
    """Calculate and return number of coprimes to n
    using Euler's totient function
    """
    return n * product((1-1/p) for p in set(factors(n)))


result = 0
for i in range(2, 1_000_001):
    result += totient(i)
print(result)