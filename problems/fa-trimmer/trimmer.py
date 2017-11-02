#!/usr/bin/env python3
"""docstring"""

import argparse
import sys

#-----------------------------------------------------------------
def get_args():
	"""get args"""
	parser = argparse.ArgumentParser(description='FASTA trimmer')
	parser.add_argument('file', metavar='fasta file', help='FASTA file')
	parser.add_argument('-s', '--start', help='Start position,
				metavar='int', type=int, default=1)
	
