#!/bin/bash

../joinResults.py -i 01_local/ -o experiment3_1local.csv 
sed 's/agents_biomin0.1_mean4791_stddev//g' experiment3_1local.csv > foo
sed 's/_ex[0-9]\.csv//g' foo > foo2
../transpose.py -i foo2 -o experiment3_1local.csv

../joinResults.py -i 02_regional/ -o experiment3_2regional.csv 
sed 's/agents_biomin0.1_mean5584_stddev//g' experiment3_2regional.csv > foo
sed 's/_ex[0-9]\.csv//g' foo > foo2
../transpose.py -i foo2 -o experiment3_2regional.csv

../joinResults.py -i 03_global/ -o experiment3_3global.csv 
sed 's/agents_biomin0.1_mean11140_stddev//g' experiment3_3global.csv > foo
sed 's/_ex[0-9]\.csv//g' foo > foo2
../transpose.py -i foo2 -o experiment3_3global.csv

rm foo foo2

