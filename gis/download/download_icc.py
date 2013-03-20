#!/usr/bin/python
import sys, os

# usage: ./download_icc.py left top size mapType mapScale outputName
# example: ./download_icc.py 420000 4647000 5000 mtc5m 5000 topo5puigciutat
# mapType: orto5m, orto25m, mtc50m (topo), sat250m, mgc50m (geologic)

def defineRegion(left, right, top, bottom, resolution):
	commandBoundaries = 'g.region w='+str(left)+' e='+str(right)+' n='+str(top)+' s='+str(bottom)
	commandResolution = 'g.region res='+str(resolution)
	os.system(commandBoundaries)
	os.system(commandResolution)

def importTiles(numRows, numColumns):
	print 'importing ' + str(numRows*numColumns) + ' files'
	for i in range(numRows):
		for j in range(numColumns):
			nameTile = 'tile_'+str(i)+'_'+str(j)
			extension = '.tif'
			print 'importing tile: ' + nameTile+extension
			command = 'r.in.gdal input=tmp/'+nameTile+extension + ' output='+nameTile+' -o'
			os.system(command)

def composite(numRows, numColumns, outputName):
	print 'composite of: ' + str(numRows*numColumns) + ' rasters'
	redMapCommand = 'r.patch input='
	blueMapCommand = 'r.patch input='
	greenMapCommand = 'r.patch input='
	for i in range(numRows):
		for j in range(numColumns):
			# if not the first map, append
			if i != 0  or j != 0:			
				redMapCommand += ','
				blueMapCommand += ','
				greenMapCommand += ','
			nameTile = 'tile_'+str(i)+'_'+str(j)
			redMapCommand += nameTile+'.red'
			greenMapCommand += nameTile+'.green'
			blueMapCommand += nameTile+'.blue'
	redMapCommand += ' output=map.red'
	greenMapCommand += ' output=map.green'
	blueMapCommand += ' output=map.blue'
	print redMapCommand
	os.system(redMapCommand)
	print greenMapCommand
	os.system(greenMapCommand)
	print blueMapCommand
	os.system(blueMapCommand)
	compositeCommand = 'r.composite r=map.red g=map.green b=map.blue output='+outputName
	print compositeCommand
	os.system(compositeCommand)
	os.system('g.remove map.red,map.green,map.blue')

def cleanGrassTmpFiles(numRows, numColumns):
	print 'cleaning GRASS tmp files'
	for i in range(numRows):
		for j in range(numColumns):
			nameTile = 'tile_'+str(i)+'_'+str(j)
			redNameTile = nameTile+'.red'
			greenNameTile = nameTile+'.green'
			blueNameTile = nameTile+'.blue'
			os.system('g.remove rast='+redNameTile+','+greenNameTile+','+blueNameTile)
			os.system('g.remove group='+nameTile)

def cleanSystem():
	os.system('rm -rf tmp')
	os.system('mkdir tmp')

def cleanGrass(outputName):
	os.system('g.remove '+outputName)
	os.system('g.remove map.red,map.green,map.blue')

