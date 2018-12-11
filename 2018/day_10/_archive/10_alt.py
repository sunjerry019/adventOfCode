#!/bin/python3

import numpy as np

class Problem():
    def __init__ (self):
        self.input = open("10.in","r")
        self.inputContents = self.input.readlines()
        self.stars = []
        self.currentState = dict()

        self.processInput()

    def processInput(self):
        q = False

        for star in self.inputContents:
            if q:
                print(",", end="")
            else:
                q = True
            a = star.split(" velocity=<")
            v = a[1].split(", ")
            vx = int(v[0].strip())
            vy = int(v[1].strip()[:-1])
            p = a[0].split("=<")[1].split(", ")
            posx = int(p[0].strip())
            posy = int(p[1].strip()[:-1])

            self.stars.append({
                "pos": { "x" : posx, "y" : posy },
                "velocity": {"x": vx, "y" : vy }
            })


        self.doTheThing()

    def producePositionsAtTime(self, t):
        self.currentState = dict()
        for i in range(len(self.stars)):
            x = self.stars[i]["pos"]["x"] + self.stars[i]["velocity"]["x"]*t
            y = self.stars[i]["pos"]["y"] + self.stars[i]["velocity"]["y"]*t
            self.currentState[(x, y)] = 1

    def checkSurrounding(self, x, y):
        # start at right, go anticlockwise
        return (x + 1, y + 0) in self.currentState or \
               (x + 1, y - 1) in self.currentState or \
               (x + 0, y - 1) in self.currentState or \
               (x - 1, y - 1) in self.currentState or \
               (x - 1, y + 0) in self.currentState or \
               (x - 1, y + 1) in self.currentState or \
               (x + 0, y + 1) in self.currentState or \
               (x + 1, y + 1) in self.currentState

    def checkIfPossible(self):
        numFails = 0
        for i, it in enumerate(self.currentState):
            if not self.checkSurrounding(it[0], it[1]):
                numFails += 1

            if numFails > 10:
                return False

        return True

    def doTheThing(self):
        for t in range(12000):
            self.producePositionsAtTime(t)
            is_possible = self.checkIfPossible()

            if is_possible:
                print("t = {} is possible".format(t))
                xs = [ x[0] for x in list(self.currentState.keys()) ]
                ys = [ x[1] for x in list(self.currentState.keys()) ]

                minx = min(xs)
                maxx = max(xs)
                miny = min(ys)
                maxy = max(ys)

                rows = maxy - miny + 1
                cols = maxx - minx + 1

                grid = dict()

                print("size = {}x{}".format(cols, rows))
                for i, (x, y) in enumerate(self.currentState):
                    grid[(x - minx, y - miny)] = True

                for y in range(rows):
                    line = ""
                    for x in range(cols):
                        if (x, y) in grid:
                            line += "#"
                        else:
                            line += " "
                    print(line)

                return


prob = Problem()
#print("[")
#print("{{pos: {{'x': {}, 'y': {}}}, velocity: {{'x': {}, 'y': {}}}}}".format(posx, posy, vx, vy), end="")
#print("]")
