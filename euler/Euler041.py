#!/usr/bin/env python3

from pyprimes import isprime
from itertools import permutations


def euler040():
    """Pandigital Prime
    We shall say that an n-digit number is pandigital if it makes
    use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """
    for length in range(10, 1, -1):
        # Yeah I'm kind of cheating by not testing 10 digit numbers
        # I'm not yet sure how to avoid that in an efficient manner
        for perm in permutations((str(d) for d in range(9, -1, -1)), 9):
                number = int(''.join(perm))
                if isprime(number):
                    return number



if __name__ == "__main__":
    print(euler040())