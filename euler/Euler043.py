#!/usr/bin/env python3

from itertools import takewhile, permutations
from pyprimes import primes
from project_euler import list2int


def subnums(array):
    start, end = 1, 4
    while end <= 10:
        yield list2int(array[start:end])
        start += 1
        end += 1


def euler043():
    """Sub-string Divisibility
    The number, 1406357289, is a 0 to 9 pandigital number because
    it is made up of each of the digits 0 to 9 in some order, but
    it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
    In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """
    result = 0
    # Iterate through all permutations of numbers 0-9
    # while ignoring permutations that start with 0
    for perm in takewhile(lambda p: p[0] != 0,
                          permutations(range(9, -1, -1))):
        primegen = primes()
        for subnum in subnums(perm):
            if subnum % next(primegen) != 0:
                break
        else:
            result += list2int(perm)
    return result


if __name__ == "__main__":
    print(euler043())