#!/usr/bin/python
import os, sys, random

# this script calculates the number of active sites per time step from montecarlo simulations

def processSimulation(numSteps, simulationFile, separator, output):
	simulation = open('../montecarlo/'+simulationFile, 'r')

	numSites = []
	distNaturalRoutes= []
	for siteLine in simulation:
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
					# print splittedSiteLine[1] + ' exists in step: ' + str(j) + ' with location: ' + x + '/' + y
					# fer consulta i agafar valor com sigui
					distNaturalRoutes[j] = distNaturalRoutes[j] + value
					numSites[j] = numSites[j] + 1 

	simulation.close()	
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

	output = open('../data/distNaturalRoutesMC.csv', 'w')

	numSteps = 0
	for step in range(iniciTotal, fiTotal, -timeStep):
		token = separator
		if step==fiTotal+timeStep:
			token = '\n'
		output.write(str(step)+token)
		numSteps = numSteps+1

	for root, dirs, simulationFiles in os.walk('../montecarlo'):
		for simulationFile in simulationFiles:
			print 'processing simulation results in file: ' + simulationFile
			processSimulation(numSteps, simulationFile, separator, output)
	output.close()

if __name__ == "__main__":
    main()

