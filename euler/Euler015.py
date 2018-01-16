#!/usr/bin/env python3

from math import factorial


def coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


def euler015():
    """
    --- Lattice Paths ---
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
    """
    return coefficient(20+20, 20)


if __name__ == "__main__":
    print(euler015())