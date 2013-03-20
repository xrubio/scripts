#!/usr/bin/python
import os, sys, random

# this script calculates the number of active sites per time step from montecarlo simulations

def processFile(numSteps, data, separator, output):
	
	numSites = []
	distNaturalRoutes = []
	
	for siteLine in data:
		if siteLine.startswith('id'):
			# beginning, initialize values	
			for i in range(numSteps):
				numSites.append(0)
				distNaturalRoutes.append(0)
		else:	
			splittedSiteLine = siteLine.split(separator)
			x = splittedSiteLine[2]
			y = splittedSiteLine[3]

			os.system('r.what input=distance east_north='+x+','+y + ' fs=";" > tmp')
			tmpFile = open('tmp', 'r')
			tmpData = tmpFile.readline()
			splittedTmpData = tmpData.split(';')
			value = float(splittedTmpData[3])
			tmpFile.close()
			os.system('rm tmp')
#			print splittedSiteLine[1] + ' with location: ' + x + '/' + y + ' is far from natural route: ' + str(value)

			for j in range(numSteps):
				exists = int(splittedSiteLine[j+4])
				if exists == 1:
					# fer consulta i agafar valor com sigui
					distNaturalRoutes[j] = distNaturalRoutes[j] + value
					numSites[j] = numSites[j] + 1

	for i in range(numSteps):	
		token = separator
		if i==numSteps-1:
			token = '\n'

		if numSites[i] == 0:
			output.write(token)
		else:
			mean = distNaturalRoutes[i]/float(numSites[i])
			output.write(str(mean)+token)

def main():

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50
	separator = ';'

	data = open('../data/standardValues.csv', 'r')
	output = open('../data/distNaturalRoutesStd.csv', 'w')

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

