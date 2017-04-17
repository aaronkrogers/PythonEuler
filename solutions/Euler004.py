#!/usr/bin/env python3

from itertools import combinations
import pyprimes


def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False


def is_acceptable(number):
    prime_factors = pyprimes.factors(number)

    for r in range(len(prime_factors)):
        for subset in combinations(prime_factors, r):
            product = 1
            for s in subset:
                product *= s
            if ((99 < product < 1000) and
                    (99 < number//product < 1000)):
                return True
    else:
        return False


def euler004():
    """
    ---Largest palindrome product---

    A palindromic number reads the same both ways. 
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    lower_bound = 100 ** 2
    upper_bound = 999 ** 2

    for num in range(upper_bound, lower_bound, -1):
        if is_palindrome(num) and is_acceptable(num):
            return num


if __name__ == "__main__":
    print(euler004())