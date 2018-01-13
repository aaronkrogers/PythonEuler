#!/usr/bin/env python3

from math import sqrt
from project_euler import RESOURCE_DIR


def is_triangle(num):
    """Test if num is a triangle number
    """
    if (-1 + sqrt(1 + (8*num)))/2 % 1 == 0:
        return True


def euler042():
    """Coded Triangle Numbers
    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
    so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
    If the word value is a triangle number then we shall call the word
    a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text
    file containing nearly two-thousand common English words,
    how many are triangle words?
    """
    result = 0
    with open(f"{RESOURCE_DIR}/Euler042.txt", "r") as file:
        words = [word.strip('"') for word in file.read().split(",")]
        for word in words:
            letter_sum = 0  # Sum of index values for each letter in the word
            for letter in word:
                letter_sum += ord(letter)-64  # Get index of letter
            if is_triangle(letter_sum):
                result += 1
    return result


if __name__ == "__main__":
    print(euler042())