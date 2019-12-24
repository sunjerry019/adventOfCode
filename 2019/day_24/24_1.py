#!/usr/bin/env python3

import numpy as np
import itertools
import copy

class Problem():
    def __init__(self):
        self.input = open("24.in","r")
        self.inputContents = self.input.readlines()

        self.grid = []
        self.gridsseen = {}
        self.readContents()
        self.iterations = 0

        checksum = self.checksum()

        while(checksum not in self.gridsseen):
            self.gridsseen[checksum] = 1
            self.iterate()
            checksum = self.checksum()

        print(self.iterations, checksum)
        self.printGrid()

    def readContents(self):
        for line in self.inputContents:
            line = line.strip()
            line = [1 if x == '#' else 0 for x in line]
            self.grid.append(line)

    def iterate(self):
        newgrid = [[None]*5 for x in range(5)]

        # Diagonals don't count
        for i in range(5):
            for j in range(5):
                summe = 0
                summe += self.grid[i-1][j] if (i - 1 >= 0) else 0
                summe += self.grid[i][j-1] if (j - 1 >= 0) else 0
                summe += self.grid[i+1][j] if (i + 1 <= 4) else 0
                summe += self.grid[i][j+1] if (j + 1 <= 4) else 0
                
                if self.grid[i][j]:
                    newgrid[i][j] = 1 if summe == 1 else 0
                else:
                    newgrid[i][j] = 1 if 0 < summe <= 2 else 0

        self.grid = newgrid
        self.iterations += 1

    def checksum(self):
        flatarray = list(itertools.chain.from_iterable(self.grid))
        ret = 0
        i = 24
        # j = 0
        while(i >= 0):
            ret += flatarray[i] * (1<<i)
            i -= 1
            # j += 1
        return ret

    def printGrid(self):
        for i in range(5):
            for j in range(5):
                print('#' if self.grid[i][j] else '.', end="")
            print("")

Problem()
