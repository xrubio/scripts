#!/bin/bash

echo 'INICIANT CÀLCUL RUTES MÍNIM COST'

costValues='penedes-valles_slope'
output='least_cost_network_jaciments_fe'
sitesFile='jaciments_fe'

echo 'mapa: '$output' serà creat des del vector: '$sitesFile' amb costos de: '$costValues
sites=`v.db.select map=$sitesFile columns=cat -c`
r.mapcalc "'$output'=0"

indexSite=0
for siteId in $sites;
	do
		x=`v.db.select map=$sitesFile columns=X where='cat='$siteId'' -c`
		y=`v.db.select map=$sitesFile columns=Y where='cat='$siteId'' -c`
		costMap='costMap_'$siteId
		echo 'Analysing site: '$siteId' index:'$indexSite' amb coordenades: '$x','$y'...'		
		r.cost input=$costValues output=$costMap coordinate=$x,$y --o
		
		for targetId in $sites;
			do
				routeMap='routeMap_'$siteId'_'$targetId
				echo 'calculating cost route from: '$siteId' to: '$targetId'...'
				targetX=`v.db.select map=$sitesFile columns=X where='cat='$targetId'' -c`
				targetY=`v.db.select map=$sitesFile columns=Y where='cat='$targetId'' -c`
				r.drain in=$costMap coordinate=$targetX,$targetY out=$routeMap --o
				r.mapcalc "'$output'=if(isnull('$routeMap'),'$output','$output'+1)"
				g.remove $routeMap
				echo 'done!'
			done
		let indexSite=$indexSite+1
		echo 'site number:'$indexSite ' with id: '$siteId' done!'
		g.remove $costMap
	done
echo 'ACABAT CÀLCUL RUTES MÍNIM COST, DESAT A: '$output

