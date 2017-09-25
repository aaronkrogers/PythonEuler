#!/usr/bin/env python3

from fractions import Fraction


def converge(seq: list) -> Fraction:
    """Return the convergent of the infinite
    fraction represented by the terms in seq.
    The length of seq will be the nth convergent
    of our infinite fraction. For example a seq
    of len 10 will return the 10th convergent of
    our fraction
    """
    assert type(seq) is list, "seq must be of type list"
    assert len(seq) > 1, "seq must have at least two items"

    whole_part = seq.pop(0)
    fractal_part = 1 / Fraction(seq.pop())

    while seq:
        fractal_part = 1 / (seq.pop() + fractal_part)

    return whole_part + fractal_part


def e_fractal_terms(n: int) -> list:
    """Return a list of the first n terms
    of the infinite fraction for e"""
    assert type(n) is int, f"n must be of type int, not type(n)"

    result = []
    special = 0

    for i in range(1, n+1):
        if i == 1:
            result.append(2)
        elif i % 3 == 0:
            special += 2
            result.append(special)
        else:
            result.append(1)

    return result


def euler065() -> int:
    """Convergents of e
    The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
    The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

    Find the sum of digits in the numerator of the 100th convergent of the
    continued fraction for e.
    """
    convergent = converge(e_fractal_terms(100))
    return sum(int(d) for d in str(convergent.numerator))


if __name__ == "__main__":
    print(euler065())
