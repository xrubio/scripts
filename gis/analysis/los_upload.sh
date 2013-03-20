#!/bin/bash

echo 'INICIANT LOS'

jaciments='jaciments'
prefix='los_site_'

sites=`v.db.select map=$jaciments columns=cat -c`
for sitePointId in $sites;
	do
		nameLos=$prefix$sitePointId
		nameLosTmp=$nameLos'_tmp'
		r.mapcalc "$nameLosTmp=if(isnull($nameLos),null(),1)"
		value=`r.sum rast=$nameLosTmp`
		echo $value
		value=`echo $value | sed "s/SUM = //g"`
		value=`echo $value | sed "s/.000000//g"`
		let finalValue=$value
		v.db.update map=$jaciments column=los value=$finalValue where='cat='$sitePointId''
		g.remove $nameLosTmp
	done

