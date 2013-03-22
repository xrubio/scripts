#!/bin/bash

echo 'INICIANT LOS'

jaciments='jac_sabadell'
losMap='cat_altures_15'
#accumulatedLos='fortificacions_los_acumulada'
sites=`v.db.select map=$jaciments columns=cat -c`
indexSite=0

#r.mapcalc "$accumulatedLos=0"

for sitePointId in $sites;
	do
		x=`v.db.select map=$jaciments columns=X where='cat='$sitePointId'' -c`
		y=`v.db.select map=$jaciments columns=Y where='cat='$sitePointId'' -c`

		echo 'Analysing site: '$sitePointId' index:'$indexSite' amb coordenades: '$x','$y'...'
		losMapName='los_posicio_'$sitePointId
		g.remove $losMapName
		r.los input=$losMap output=los_tmp coordinate=$x,$y --o
		r.mapcalc "los_tmp2=if(isnull(los_tmp),null(),1)"
		#r.mapcalc "$accumulatedLos=if(isnull(los_tmp2),$accumulatedLos,$accumulatedLos+1)"
		value=`r.sum rast=los_tmp2`
		value=`echo $value | sed "s/SUM = //g"`
		g.copy rast=los_tmp2,$losMapName
		g.remove los_tmp
		g.remove los_tmp2
		echo 'VISIÓ ACUMULADA DES DE:'$sitePointId' amb coordenades: '$x'/'y': -> '$value
		v.db.update map=$jaciments column=los value=$value where='cat='$sitePointId''
		let indexSite=$indexSite+1
	done
echo 'ACABAT LOS'

