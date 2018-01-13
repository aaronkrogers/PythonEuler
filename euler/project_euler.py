import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = ROOT_DIR + '/resources'


def list2int(array):
    result = 0
    for a in array:
        result *= 10
        result += a
    return result