#!/usr/bin/env python3

import math
import copy

class Problem():
    def __init__(self):
        self.input = open("12.in","r")
        self.inputContents = self.input.readlines()
        self.part1 = 20
        self.generations = 50000000000
        self.generationsDigits = str(int(math.log10(self.generations)) + 1)
        self.currGen = 0
        self.prevAnswer = 0
        self.prevAnswerDiff = 0
        self.currAnswer = 0
        self.justRun = False

        self.pflanzeMapping = {
            "#" : 1,
            "." : 0
        }
        self.pflanzeMappingR = [".", "#"]
        self.masks = {}

        self.initialState = self.inputContents[0][15:].strip()
        # Negative numbers, [0][0] = -1, then positive numbers starting from zero
        self.state = [[], [ self.pflanzeMapping[x] for x in self.initialState ]]
        self.bounds = (-len(self.state[0]), len(self.state[1]) - 1)
        self.checkIfPadEnds()

        for line in self.inputContents[2:]:
            x = line.strip().split(" => ")
            a = [self.pflanzeMapping[char] for char in x[0]]
            self.masks[tuple(a)] = self.pflanzeMapping[x[1]]

        # self.printState()
        for i in range(self.generations):
            self.currGen = i + 1
            if not self.justRun:
                self.tick()
                if self.currGen == self.part1:
                    self.sum = 0
                    for i in range(self.bounds[0], self.bounds[1] + 1):
                        if self.getStateAtIndex(self.state, i):
                            self.sum += i
                    print("\033[2KPart 1 = {}".format(self.sum))
            else:
                self.currAnswer += (self.generations - i) * self.prevAnswerDiff
                break
            self.printProgress()

        print("\033[2KPart 2 = {}".format(self.currAnswer))

    def tick(self):
        newGen = copy.deepcopy(self.state)
        for i in range(self.bounds[0], self.bounds[1] + 1):
            patt = self.constructSubstring(i)
            if patt in self.masks:
                newGen = self.putStateAtIndex(newGen, i, self.masks[patt])
            else:
                newGen = self.putStateAtIndex(newGen, i, 0)
        self.state = copy.deepcopy(newGen)
        self.checkIfPadEnds()
        # self.printState()

    def checkIfPadEnds(self):
        # Check if need to pad sides to keep the refIdx within bounds
        min_idx = float('+inf')
        for idx in range(self.bounds[0], self.bounds[1] + 1):
            a = self.getStateAtIndex(self.state, idx)
            if a:
                min_idx = idx
                break

        max_idx = float('-inf')
        for idx in range(self.bounds[1], self.bounds[0] - 1, -1):
            a = self.getStateAtIndex(self.state, idx)
            if a:
                max_idx = idx
                break

        # Pad until last plant on each side is 2 empty slots away so that the code can check ....# and #....
        if min_idx < float('+inf') and min_idx < self.bounds[0] + 2 : self.state = self.putStateAtIndex(self.state, min_idx - 2, 0)
        if max_idx > float('-inf') and max_idx > self.bounds[1] - 2 : self.state = self.putStateAtIndex(self.state, max_idx + 2, 0)

        # Update bounds
        self.bounds = (-len(self.state[0]), len(self.state[1]) - 1)

    def constructSubstring(self, refIdx):
        if (refIdx >= 2) and (refIdx + 2 <= self.bounds[1]):
            # need only use the positive array
            p = self.state[1][refIdx - 2:refIdx + 3]
        else:
            p = []
            for idx in range(refIdx - 2, refIdx + 3):
                p.append(self.getStateAtIndex(self.state, idx))
        return tuple(p)

    def putStateAtIndex(self, stateArray, refIdx, state):
        bounds = (-len(stateArray[0]), len(stateArray[1]) - 1)
        stateArray = copy.deepcopy(stateArray)
        if bounds[0] <= refIdx <= bounds[1]:
            if refIdx >= 0:
                stateArray[1][refIdx] = state
            else:
                stateArray[0][abs(refIdx) - 1] = state
        else:
            if refIdx >= 0 and refIdx > bounds[1]:
                for i in range(bounds[1] + 1, refIdx):
                    # until 1 before the refIdx
                    stateArray[1].append(0)
                stateArray[1].append(state)
            elif refIdx < 0 and refIdx < bounds[0]:
                for i in range(bounds[0] - 1, refIdx, -1):
                    # until 1 before the refIdx
                    stateArray[0].append(0)
                stateArray[0].append(state)
            else:
                print("Hmm idx {} received, range = [{}, {}]".format(refIdx, bounds[0], bounds[1]))
                quit()
        return stateArray

    def getStateAtIndex(self, stateArray, refIdx):
        bounds = (-len(stateArray[0]), len(stateArray[1]) - 1)
        if bounds[0] <= refIdx <= bounds[1]:
            if refIdx >= 0:
                return stateArray[1][refIdx]
            else:
                return stateArray[0][abs(refIdx) - 1]
        else:
            return 0

    def printProgress(self, currentIdx=0):
        if not self.justRun:
            self.currAnswer = 0
            for i in range(self.bounds[0], self.bounds[1] + 1):
                if self.getStateAtIndex(self.state, i):
                    self.currAnswer += i

            diff = self.currAnswer - self.prevAnswer
            if diff == self.prevAnswerDiff:
                self.justRun = True
            self.prevAnswerDiff = diff
            self.prevAnswer = self.currAnswer

        # outputStr = "\033[2K[{:>" + self.generationsDigits + "}/{:>" + self.generationsDigits + "}] At ({:>7}/{:>7})"
        outputStr = "\033[2K[{:>" + self.generationsDigits + "}/{:>" + self.generationsDigits + "}]"
        print(outputStr.format(self.currGen, self.generations), end="")
        print(" Bounds = ({},{}) => Current Answer = {}".format(self.bounds[0], self.bounds[1], self.currAnswer), end="\r")
        # print("{:>3})".format(self.bounds[0]), end="")
        # for i in range(self.bounds[0], self.bounds[1] + 1):
        #     print(self.pflanzeMappingR[self.getStateAtIndex(self.state, i)], end="")
        # print("({}".format(self.bounds[1]), end="\r")

    def printState(self):
        outputStr = "[{:>" + self.generationsDigits + "}/{:>" + self.generationsDigits + "}]: "
        print(outputStr.format(self.currGen, self.generations), end="")
        print("{:>3})".format(self.bounds[0]), end="")
        for i in range(self.bounds[0], self.bounds[1] + 1):
            print(self.pflanzeMappingR[self.getStateAtIndex(self.state, i)], end="")
        print("({}".format(self.bounds[1]))

Problem()
