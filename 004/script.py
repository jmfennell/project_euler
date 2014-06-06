#!/usr/bin/env python3

def is_pallindrome(i):
    str_ = str(i)
    str_rev = rev(str_)
    return str_ == str_rev

def rev(s):
    return s[::-1]

def main():
    i=999
    j=999
    palindromes = []
    for m in range(i,100,-1):
        for n in range(j,100,-1):
            if is_pallindrome(m * n):
                palindromes.append(m*n)
    print(max(palindromes))

if __name__ == '__main__':
    main()