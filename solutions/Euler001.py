#!/usr/bin/env python3

###
# --Multiples of 3 and 5--
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
###


def main():
    """
    Return the sum of all natural numbers below 1000 that are
    multiples of 3 or 5
    """
    results = set()
    for i in range(0, 1000, 3):
        results.add(i)
    for i in range(0, 1000, 5):
        results.add(i)
    print(sum(results))

if __name__ == "__main__":
    main()
