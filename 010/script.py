#!/usr/bin/env python3

import math

max_ = 2000000

def prime_sieve(n):
    sieve = [True] * n
    sieve[0] = False
    sieve[1] = False

    largest = math.floor(math.sqrt(n)) + 1
    i = 2
    while i < largest:
        j = i + i
        while j < n:
            sieve[j] = False
            j += i
        while True:
            i += 1
            if sieve[i]:
                break;
    return sieve

def primes(n):
    sieve = list(enumerate(prime_sieve(n)))
    return [val for val,is_prime in sieve if is_prime]


def main():
    print(sum(primes(max_)))

if __name__ == '__main__':
    main()