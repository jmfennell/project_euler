#!/usr/bin/env python3

units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def int2text(n):
	n_str = str(n)
	if n == 1000:
		return 'onethousand'
	elif len(n_str) == 3:
		if n_str[1] == '0' and n_str[2] == '0':
			return units[int(n_str[0])]+'hundred'
		elif n_str[1] == '1':
			return units[int(n_str[0])]+'hundredand'+teens[int(n_str[2])]
		else:
			return units[int(n_str[0])]+'hundredand'+tens[int(n_str[1])]+units[int(n_str[2])]
	elif n < 10:
		return units[n]
	elif 10 <= n < 20:
		return teens[int(n_str[1])]
	else:
		return tens[int(n_str[0])]+units[int(n_str[1])]

def main():
	sum_ = 0
	for i in range (1, 1001):
		sum_ += len(int2text(i))
	print(sum_)

if __name__ == '__main__':
	main()