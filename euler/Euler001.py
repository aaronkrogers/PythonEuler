#!/usr/bin/env python3


def euler001() -> int:
    """
    --Multiples of 3 and 5--
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    
    Return solution to project euler #1
    """
    values = set()  # Using a set to eliminate duplicate values
    for i in range(0, 1000, 3):
        # Add all numbers divisible by 3 to set of values
        values.add(i)
    for i in range(0, 1000, 5):
        # Add all numbers divisible by 5 to set of values
        values.add(i)
    return sum(values)


if __name__ == "__main__":
    print(euler001())
