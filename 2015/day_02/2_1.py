#!/usr/bin/env python3

inputFile = open("2.in",'r')
inputContents = inputFile.readlines()

totalArea = 0
for present in inputContents:
    l, w, h = [int(x) for x in present.strip().split("x")]
    areas = [l * w, w * h, h * l]
    totalArea += 2 * sum(areas) + min(areas)

print(totalArea)
