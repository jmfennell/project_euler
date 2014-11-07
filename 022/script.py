#!/usr/bin/env python3

import string

def name_score(name, position):
	nums = []
	for char in name.lower():
		nums.append(ord(char) - 96)
	return (sum(nums) * position)


def main():
	rows = []
	with open('names.txt') as f:
		names_string = f.read().replace('"', '')
		names = sorted(names_string.split(','))
		scores = []
		for i,name in enumerate(names, start=1):
			score = name_score(name, i)
			scores.append(score)
		print(sum(scores))
if __name__ == '__main__':
	main()