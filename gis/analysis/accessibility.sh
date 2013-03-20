#!/bin/bash

echo 'INICIANT ACCESSIBILITY'

grid='valles_grid'
costMap='valles_slope'
jaciments='valles_jaciments_acc'

echo 'grid map: '$grid
sites=`v.db.select map=$jaciments columns=cat -c`
gridPoints=`v.db.select map=$grid columns=cat -c`

indexSite=0
for sitePointId in $sites;
	do
		x=`v.db.select map=$jaciments columns=X where='cat='$sitePointId'' -c`
		y=`v.db.select map=$jaciments columns=Y where='cat='$sitePointId'' -c`

		echo 'Analysing site: '$sitePointId' index:'$indexSite' amb coordenades: '$x','$y'...'
		costMapName='cost_site_'$sitePointId
		r.cost input=$costMap output=$costMapName coordinate=$x,$y --o
		
		totalCost=0
		indexGrid=0

		for gridPointId in $gridPoints;	
		do		
			gridX=`v.db.select map=$grid columns=x where='cat='$gridPointId'' -c`
			gridY=`v.db.select map=$grid columns=y where='cat='$gridPointId'' -c`
			echo '	step: '$indexGrid' checking point number: ' $indexSite ' with coords: '$x'/'$y' to: '$gridX'/'$gridY' '
			r.drain in=$costMapName coordinate=$gridX,$gridY out=min_cost --o
			value=`r.sum rast=min_cost`
			value=`echo $value | sed "s/SUM = //g"`
			value=`echo $value | sed "s/.000000//g"`
			let totalCost=$totalCost+$value
			echo '	step: '$indexGrid' finished. Cost from: '$x'/'$y' to: '$gridX'/'$gridY' is '$value' and sum: '$totalCost
			let indexGrid=$indexGrid+1
			g.remove min_cost
		done
		let averageCost=$totalCost/$indexGrid
		#if [ "$averageCost" -gt "$maxAverage" ]
		#then
		#	let maxAverage=$averageCost
		echo 'Average cost for sitePointId:'$sitePointId ' with coords:'$x,$y ' is: '$averageCost' with total:'$totalCost' calculated from:'$indexGrid' points'
		v.db.update map=$jaciments column=acc value=$averageCost where='cat='$sitePointId''
		g.remove $costMapName
		let indexSite=$indexSite+1
	done
echo 'ACABAT ACCESSIBILITY'

