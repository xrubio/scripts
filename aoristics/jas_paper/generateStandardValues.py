#!/usr/bin/python
import sys

def parseLine( line, separator, dictNames, standardValues, iniciTotal, fiTotal, timeStep ):
	print 'parsing line: ' + line
	splittedLine = line.split(separator)
	idSite = splittedLine[0]
	# if id already registered we need to skip this part
	if idSite not in dictNames:
		name = splittedLine[1]
		x = splittedLine[2]
		y = splittedLine[3]
		listData = [name, x, y]
		dictNames[idSite] = listData
		print '\tnew register: ' + idSite + ' - ' + str(listData)
		
		# standard values to 0
		listStandardValues = []
		rangeValues = iniciTotal - fiTotal
		rangeValues = rangeValues / timeStep

		for i in range(0, rangeValues):
			listStandardValues.append(0)
		standardValues[idSite] = listStandardValues

	# calculate num sites
	iniciAne = int(splittedLine[5])
	fiAne = int(splittedLine[6])

	indexInici = (iniciTotal - iniciAne)/timeStep
	indexFinal = (iniciTotal - fiAne)/timeStep
	print 'index inici pe: ' + idSite + ' is: ' + str(indexInici) + ' and fi: ' + str(indexFinal)
	listStandardValues = standardValues[idSite]
	for i in range(indexInici, indexFinal):
		listStandardValues[i] = 1 
	
	
def writeFile( dictNames, standardValue, iniciTotal, fiTotal, timeStep ):
	f = open('../standardValues.csv', 'w')
	f.write('id;nom;x;y')
	for i in range(iniciTotal, fiTotal, -timeStep):
		f.write(';')
		f.write(str(i))
	f.write('\n')
	for key,values in dictNames.iteritems():
		# id
		f.write(str(key))
		# name, x, y
		for i in range(0,len(values)):
			f.write(';')
			f.write(str(values[i]))
		# standard values
		listStandardValues = standardValue[key]
		for i in range(0, len(listStandardValues)):
			f.write(';')
			f.write(str(listStandardValues[i]))
		f.write('\n')
	f.close()

def main():

	dictNames = {}
	standardValues = {}

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50

	f = open('../input/jaciments_periodes.csv', 'r')
	separator = ';'

	for line in f:
		if line.startswith('ID'):
			print 'Header: ' + line
		else:
			parseLine( line, separator, dictNames, standardValues, iniciTotal, fiTotal, timeStep )
	f.close()
	writeFile(dictNames, standardValues, iniciTotal, fiTotal, timeStep)

if __name__ == "__main__":
    main()

