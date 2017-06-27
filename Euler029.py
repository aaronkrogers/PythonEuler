#!/usr/bin/env python3

from itertools import product


def euler029():
    output = set()
    values = range(2, 101)
    for a, b in product(values, values):
        output.add(a**b)

    return len(output)


if __name__ == "__main__":
    print(euler029())