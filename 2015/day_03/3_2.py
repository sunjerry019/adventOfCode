#!/usr/bin/env python3
import numpy as np

inputFile = open("3.in",'r')
inputContents = inputFile.readlines()[0].strip()

visited = {(0, 0)}
currPerson = 0
currPositions = [np.array([0, 0], dtype=int), np.array([0, 0], dtype=int)] # x, y
ordnung = {
    '^' : np.array([  0,  1], dtype=int),
    '>' : np.array([  1,  0], dtype=int),
    '<' : np.array([ -1,  0], dtype=int),
    'v' : np.array([  0, -1], dtype=int)
}

for instruction in inputContents:
    currPerson ^= 1
    currPositions[currPerson] += ordnung[instruction]
    visited.add(tuple(currPositions[currPerson]))

print(len(visited))
