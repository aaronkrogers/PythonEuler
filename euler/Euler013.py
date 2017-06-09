#!/usr/bin/env python3

from definitions import RESOURCE_DIR


def euler013():
    """
    --- Large sum ---
    Work out the first ten digits of the sum of the
    one hundred 50-digit numbers located in resources/Euler013.txt
    """
    result = 0
    with open(f'{RESOURCE_DIR}/Euler013.txt', 'r') as input:
        for line in input:
            result += int(line.strip())

    return f'{str(result):.10}'


if __name__ == "__main__":
    print(euler013())