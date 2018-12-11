#!/bin/python3

import numpy as np

input = open("2.in","r")
inputContents = input.readlines()

npContents = [np.array([ord(ch) for ch in box]) for box in inputContents]


for i in range(len(npContents)):
    for j in range(i + 1, len(npContents)):
        comp = np.bincount(np.not_equal(npContents[i], npContents[j]))
        if comp[1] == 1:
            print("{}\n{}\n-> ".format(inputContents[i], inputContents[j]), end="")
            for k in range(len(inputContents[i])):
                if inputContents[i][k] == inputContents[j][k]:
                    print(inputContents[i][k], end="")
            break;
