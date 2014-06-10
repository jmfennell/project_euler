#!/usr/bin/env python3

from math import factorial

def main():
	fac = str(factorial(100))
	print (sum([int(fac[i]) for i in range(len(fac))]))

if __name__ == '__main__':
	main()