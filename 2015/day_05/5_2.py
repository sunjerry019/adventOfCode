#!/usr/bin/env python3
import re

inputFile = open("5.in",'r')
inputContents = inputFile.readlines()

def isNice(_str):
    repeated = re.search(r'([a-z][a-z])[a-z]*\1{1,}', _str)
    oneLetter = re.search(r'([a-z])[a-z]\1{1,}', _str)

    return (repeated is not None) and (oneLetter is not None)

niceCount = 0
for shengzi in inputContents:
    niceCount += isNice(shengzi.strip())

print(niceCount)
