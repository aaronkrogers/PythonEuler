#!/usr/bin/env python3

from itertools import combinations
import pyprimes


def is_palindrome(number: int) -> bool:
    """Return True is number is palindromic
    otherwise return False
    """
    number = str(number)
    # True if our number and its reverse are equal
    return number == number[::-1]


def is_acceptable(number: int) -> bool:
    """Return True if number is the product of two 3-digit numbers
    otherwise return False
    """
    prime_factors = pyprimes.factors(number)

    for i in range(len(prime_factors)):
        for subset in combinations(prime_factors, i):
            product = 1
            for s in subset:
                product *= s

            # True if our product and its multiplicand are 3-digit numbers
            if ((99 < product < 1000) and
                    (99 < number//product < 1000)):
                return True

    # False unless proven otherwise
    return False


def euler004() -> int:
    """Largest palindrome product

    A palindromic number reads the same both ways. 
    The largest palindrome made from the product
    of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    
    Return solution to project euler #4
    """
    lower_bound = 100 ** 2
    upper_bound = 999 ** 2

    for num in range(upper_bound, lower_bound, -1):
        if is_palindrome(num) and is_acceptable(num):
            return num


if __name__ == "__main__":
    print(euler004())