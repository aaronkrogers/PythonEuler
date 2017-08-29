#!/usr/bin/env python3


def square_digit_sum(num):
    result = 0
    for n in str(num):
        result += int(n) ** 2
    return result


def square_digit_chain(num):
    yield num
    while num not in (1, 89):
        num = square_digit_sum(num)
        yield num


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
    known = {1: 1, 89: 89}
    result = 0

    for number in range(1, 10000000):
        chain = []
        for link in square_digit_chain(number):
            if link in known:
                known.update({l: known[link] for l in chain})
                if known[link] == 89:
                    result += 1
                break
            else:
                chain.append(link)

    return result


if __name__ == '__main__':
    print(euler092())
