#!/usr/bin/env python3

from itertools import count
from math import gcd


def primitive_triples(p_target:int =1000):
    """Generate primitive pythagorean triples
    using Euclid's formula where p_target is the
    largest perimeter accepted for a generated triangle
    """
    m = 2
    for m in count(1):
        for n in range(1, m):
            if ((m % 2 == n % 2 == 1)
                    or (gcd(m, n) != 1)):
                continue
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            if sum((a, b, c)) > p_target:
                raise StopIteration
            else:
                yield tuple(sorted((a, b, c)))
        m += 1


def triples(p_target: int=1000):
    """Generate all pythagorean triples
    using a revised Euclid's formula where p_target is the
    largest perimeter accepted for a generated triangle"""
    for triple in primitive_triples(p_target):
        k = 1
        a, b, c = triple
        while True:
            new_triple = a*k, b*k, c*k
            k += 1
            if sum(new_triple) > p_target:
                break
            else:
                yield new_triple


def euler039(p_target: int=1000):
    """Integer right triangles
    If p is the perimeter of a right angle triangle with integral length
    sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    """
    triple_counts = {}  # Dictionary of perimeters of integral length triangles
    for triple in triples(p_target):
        key = sum(triple)
        triple_counts.setdefault(key, 0)
        triple_counts[key] += 1
    return max(triple_counts, key=triple_counts.get)


if __name__ == "__main__":
    print(euler039())
