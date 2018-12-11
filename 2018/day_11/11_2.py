#!/bin/python3

import numpy as np

gridID = 6303
#gridID = 7672
#gridID = 18

powerLevel = np.zeros((301,301), dtype=int)
pLNxN = np.zeros((301,301,301), dtype=int)

# the coordinates need to be 1-indexed

def getPL(X, Y):
    rackID = (X + 10)
    return int(((((rackID * Y) + gridID) * rackID)/100)%10) - 5

for y in range(1, 301):
    for x in range(1,301):
        currentPL = getPL(x, y)
        powerLevel[x,y] = powerLevel[x - 1, y    ] + \
                          powerLevel[x    , y - 1] - \
                          powerLevel[x - 1, y - 1] + \
                          currentPL
        for size in range(1,301):
            if (x >= size) and (y >= size):
                pLNxN[x - size + 1, y - size + 1, size] = powerLevel[x       , y       ] - \
                                                          powerLevel[x       , y - size] - \
                                                          powerLevel[x - size, y       ] + \
                                                          powerLevel[x - size, y - size]

maxidx = np.argmax(pLNxN)
print("Max Power level is at {} = <{},{},{}>".format(maxidx, int(maxidx/(301**2)), int(maxidx/301)%301, maxidx%301))
