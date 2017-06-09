#!/usr/bin/env python3

from itertools import combinations
from math import sqrt

def euler009():
    """
    --- Special Pythagorean Triplet ---
    
    There exists exactly one Pythagorean Triplet
    for which a + b + c = 1000.
    find the product abc
    """
    for a, b in combinations(range(1, 1000//2), 2):
        c = sqrt(a ** 2 + b ** 2)
        if (c%1 == 0) and (a+b+c == 1000):
            return int(a*b*c)

if __name__ == "__main__":
    print(euler009())