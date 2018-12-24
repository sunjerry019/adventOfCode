#!/bin/bash

echo "Creating for Day $2 for year $1"

DAY=`printf %02d $2`
mkdir -p "$1/day_$DAY"
cd "$1/day_$DAY"
touch "$2_1.py" "$2_2.py" "$2.in" "$2.txt"
