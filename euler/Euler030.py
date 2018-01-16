#!/usr/bin/env python3


from itertools import count, combinations_with_replacement as cwr
from project_euler import int2digits


def euler030():
    """Digit Fifth Powers
    Surprisingly there are only three numbers that can be 
    written as the sum of fourth powers of their digits:

    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
    As 1 = 14 is not a sum it is not included.
    
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as 
    the sum of fifth powers of their digits.
    """
    output = 0
    results = dict()

    for c in count(2):
        results[c] = set()
        # Iterate through c-length combinations of all
        # digits from 0-9
        for combination in cwr(range(10), c):
            dps = sum(d**5 for d in combination)
            # Check that the result of digit_power_sum has
            # exactly the same digits as our original number
            if sorted(int2digits(dps)) == sorted(combination):
                results[c].add(dps)

        # results[c] will remain empty until we have reached the
        # first set of results and will become empty once again
        # after it has found the last set of results.
        # Therefore we will discard empty sets within results and
        # at that point only finish when results[c] is no longer populated
        if not results[c]:  # Discard empty sets within results
            results.pop(c)
            if results:     # Do if results is not empty
                for k, v in results.items():
                    output += sum(v)
                return output


if __name__ == "__main__":
    print(euler030())
