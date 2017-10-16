#!/usr/bin/env python3

from definitions import RESOURCE_DIR
from math import log


def euler099():
    result = [1, 1]
    with open(f"{RESOURCE_DIR}/Euler099.txt", 'r') as file:
        numbers = [line.strip().split(',') for line in file.readlines()]
        for number in numbers:
            current = [int(n) for n in number]
            if current[1] * log(current[0]) > result[1] * log(result[0]):
                result = current
                output = numbers.index(number) + 1
    return output


if __name__ == "__main__":
    print(euler099())
