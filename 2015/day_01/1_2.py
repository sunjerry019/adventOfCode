#!/usr/bin/env python3

inputFile = open("1.in",'r')
inputContents = inputFile.readlines()[0].strip()

floor = 0
ordnung = {
    '(':  1,
    ')': -1
}

i = 0
for char in inputContents:
    i += 1
    floor += ordnung[char]
    if floor == -1:
        break

print(i)
