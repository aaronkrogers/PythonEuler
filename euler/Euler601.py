#!/usr/bin/env python

from math import gcd


def lcm(lst):
    output = lst[0]
    for i in lst:
        number = i
        output *= number // gcd(output, number)
    return output


def P(s, N):
    if s == 1:
        return (N-1)//2
    else:
        npk = lcm([_ for _ in range(2, s + 1)])
        npo = lcm([_ for _ in range(2, s + 2)])
        return (N-2) // npk - (N-2) // npo


def euler601():
    return sum(P(i, 4**i) for i in range(1, 31+1))


if __name__ == "__main__":
    print(euler601())