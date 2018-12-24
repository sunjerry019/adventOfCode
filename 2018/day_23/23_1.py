#!/usr/bin/env python3

import numpy as np

class Problem():
    def __init__(self):
        self.input = open("23.in","r")
        self.inputContents = self.input.readlines()
        self.nanobots = {}

        self.maxSignalBot = tuple()
        self.maxSignal = float('-inf')

        for line in self.inputContents:
            a = line.strip().split(">, r=")
            b = a[0].split("=<")
            c = b[1].split(",")
            coord = tuple(int(x) for x in c)

            self.nanobots[coord] = int(a[1])

            if self.nanobots[coord] > self.maxSignal:
                self.maxSignal = self.nanobots[coord]
                self.maxSignalBot = coord

        self.inrange = 0
        for nanobot in self.nanobots:
            if self.distance(nanobot, self.maxSignalBot) <= self.maxSignal:
                self.inrange += 1

        print(self.inrange)

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
Problem()
