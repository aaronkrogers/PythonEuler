#!/usr/bin/env python3

import pyprimes
import itertools


def mul(iterable):
    """
    multiply all terms from an iterable together and return the result
    :param iterable:
    """
    result = 1
    for i in iterable:
        result *= i
    return result


def factor(num):
    """
    return all divisors of any given number
    :type num: int
    :param num: number to factor
    """
    factors = {(1, )}
    prime_factors = pyprimes.factors(num)
    for i in range(1, len(prime_factors)):
        factors |= set(itertools.combinations(prime_factors, i))
    return map(mul, factors)


def factor_sum(num):
    """
    return the sum of the proper divisors of a number
    :type num: int
    :param num: number to factorize
    :return: sum of the factors of num
    """
    return sum(factor(num))


def is_amicable(a):
    b = factor_sum(a)
    if factor_sum(b) == a and a != b:
        result = True
    else:
        result = False
    return result


def euler021():
    result = 0
    for i in range(1, 10000):
        if is_amicable(i):
            result += i

    return result

if __name__ == "__main__":
    print(euler021())