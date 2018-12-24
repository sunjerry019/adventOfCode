#!/usr/bin/env python3

import math

class Problem():
    def __init__(self):
        self.input = open("23.in","r")
        self.inputContents = self.input.readlines()
        self.nanobots = {}
        # self.coordsInRange = {}

        self.min = [float('+inf'), float('+inf'), float('+inf')]
        self.max = [float('-inf'), float('-inf'), float('-inf')]
        self.smallestRadius = float('+inf')

        for line in self.inputContents:
            a = line.strip().split(">, r=")
            b = a[0].split("=<")
            c = b[1].split(",")
            coord = tuple(int(x) for x in c)

            self.nanobots[coord] = int(a[1])
            if self.nanobots[coord] < self.smallestRadius:
                self.smallestRadius = self.nanobots[coord]

            # minimum = [0, 0, 0]
            # maximum = [0, 0, 0]

            # for i in range(3):
            #     minimum[i] = coord[i] - self.nanobots[coord]
            #     maximum[i] = coord[i] + self.nanobots[coord]

            # self.coordsInRange[coord] = []
            # for z in range(minimum[2], maximum[2] + 1):
            #     for y in range(minimum[1], maximum[1] + 1):
            #         for x in range(minimum[0], maximum[0] + 1):
            #             if self.distance((x, y, z), coord) <= self.nanobots[coord]:
            #                 self.coordsInRange[coord].append((x, y, z))

            for i in range(3):
                self.min[i] = min(coord[i] - self.nanobots[coord], self.min[i])
                self.max[i] = max(coord[i] + self.nanobots[coord], self.max[i])


        self.diffs = [0,0,0]
        self.digits = [0,0,0]
        for i in range(3):
            self.diffs[i] = self.max[i] - self.min[i] + 1
            self.digits[i] = math.floor(math.log10(self.diffs[i])) + 1

        print("Smallest Radius: {}\nMins: {}\nMaxs: {}\nDiff: {}".format(self.smallestRadius, self.min, self.max, self.diffs))

        self.step = 10**(math.floor(math.log10(self.smallestRadius)) + 1 - 1)

        # self.min = tuple(_c + math.floor(self.step/2) for _c in self.min)
        while self.step >= 1:
            self.largestNumberOfNanobots = 0
            self.largestCoords = []
            z = self.min[2]
            while z <= self.max[2]:
                y = self.min[1]
                while y <= self.max[1]:
                    x = self.min[0]
                    while x <= self.max[0]:
                        self.printProgress(x, y, z)
                        nanobotsInRange = 0
                        for nanobot in self.nanobots:
                            if self.distance(nanobot, (x, y, z)) <= self.nanobots[nanobot]:
                                nanobotsInRange += 1

                        if nanobotsInRange > 0:
                            if nanobotsInRange > self.largestNumberOfNanobots:
                                self.largestCoords = [(x, y, z)]
                                self.largestNumberOfNanobots = nanobotsInRange
                            elif nanobotsInRange == self.largestNumberOfNanobots:
                                self.largestCoords.append((x, y, z))
                        x += self.step
                    y += self.step
                z += self.step
            print(largestCoords)
            self.min = tuple(_c for _c in min(self.largestCoords))
            # self.max = tuple(_c + math.floor(self.step/2) for _c in max(self.largestCoords))
            self.max = tuple(_c + self.step for _c in self.min)
            self.step //= 10

        print("\033[2KLargest Coords = {}\nLargest No. Of Nanobots = {}\n".format(self.largestCoords, self.largestNumberOfNanobots))

        self.smallestDistance = float('+inf')
        self.smallestCoords = []
        for coord in self.largestCoords:
            _d = sum(coord)
            if _d < self.smallestDistance:
                self.smallestCoords = [coord]
                self.smallestDistance = _d
            elif _d == self.smallestDistance:
                self.smallestCoords.append(coord)

        print("Smallest Coords = {}\nSmallest Distance = {}".format(self.smallestCoords, self.smallestDistance))

        if self.smallestDistance < 47074586:
            print("Too Low")

        # for z in range(self.min[2], self.max[2] + 1, self.step):
        #     for y in range(self.min[1], self.max[1] + 1, self.step):
        #         for x in range(self.min[0], self.max[0] + 1, self.step):
        #             self.printProgress(x,y,z)
        #             nanobotsInRange = 0
        #             for nanobot in self.nanobots:
        #                 if self.distance(nanobot, (x, y, z)) <= self.nanobots[nanobot]:
        #                     nanobotsInRange += 1
        #
        #             if nanobotsInRange > 0:
        #                 if nanobotsInRange > self.largestNumberOfNanobots:
        #                     self.largestCoords = [(x, y, z)]
        #                     self.largestNumberOfNanobots = nanobotsInRange
        #                 elif nanobotsInRange == self.largestNumberOfNanobots:
        #                     self.largestCoords.append((x, y, z))
        #
        # print(self.largestNumberOfNanobots, self.largestCoords)
	def searchInCube(self, coord, step):
		
		

    def printProgress(self, _x, _y, _z):
        map = ["x", "y", "z"]
        outputStr = ""
        _d = [str(q) for q in self.digits]
        for i in range(3):
            if i > 0:
                outputStr += "      "
            outputStr += map[i] + " [{:>" + _d[i] + "}/{:>" + _d[i] + "}]"

        outputStr += " => {}"

        print(outputStr.format(_x - self.min[0], self.diffs[0], _y - self.min[1], self.diffs[1], _z - self.min[2], self.diffs[2], self.largestNumberOfNanobots), end='\r')

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
Problem()
