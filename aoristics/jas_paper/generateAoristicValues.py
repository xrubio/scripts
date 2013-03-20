#!/usr/bin/python
import sys

def parseLine( line, separator, dictNames, aoristicValues, iniciTotal, fiTotal, timeStep ):
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
		
		# aoristic values to 0
		listAoristicValues = []
		rangeValues = iniciTotal - fiTotal
		rangeValues = rangeValues / timeStep

		for i in range(0, rangeValues):
			listAoristicValues.append(0.0)
		aoristicValues[idSite] = listAoristicValues

	# calculate aoristic value
	iniciAne = int(splittedLine[5])
	fiAne = int(splittedLine[6])
	aoristicValue = float(iniciAne) - float(fiAne)
	aoristicValue = timeStep / aoristicValue
	print '\taoristic value for starting: ' + str(iniciAne) + ' and ending: ' + str(fiAne) + ' is: ' + str(aoristicValue)

	indexInici = (iniciTotal - iniciAne)/timeStep
	indexFinal = (iniciTotal - fiAne)/timeStep
	listAoristicValues = aoristicValues[idSite]
	print '\taoristic value: ' + str(aoristicValue) + ' will be applied to site: ' + idSite + ' - ' + splittedLine[1] + ' from: ' + str(indexInici) + ' to: ' + str(indexFinal) + ' that includes period: ' + splittedLine[5] + ' beginning in: ' + str(iniciAne) + ' to: ' + str(fiAne)
	for i in range(indexInici, indexFinal):
		listAoristicValues[i] = listAoristicValues[i] + aoristicValue
	
	
def writeFile( dictNames, aoristicValue, iniciTotal, fiTotal, timeStep ):
	f = open('../aoristicValues.csv', 'w')
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
		# aoristic values
		listAoristicValues = aoristicValue[key]
		for i in range(0, len(listAoristicValues)):
			f.write(';')
			f.write(str(listAoristicValues[i]))
		f.write('\n')
	f.close()

def main():

	dictNames = {}
	aoristicValues = {}

	iniciTotal = 5500
	fiTotal = 550
	timeStep = 50

	f = open('../input/jaciments_periodes.csv', 'r')
	separator = ';'

	for line in f:
		if line.startswith('ID'):
			print 'Header: ' + line
		else:
			parseLine( line, separator, dictNames, aoristicValues, iniciTotal, fiTotal, timeStep )
	f.close()
	writeFile(dictNames, aoristicValues, iniciTotal, fiTotal, timeStep)

if __name__ == "__main__":
    main()

