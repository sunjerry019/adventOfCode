#!/usr/bin/env python3

import numpy as np
import copy

class Problem():
    def __init__ (self):
        # read input
        self.input = open("9_2.in","r")
        self.inputContents = self.input.readlines()[0].split(" players; last marble is worth ")
        self.playersNumbers = int(self.inputContents[0])
        self.lastMarblePts  = int(self.inputContents[1].split(" ")[0])

        self.digitsToDisplay = {
            "players": str(int(np.log10(self.playersNumbers))+1),
            "marble" : str(int(np.log10(self.lastMarblePts))+1 + 1) # for current marble indication
        }

        self.circle = []
        self.currentMarbleIdx = 0
        self.currentPlayer = 0

        self.players = np.zeros(self.playersNumbers, dtype=int)

        # Handle the multiples of 23 first:
        rowsPlayer = int(np.ceil(self.lastMarblePts/self.playersNumbers))
        rows23 = int(np.ceil(self.lastMarblePts/23))
        while self.playersNumbers * rowsPlayer < rows23 * 23:
            rowsPlayer += 1

        a              = np.zeros((rows23, 22))
        self.marbles23 = np.arange(1, rows23*23 + 1)
        if self.marbles23[-1] > self.lastMarblePts:
            self.marbles23[-1] = 0
        self.marbles23 = self.marbles23.reshape((rows23, 23))
        self.marbles23[:,:-1] = a
        self.marbles23 = np.concatenate((self.marbles23.flatten(), np.zeros(self.playersNumbers * rowsPlayer - rows23*23, dtype=int)))
        self.marbles23 = self.marbles23.reshape((rowsPlayer, self.playersNumbers))
        self.players += np.sum(self.marbles23, axis=0)
        # print(self.players)

        self.circle.append(0)
        for idx in range(1, self.lastMarblePts + 1):
            self.printProgress(idx)
            self.placeMarble(idx)
            #self.printCircle()
            self.currentPlayer += 1
            self.currentPlayer %= self.playersNumbers

        print("\033[2KWinning Score = {}".format(max(self.players)))

    def placeMarble(self, marbleidx):
        if marbleidx % 23 != 0:
            btwMarbles = np.array([self.currentMarbleIdx + 1, self.currentMarbleIdx + 2]) % len(self.circle)

            if np.abs(btwMarbles[0] - btwMarbles[1]) > 1:
                if max(btwMarbles) == len(self.circle) - 1 and min(btwMarbles) == 0:
                    insertIdx = len(self.circle)
                else:
                    print("Uncaught Error")
                    quit()
            else:
                insertIdx = min(btwMarbles) + 1

            # print("{} = idx {}".format(btwMarbles, insertIdx))

            self.circle.insert(insertIdx, marbleidx)
            self.currentMarbleIdx = insertIdx
        else:
            removeIdx = (self.currentMarbleIdx - 7) % len(self.circle)
            # self.players[self.currentPlayer] += marbleidx
            self.players[self.currentPlayer] += self.circle[removeIdx]
            del self.circle[removeIdx]
            self.currentMarbleIdx = removeIdx


    def printCircle(self):
        # print("\nScores: ", self.players)
        outputStr = "[{:>" + self.digitsToDisplay["players"] + "}]: "
        displayArray = copy.deepcopy(list(self.circle))
        displayArray[self.currentMarbleIdx] = ">" + str(displayArray[self.currentMarbleIdx])
        m = "{:>" + self.digitsToDisplay["marble"] + "} "
        outputStr += m * len(self.circle)
        print(outputStr.format(self.currentPlayer, *displayArray))

    def printProgress(self, idx):
        outputStr = "[{:>" + self.digitsToDisplay["players"] + "}]: Marble ["
        outputStr += "{:>" + self.digitsToDisplay["marble"] + "}/" + "{:>" + self.digitsToDisplay["marble"] + "}]"
        print(outputStr.format(self.currentPlayer, idx, self.lastMarblePts), end="\r")

Problem()
