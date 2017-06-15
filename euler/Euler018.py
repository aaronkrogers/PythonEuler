#!/usr/bin/env python3

from definitions import RESOURCE_DIR


def shrink(triangle):
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i:i+2])
    triangle.pop()
    return triangle


def euler018(filename):
    triangle = []
    with open(f'{RESOURCE_DIR}/{filename}', 'r') as triangle_file:
        for line in triangle_file.read().splitlines():
            triangle.append([int(i) for i in line.split(' ')])

    while len(triangle) != 1:
        triangle = shrink(triangle)

    return triangle[0][0]


if __name__ == "__main__":
    print(euler018('Euler018.txt'))