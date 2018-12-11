#!/bin/python3

import numpy as np

gridID = 6303
#gridID = 7672

powerLevel = np.zeros((301,301), dtype=int)
pL3x3 = np.zeros((301,301), dtype=int)

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
        if (x >= 3) and (y >= 3):
            pL3x3[x-2, y-2] = powerLevel[x    , y    ] - \
                              powerLevel[x    , y - 3] - \
                              powerLevel[x - 3, y    ] + \
                              powerLevel[x - 3, y - 3]

maxidx = np.argmax(pL3x3)
print("Max Power level is at <{},{}>".format(int(np.floor(maxidx/301)), maxidx%301))
