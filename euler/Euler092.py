#!/usr/bin/env python3


def square_digit_sum(num):
    result = 0
    for n in str(num):
        result += int(n) ** 2
    return result


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
    known = {}
    result = 0

    for i in range(1, 10000000):
        chain = [i]
        link = i

        while 1:
            link = known.get(link, link)
            if link in (1, 89):
                break
            link = square_digit_sum(link)
            chain.append(link)

        if link == 89:
            result += 1

        known.update({n: link for n in chain})

    return result

if __name__ == '__main__':
    print(euler092())