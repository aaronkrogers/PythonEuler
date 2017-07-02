#!/usr/bin/env python3


from itertools import count, combinations_with_replacement as cwr


def digit_power_sum(number, power=5):
    output = 0

    if type(number) == int:
        number = str(number)

    for digit in number:
        output += int(digit) ** power

    return output


def euler030():
    output = 0
    results = dict()

    for c in count(2):
        results[c] = set()
        for combination in cwr(range(10), c):
            dps = digit_power_sum(combination)
            if sorted(map(int, str(dps))) == sorted(combination):
                results[c].add(dps)

        if results[c] == set():
            results.pop(c)
            if results != dict():
                for k, v in results.items():
                    output += sum(v)
                return output

if __name__ == "__main__":
    print(euler030())