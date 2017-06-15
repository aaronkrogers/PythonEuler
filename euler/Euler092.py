#!/usr/bin/env python3


def square_digit_sum(num):
    result = 0
    for n in str(num):
        result += int(n) ** 2
    return result


def euler092():
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