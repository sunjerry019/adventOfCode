#!/usr/bin/env python3

import numpy as np

input = open("6.in","r")
inputContents = input.readlines()
points = dict()

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
            if d not in distanceMap[y - min_y][x - min_x]:
                distanceMap[y - min_y][x - min_x][d] = [point]
            else:
                distanceMap[y - min_y][x - min_x][d].append(point)
        min_d = min(distanceMap[y - min_y][x - min_x].keys())
        print("{:>3}/{} {:>3}/{}: {}".format(x - min_x, max_x - min_x , y - min_y, max_y - min_y, min_d), end="\r")
        min_d_pts = distanceMap[y - min_y][x - min_x][min_d]

        if len(min_d_pts) == 1:
            # we only care if it isn't tied
            if x == max_x or x == min_x or y == max_y or y == min_y:
                # coord is on the edge, the points closest to an edge coord is disqualified
                points[min_d_pts[0]] = -100000
            else:
                points[distanceMap[y - min_y][x - min_x][min_d][0]] += 1

# max(points, key=points.get)
print("Max area is {} points".format(max(points.values())))
