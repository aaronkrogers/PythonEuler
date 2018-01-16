#!/usr/bin/env python3

from project_euler import RESOURCE_DIR
from string import ascii_uppercase


def alpha_value(word):
    result = 0
    for letter in word:
        result += ascii_uppercase.index(letter) + 1
    return result


def euler022():
    with open(f"{RESOURCE_DIR}/Euler022.txt", 'r') as names_file:
        names = [name.strip('"') for name in names_file.read().split(',')]
        names.sort()

    result = 0

    for name in names:
        result += alpha_value(name) * (names.index(name) + 1)

    return result



if __name__ == "__main__":
    print(euler022())