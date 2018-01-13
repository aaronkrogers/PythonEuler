#!/usr/bin/env python3

from project_euler import RESOURCE_DIR
from itertools import product


class Digit:
    def __init__(self, digit):
        self.value = digit
        self.before = set()  # digits after self
        self.after = set()   # digits before self

    def is_after(self, n):
        """Return True if self is after n
        """
        return n in self.after

    def is_before(self, n):
        """Return True if self is before n
        """
        return n in self.before

    def __lt__(self, other):
        return self.is_before(other.value)

    def __gt__(self, other):
        return self.is_after(other.value)

    def __eq__(self, other):
        self.value == other.value

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


def euler079() -> str:
    """Passcode Derivation
    A common security method used for online banking is to ask the user
    for three random characters from a passcode. For example, if the
    passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
    the expected reply would be: 317.

    The text file, keylog.txt, contains fifty successful login attempts.

    Given that the three characters are always asked for in order,
    analyse the file so as to determine the shortest possible secret
    passcode of unknown length."""
    with open(f"{RESOURCE_DIR}/Euler079.txt", 'r') as keylog:
        log = set(map(str.rstrip, keylog))

    digits = {}

    for line, index in product(log, range(3)):
        if line[index] in digits:
            digit = digits[line[index]]
        else:
            digit = Digit(line[index])
            digits[line[index]] = digit

        digit.before.update(set(line[index+1:]))
        digit.after.update(set(line[:index]))

    return ''.join(str(d) for d in sorted(digits.values()))


if __name__ == "__main__":
    print(euler079())
