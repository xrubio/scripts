#!/bin/bash

echo 'CALCULANT DISTÀNCIA MÍNIMA A NECROPOLIS'

dem='dem'
friction='slope'
necropolis='funerari_fe'
assentaments='assentaments_fe'
minDistanceToNecropolis='minDistance_fe'
prefix='walk_fe_'

llistatNecropolis=`v.db.select map=$necropolis columns=cat -c`
stringNecropolis=''
for necropolisId in $llistatNecropolis;
do
	x=`v.db.select map=$necropolis columns=X where='cat='$necropolisId'' -c`
	y=`v.db.select map=$necropolis columns=Y where='cat='$necropolisId'' -c`
	echo 'calculating cost map for id: '$necropolisId' with position: '$x'/'$y
	stringNecropolis=$stringNecropolis$prefix$necropolisId','
	r.walk elevation=$dem friction=$friction coordinate=$x,$y output=$prefix$necropolisId
done
# we remove the last ','
stringNecropolis=`echo "${stringNecropolis%?}"`
r.mapcalc "$minDistanceToNecropolis=min($stringNecropolis)"
# we pass to minutes
r.mapcalc "$minDistanceToNecropolis=$minDistanceToNecropolis/60"

llistatAssentaments=`v.db.select map=$assentaments columns=cat -c`
for assentamentsId in $llistatAssentaments;
do
	echo 'looking for minimum distance to necropolis for id: '$assentamentsId
	v.what.rast vector=$assentaments raster=$minDistanceToNecropolis column=distNecro where='cat='$assentamentsId''
done

echo ACABAT CÀLCUL DISTÀNCIA MÍNIMA A NECRÒPOLIS 

