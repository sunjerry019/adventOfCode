#!/bin/python3

import numpy as np
import sys

sys.setrecursionlimit(5000)

class Problem():
    def __init__(self):
        self.input = open("17.in","r")
        self.inputContents = self.input.readlines()

        self.blocks = {}        # includes clay and settled water
        self.clays = {}         # purely for printing purposes
        self.waterTouched = {}
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.min_x = float('inf')
        self.max_x = float('-inf')

        for clay in self.inputContents:
            a = clay.strip().split(", ")
            coord1 = a[0].split("=")
            coord2 = a[1].split("=")

            if coord1[0] == "x":
                x = int(coord1[1])
                ys = coord2[1].split("..")
                if x > self.max_x: self.max_x = x
                if x < self.min_x: self.min_x = x
                for y in range(int(ys[0]), int(ys[1]) + 1):
                    self.blocks[(x, y)] = 1
                    self.clays[(x, y)] = 1
                    if y > self.max_y: self.max_y = y
                    if y < self.min_y: self.min_y = y

            if coord1[0] == "y":
                y = int(coord1[1])
                if y > self.max_y: self.max_y = y
                if y < self.min_y: self.min_y = y

                xs = coord2[1].split("..")
                for x in range(int(xs[0]), int(xs[1]) + 1):
                    self.blocks[(x, y)] = 1
                    self.clays[(x, y)] = 1
                    if x > self.max_x: self.max_x = x
                    if x < self.min_x: self.min_x = x

        while self.flow(500, 0, {}):
            pass
        # self.printMap()
        print("Part 1 = {} blocks".format(len([coord for coord in self.waterTouched.keys() if self.min_y <= coord[1] <= self.max_y])))
        self.printMap()

    def flow(self, currX, currY, visited):
        # print("Current Position ({}, {}). x = [{}, {}] y = [{}, {}]".format(currX, currY, self.min_x, self.max_x, self.min_y, self.max_y))
        # self.printMap()

        self.waterTouched[(currX, currY)] = 1
        visited[(currX, currY)] = 1

        if currX > self.max_x: self.max_x = currX
        if currX < self.min_x: self.min_x = currX

        if currY > self.max_y:
            return False

        canFlowDown  = ((currX, currY + 1) not in self.blocks and (currX, currY + 1) not in visited)
        canFlowRight = ((currX + 1, currY) not in self.blocks and (currX + 1, currY) not in visited)
        canFlowLeft  = ((currX - 1, currY) not in self.blocks and (currX - 1, currY) not in visited)
        if canFlowDown: return self.flow(currX, currY + 1, visited) # can flow downwards
        elif canFlowLeft or canFlowRight:
            v1 = True
            v2 = True
            if canFlowRight: v1 = self.flow(currX + 1, currY, visited) # can flow right
            if canFlowLeft : v2 = self.flow(currX - 1, currY, visited) # can flow left
        else:
            # cannot flow anywhere, I settle
            self.blocks[(currX, currY)] = 1
            return True

        return (v1 & v2)

    def printMap(self):
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if x == 500 and y == 0:
                    print("+", end="")
                elif (x, y) in self.clays:
                    print("#", end="")
                elif (x, y) in self.blocks:
                    print("~", end="")
                elif (x, y) in self.waterTouched:
                    print("|", end="")
                else:
                    print(" ", end="")
            print("")
        print("")
Problem()
