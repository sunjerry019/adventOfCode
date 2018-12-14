#!/bin/python3

import numpy as np
import copy

class Marble():
    """
    A node in a circularly doubly-linked list.
    """
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        # return "< prev = {}, data = {}, next = {}>".format(self.prev.data, self.data, self.next.data)
        return repr(self.data)

    def walkcw(self, steps):
        curr = self
        for i in range(steps):
            if curr.next is not None:
                curr = curr.next
            else:
                raise ValueError('No next node to traverse')
        return curr

    def walkccw(self, steps):
        curr = self
        for i in range(steps):
            if curr.prev is not None:
                curr = curr.prev
            else:
                raise ValueError('No prev node to traverse')
        return curr

class Circle():
    """
    This is circularly linked list
    """
    def __init__(self):
        self.origin = None
        self.length = 0

    def __repr__(self):
        return '[' + ', '.join(self.toList()) + ']'

    def toList(self):
        nodes = [repr(self.origin)]
        curr = self.origin
        if self.origin.next != self.origin:
            curr = self.origin.next
            while curr != self.origin:
                nodes.append(repr(curr))
                curr = curr.next
        return nodes

    def addMarbleAtOrigin(self, data):
        node = Marble(data=data)

        if self.origin:
            node.prev = self.origin.prev
            self.origin.prev = node
            node.next = self.origin

        self.origin = node

        if self.origin.next is None:
            self.origin.next = self.origin

        if self.origin.prev is None:
            self.origin.prev = self.origin

        self.length += 1

        return self.origin

    def insertAfter(self, node, data):
        new_node = Marble(data=data)

        # if self.length == 1:
        #     # inserting at right of origin with only 1 node
        #     new_node.prev = self.origin
        #     new_node.next = self.origin
        #     self.origin.next = new_node
        #     self.origin.prev = new_node
        # else:
        if node.next is not None:
            node.next.prev = new_node
            new_node.next = node.next

        new_node.prev = node
        node.next = new_node

        self.length += 1

        return new_node

    def remove_elem(self, node):
        """
        Unlink an element from the list.
        Takes O(1) time.
        """
        next_node = node.next
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node is self.origin:
            self.origin = node.next
        node.prev = None
        node.next = None

        self.length -= 1

        return next_node

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

        self.circle = Circle()
        self.currentMarble = self.circle.addMarbleAtOrigin(0)
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

        for idx in range(1, self.lastMarblePts + 1):
            self.printProgress(idx)
            self.placeMarble(idx)
            # self.printCircle()
            self.currentPlayer += 1
            self.currentPlayer %= self.playersNumbers

        print("\033[2KWinning Score = {}".format(max(self.players)))

    def placeMarble(self, marbleidx):
        if marbleidx % 23 != 0:
            # temp = self.currentMarble.walkcw(1)
            # print(temp == self.circle.origin)
            self.currentMarble = self.circle.insertAfter(self.currentMarble.walkcw(1), marbleidx)
        else:
            removedMarble = self.currentMarble.walkccw(7)
            # print("\033[2K", type(removedMarble))
            self.players[self.currentPlayer] += removedMarble.data
            self.currentMarble = self.circle.remove_elem(removedMarble)

    def printCircle(self):
        # print("\nScores: ", self.players)
        # outputStr = "[{:>" + self.digitsToDisplay["players"] + "}]: "
        # displayArray = copy.deepcopy(repr(self.circle))
        # for i in range(len(displayArray)):
        #     if displayArray[i] == self.currentMarble.data:
        #         displayArray[i] = ">" + displayArray[i]
        #
        # m = "{:>" + self.digitsToDisplay["marble"] + "} "
        # outputStr += m * self.circle.length
        # print(outputStr.format(self.currentPlayer, *displayArray))

        print(self.circle)

    def printProgress(self, idx):
        outputStr = "[{:>" + self.digitsToDisplay["players"] + "}]: Marble ["
        outputStr += "{:>" + self.digitsToDisplay["marble"] + "}/" + "{:>" + self.digitsToDisplay["marble"] + "}]"
        print(outputStr.format(self.currentPlayer, idx, self.lastMarblePts), end="\r")

Problem()
