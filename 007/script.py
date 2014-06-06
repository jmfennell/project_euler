#!/usr/bin/env python3

import math

n = 10001

def is_prime(i):
    largest = math.ceil(math.sqrt(i))
    for j in range(2, largest+1):
        if i % j == 0:
            return False;
    return True

def main():
	prime = 2
	i = 1
	j = 3
	while i < n:
		if is_prime(j):
			prime = j
			i += 1
		j += 2
	print(prime)

if __name__ == '__main__':
    main()