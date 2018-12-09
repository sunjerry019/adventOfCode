#!/bin/bash

echo "Creating for Day $1"

mkdir "Day $1"
cd "Day $1"
touch "$1_1.py" "$1_2.py" "$1.in" "$1.txt"
