#!/usr/bin/python
import sys


#!/usr/bin/python
import os, sys, random

def parseLine( numExec, fo, line, separator, iniciTotal, fiTotal, timeStep):
	splittedLine = line.split(separator)
	# if id already registered we need to skip this part
	idSite = splittedLine[0]
	name = splittedLine[1]
	x = splittedLine[2]
	y = splittedLine[3]
	i = 4
	print 'simulating site: ' + name + ' for execution: ' + str(numExec+1)
	fo.write(idSite+separator+name+separator+x+separator+y+separator)
	for step in range (iniciTotal, fiTotal, -timeStep):
		weight = float(splittedLine[i].replace(',','.'))	
		
		token = separator
		if step==fiTotal+timeStep:
			token = '\n'

		if weight > 0.0:
			#print 'site: ' + name + ' contributing with weight: ' + str(weight) + ' to time step: ' + str(timeStep)
			if random.random()<float(weight):
				fo.write('1'+token)
			else:
				fo.write('0'+token)
		else:
			fo.write('0'+token)
		i = i+1

def main():

	executions = 10000

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50
	separator = ';'


	if not os.path.exists('../montecarlo'):
	    os.makedirs('../montecarlo')

	print 'creating ' + str(executions) + ' simulations...'
	for numExec in range(0,executions):
		fo = open('../montecarlo/simulation_'+str(numExec+1)+'.csv','w')
		fo.close()
	print 'done'

	f = open('../aoristicValues.csv', 'r')
	for line in f:
		print 'processing site: ' + line
		for numExec in range(0, executions):
			fo = open('../montecarlo/simulation_'+str(numExec+1)+'.csv','a')
			if line.startswith('id'):
				fo.write(line)
			else:
				parseLine( numExec, fo, line, separator, iniciTotal, fiTotal, timeStep )
			fo.close()
	f.close()
	print 'done'

if __name__ == "__main__":
    main()

