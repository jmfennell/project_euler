#!/usr/bin/env python3

num = 1000

def main():
    for a in range(1,num,1):
        for b in range (1,num-1,1):
            c = num - a - b
            if a**2 + b**2 == c**2:
                print(a * b * c)
                return



if __name__ == '__main__':
    main()