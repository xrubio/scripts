#!/usr/bin/python
import sys


#!/usr/bin/python
import sys

def parseLine( line, separator, dictTimes, iniciTotal, fiTotal, timeStep):
#	print 'parsing line: ' + line
	splittedLine = line.split(separator)
	# if id already registered we need to skip this part
	name = splittedLine[1]
	x = splittedLine[2]
	y = splittedLine[3]
	i = 4
	for timeStep in range (iniciTotal, fiTotal, -timeStep):
		weight = float(splittedLine[i].replace(',','.'))
#		if weight > 0.0:
		print 'site: ' + name + ' contributing with weight: ' + str(weight) + ' to time step: ' + str(timeStep)
		timeStepValues = dictTimes[timeStep]
		timeStepValues[0] = timeStepValues[0] + weight*float(x)
		timeStepValues[1] = timeStepValues[1] + weight*float(y)
		timeStepValues[2] = timeStepValues[2] + weight
		dictTimes[timeStep] = timeStepValues
		i = i+1
	
def writeFile( dictTimes ):
	f = open('../aoristicWeightedMeans.csv', 'w')
	f.write('timeStep;x;y\n')
	for timeStep,timeStepValues in dictTimes.iteritems():
		f.write(str(timeStep))
		f.write(';')
		f.write(str(timeStepValues[0]))
		f.write(';')
		f.write(str(timeStepValues[1]))
		f.write('\n')
	f.close()

def calculateWeightedMean( dictTimes ):
	for timeStep, timeStepValues in dictTimes.iteritems():
		sumOfWeights = timeStepValues[2]
		timeStepValues[0] = timeStepValues[0]/sumOfWeights
		timeStepValues[1] = timeStepValues[1]/sumOfWeights

def main():

	dictTimes = {}

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50

	f = open('../aoristicValues.csv', 'r')
	separator = ';'
 	for i in range (iniciTotal, fiTotal, -timeStep):
		# each time slice: key = timeStep; values = weighted x, weighted y, sum of weights
		timeSlice = [0.0,0.0, 0.0]
		dictTimes[i] = timeSlice 
	for line in f:
		if line.startswith('id'):
			print 'Header: ' + line
		else:
			parseLine( line, separator, dictTimes, iniciTotal, fiTotal, timeStep )
	f.close()
	calculateWeightedMean( dictTimes )
	writeFile(dictTimes)

if __name__ == "__main__":
    main()

