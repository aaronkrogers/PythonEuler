#!/usr/bin/env python3

from definitions import RESOURCE_DIR


class Roman:
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
           'C': 100, 'D': 500, 'M': 1000}
    rmap = {value: key for key, value in map.items()}
    rmap.update({4: 'IV', 9: 'IX',
                 40: 'XL', 90: 'XC',
                 400: 'CD', 900: 'CM'})

    def __init__(self, roman: str):
        """Initialize class
        :param roman: Number in roman numeral format
        """
        self.roman_value = roman
        self.value = self.get_value()
        self.preferred = self.optimize()

    def get_value(self):
        result = 0
        skip = False
        for index in range(len(self.roman_value)):
            value_pair = self.roman_value[index:index+2]
            if skip:
                skip = False
                continue
            elif ((len(value_pair) == 2) and
                    (self.map[value_pair[0]] < self.map[value_pair[1]])):
                result += (self.map[value_pair[1]]
                           - self.map[value_pair[0]])
                skip = True
            else:
                result += self.map[self.roman_value[index]]
        return result

    def optimize(self):
        result = ""
        value = self.value
        digits = sorted(self.rmap.keys(), reverse=True)
        for digit in digits:
            while value - digit >= 0:
                value -= digit
                result += self.rmap[digit]
        return result

    def space_saved(self):
        return len(self.roman_value) - len(self.preferred)

    def __repr__(self):
        return self.preferred


def euler089():
    result = 0
    with open(f"{RESOURCE_DIR}/Euler089.txt", 'r') as roman_file:
        for line in roman_file:
            roman = Roman(line.strip())
            result += roman.space_saved()

    return result


if __name__ == "__main__":
    print(euler089())