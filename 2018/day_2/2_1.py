#!/bin/python3

#from collections import Counter
import numpy as np

input = open("2.in","r")
inputContents = input.readlines()

two = 0
three = 0

for box in inputContents:
    #Counter(box)
    count = np.bincount(np.array([ord(ch) for ch in box]))
    if 2 in count:
        two = two + 1
    if 3 in count:
        three = three + 1

print(two * three)
