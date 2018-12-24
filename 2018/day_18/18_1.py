#!/usr/bin/env python3

import math
import copy

class Problem():
    def __init__(self):
        self.input = open("18.in","r")
        self.inputContents = self.input.readlines()
        self.part1 = 20
        self.generations = 20
        self.generationsDigits = str(int(math.log10(self.generations)) + 1)
        self.currGen = 0
        self.prevAnswer = 0
        self.prevAnswerDiff = 0
        self.currAnswer = 0
        self.justRun = False

        self.pflanzeMapping = {
            "|" : 2,
            "#" : 1,
            "." : 0
        }
        self.pflanzeMappingR = [" ", "#", "|"]

        
Problem()
