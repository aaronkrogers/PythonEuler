#!/usr/bin/env python3

from fractions import Fraction


def transform(n, d, x):
    result = [(n+x*10, d+x*10),
              (n+x*10, d*10+x),
              (n*10+x, d+x*10),
              (n*10+x, d*10+x)]
    return result


def euler033():
    """Digit Cancelling Fractions
    """
    result = 1
    for n in range(1, 10):
        for d in range(n, 10):
            q = Fraction(n, d)

            for i in range(1, 10):
                for pair in transform(n, d, i):
                    # Test for equality and trivial pairs
                    if Fraction(*pair) == q and len(set(pair)) != 1:
                        result *= Fraction(*pair)
    return result.denominator


if __name__ == "__main__":
    print(euler033())
