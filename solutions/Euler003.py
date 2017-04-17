#!/usr/bin/env python3

"""
---Largest prime factor---
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from pyprimes import factors


def main():
    print(max(factors(600851475143)))


if __name__ == "__main__":
    main()