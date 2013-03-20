#!/usr/bin/python
import os, sys, random
import argparse

def applyWindow(inputLine, outputFile, separator, offset):
	splittedInputLine = inputLine.split(separator)
	for i in range(len(splittedInputLine)):
		sumSamples = 0.0
		numSamples = 0.0
		for j in range(i-offset, i+1+offset):
			if j>=0 and j<len(splittedInputLine) and splittedInputLine[j]!='':
				sumSamples = sumSamples+float(splittedInputLine[j])
				numSamples = numSamples+1.0

		if numSamples != 0:
			outputFile.write(str(sumSamples/numSamples))

		if i != len(splittedInputLine)-1:
			outputFile.write(separator)
		else:
			outputFile.write('\n')

def main():
	parser = argparse.ArgumentParser(description='applies a sliding window to a dataset, calculating the average value around each time step')
	parser.add_argument('-i', '--input', default='distNaturalRoutesMC.csv', help='file where values are stored')
	parser.add_argument('-o', '--output', default='windowOutput.csv', help='output file')
	parser.add_argument('-s', '--separator', default=';', help='separator token between values')
	parser.add_argument('-w', '--window', default='3', help='window size, being the original sample in the middle (it should be odd)')
	args = parser.parse_args()

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50

	inputFile = open(args.input, 'r')
	outputFile = open(args.output, 'w')

	# header
	outputFile.write(inputFile.readline())
	offset = (int(args.window)-1)/2
	for inputLine in inputFile:
		applyWindow(inputLine, outputFile, args.separator, offset)

	inputFile.close()
	outputFile.close()

if __name__ == "__main__":
    main()

