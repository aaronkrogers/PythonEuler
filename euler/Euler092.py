#!/usr/bin/env python3

from itertools import combinations_with_replacement as cwr
from itertools import permutations


def square_digit_end(array) -> int:
    """Return the end result of a square digit chain of a given number
    :param array: An array of digits in the number to be tested
    :return: The end of the square digit chain
    """
    link = sum(d**2 for d in array)
    while link not in (0, 1, 89):
        array = list(str(link))
        array = [int(d) for d in array]
        link = sum(d**2 for d in array)
    return link


def euler092() -> int:
    """
    --- Square digit chains ---
    A number chain is created by continuously adding the square
    of the digits in a number to form a new number until it
    has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck
    in an endless loop. What is most amazing is that EVERY
    starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """
    result = 0
    # Iterate through all combinations of the numbers 0-9 below 10 million
    for number in cwr(range(10), 7):
        if square_digit_end(number) == 89:
            # Add the count of all permutations of the successful digits
            result += len(set(permutations(number)))
    return result


if __name__ == '__main__':
    print(euler092())