#!/usr/bin/env python3
import numpy as np

inputFile = open("6.in",'r')
inputContents = inputFile.readlines()
lights = np.zeros((1000,1000), dtype=int)

i = 1
for instruction in inputContents:
    print("[{:>3}/300]".format(i), end='\r')
    instruction = instruction.strip()

    ins = -2
    if instruction[:8] == "turn off":
        instruction = instruction[9:]
        ins = -1
    elif instruction[:7] == "turn on":
        instruction = instruction[8:]
        ins = 1
    elif instruction[:6] == "toggle":
        instruction = instruction[7:]
        ins = 2

    if ins > -2:
        a = instruction.split(" through ")
        coord1 = [int(x) for x in a[0].split(",")]
        coord2 = [int(x) for x in a[1].split(",")]
        for _y in range(coord1[1], coord2[1] + 1):
            for _x in range(coord1[0], coord2[0] + 1):
                lights[_x, _y] += ins
                if lights[_x, _y] < 0: lights[_x, _y] = 0
    else:
        print("Error, instruction {}".format(instruction))
        quit()
    i += 1

print('\n', np.sum(lights))
