#!/bin/python3

import numpy as np
import anytree as at

class Problem():
    def __init__ (self):
        self.input = open("8.in","r")
        self.inputContents = [int(x) for x in self.input.readlines()[0].split(" ")]
        # self.inputContents = [int(x) for x in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")]

        self.root = at.Node(0, kindnodes=self.inputContents[0], metanodes=self.inputContents[1])
        self.nodeCount = -1
        self.it = 1
        self.searchNodes(self.root, self.inputContents[0], self.inputContents[1])
        # print(at.RenderTree(self.root).by_attr())

        # we want to find the value of node name=1
        totalVal = 0
        totalVal += self.findValue(self.root)
        print("Total value of the root node is {}".format(totalVal))

    def findValue(self, node):
        wert = 0
        if (node.kindnodes > 0 and node.metanodes > 0):
            # sprint("got child nodes")
            for meta in node.children[-1].metadaten:
                if meta <= node.kindnodes:
                    wert += self.findValue(node.children[meta - 1])
        elif (node.kindnodes == 0 and node.metanodes > 0):
            # print("No child nodes")
            wert += sum(node.children[0].metadaten)
        else:
            print("Uncaught Error")
            quit()
        return wert

    def searchNodes(self, eltern, kindNodes, metaNodes):
        self.nodeCount += 1
        if self.nodeCount > 0:
            curNode = at.Node(self.nodeCount, parent=eltern, kindnodes=kindNodes, metanodes=metaNodes)
        else:
            curNode = eltern
        if kindNodes > 0:
            for i in range(kindNodes):
                self.it += 2
                self.searchNodes(curNode, self.inputContents[self.it - 1], self.inputContents[self.it])
        if metaNodes > 0:
            metaArr = []
            for j in range(metaNodes):
                self.it += 1
                metaArr.append(self.inputContents[self.it])
            meta = at.Node("Metadata", parent=curNode, metadaten=metaArr)
        return


Problem()
