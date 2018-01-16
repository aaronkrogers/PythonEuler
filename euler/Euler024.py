#!/usr/bin/env python3

from itertools import permutations


def euler024():
    """
    --- Lexicographic permutations ---
    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8, and 9
    """
    count = 0
    digits = '0123456789'

    for permutation in permutations(digits):
        count += 1
        if count == 1_000_000:
            return f'{"".join(permutation)}'


if __name__ == "__main__":
    print(euler024())