#!/usr/bin/env python

from math import gcd


def lcm(lst):
    output = lst[0]
    for i in lst:
        number = i
        output *= number // gcd(output, number)
    return output


def p(s, N):
    if s == 1:
        return (N-1)//2
    else:
        x0 = lcm([_ for _ in range(2, s + 1)])
        x1 = lcm([_ for _ in range(2, s + 2)])
        return (N-2) // x0 - (N-2) // x1


def euler601():
    return sum(p(i, 4**i) for i in range(1, 31+1))


if __name__ == "__main__":
    print(euler601())