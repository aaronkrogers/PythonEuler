#!/usr/bin/env python3


def sum_of_squares(upper_bound):
    """
    Return the sum of the squares for every number from 1 to upper_bound
    :param upper_bound: int
    :return: int
    """
    return sum(x ** 2 for x in range(1, upper_bound + 1))


def square_of_sum(upper_bound):
    """
    Return the square of the sum of each number from 1 to upper_bound
    :param upper_bound: int
    :return: int
    """
    return sum(range(1, upper_bound + 1)) ** 2


def euler006(upper_bound=100):
    """
    ---Sum square difference---
    The sum of the squares of the first ten natural numbers is:    
    12 + 22 + ... + 102 = 385
    
    The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)2 = 552 = 3025
    
    Hence the difference between the sum of the squares of the first ten natural numbers
    and the square of the sum is 3025 − 385 = 2640.
    
    Find the difference between the sum of the squares of the first one hundred natural
    numbers and the square of the sum.
    :param upper_bound: int
    :return: int
    """
    return square_of_sum(upper_bound) - sum_of_squares(upper_bound)


if __name__ == "__main__":
    print(euler006())
