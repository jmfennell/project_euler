#!/usr/bin/env python3

from datetime import date

def main():
	sum_ = 0
	for y in range(1901, 2001):
		for m in range(1,13):
			if date(y, m, 1).weekday() == 6:
				sum_ += 1
	print(sum_)

if __name__ == '__main__':
	main()