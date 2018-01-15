#!/usr/bin/env python3

import pyprimes
from itertools import count


def euler046():
    for C in count(644):
        for i in range(4):
            if len(list(pyprimes.factorise(C+i))) != 4:
                break
        else:
            return C


if __name__ == "__main__":
    print(euler046())