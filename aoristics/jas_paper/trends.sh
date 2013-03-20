#!/bin/bash

# distance to natural routes
./windowSlide.py -i ../data/distNaturalRoutesMC.csv -o foo.csv -w 3
./calculateTrend.py -i foo.csv -o ../data/distNaturalTrendMC.csv

# slope
./windowSlide.py -i ../data/slopeMC.csv -o foo.csv -w 3
./calculateTrend.py -i foo.csv -o ../data/slopeTrendMC.csv

# number of sites
./windowSlide.py -i ../data/numSitesMC.csv -o foo.csv -w 3
./calculateTrend.py -i foo.csv -o ../data/numSitesTrendMC.csv

rm foo.csv

