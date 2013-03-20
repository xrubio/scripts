#!/usr/bin/python
import os, sys, random, math
import argparse
import csv
from itertools import izip

def transpose(inputFile, outputFile, separator):
	file = csv.reader(open(inputFile, "rb"), delimiter=separator)
	a = izip(*file)
	csv.writer(open(outputFile, "wb"), delimiter=separator).writerows(a)
	
def main():
	parser = argparse.ArgumentParser(description='transpose a csv file')
	parser.add_argument('-i', '--input', default='inputFile.csv', help='file where values are stored')
	parser.add_argument('-o', '--output', default='outputFile.csv', help='output file')
	parser.add_argument('-s', '--separator', default=';', help='separator token between values')
	args = parser.parse_args()

	transpose(args.input, args.output, args.separator)
	
if __name__ == "__main__":
    main()


