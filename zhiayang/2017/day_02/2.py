#!/bin/python3

import itertools as it

input = open("2.in","r").readlines()

sum = 0
for l in range(len(input)):
    nums = list(map(int, input[l].split()))
    sum += abs(max(nums) - min(nums))

print("part 1: checksum = {}".format(sum))


sum = 0
for l in range(len(input)):
    nums = list(map(int, input[l].split()))
    for p in it.combinations(nums, 2):
        if p[0] > p[1]:
            if p[0] % p[1] == 0:
                sum += p[0] // p[1]
        else:
            if p[1] % p[0] == 0:
                sum += p[1] // p[0]

print("part 2: checksum = {}".format(sum))
