#!/usr/bin/env python3

max_ = 100

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1,n+1))

def square_of_sum(n):
    sum_ = sum(i for i in range(1,n+1))
    return sum_**2


def main():
    print (square_of_sum(max_) - sum_of_squares(max_))

if __name__ == '__main__':
    main()