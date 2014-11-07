#!/usr/bin/env python3

import math
from itertools import count
from functools import lru_cache

@lru_cache(maxsize=None)
def factors(n):
    factors = []
    top = math.ceil(math.sqrt(n))
    for i in range(1,top + 1):
        if n % i == 0:
            if (i < n):
                factors.append(i)
            if i != top and int(n / i) != n:
                factors.append(int(n / i))
    return factors

@lru_cache(maxsize=None)
def sum_of_factors(m):
    num = 0
    for i in factors(m):
        num+=i
    return num


def main():
    amicable_numbers = []
    for i in range(0,10001):
        a = sum_of_factors(i)
        b = sum_of_factors(a)
        if (a > i and b == i):
            amicable_numbers.append(i)
            amicable_numbers.append(a)
    print(sum(amicable_numbers))
    

if __name__ == '__main__':
    main();