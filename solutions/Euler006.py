#!/usr/bin/env python3


def sum_of_squares(upper_bound):
    """
    Return the sum of the squares for every number from 1 to upper_bound
    :param upper_bound: int
    :return: int
    """
    return sum(x**2 for x in range(1, upper_bound+1))


def square_of_sum(upper_bound):
    """
    Return the square of the sum of each number from 1 to upper_bound
    :param upper_bound: int
    :return: int2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    return sum(range(1, upper_bound+1)) ** 2


def euler006(upper_bound=100):
    return square_of_sum(upper_bound) - sum_of_squares(upper_bound)

if __name__ == "__main__":
    print(euler006())