#!/usr/bin/env python3

from itertools import count
from functools import lru_cache

max_val = 4000000
@lru_cache(maxsize=None)
def fib(i):
    if i <= 2:
        return i
    return fib(i-1) + fib(i-2)

def main():
    num = 0
    for i in count():
        if fib(i) > max_val:
            break
        if fib(i) % 2 == 0:
            num += fib(i)

    print(num)

if __name__ == '__main__':
    main()