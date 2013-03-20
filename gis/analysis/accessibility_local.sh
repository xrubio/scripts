#!/bin/bash

echo 'INICIANT LOCAL ACCESSIBILITY'

costMap='slope'
jaciments='jaciments'
resolution=500
maxDist=2000

sites=`v.db.select map=$jaciments columns=cat -c`

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
		for xOffset in `seq -$maxDist $resolution $maxDist`
		do
			for yOffset in `seq -$maxDist $resolution $maxDist`
			do
				let gridX=$x+$xOffset
				let gridY=$y+$yOffset
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
		done

		let averageCost=$totalCost/$indexGrid
		echo 'Average cost for sitePointId:'$sitePointId ' with coords:'$x,$y ' is: '$averageCost' with total:'$totalCost' calculated from:'$indexGrid' points'
		v.db.update map=$jaciments column=acc_local value=$averageCost where='cat='$sitePointId''
		g.remove $costMapName
		let indexSite=$indexSite+1
	done
echo 'ACABAT LOCAL ACCESSIBILITY'

