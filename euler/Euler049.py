#!/usr/bin/env python3

from pyprimes import primes_above
from itertools import takewhile, combinations


def get_sequence(lst: list) -> list:
    for combination in combinations(lst, 3):
        if combination[2]-combination[1] == combination[1]-combination[0]:
            return combination


def euler049() -> str:
    # Create an empty dictionary to store all
    # prime permutations of 4-digit primes
    perm = {}
    # Create a generator for all 4-digit primes
    primes = takewhile(lambda x: x <= 9999, primes_above(1000))

    for prime in primes:
        # For each 4-digit prime we will put the primes into a list in
        # perm with the key being the prime's sorted value
        prime = str(prime)  # Using strings for permutation problem
        perm.setdefault(''.join(sorted(prime)), []).append(int(prime))

    # Disregard all primes with less than 3 prime permutations
    perm = {k: v for k, v in perm.items() if len(v) >= 3}

    for value in perm.values():
        sequence = get_sequence(value)
        if sequence and sequence[0] != 1487:
            return ''.join(str(s) for s in sequence)


if __name__ == "__main__":
    print(euler049())
