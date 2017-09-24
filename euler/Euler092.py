#!/usr/bin/env python3


class Chain:
    def __init__(self):
        self.known = {1: 1, 89: 89}

    def update(self, values, chain_end):
        for val in values:
            self.known[val] = chain_end

    @staticmethod
    def square_digit_sum(num):
        result = 0
        for n in str(num):
            result += int(n) ** 2
        return result

    def square_digit_chain(self, num):
        yield num
        while num not in (1, 89):
            num = self.square_digit_sum(num)
            yield num

    def chain_end(self, num):
        tmp_chain = set()
        for val in self.square_digit_chain(num):
            if val in self.known:
                result = self.known[val]
                self.update(tmp_chain, result)
                return result
            else:
                tmp_chain.add(val)

    def __call__(self, num):
        return self.chain_end(num)


def euler092():
    """
    --- Square digit chains ---
    A number chain is created by continuously adding the square of the digits in a number to form a new number until it
    has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
    starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """
    chain = Chain()
    result = 0
    for number in range(1, 10_000_000):
        if chain(number) == 89:
            result += 1
    return result


if __name__ == '__main__':
    print(euler092())