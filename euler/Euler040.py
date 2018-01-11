#!/usr/bin/env python3

from itertools import count


def euler040():
    """Champernowne's constant
    An irrational decimal fraction is created by concatenating the
    positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part,
    find the value of the following expression:

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    """
    result = 1
    needed_index = 1
    current_index = 0
    for num in count():
        num = str(num)
        next_index = current_index + len(num)
        # Check if the length of the next number exceeds the next index
        # If it does then extract the necessary digit from the number
        if next_index > needed_index:
            result *= int(num[needed_index-current_index])
            needed_index *= 10
        if needed_index > 1000000:
            break
        current_index = next_index

    return result


if __name__ == "__main__":
    print(euler040())