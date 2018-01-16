#!/usr/bin/env python


def euler016():
    """
    --- Power digit sum ---
    What is the sum of the digits of the number 2**1000
    """
    return sum(int(n) for n in str(2**1000))


if __name__ == "__main__":
    print(euler016())