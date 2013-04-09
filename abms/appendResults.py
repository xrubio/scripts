#!/usr/bin/python
import os, sys, random
import argparse

# this script processes all the log simulations in one dir into one file ignoring headers

def prepareProcess(inputDir,simulationFile, separator, output ):
	output = open(output, 'w')	
	simulation = open(inputDir+'/'+simulationFile, 'r')

	output.write(simulation.readline())
	output.close()

def processSimulation(inputDir, simulationFile, separator, outputName):
	# copy content
	outputTmp = open('tmp', 'w')
	output = open(outputName, 'r')

	for line in output.readlines():
		outputTmp.write(line)
	output.close()

	# new content
	simulation = open(inputDir+'/'+simulationFile, 'r')
	# avoid header
	simulation.readline()
	for simulationLine in simulation:
		outputTmp.write(simulationLine)
	
	simulation.close()	
	outputTmp.close()
	os.rename('tmp', outputName)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', default='input', help='directory where simulated files are stored')
	parser.add_argument('-o', '--output', default='results.csv', help='output file')
	parser.add_argument('-s', '--separator', default=';', help='separator token between values')
	args = parser.parse_args()

	outputFile = open(args.output, 'w')
	outputFile.close()

	header = 0
	for root, dirs, simulationFiles in os.walk(args.input):
		for simulationFile in simulationFiles:
			if not simulationFile.endswith('.csv'):
				continue
			if header == 0:
				prepareProcess(args.input,simulationFile, args.separator, args.output)
				header = 1
			print 'processing simulation results in file: ' + simulationFile
			processSimulation(args.input, simulationFile, args.separator, args.output)

if __name__ == "__main__":
    main()

