#!/usr/bin/env python3

import math
from itertools import count

def triangle(n):
    return sum(range(n+1))

def factors(n):
    factors = []
    top = math.floor(math.sqrt(n))
    for i in range(1,top + 1):
        if n % i == 0:
            factors.append(i)
            if i != top:
                factors.append(int(n / i))
    return factors
    

def main():
    for i in count():
        tri = triangle(i)
        facts = factors(tri)
        if len(facts) > 500:
            print(tri)
            return

if __name__ == '__main__':
    main()