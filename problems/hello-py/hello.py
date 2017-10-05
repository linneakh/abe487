#!/usr/bin/env python3

import sys
import os

def main():
	"""main"""
	args= sys.argv

	x=len(args)


	if x < 2:
		script = os.path.basename(args[0])
		print('Usage: {} NAME [NAME2 ...]'.format(script))
		sys.exit(1)
	elif x == 2:
		print('Hello to the 1 of you: {}!'.format(args[1]))
	elif x == 3:
		print('Hello to the 2 of you: {}!'.format(' and '.join(args[1:x])))

	else:
		
		print('Hello to the {} of you: {}, and {}!'.format(x-1,', '.join(args[1:x-1]), args[x-1]))

if __name__=='__main__':
	main()


