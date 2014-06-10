#!/usr/bin/env python3

from math import factorial

n = 1000

def main():
	str_ = str(2 ** n)
	sum_ = 0
	for i in range(0, len(str_)):
		sum_ += int(str_[i])
	print(sum_)

if __name__ == '__main__':
	main()