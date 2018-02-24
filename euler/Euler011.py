#!/usr/bin/env python3

from itertools import product
import numpy as np
from project_euler import RESOURCE_DIR


def euler011():
    """
    --- Largest product in a grid ---
    What is the greatest product of four adjacent numbers
    in the same direction in the 20x20 grid?
    *Grid given in resources/Euler011.txt*
    """

    # Set project directory
    result = 0

    with open(f'{RESOURCE_DIR}/Euler011.txt', 'r') as grid_file:
        grid = []
        for line in grid_file:
            grid.append([int(item) for item in line.split()])

    grid = np.array(grid)
    grid_size = len(grid)

    for x, y in product(range(grid_size), range(grid_size)):
        round_results = []
        # TODO: Condense this section
        if x < grid_size-3:
            # Test for down straight
            round_results.append(grid[x:x+4, y])

        if y < grid_size - 3:
            # Test for right straight
            round_results.append(grid[x, y:y + 4])

        if y > 3 and x < grid_size-3:
            # Test for left-down diagonal
            nx = range(x, x+4)
            ny = range(y, y-4, -1)
            round_results.append(grid[nx, ny])

        if y < grid_size-3 and x < grid_size-3:
            # Test for right-down diagonal
            nx = range(x, x+4)
            ny = range(y, y+4)
            round_results.append(grid[nx, ny])

        for r in round_results:
            if mult(r) > result:
                result = mult(r)

    return result


def mult(iterable):
    result = 1
    for item in iterable:
        result *= item
    return result


if __name__ == "__main__":
    print(euler011())