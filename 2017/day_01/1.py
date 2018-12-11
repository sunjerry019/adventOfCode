#!/bin/python3

def next(input, idx, step):
    return input[(idx + step) % len(input)]


input = open("1.in","r").readlines()[0][:-1]

sum = 0
for i in range(len(input)):
    if next(input, i, 1) == input[i]:
        sum += int(input[i])

print("part 1: sum = {}".format(sum))

sum = 0
for i in range(len(input)):
    if next(input, i, len(input) // 2) == input[i]:
        sum += int(input[i])

print("part 2: sum = {}".format(sum))
