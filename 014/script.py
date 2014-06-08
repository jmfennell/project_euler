#!/usr/bin/env python3

limit = 1000000

def main():
	lengths = [0] * limit
	lengths[1] = 1
	max_length = [1,1]

	for i in range(1, limit):
		n = i
		length = 0
		unknown_lengths = []
		while (n > limit - 1) or (lengths[n] < 1):
			unknown_lengths.append(n)
			if n % 2 == 0:
				n = int(n / 2)
			else:
				n = 3*n + 1
			length += 1

		for j in range(length):
			m = unknown_lengths[j]
			if m < limit:
				new_length = length + lengths[n] - j
				lengths[m] = new_length
				if new_length > max_length[1]:
					max_length = [i,new_length]
	print(max_length[0])

if __name__ == '__main__':
	main()