#!/usr/bin/env python3

from math import factorial as f


def nCr(n, r):
    return f(n) / (f(r) * f(n-r))


def euler053():
    """Combinatoric Selections
    There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, 5C3 = 10.

    In general,

    nCr = n! / r!(n−r)!

    where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

    It is not until n = 23, that a value exceeds one-million:

    23 C 10 = 1144066.

    How many, not necessarily distinct, values of  nCr,
    for 1 ≤ n ≤ 100,are greater than one-million?
    """
    result = 0
    for n in range(1, 101):
        done = False  # Flag determines when to stop
        for r in range(n):
            if nCr(n, r) > 1_000_000:
                result += 1
                done = True  # Set to signify upward turn in nCr
            elif done:
                # Break when downward turn in
                # nCr drops below 1 million
                break

    return result


if __name__ == "__main__":
    print(euler053())