def main():
	cleanSystem()
	# conversion from meter to inches
	meterToInches = 100.0/2.54
	# epsg code
	epsg = '23031'
	# quality of resulting image (in pixels per inch)
	# quality = 75
	quality = 300
	# quality = 300
	# size of tiles in pixels that will be downloaded
	tileSizeInPixels = 2000
		
	left = int(sys.argv[1])
	top = int(sys.argv[2]) 
	# squared, size of target in reality
	realSize = int(sys.argv[3]) 
	mapType = sys.argv[4]
	# map scale, in terms of how many meters are represented in 1 meter of map (1:5000, 1:50000, ...)
	mapScale = int(sys.argv[5])
	outputName = sys.argv[6]
	
	cleanGrass(outputName)

	# size of target in map (meters)
	sizeInMapUnits = float(realSize)/float(mapScale)

	# image size in pixels = sizeInMapUnits (m.) * conversionToInches (m/inches) * quality (inches)
	imageSizeInPixels = int(float(sizeInMapUnits*meterToInches*float(quality))+0.5)

	print 'target area is: ' + str(realSize) +'x'+str(realSize)+' meters. Map will have a size of: ' + str(sizeInMapUnits)+'x'+str(sizeInMapUnits) + ' meters with scale: ' + str(mapScale)
	print 'Generating an image with: ' + str(imageSizeInPixels) + 'x'+str(imageSizeInPixels) + ' pixels with quality: ' + str(quality)

	# width/length of tile in reality
	tmpTileSizeInMeters = float(tileSizeInPixels) * (1/float(quality)) * (1/meterToInches) * float(mapScale)
	tileSizeInMeters = int(tmpTileSizeInMeters+0.5)
	numRows = 1+int(float(float(realSize)/float(tileSizeInMeters)))
	numColumns = 1+int(float(float(realSize)/float(tileSizeInMeters)))
	resolution = float(tileSizeInMeters)/float(tileSizeInPixels)
	print str(numRows*numColumns) + ' tiles, ' + str(numRows) + 'x' + str(numColumns) + ' will be downloaded, each of one depicting: ' + str(tileSizeInMeters) + 'x' + str(tileSizeInMeters) + ' meters with a resolution of: ' + str(resolution) + ' meters per pixel'

	right = left+realSize
	bottom = top-realSize

	y = top
	indexRow = 0
	while y > bottom:
		print 'row ' + str(indexRow+1) + ' of: ' + str(numRows)
		x = left
		indexColumn = 0
		while x < right:
			print '\tcolumn ' + str(indexColumn+1) + ' of: ' + str(numColumns)
			print 'new tile - from top/left: ' +str(y)+'/'+str(x)+' to bottom/right: ' + str(y-tileSizeInMeters) + '/' + str(x+tileSizeInMeters)
			command = 'wget'
			queryURL = 'http://shagrat.icc.es/lizardtech/iserv/'
			sentence = 'ows?REQUEST=GetMap&VERSION=1.1.0&SRS=EPSG:'+epsg+'&Service=WMS&BBOX='+str(x)+','+str(y-tileSizeInMeters)+','+str(x+tileSizeInMeters)+','+str(y)+'&WIDTH='+str(tileSizeInPixels)+'&HEIGHT='+str(tileSizeInPixels)+'&LAYERS='+mapType+'&STYLES=&FORMAT=TIFF&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&EXCEPTION=INIMAGE'
			print command + ' "'+queryURL+sentence+'"'
			os.system(command + ' "'+queryURL+sentence+'"')
			print 'writing on: tile_'+str(indexRow)+'_'+str(indexColumn)+'.tif'
			os.system('mv "'+sentence+'" tmp/'+'tile_'+str(indexRow)+'_'+str(indexColumn)+'.tif')
			tfwFileName = 'tile_'+str(indexRow)+'_'+str(indexColumn)+'.tfw'
			tfwFile = open('tmp/'+tfwFileName, 'w')
			tfwFile.write(str(resolution)+'\n')
			tfwFile.write('0.000000000000000\n')
			tfwFile.write('0.000000000000000\n')
			tfwFile.write('-'+str(resolution)+'\n')
			tfwFile.write(str(x)+'\n')
			tfwFile.write(str(y)+'\n')
			tfwFile.close()
			x = x+tileSizeInMeters
			indexColumn = indexColumn+1
		y = y-tileSizeInMeters
		indexRow = indexRow + 1

	print 'download finished, defining region and starting import...'
	defineRegion(left, right, top, bottom, resolution)
	importTiles(numRows, numColumns)
	composite(numRows, numColumns, outputName)
	cleanGrassTmpFiles(numRows, numColumns)

if __name__ == "__main__":
    main()

