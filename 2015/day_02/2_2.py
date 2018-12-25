#!/usr/bin/env python3

inputFile = open("2.in",'r')
inputContents = inputFile.readlines()

totalLength = 0
for present in inputContents:
    l, w, h = [int(x) for x in present.strip().split("x")]
    lengths = [l + w, w + h, h + l]
    totalLength += min(lengths) * 2 + l * w * h

print(totalLength)
