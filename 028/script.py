#!/usr/bin/env python3

import math

def main():
    gridSize = 1001
    maxNum = gridSize ** 2
    sum = 0

    sum = 25
    iteration = 2
    count = 0
    added_in_iteration = 0
    number_to_skip = 3
    for i in range(10, maxNum+1):
        count += 1
        if count > number_to_skip:
            sum += i
            count = 0
            added_in_iteration += 1
        if added_in_iteration == 4:
            added_in_iteration = 0
            number_to_skip += 2
    print(sum)

if __name__ == '__main__':
    main()