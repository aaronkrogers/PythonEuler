#!/usr/bin/env python3

from itertools import count


def euler014():

    stored_results = {}

    result = 0
    top_chain = 0
    for num in range(1, 1000000):
        n = num
        for length in count(start=1):
            if n in stored_results:
                length += stored_results[n]
                break
            if n % 2 == 0:  # If n is even
                n = n // 2
            elif n % 2 != 0:           # If n is odd
                n = 3*n + 1
            if n == 1:
                break

        stored_results[num] = length

        if length > top_chain:
            top_chain = length
            result = num

    return result


if __name__ == "__main__":
    print(euler014())