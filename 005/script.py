#!/usr/bin/env python3

num = 20
step = 2520

def divisible(i):
    count_ = 0;
    for j in range(1, num+1):
        if i%j == 0:
            count_ += 1
            if count_ == num:
                return i
        else:
            return 1

def main():
    n = step
    while True:
        smallest = divisible(n)
        if smallest != 1:
            print(smallest)
            return
        else:
            n += step

if __name__ == '__main__':
    main()