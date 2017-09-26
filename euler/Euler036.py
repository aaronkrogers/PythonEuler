#!/usr/bin/env python3


def is_bin_palindrome(num: int) -> bool:
    binary = bin(num)[2:]
    return binary == binary[::-1]


def is_palindrome(num: int) -> bool:
    num = str(num)
    return num == num[::-1]


def euler036() -> int:
    """Double-base palindromes
    The decimal number, 585 = 10010010012 (binary), is
    palindromic in both bases.

    Find the sum of all numbers, less than one million,
    which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base,
    may not include leading zeros.)
    """
    # Only test odd numbers since even binary numbers would
    # have a leading zero when reversed
    return sum([n for n in range(1, 1_000_000, 2)
                if is_palindrome(n) and is_bin_palindrome(n)])


if __name__ == "__main__":
    print(euler036())
