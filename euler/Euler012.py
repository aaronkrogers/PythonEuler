#!/usr/bin/env python3

from pyprimes import factors
from itertools import count


def factor_count(n):
    """Return the number of factors of any given integer
    :type n: int
    :return: number of factors of n
    """
    result = 1
    p_factors = factors(n)
    for factor in set(p_factors):
        result *= p_factors.count(factor)+1
    return result


def triangle_numbers():
    next_t = 0
    for i in count(start=1):
        next_t += i
        yield next_t


def euler012():
    """
    --- Highly divisible triangle number ---
    What is the value of the first triangle number to have over five hundred divisors?
    """
    for num in triangle_numbers():
        if factor_count(num) > 500:
            return num


if __name__ == "__main__":
    print(euler012())