#!/usr/bin/env python3

import math
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
    return set(factors)

@lru_cache(maxsize=None)
def sum_of_factors(m):
    num = 0
    for i in factors(m):
        num+=i
    return num

def is_abundant(n):
    if n < 12:
        return False
    return sum_of_factors(n) > n

def is_abundant_sum(n):
   for i in abundants:
       if i > n:
         return False
       if (n - i) in abundants:
           return True
   return False

abundants = set(x for x in range(1, 28123) if is_abundant(x))

def main():
    sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))
    print(sum_of_non_abundants)
if __name__ == '__main__':
    main()