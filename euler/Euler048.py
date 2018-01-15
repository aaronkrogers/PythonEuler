#!/usr/bin/env python3


def euler048():
    """Self Powers
    The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000
    """
    return str(sum(i**i for i in range(1, 1001)))[-10:]


if __name__ == "__main__":
    print(euler048())