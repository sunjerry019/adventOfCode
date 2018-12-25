#!/usr/bin/env python3

inputFile = open("1.in",'r')
inputContents = inputFile.readlines()[0].strip()

floor = 0
ordnung = {
    '(':  1,
    ')': -1
}

for char in inputContents:
    floor += ordnung[char]

print(floor)
