#!/usr/bin/env python3

import sys
import os

def main():
	"""main"""
	args= sys.argv

	if len(args) < 2:
                script = os.path.basename(args[0])
                print('Usage: {} STRING'.format(script))
                sys.exit(1)
	
	count_a, count_e, count_i, count_o, count_u = 0,0,0,0,0
	
	for letter in args[1]:
		if letter == 'a' or letter == 'A':
			count_a += 1
		elif letter == 'e' or letter == 'E':
			count_e += 1
		elif letter == 'i' or letter == 'I':
			count_i += 1
		elif letter == 'o' or letter == 'O':
			count_o += 1
		elif letter == 'u' or letter == 'U':
			count_u += 1
	count = count_a + count_e + count_i + count_o + count_u
	
	if count == 1:
		print('There is {} vowel in "{}."'.format(count,args[1]))
	else:
		print('There are {} vowels in "{}."'.format(count,args[1]))

if __name__=='__main__':
	main()

