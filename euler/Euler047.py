#!/usr/bin/env python3

import pyprimes
from itertools import count


def euler047():
    """Distinct Prime Factors
    The first two consecutive numbers to have
    two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have
    three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct
    prime factors each. What is the first of these numbers?
    """
    for C in count(644):
        for i in range(4):
            if len(list(pyprimes.factorise(C+i))) != 4:
                break
        else:
            return C


if __name__ == "__main__":
    print(euler047())