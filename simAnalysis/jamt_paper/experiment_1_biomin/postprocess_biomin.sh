#!/bin/bash

../joinResults.py -i 01_local/ -o experiment1_1local.csv 
sed 's/agents_biomin//g' experiment1_1local.csv > foo
sed 's/_mean4955_stddev1934//g' foo > foo2
sed 's/_ex[0-9]\.csv//g' foo2 > foo3
../transpose.py -i foo3 -o experiment1_1local.csv

../joinResults.py -i 02_regional/ -o experiment1_2regional.csv 
sed 's/agents_biomin//g' experiment1_2regional.csv > foo
sed 's/_mean5775_stddev1365//g' foo > foo2
sed 's/_ex[0-9]\.csv//g' foo2 > foo3
../transpose.py -i foo3 -o experiment1_2regional.csv

../joinResults.py -i 03_global/ -o experiment1_3global.csv 
sed 's/agents_biomin//g' experiment1_3global.csv > foo
sed 's/_mean11521_stddev1011//g' foo > foo2
sed 's/_ex[0-9]\.csv//g' foo2 > foo3
../transpose.py -i foo3 -o experiment1_3global.csv

rm foo foo2 foo3

