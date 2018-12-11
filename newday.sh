#!/bin/bash

echo "Creating for Day $2 for year $1"

$1 = `printf %02d $1`
mkdir -p "$1/day_$2"
cd "$1/$2"
touch "$2_1.py" "$2_2.py" "$2.in" "$2.txt"
