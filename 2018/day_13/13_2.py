#!/usr/bin/env python3

import numpy as np
import copy

class Problem():
    def __init__ (self):
        self.input = open("13.in","r")
        self.inputContents = self.input.readlines() # remove the last newline
        self.size = (len(self.inputContents[0][:-1]), len(self.inputContents))
        print("Size = {}".format(self.size))
        self.karte = np.zeros(self.size, dtype=int)
        self.zugen = dict()
        self.ticks = 0
        self.karteMapping = {
            " " : 0,
            "-" : 1,
            ">" : 1,
            "<" : 1,
            "|" : 2,
            "^" : 2,
            "v" : 2,
            "/" : 3,
            "\\" : 4,
            "+" : 5
        }
        self.reverseKarteMapping = {
            0 : " " ,
            1 : "-" ,
            2 : "|" ,
            3 : "/" ,
            4 : "\\",
            5 : "+"
        }
        self.zugenMapping = {
            "^" : 0,
            ">" : 90,
            "v" : 180,
            "<" : 270,
            " " : -1,
            "-" : -1,
            "|" : -1,
            "/" : -1,
            "\\" : -1,
            "+" : -1
        }
        self.reverseZugenMapping = {
            0   : "^",
            90  : ">",
            180 : "v",
            270 : "<",
        }
        self.richtungMapping = {
            0:   np.array([ 0, -1]),
            90:  np.array([ 1,  0]),
            180: np.array([ 0,  1]),
            270: np.array([-1,  0])
        }
        self.intersectionMapping = { # we %3 the number of intersections
            1: -90,
            2:   0,
            0:  90
        }

        y = 0
        for line in self.inputContents:
            x = 0
            for char in line[:-1]:
                self.karte[x, y] = self.karteMapping[char]
                if self.zugenMapping[char] > -1:
                    self.zugen[(x, y)] = {
                        "dir": self.zugenMapping[char],
                        "intersections": 0
                    }
                x += 1
            y += 1

        while self.tick():
            self.ticks += 1

        print("t = {}\tLast train standing = {}".format(self.ticks, list(self.zugen.keys())[0]))

        #while True:
        #    self.tick()
        #    if np.amax(self.zugen) == 5:
        #        maxidx = np.argmax(self.zugen)
        #        print("Trains Crashed at ({}, {})".format(int(maxidx/150), maxidx%150)
        #        break;

    def checkSafe(self, x, y):
        checkCoord = tuple(np.array([x, y]) + self.richtungMapping[self.zugen[x, y]["dir"]])
        # print("Checking if train at ({}, {}) is safe to move to {}".format(x, y, checkCoord))
        return not(checkCoord in self.zugen)

    def moveZug (self, x, y):
        # Trains shall always face the direction of where they are going next (i.e. at bend, they will turn on the bend)
        travelInformation = self.zugen[x, y]
        newCoord = tuple(np.array([x, y]) + self.richtungMapping[travelInformation["dir"]])
        del self.zugen[(x, y)]

        # Calculate new travelDir
        if self.karte[newCoord[0], newCoord[1]] == 5:
            # intersection
            travelInformation["intersections"] += 1
            travelInformation["intersections"] %= 3
            travelInformation['dir'] += self.intersectionMapping[travelInformation["intersections"]]
        elif self.karte[newCoord[0], newCoord[1]] == 3:
            # the / char
            if travelInformation['dir'] == 0 or travelInformation['dir'] == 180:
                travelInformation['dir'] += 90
            else:
                travelInformation['dir'] -= 90
        elif self.karte[newCoord[0], newCoord[1]] == 4:
            # the \ char
            if travelInformation['dir'] == 0 or travelInformation['dir'] == 180:
                travelInformation['dir'] -= 90
            else:
                travelInformation['dir'] += 90

        travelInformation['dir'] %= 360
        self.zugen[newCoord] = travelInformation

    def tick(self):
        # self.printMap()
        currentListOfZugen = copy.deepcopy(self.zugen)
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if (x, y) in currentListOfZugen and self.checkSafe(x, y):
                    self.moveZug(x, y)
                elif (x, y) in currentListOfZugen:
                    # Crashed
                    neuCoord = tuple(np.array([x, y]) + self.richtungMapping[self.zugen[x, y]["dir"]])
                    print("Crash at {}".format(neuCoord))
                    del self.zugen[(x, y)]
                    try:
                        del currentListOfZugen[(x, y)]
                    except:
                        pass

                    del self.zugen[neuCoord]
                    try:
                        del currentListOfZugen[neuCoord]
                    except:
                        pass
                    print(len(self.zugen), "trains left")

        if(len(self.zugen) == 1):
            return False
        return True

    def printMap(self):
        print("t = {}".format(self.ticks))
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                if (x, y) in self.zugen:
                    print(self.reverseZugenMapping[self.zugen[(x, y)]["dir"]], end="")
                else:
                    print(self.reverseKarteMapping[self.karte[x, y]], end="")
            print("")

Problem()
