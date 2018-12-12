#!/bin/python3

import numpy as np

input = open("6.in","r")
inputContents = input.readlines()
points = dict()
area = 0

def distance(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])

for point in inputContents:
    points[tuple([int(c) for c in point.split(", ")])] = 0

# find bounding box for searching
xys = list(zip(*points.keys()))
max_x = max(xys[0])
min_x = min(xys[0])
max_y = max(xys[1])
min_y = min(xys[1])

distanceMap = []

for y in range(min_y, max_y + 1):
    distanceMap.append([])
    for x in range(min_x, max_x + 1):
        distanceMap[y - min_y].append(dict())
        for point in points:
            d = distance(point, (x, y))
            distanceMap[y - min_y][x - min_x][point] = d

        if np.sum(np.array(list(distanceMap[y - min_y][x - min_x].values()))) < 10000:
            area += 1

        print("{:>3}/{} {:>3}/{}: {}".format(x - min_x, max_x - min_x , y - min_y, max_y - min_y, area), end="\r")

# max(points, key=points.get)
print("Max area is {} points".format(area))
