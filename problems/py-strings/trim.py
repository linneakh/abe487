#!/usr/bin/env python3

import sys
import os

def main():
	"""main"""
	args= sys.argv

	if len(args) < 2:
		script = os.path.basename(args[0])
		print ('Usage: {} sequence or filename'.format(script))
		sys.exit(1)
	
	seq = args[1]
	
	if len(args) == 3:
		trim = int(args[2])
	else:
		trim = 5
	
	if os.path.isfile(seq):
		s = open(seq)
		for line in s:		
			print ('{}'.format(line[0:(trim)]))
	else: 
		print ('{}'.format(seq[0:(trim)]))

if __name__=='__main__':
        main()

