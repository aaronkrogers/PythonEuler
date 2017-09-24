#!/usr/bin/env python3


def euler019():
    """
    --- Counting Sundays ---
    How many Sundays fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    return int((12 * 100) / 7)

if __name__ == '__main__':
    print(euler019())