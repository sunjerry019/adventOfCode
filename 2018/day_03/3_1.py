#!/usr/bin/env python3

import numpy as np

input = open("3.in","r")
inputContents = input.readlines()

fabric = np.zeros((1000,1000), dtype=int)
# l = 998
# w = 999

for claim in inputContents:
    a = claim.split(" @ ")[1].split(": ")
    b1 = a[0].split(",")
    b2 = a[1].split("x")
    """
        The number of inches between the left edge of the fabric and the left edge of the rectangle.
        The number of inches between the top edge of the fabric and the top edge of the rectangle.
        The width of the rectangle in inches.
        The height of the rectangle in inches.
    """
    c = {
        "pos" : {"x": int(b1[0]), "y": int(b1[1])},
        "area": {"w": int(b2[0]), "h": int(b2[1])}
    }

    #if c["pos"]["x"] + c["area"]["w"] > w:
    #    w = c["pos"]["x"] + c["area"]["w"]
    #if c["pos"]["y"] + c["area"]["h"] > l:
    #    l = c["pos"]["y"] + c["area"]["h"]

    for x in range(c["pos"]["x"], c["pos"]["x"] + c["area"]["w"]):
        for y in range(c["pos"]["y"], c["pos"]["y"] + c["area"]["h"]):
            fabric[x, y] = fabric[x, y] + 1

print(np.count_nonzero(fabric > 1))
