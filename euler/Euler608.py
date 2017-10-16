#!/usr/bin/env python3
"""This is a very bad solution which should
display the correct answer given a very,
very, very large amount of time.
I will come back to this later"""
from pyprimes import factorise
from itertools import product
from math import factorial as fact
from time import time


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


def divisor_count(num):
    return prod(a + 1 for p, a in factorise(num))


def D(m, n):
    result = 0
    start = time()
    c = 0
    dc = divisor_count(m)
    for d in divisors(m):
        for k in range(1, n+1):
            c += 1
            if c % 1000 == 0:
                print(
                        f"\r{c/dc*100:.2f}% done after "
                        f"{(time()-start)//60} minutes",
                        end=''
                )
            result += divisor_count(d*k)
    return result - 1


if __name__ == "__main__":
    print(D(fact(400), 10**14))