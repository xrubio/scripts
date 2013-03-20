#!/usr/bin/python
#./dominance_analysis.py 429000 4644500 7000 1000 

import sys, os

if(len(sys.argv)!=6):
	print 'wrong number of parameters'
	print 'use: ./dominance_analysis.py left top size resolution dem'
	exit(0)

left = int(sys.argv[1])
top = int(sys.argv[2])
size = int(sys.argv[3])
resolution = int(sys.argv[4])
demName = sys.argv[5]

offset = resolution/2
bottom = top-size

numPoints = 1+size/resolution

os.system('g.remove vect=grid_dominance')
os.system('v.mkgrid map=grid_dominance position=coor coor='+str(left)+','+str(top-size)+' box='+str(resolution)+','+str(resolution)+' grid='+str(numPoints)+','+str(numPoints)+' -p')
os.system('v.db.addcol map=grid_dominance columns=\'dominance INT\'')


indexX = 1

for indexX in range(1,1+numPoints):
	for indexY in range(1,1+numPoints):
		x = left+offset + (indexX-1) * resolution
		y = top+offset - (indexY-1) * resolution
		print 'checking los of point: ' + str(x) + '/' + str(y) +' with index: ' + str(indexX) + '/'+str(indexY)
		os.system('g.remove los_'+str(indexX)+'_'+str(indexY))
		os.system('g.remove dominance_'+str(indexX)+'_'+str(indexY))
		os.system('r.los input='+demName+' output=los_'+str(indexX)+'_'+str(indexY)+' coordinate='+str(x)+','+str(y)+' max_dist=5000 obs_elev=3 --o')
		os.system('r.mapcalc "dominance_analysis_'+str(indexX)+'_'+str(indexY)+'=if(los_'+str(indexX)+'_'+str(indexY)+'<90,1,0)"')
		os.system('v.db.update map=grid_dominance column=dominance value=`r.sum --q rast=dominance_analysis_'+str(indexX)+'_'+str(indexY)+' | sed "s/SUM = //g"` where="row='+str(indexY)+' AND col='+str(indexX)+'"')

