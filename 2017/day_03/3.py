#!/bin/python3

import math
import itertools as it

input = 361527

def part1(input):
    # bottom-right corners are the odd square numbers
    root = int(math.ceil(math.sqrt(input)))
    if root % 2 == 0:
        root += 1

    sq = root * root

    # find a path from the current number, until we can go straight to the centre.
    halfside = (root - 1) // 2

    # calc the edge numbers for our square
    bottom  = sq - halfside
    left    = bottom - (2 * halfside)
    top     = left - (2 * halfside)
    right   = top - (2 * halfside)

    # this is the shortest distance from our input to any edge
    shortest = min(abs(input - bottom), abs(input - left), abs(input - top), abs(input - right))

    print("part 1: distance = {}".format(shortest + halfside))

def part2(input):
    grid = dict()
    grid[(0, 0)] = 1

    current = 1
    nextRoot = 3

    moves = 0
    direction = 0  # 0 = right, 1 = up, 2 = left, 3 = down

    xpos = 0
    ypos = 0
    while current <= input:
        halfside = (nextRoot - 1) // 2

        if







part1(input)
part2(input)
