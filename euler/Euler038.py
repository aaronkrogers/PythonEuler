#!/usr/bin/env python3

from itertools import permutations


def make_chunks(seq):
    """Create chunks of seq
    so that result is suitable for
    testing as a pandigital multiple
    """
    c_maps = [[2, 2, 2, 3],
              [3, 3, 3],
              [4, 5]]

    for c_map in c_maps:
        index = 0
        output = []
        for item in c_map:
            output.append(int(seq[index:index+item]))
            index += item

        yield output


def is_pan_product(num) -> bool:
    num = str(num)
    for chunk_set in make_chunks(num):
        for index in range(len(chunk_set)):
            chunk_set[index] /= index + 1
        if len(set(chunk_set)) == 1:
            return True
    return False


def euler038() -> str:
    for p in permutations("987654321"):
        seq = ''.join(p)
        if is_pan_product(seq):
            return seq


if __name__ == "__main__":
    print(euler038())
