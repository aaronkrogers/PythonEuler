#!/usr/bin/env python3


def num_to_word(n):
    singles = {'1': 'one', '2': 'two', '3': 'three',
               '4': 'four', '5': 'five', '6': 'six',
               '7': 'seven', '8': 'eight', '9': 'nine'}
    teens = {'10': 'ten', '11': 'eleven', '12': 'twelve',
             '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
             '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
             '19': 'nineteen'}
    tens = {'2': 'twenty', '3': 'thirty', '4': 'forty',
            '5': 'fifty', '6': 'sixty', '7': 'seventy',
            '8': 'eighty', '9': 'ninety'}

    result = []
    n = str(n)[::-1]
    for i in range(len(n)):
        value = n[i]
        if i == 0 and value in singles:
            result.append(singles[n[i]])

        if i == 1:
            if n[:2][::-1] in teens:
                result = [teens[n[:2][::-1]]]
            elif value in tens:
                result.append(tens[value])

        if i == 2 and value in singles:
            if result != []:
                result.append('and')
            result.append('hundred')
            result.append(singles[value])

        if i == 3:
            result.append('onethousand')

    return ''.join(list(reversed(result)))


def euler017():
    result = 0
    for i in range(1, 1001):
        result += len(num_to_word(i))

    return result


if __name__ == "__main__":
    print(euler017())