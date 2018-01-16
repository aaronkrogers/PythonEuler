#!/usr/bin/env python3

from project_euler import RESOURCE_DIR


def shrink(triangle):
    for i in range(len(triangle[-2])):
        triangle[-2][i] += max(triangle[-1][i:i+2])
    triangle.pop()
    return triangle


def euler018(filename):
    """
    --- Maximum path sum ---
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

    3
    7 4
    2 4 6
    8 5 9 3
    
    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle
    """
    triangle = []
    with open(f'{RESOURCE_DIR}/{filename}', 'r') as triangle_file:
        for line in triangle_file.read().splitlines():
            triangle.append([int(i) for i in line.split(' ')])

    while len(triangle) != 1:
        triangle = shrink(triangle)

    return triangle[0][0]


if __name__ == "__main__":
    print(euler018('Euler018.txt'))