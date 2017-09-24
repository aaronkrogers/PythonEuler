#!/usr/bin/env python3

import pyprimes
from itertools import count
from itertools import product


def quadratic(n, a, b):
    return n**2 + a*n + b


def euler027():
    results = [0, 0, 0]
    primes = list(pyprimes.primes_below(1000))  # Positive primes
    nprimes = [-p for p in primes]              # Negative primes

    # b and a should both be primes
    # b should be positive
    for b, a in product(primes, nprimes + primes):
        for n in count():
            q = quadratic(n, a, b)
            if not pyprimes.isprime(q):
                if n >= results[0]:
                    results = [n, a, b]
                break

    return results[1] * results[2]


if __name__ == "__main__":
    print(euler027())
