# This module is to contain constants and tools to 
# be reused throughout my Project Euler journey

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = ROOT_DIR + '/resources'


def digits2int(digits):
    return int(''.join(map(str, digits)))


def int2digits(number, as_type=int):
    assert as_type in (str, int), \
        f"as_type must be int or str, not {as_type}"

    def generator():
        for digit in str(number):
            yield as_type(digit)
    return generator()
