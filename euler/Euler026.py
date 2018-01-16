#!/usr/bin/env python3


def cycle_size(n, d):
    n_values = []
    while True:
        n *= 10
        t = n // d
        n = n - t*d

        if n not in n_values:
            n_values.append(n)
        else:
            i = n_values.index(n)
            return len(n_values[i:])


def euler026():
    result = tuple()
    for d in range(1, 1000):
        size = cycle_size(1, d)
        if (size, d) > result:
            result = size, d

    return result[1]


if __name__ == '__main__':
    print(euler026())