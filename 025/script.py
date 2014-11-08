#!/usr/bin/env python3

from functools import lru_cache
from itertools import count

length = 1000

@lru_cache(maxsize=None)
def fib(i):
    if i <= 2:
        return i
    return fib(i-1) + fib(i-2)

def main():
	for i in count():
		l = str(fib(i))
		if len(l) == length:
			print(i+1)
			break

if __name__ == '__main__':
    main()