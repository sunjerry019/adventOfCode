#!/usr/bin/env python3

input = open("1.in","r")
inputContents = input.readlines()

freq = 0

for line in inputContents:
    freq =  freq + int(line)

print(freq)
