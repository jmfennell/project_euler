#!/usr/bin/env python3

import itertools

def main():
    digits = list(str(x) for x in range(0,10))
    perms = list(itertools.permutations(digits))
    perm_list = [''.join(i) for i in perms]
    print(perm_list[999999])
if __name__ == '__main__':
    main()