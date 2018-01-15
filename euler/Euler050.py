#!/usr/bin/env python3

import pyprimes


def euler050():
    """Consecutive Prime Sum
    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds
    to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand
    that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of
    the most consecutive primes?
    """
    primes = []
    prime_sum = 0

    for prime in pyprimes.primes():
        if prime_sum + prime > 1000000:
            break
        else:
            prime_sum += prime
            primes.append(prime)

    for size in range(len(primes)-1, 0, -1):
        start = 0
        end = start + size
        while end <= len(primes):
            prime_sum = sum(primes[start:end])
            if pyprimes.isprime(prime_sum):
                return prime_sum
            else:
                start += 1
                end += 1


if __name__ == "__main__":
    print(euler050())