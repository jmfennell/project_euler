#!/usr/bin/env python3

import math

num = 600851475143

def is_prime(i):
    largest = math.ceil(math.sqrt(i))
    for j in range(2, largest+1):
        if i % j == 0:
            return False;
    return True

def main():
    largest = math.ceil(math.sqrt(num))
    for j in range(largest,0,-1):
        if num%j==0 and is_prime(j):
            print(j)
            break;

if __name__ == '__main__':
    main()