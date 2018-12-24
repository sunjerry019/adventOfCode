#!/usr/bin/env python3

import PyGnuplot as gp

class Problem():
    def __init__(self):
        self.input = open("23.in","r")
        self.output = open("23.dat", "w+")
        self.inputContents = self.input.readlines()
        self.nanobots = {}
        # self.coordsInRange = {}

        self.min = [float('+inf'), float('+inf'), float('+inf')]
        self.max = [float('-inf'), float('-inf'), float('-inf')]

        gp.c("set term x11 size 1280, 720")

        for line in self.inputContents:
            a = line.strip().split(">, r=")
            b = a[0].split("=<")
            c = b[1].split(",")
            coord = tuple(int(x) for x in c)

            self.nanobots[coord] = int(a[1])

            for i in range(3):
                self.min[i] = min(coord[i] - self.nanobots[coord], self.min[i])
                self.max[i] = max(coord[i] + self.nanobots[coord], self.max[i])

            self.output.write("{}\t{}\t{}".format(coord[0], coord[1], coord[2]))

Problem()
