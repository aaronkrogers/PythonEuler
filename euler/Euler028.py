#!/usr/bin/env python3


def spiral_sum(spiral_size):
    assert spiral_size % 2 != 0, 'spiral_size must be an odd integer'

    size = 1
    current = 1
    additive = 2
    output = 1

    while size < spiral_size:
        for _ in range(4):
            current += additive
            output += current
        additive += 2
        size += 2

    return output


def euler028():
    """
    --- Number spiral diagonals ---
    What is the sum of the numbers on the diagonals in a 1001x10001
    spiral formed by starting with 1 and moving in a clockwise direction?
    """
    return spiral_sum(1001)


if __name__ == "__main__":
    print(euler028())