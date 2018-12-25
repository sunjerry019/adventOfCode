#!/usr/bin/env python3
import re

inputFile = open("5.in",'r')
inputContents = inputFile.readlines()

def isNice(_str):
    v = [ord(c) for c in _str if c in "aeiou"]
    repeated = re.search(r'([a-z])\1{1,}', _str)
    forbidden = re.search(r'(ab|cd|pq|xy)', _str)

    return (len(v) >= 3) and (repeated is not None) and (forbidden is None)

niceCount = 0
for shengzi in inputContents:
    niceCount += isNice(shengzi.strip())

print(niceCount)
