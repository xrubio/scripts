#!/usr/bin/python
import os, sys, random, math
import argparse

def calculateTrend(inputLine, outputFile, separator, timeStep):
	splittedInputLine = inputLine.split(separator)
	for i in range(len(splittedInputLine)):
		if i==0:
			outputFile.write(str(0))
		else:
			if splittedInputLine[i]=='' or splittedInputLine[i-1]=='':
				outputFile.write('')
			else:
				base = 50
				height = float(splittedInputLine[i])-float(splittedInputLine[i-1])
				hypot = math.hypot(base, height)
				angle = math.asin(height/hypot)
				outputFile.write(separator+str(math.degrees(angle)))
	outputFile.write('\n')

def main():
	parser = argparse.ArgumentParser(description='generates a file with the slope variation every time step, using timeStep=50 and applying simple triangle calculations')
	parser.add_argument('-i', '--input', default='distNaturalRoutesMC.csv', help='file where values are stored')
	parser.add_argument('-o', '--output', default='dataTrend.csv', help='output file')
	parser.add_argument('-s', '--separator', default=';', help='separator token between values')
	args = parser.parse_args()

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50

	inputFile = open(args.input, 'r')
	outputFile = open(args.output, 'w')

	# header
	outputFile.write(inputFile.readline())
	for inputLine in inputFile:
		calculateTrend(inputLine, outputFile, args.separator, timeStep)

	inputFile.close()
	outputFile.close()

if __name__ == "__main__":
    main()

