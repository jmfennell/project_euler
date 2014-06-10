#!/usr/bin/env python3

def row_sum(rows, row_num):
	for i in range(len(rows[row_num])):
		rows[row_num][i] += max(rows[row_num + 1][i], rows[row_num + 1][i + 1])
	if len(rows[row_num]) == 1:
		return rows[row_num][0]
	else:
		return row_sum(rows, row_num - 1)

def main():
	rows = []
	with open('triangle.txt') as f:
		for line in f:
			rows.append([int(i) for i in line.split(" ")])
	print(row_sum(rows, len(rows) - 2))
if __name__ == '__main__':
	main()