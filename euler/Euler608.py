#!/usr/bin/env python3
"""This is a very bad solution which should
display the correct answer given a very,
very, very large amount of time.
I will come back to this later"""
from pyprimes import factorise
from itertools import product
from math import factorial as fact


def count_factors(num):
    """Return the numbers of divisors for num
    """
    return prod(f[1]+1 for f in factorise(num))


def prod(lst):
    result = 1
    for i in lst:
        result *= i
    return result


def powered(factors, powers):
    return prod(f**p for (f, p) in zip(factors, powers))


def divisors(num):
    pf = list(factorise(num))
    primes = [p[0] for p in pf]
    # For each prime, possible exponents
    exponents = [range(i[1] + 1) for i in pf]
    yield from (powered(primes, es) for es in product(*exponents))


def D(m, n):
    result = 0
    for d, k in product(divisors(m), range(1, n+1)):
        result += count_factors(d*k)
    return result - 1


print(D(fact(400), 10**12))