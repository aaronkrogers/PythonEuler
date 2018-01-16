#!/usr/bin/env python3

from itertools import combinations_with_replacement
from Euler021 import factor_sum


def is_abundant(n):
    result = False
    if factor_sum(n) > n:
        result = True
    return result


def euler023():
    """
    --- Non-abundant sums ---
    Find the sum of all the positive integers which cannot be written as
    the sum of two abundant numbers
    """
    result  = 0
    limit = 28123 + 1
    abundants = (x for x in range(1, limit) if is_abundant(x))
    abundsums = {sum(x) for x in combinations_with_replacement(abundants, 2)}

    for i in range(1, limit):
        if i not in abundsums:
            result += i

    return result

if __name__ == "__main__":
    print(euler021())