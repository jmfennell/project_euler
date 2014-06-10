#!/usr/bin/env python3

from math import factorial

n = 20

def main():
	print (int((factorial(2 * n) / (factorial(n) * factorial(n)))))

if __name__ == '__main__':
	main()