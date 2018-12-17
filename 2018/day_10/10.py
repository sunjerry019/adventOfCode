#!/usr/bin/env python3

import numpy as np

class Problem():
    def __init__ (self):
        self.input = open("10.in","r")
        self.inputContents = self.input.readlines()
        self.stars = []
        self.currentState = dict() # Using dictionaries as arrays
        self.t = 0

        self.processInput()
        while self.t < 10**6:
            # print("t = {}".format(self.t), end="\r")
            self.producePositionsAtTime()
            if self.checkIfPossible():
                self.draw()
            self.t += 1

    def processInput(self):
        for star in self.inputContents:
            a = star.split(" velocity=<")
            v = a[1].split(", ")
            vx = int(v[0].strip())
            vy = int(v[1].strip()[:-1])
            p = a[0].split("=<")[1].split(", ")
            posx = int(p[0].strip())
            posy =int(p[1].strip()[:-1])

            self.stars.append({
                "pos": { "x" : posx, "y" : posy },
                "velocity": {"x": vx, "y" : vy }
            })

    def producePositionsAtTime(self):
        self.currentState = dict()
        for i in range(len(self.stars)):
            x = self.stars[i]["pos"]["x"] + self.stars[i]["velocity"]["x"]*self.t
            y = self.stars[i]["pos"]["y"] + self.stars[i]["velocity"]["y"]*self.t
            self.currentState[(x, y)] = 1

    def checkSurrounding(self, coord):
        return (coord[0]+1, coord[1]-1) in self.currentState or \
               (coord[0]+1, coord[1]  ) in self.currentState or \
               (coord[0]+1, coord[1]+1) in self.currentState or \
               (coord[0]  , coord[1]+1) in self.currentState or \
               (coord[0]-1, coord[1]+1) in self.currentState or \
               (coord[0]-1, coord[1]  ) in self.currentState or \
               (coord[0]-1, coord[1]-1) in self.currentState or \
               (coord[0]  , coord[1]-1) in self.currentState


    def checkIfPossible(self):
        numFails = 0
        for starCoord in self.currentState:
            if not self.checkSurrounding(starCoord):
                numFails += 1

            if numFails > 0.3*len(self.currentState):
                return False

        return True

    def draw(self):
        # Draw the currentState

        # Check bounds
        xys = list(zip(*self.currentState.keys()))
        #xys = [[c[0] for c in self.currentState.keys()], [c[1] for c in self.currentState.keys()]]
        max_x = max(xys[0])
        min_x = min(xys[0])
        max_y = max(xys[1])
        min_y = min(xys[1])

        print ("t = {}".format(self.t))
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if (x, y) in self.currentState:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("\n", end="")
        print("\n")


Problem()

# print("[")
# print("{{pos: {{'x': {}, 'y': {}}}, velocity: {{'x': {}, 'y': {}}}}}".format(posx, posy, vx, vy), end="")
# print("]")
