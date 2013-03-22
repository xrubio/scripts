#!/bin/bash

echo 'INICIANT LOS'

jaciments='valles_jaciments_los'
losMap='valles_los'
sites=`v.db.select map=$jaciments columns=cat -c`

indexSite=0
sitesTmp=`seq 77 88`
#for sitePointId in $sites;
for sitePointId in $sitesTmp;
	do
		x=`v.db.select map=$jaciments columns=X where='cat='$sitePointId'' -c`
		y=`v.db.select map=$jaciments columns=Y where='cat='$sitePointId'' -c`

		echo 'Analysing site: '$sitePointId' index:'$indexSite' amb coordenades: '$x','$y'...'
		losMapName='los_site_'$sitePointId
		r.los input=$losMap output=$losMapName coordinate=$x,$y --o
		r.mapcalc "los_sum=if(isnull('$losMapName'),null(),1)"
		value=`r.sum rast=los_sum`
		value=`echo $value | sed "s/SUM = //g"`
		echo 'VISIÓ ACUMULADA DES DE:'$sitePointId' amb coordenades: '$x'/'y': -> '$value
		v.db.update map=$jaciments column=los value=$value where='cat='$sitePointId''
		let indexSite=$indexSite+1
	done
echo 'ACABAT LOS'

