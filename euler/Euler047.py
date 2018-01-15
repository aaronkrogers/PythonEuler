#!/usr/bin/env python3

import pyprimes
from itertools import count


def euler046():
    for C in count(1):
        for i in range(3):
            if len(list(pyprimes.factorise(C+i))) != 3:
                break
        else:
            return


if __name__ == "__main__":
    euler046()