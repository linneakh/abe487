#!/usr/bin/env python3

import sys
import os

def main():
	"""main"""
	args= sys.argv

	if len(args) < 2:
		script = os.path.basename(args[0])
		print('Usage: {} sequence'.format(script))
		sys.exit(1)
	
	count_a, count_g, count_t, count_c = 0,0,0,0
	
	for letter in args[1]:
		if letter == 'g' or letter == 'G':
			count_g += 1
		elif letter == 'c' or letter == 'C':
			count_c += 1
		elif letter == 'a' or letter == 'A':
			count_a += 1
		elif letter == 't' or letter == 'T':
			count_t += 1
	total_count = count_a + count_g + count_t + count_c
	total_gc = count_g + count_c
	perc_gc = total_gc/total_count *100
	
	print ('{}% GC'.format(int(perc_gc))) 

if __name__=='__main__':
        main()


		
