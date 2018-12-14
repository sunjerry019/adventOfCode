#!/bin/python3

import numpy as np
import anytree as at

class Problem():
    def __init__ (self):
        self.input = open("8.in","r")
        self.inputContents = [int(x) for x in self.input.readlines()[0].split(" ")]
        # self.inputContents = [int(x) for x in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(" ")]

        self.root = at.Node(0)
        self.nodeCount = 0
        self.it = 1
        self.searchNodes(self.root, self.inputContents[0], self.inputContents[1])
        # print(at.RenderTree(self.root).by_attr())

        self.metadataNodes = at.search.findall(self.root, filter_=lambda node: node.name == "Metadata")
        self.metadata = []
        for node in self.metadataNodes:
            self.metadata += node.metadaten

        print(sum(self.metadata))

    def searchNodes(self, eltern, kindNodes, metaNodes):
        self.nodeCount += 1
        curNode = at.Node(self.nodeCount, parent=eltern)
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
