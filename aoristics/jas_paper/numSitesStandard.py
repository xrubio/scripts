#!/usr/bin/python
import os, sys, random

# this script calculates the number of active sites per time step from montecarlo simulations

def processFile(numSteps, data, separator, output):
	numSites = []
	for siteLine in data:
		if siteLine.startswith('id'):
			# beginning, initialize values	
			for i in range(numSteps):
				numSites.append(0)
		else:
			splittedSiteLine = siteLine.split(separator)
			for j in range(numSteps):
				numSites[j] = numSites[j] + int(splittedSiteLine[j+4])

	for i in range(numSteps):	
		token = separator
		if i==numSteps-1:
			token = '\n'
		output.write(str(numSites[i])+token)

def main():

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50
	separator = ';'

	data = open('../data/standardValues.csv', 'r')
	output = open('../numSitesStd.csv', 'w')
	numSteps = 0
	for step in range(iniciTotal, fiTotal, -timeStep):
		token = separator
		if step==fiTotal+timeStep:
			token = '\n'
		output.write(str(step)+token)
		numSteps = numSteps+1
	
	processFile(numSteps, data, separator, output)
	data.close()
	output.close()

if __name__ == "__main__":
    main()

