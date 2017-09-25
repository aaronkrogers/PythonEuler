#!/usr/bin/env python3

from itertools import permutations


def pandigital_product(seq) -> int:
    """Return the product of an identity
    if the identity is pandigital, otherwise
    return 0
    """
    for i in range(1, 3):
        multiplicand = int(''.join(str(s) for s in seq[:i]))
        multiplier = int(''.join(str(s) for s in seq[i:9-4]))
        product = int(''.join(str(s) for s in seq[-4:]))
        if multiplicand * multiplier == product:
            return product
    return 0


def euler032() -> int:
    """Pandigital Products
    We shall say that an n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once; for example, the 5-digit number,
    15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254,
    containing multiplicand, multiplier, and product is 1 through 9
    pandigital.

    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.
    """

    digits = list(range(1, 10))

    return sum(set(pandigital_product(comb)
                   for comb in permutations(digits)))


if __name__ == "__main__":
    print(euler032())