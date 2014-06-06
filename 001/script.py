#!/usr/bin/env python3

from itertools import count

max = 1000

def multiple(i):
    return (i % 3 == 0) or (i % 5 == 0)

def main():
    num = 0
    for i in count():
        if i >= max:
            break;
        if multiple(i):
            num += i
    print(num)

if __name__ == '__main__':
    main()